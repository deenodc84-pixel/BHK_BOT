import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from config import BOT_TOKEN, COMMANDS
from data import *

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcome_message = f"""
🏀 Welcome to BallHK, {user.first_name}!

I'm your ultimate basketball companion! Get NBA stats, player info, game schedules, and fun trivia instantly.

📌 Use /help to see all available commands.

Brought to you with ❤️ for basketball fans!
"""
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    help_text = """
🏀 *BallHK Commands List*

/start - Start the bot & welcome message
/help - Show this help menu
/stats [player_name] - Get player statistics
/champions - See NBA champions by year
/teams - List all NBA teams
/schedule - View upcoming games
/trivia - Random basketball trivia
/facts - Random basketball facts
/records - NBA all-time records
/about - About this bot

*Examples:*
/stats LeBron James
/stats Michael Jordan
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send information about the bot."""
    about_text = """
🏀 *BallHK Bot*

Version: 1.0
Purpose: NBA stats, facts, and trivia

*Features:*
• Historical NBA champions data
• All-time player records
• Upcoming game schedules
• Basketball trivia and facts

*Built with:*
• Python + python-telegram-bot
• Hosted on Railway

Created for basketball enthusiasts worldwide!
"""
    await update.message.reply_text(about_text, parse_mode='Markdown')

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get stats for a basketball player."""
    if not context.args:
        await update.message.reply_text(
            "🏀 Please provide a player name!\n"
            "Example: /stats LeBron James"
        )
        return
    
    player_name = ' '.join(context.args)
    player_stats = get_player_stats(player_name)
    
    if player_stats:
        stats_text = f"""
🏀 *{player_stats['name']} Statistics*

📊 Points: {player_stats['points']:,}
💨 Rebounds: {player_stats['rebounds']:,}
🎯 Assists: {player_stats['assists']:,}
🏆 Championships: {player_stats['championships']}
⭐ MVP Awards: {player_stats['mvp_awards']}
"""
        await update.message.reply_text(stats_text, parse_mode='Markdown')
    else:
        await update.message.reply_text(
            f"❌ Sorry, I couldn't find stats for '{player_name}'.\n"
            "Try these players: LeBron James, Michael Jordan, Kobe Bryant, Stephen Curry"
        )

async def champions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show NBA champions."""
    champions_text = "🏆 *NBA Champions (2010-2023)*\n\n"
    for year, team in sorted(NBA_CHAMPIONS.items(), reverse=True):
        champions_text += f"• {year}: {team}\n"
    
    await update.message.reply_text(champions_text, parse_mode='Markdown')

async def teams(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show all NBA teams."""
    teams_text = "🏀 *All 30 NBA Teams*\n\n"
    teams_text += "• " + "\n• ".join(NBA_TEAMS)
    
    await update.message.reply_text(teams_text, parse_mode='Markdown')

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show upcoming games."""
    games = get_upcoming_games()
    schedule_text = "📅 *Upcoming NBA Games*\n\n"
    for game in games:
        schedule_text += f"• {game}\n"
    
    await update.message.reply_text(schedule_text, parse_mode='Markdown')

async def trivia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a random trivia question."""
    question = random.choice(TRIVIA_QUESTIONS)
    trivia_text = f"🧠 *Basketball Trivia*\n\n{question['question']}\n\n"
    trivia_text += f"💡 *Answer:* {question['answer']}"
    
    await update.message.reply_text(trivia_text, parse_mode='Markdown')

async def facts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send random basketball facts."""
    fact = random.choice(BASKETBALL_FACTS)
    await update.message.reply_text(f"🏀 *Did you know?*\n\n{fact}", parse_mode='Markdown')

async def records(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show NBA all-time records."""
    records_text = "📊 *NBA All-Time Records*\n\n"
    
    records_text += "*Most Points:*\n"
    for player, points in ALL_TIME_POINTS[:3]:
        records_text += f"• {player}: {points:,}\n"
    
    records_text += "\n*Most Rebounds:*\n"
    for player, rebounds in ALL_TIME_REBOUNDS[:3]:
        records_text += f"• {player}: {rebounds:,}\n"
    
    records_text += "\n*Most Assists:*\n"
    for player, assists in ALL_TIME_ASSISTS[:3]:
        records_text += f"• {player}: {assists:,}\n"
    
    await update.message.reply_text(records_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle non-command messages."""
    message_text = update.message.text.lower()
    
    # Simple keyword responses
    if 'hello' in message_text or 'hi' in message_text:
        await update.message.reply_text("🏀 Hello! Use /help to see what I can do!")
    elif 'thanks' in message_text or 'thank you' in message_text:
        await update.message.reply_text("🏀 You're welcome! Enjoy the game! 🏀")
    elif 'ball' in message_text or 'basketball' in message_text:
        await update.message.reply_text("🏀 Basketball is life! What would you like to know?")
    else:
        await update.message.reply_text(
            "🏀 I'm not sure what you mean. Try /help to see available commands!"
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors."""
    logger.warning(f'Update {update} caused error {context.error}')

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("champions", champions))
    application.add_handler(CommandHandler("teams", teams))
    application.add_handler(CommandHandler("schedule", schedule))
    application.add_handler(CommandHandler("trivia", trivia))
    application.add_handler(CommandHandler("facts", facts))
    application.add_handler(CommandHandler("records", records))

    # Handle non-command messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Add error handler
    application.add_error_handler(error_handler)

    # Start the Bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
