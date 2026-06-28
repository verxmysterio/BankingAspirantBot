import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

GROUP_LINK = "https://t.me/+6MrZJrJ8MmYyZGU1"

ABOUT_TEXT = """
🏦 <b>Banking Aspirants 2027</b>

Welcome to <b>Banking Aspirants Manager</b>, the official companion bot of our private study group.

━━━━━━━━━━━━━━━━━━━━━━

🎯 <b>Our Goal</b>

We are a small group of dedicated friends preparing together to secure Banking jobs in 2027. This bot helps us keep all our study resources organized in one place so that everyone can access them anytime.

━━━━━━━━━━━━━━━━━━━━━━

📚 <b>Available Resources</b>

• Quantitative Aptitude
• Reasoning Ability
• English Language
• General Awareness
• Computer Knowledge
• Banking Awareness
• Current Affairs

━━━━━━━━━━━━━━━━━━━━━━

🤝 <b>Our Motto</b>

Study Together
Support Each Other
Stay Consistent
Achieve Success Together

━━━━━━━━━━━━━━━━━━━━━━

👨‍💻 <b>Developer</b>

Aakash Kumar Singh
Telegram: @verx_mysterio

<i>Good Luck to all Banking Aspirants! 🌟</i>
"""

SUBJECTS = {
    "📘 Quant": "https://drive.google.com/drive/folders/1dnqkjk-rxvH_egVHQlSWkOhGU_wGUZGa?usp=sharing",
    "🧠 Reasoning": "https://drive.google.com/drive/folders/1fk-YZ8Ik_SPIvF3QQaPR1Msg4EefmZmV?usp=sharing",
    "🇬🇧 English": "https://drive.google.com/drive/folders/1s_a20A0k-UWcn_xbOi2PNPsf4T4bpsCW?usp=sharing",
    "🌍 General Awareness": "https://drive.google.com/drive/folders/1dkT5KzLozh8pmuxudmj6CTMgc4gAvRvb?usp=sharing",
    "💻 Computer": "https://drive.google.com/drive/folders/1QHdvfVgu0kNELLnQO0XYuiAFt4fDZ4Bh?usp=sharing",
    "🏦 Banking Awareness": "https://drive.google.com/drive/folders/1d2hkfHBE-k9o_SX-_TUa4osmLdMIBuBK?usp=sharing",
    "📰 Current Affairs": "https://drive.google.com/drive/folders/1VrhpWxcC9oVtQptTxVsRRnEoTuxNbM6f?usp=sharing",
}