"""
Registers every command/message handler on the Application.
"""

from telegram.ext import Application, CommandHandler, PollAnswerHandler

from app.handlers.leaderboard import leaderboard_command
from app.handlers.quiz import handle_poll_answer, quiz_command
from app.handlers.start import help_command, start_command


def register_handlers(app: Application) -> None:
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("quiz", quiz_command))
    app.add_handler(CommandHandler("leaderboard", leaderboard_command))
    app.add_handler(PollAnswerHandler(handle_poll_answer))
