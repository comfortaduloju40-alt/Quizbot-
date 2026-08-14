"""
/leaderboard command — top scorers for the current chat.
"""

from telegram import Update
from telegram.ext import ContextTypes

from app.database import get_db_context
from app.models import Score


async def leaderboard_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id

    with get_db_context() as db:
        rows = (
            db.query(Score)
            .filter(Score.chat_id == chat_id, Score.total > 0)
            .order_by(Score.correct.desc(), Score.total.asc())
            .limit(10)
            .all()
        )

    if not rows:
        await update.message.reply_text("No scores yet — run /quiz to get started!")
        return

    medals = ["🥇", "🥈", "🥉"]
    lines = ["*🏆 Leaderboard*", ""]
    for i, row in enumerate(rows):
        prefix = medals[i] if i < 3 else f"{i + 1}."
        lines.append(f"{prefix} {row.username} — {row.correct}/{row.total}")

    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")
