"""
Sends quiz polls and records answers against per-chat, per-user scores.
"""

from telegram import Poll, Update
from telegram.ext import ContextTypes

from app.database import get_db_context
from app.logger import get_logger
from app.models import ActivePoll, Score
from app.quiz_bank import get_random_question

logger = get_logger(__name__)


async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    q = get_random_question()

    message = await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question=q["question"],
        options=q["options"],
        type=Poll.QUIZ,
        correct_option_id=q["correct_index"],
        is_anonymous=False,
        explanation=f"Category: {q['category']}",
    )

    with get_db_context() as db:
        db.merge(
            ActivePoll(
                poll_id=message.poll.id,
                chat_id=update.effective_chat.id,
                correct_option_id=q["correct_index"],
            )
        )


async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = update.poll_answer
    if not answer.option_ids:
        return  # user retracted their vote

    user = answer.user
    selected = answer.option_ids[0]

    with get_db_context() as db:
        active_poll = db.get(ActivePoll, answer.poll_id)
        if active_poll is None:
            logger.warning("Received answer for unknown poll_id=%s", answer.poll_id)
            return

        is_correct = selected == active_poll.correct_option_id
        score = db.get(Score, (active_poll.chat_id, user.id))
        if score is None:
            score = Score(chat_id=active_poll.chat_id, user_id=user.id)
            db.add(score)

        score.username = user.username or user.first_name or "Unknown"
        score.total += 1
        if is_correct:
            score.correct += 1
