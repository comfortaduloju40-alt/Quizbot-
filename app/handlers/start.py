"""
/start and /help command handlers.
"""

from telegram import Update
from telegram.ext import ContextTypes

_HELP_TEXT = (
    "🧠 *Quiz Bot*\n\n"
    "• `/quiz` — get a random question\n"
    "• `/leaderboard` — see top scorers in this chat\n\n"
    "Add me to a group and everyone can compete — I track correct "
    "answers per person, per chat."
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(_HELP_TEXT, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(_HELP_TEXT, parse_mode="Markdown")
