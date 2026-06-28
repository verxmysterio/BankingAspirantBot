from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import SUBJECTS, GROUP_LINK


def home_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("📚 Notes", callback_data="notes")
        ],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def notes_keyboard():
    keyboard = []

    # Subject buttons (one per row)
    for subject in SUBJECTS.keys():
        keyboard.append([
            InlineKeyboardButton(subject, callback_data=f"subject|{subject}")
        ])

    # Navigation buttons
    keyboard.append([
        InlineKeyboardButton("⬅ Back", callback_data="home"),
        InlineKeyboardButton("🏠 Home", callback_data="home")
    ])

    return InlineKeyboardMarkup(keyboard)


def subject_keyboard(subject_name):
    keyboard = [
        [
            InlineKeyboardButton(
                "📂 Open Google Drive",
                url=SUBJECTS[subject_name]
            )
        ],
        [
            InlineKeyboardButton("⬅ Back", callback_data="notes"),
            InlineKeyboardButton("🏠 Home", callback_data="home")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


def about_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                "👥 Open Study Group",
                url=GROUP_LINK
            )
        ],
        [
            InlineKeyboardButton("📚 Notes", callback_data="notes")
        ],
        [
            InlineKeyboardButton("🏠 Home", callback_data="home")
        ]
    ]

    return InlineKeyboardMarkup(keyboard)