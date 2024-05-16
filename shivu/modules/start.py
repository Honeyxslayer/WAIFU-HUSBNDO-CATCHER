import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

from shivu import application, PHOTO_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection 


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        
        await context.bot.send_message(chat_id=GROUP_ID, 
                                       text=f"New user Started The Bot..\n User: <a href='tg://user?id={user_id}'>{escape(first_name)})</a>", 
                                       parse_mode='HTML')
    else:
        
        if user_data['first_name'] != first_name or user_data['username'] != username:
            
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    

    if update.effective_chat.type== "private":
        
        
        caption = f"""
        ***ʜᴇʏ...ʙᴀʙʏ🀄***

***◎ ─━──━─❖─━──━─ ◎
⍟ ɪ ᴀᴍ ᴄᴀᴛᴄʜ ʏᴏᴜʀ ᴡᴀɪғᴜ ʙᴏᴛ,
ɪ sᴘᴀᴡɴ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs, ᴀɴᴅ ʟᴇᴛ ᴜsᴇʀs ᴄᴏʟʟᴇᴄᴛ ᴛʜᴇᴍ.
⍟ sᴏ ᴡʜᴀᴛ ᴀʀᴇ ʏᴏᴜ ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.
◎ ─━──━─❖─━──━─ ◎

ʜɪᴛ help ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ.***
        """
        
        keyboard = [
            [InlineKeyboardButton("✦ ᴀᴅᴅ ᴍᴇ ✦", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("⌬ sᴜᴘᴘᴏʀᴛ ⌬", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("⍟ ᴜᴘᴅᴀᴛᴇs ⍟", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("▣ ʜᴇʟᴘ ▣", callback_data='help')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice(PHOTO_URL)

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

    else:
        photo_url = random.choice(PHOTO_URL)
        keyboard = [
            [InlineKeyboardButton("✦ ᴀᴅᴅ ᴍᴇ ✦", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("⌬ sᴜᴘᴘᴏʀᴛ ⌬", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("⍟ ᴜᴘᴅᴀᴛᴇs ⍟", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("▣ ʜᴇʟᴘ ▣", callback_data='help')],
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption="🎴Alive!?... \n connect to me in PM For more information ",reply_markup=reply_markup )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
    
***➲ ʙᴇʟᴏᴡ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴜsᴇʀs:***

***━━━━━━━ ᴄᴏᴍᴍᴀɴᴅs ━━━━━━━***
***⎆/collect: ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀʀᴀᴛᴇʀ***
***⎆/fav: ᴀᴅᴅ ᴛᴏ ғᴀᴠᴏʀᴏɪᴛᴇ***
***⎆/trade: ᴛᴏ ᴛʀᴀᴅᴇ ᴄʜᴀʀᴀᴄᴛᴇʀs***
***⎆/gift: ᴛᴏ ɢɪғᴛ ᴀ ʜᴜsʙᴀɴᴅᴏ***
***⎆/collection: ᴛᴏ sᴇ ʏᴏᴜʀ ᴄᴏʟʟᴇᴄᴛɪᴏɴ***
***⎆/topgroups: ᴛᴏ sᴇᴇ ᴛᴏᴘ ɢʀᴏᴜᴘs***
***⎆/top: ᴛᴏ sᴇ ᴛᴏᴘ ᴜsᴇʀs***
***⎆/ctop: ʏᴏᴜʀ ᴄʜᴀᴛ ᴛᴏᴘ***
***⎆/changetime: ᴛᴏ ᴄʜᴀɴɢᴇ ᴡᴀɪғᴜ sᴘᴀᴡɴ ᴛɪᴍᴇ***
***━━━━━━━ ᴄᴏᴍᴍᴀɴᴅs ━━━━━━━***
   """
        help_keyboard = [[InlineKeyboardButton("⤾ Bᴀᴄᴋ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='markdown')

    elif query.data == 'back':

        caption = f"""
        ***ʜᴇʏ...ʙᴀʙʏ🀄***

***◎ ─━──━─❖─━──━─ ◎
⍟ ɪ ᴀᴍ ᴄᴀᴛᴄʜ ʏᴏᴜʀ ᴡᴀɪғᴜ ʙᴏᴛ,
ɪ sᴘᴀᴡɴ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs, ᴀɴᴅ ʟᴇᴛ ᴜsᴇʀs ᴄᴏʟʟᴇᴄᴛ ᴛʜᴇᴍ.
⍟ sᴏ ᴡʜᴀᴛ ᴀʀᴇ ʏᴏᴜ ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.
◎ ─━──━─❖─━──━─ ◎

ʜɪᴛ help ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ.***
        """

        
        keyboard = [
            [InlineKeyboardButton("✦ ᴀᴅᴅ ᴍᴇ ✦", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("⌬ sᴜᴘᴘᴏʀᴛ ⌬", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("⍟ ᴜᴘᴅᴀᴛᴇs ⍟", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("▣ ʜᴇʟᴘ ▣", callback_data='help')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='markdown')


application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)
