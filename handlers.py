from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID, ABOUT_TEXT
from database import (
    add_user,
    get_total_users,
    get_all_user_ids,
)
from keyboards import (
    home_keyboard,
    notes_keyboard,
    subject_keyboard,
    about_keyboard,
)


# --------------------------
# /start
# --------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    add_user(
        user.id,
        user.first_name,
        user.username,
    )

    text = f"""
👋 Welcome <b>{user.first_name}</b>!

🎯 <b>Banking Aspirants 2027</b>

Your one-stop destination for Banking Exam Preparation.

Choose an option below.
"""

    await update.message.reply_text(
        text,
        parse_mode="HTML",
        reply_markup=home_keyboard(),
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text=ABOUT_TEXT,
        parse_mode="HTML",
        reply_markup=about_keyboard(),
    )
# --------------------------
# /stats
# --------------------------
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    total = get_total_users()

    await update.message.reply_text(
        f"📊 Total Users : <b>{total}</b>",
        parse_mode="HTML",
    )


# --------------------------
# /broadcast
# --------------------------
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    if not context.args:
        await update.message.reply_text(
            "Usage:\n\n/broadcast Your message"
        )
        return

    message = " ".join(context.args)

    users = get_all_user_ids()

    success = 0

    for user_id in users:

        try:
            await context.bot.send_message(
                chat_id=user_id,
                text=message,
            )
            success += 1

        except Exception:
            pass

    await update.message.reply_text(
        f"✅ Broadcast sent to {success} users."
    )


# --------------------------
# Button Clicks
# --------------------------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    data = query.data

    # ---------------- HOME ----------------

    if data == "home":

        await query.edit_message_text(
            text="""
👋 Welcome!

🎯 Banking Aspirants 2027

Choose an option below.
""",
            reply_markup=home_keyboard(),
        )

        return

    # ---------------- NOTES ----------------

    if data == "notes":

        await query.edit_message_text(
            text="📚 Select a Subject",
            reply_markup=notes_keyboard(),
        )

        return

    # ---------------- ABOUT ----------------

    if data == "about":

        await query.edit_message_text(
            text=ABOUT_TEXT,
            parse_mode="HTML",
            reply_markup=about_keyboard(),
        )

        return

    # ---------------- SUBJECT ----------------

    if data.startswith("subject|"):

        subject = data.split("|")[1]

        await query.edit_message_text(
            text=f"📚 <b>{subject}</b>\n\nClick the button below to open the Google Drive folder.",
            parse_mode="HTML",
            reply_markup=subject_keyboard(subject),
        )