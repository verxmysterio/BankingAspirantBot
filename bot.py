from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from config import BOT_TOKEN
from database import init_db
from handlers import (
    start,
    about,
    stats,
    broadcast,
    button,
)


def main():
    # Initialize database
    init_db()

    # Create application
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("broadcast", broadcast))

    # Button callbacks
    app.add_handler(CallbackQueryHandler(button))

    print("===================================")
    print(" Banking Aspirant Manager Started ")
    print("===================================")

    # Start bot
    app.run_polling()


if __name__ == "__main__":
    main()