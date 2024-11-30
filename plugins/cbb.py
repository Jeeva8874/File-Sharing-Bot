#(©)NovaXTG

from pyrogram import __version__
from bot import Bot
from config import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/{BOT_USERNAME}><b>{BOT_NAME}</b></a>\n\n‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/NovaxTG><b>ɴᴏᴠᴀ</b></a>\n\n‣ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org><b>ᴘʏᴛʜᴏɴ</b></a>\n\n‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>\n\n‣ ʜᴏsᴛᴇᴅ ᴏɴ : <a href=heroku.com><b>ʜᴇʀᴏᴋᴜ</b></a>\n\n‣ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Nova_Botz><b>ɴᴏᴠᴀ ʙᴏᴛᴢ ™</b></a>\n</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('♙ ʜᴏᴍᴇ', callback_data='home'),
                        InlineKeyboardButton('ᴄʟᴏsᴇ ⊝', callback_data='close')
                    ]
                ]
            )
        )
    elif data == "owner_info":
        await query.message.edit_text(
            text = f"<b>↞⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟↠</b>\n\n<b>• ꜰᴜʟʟ ɴᴀᴍᴇ :</b> | ɴᴏᴠᴀ ☣ |\n<b>• ᴜꜱᴇʀɴᴀᴍᴇ : @NovaxTG</b>\n<b>• ɴᴀᴛɪᴠᴇ : ʀᴏsᴀʀɪᴏ, ᴀʀɢᴇɴᴛɪɴᴀ </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('♙ ʜᴏᴍᴇ', callback_data='home'),
                        InlineKeyboardButton('ᴄʟᴏsᴇ ⊝', callback_data='close')
                    ]
                ]
            )
        )
    elif data == "support":
        await query.message.edit_text(
            text = f"<b>ᴜᴘᴅᴀᴛᴇs ᴀɴᴅ ᴄᴏɴᴛᴀᴄᴛ ᴍᴏᴅᴜʟᴇ 🌿</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [[
            InlineKeyboardButton('ʏᴛᴜʙᴇ', url='https://www.youtube.com/@Nova_Botz'),
            InlineKeyboardButton('​ᴘᴀɪᴅ ᴅᴇᴠ', url='t.me/NovaxTG'),
            InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs​', url='t.me/Nova_Botz')
            ],[
            InlineKeyboardButton('✇ ʜᴏᴍᴇ ✇', callback_data="home")
                ]]
            ))
    elif data == "connect":
        await query.message.edit_text(
            text = f"<b>❉ Hᴏᴡ Tᴏ Cᴏɴɴᴇᴄᴛ Yᴏᴜʀ Oᴡɴ Sʜᴏʀᴛɴᴇʀ\n\n➥ Iғ Yᴏᴜ Wᴀɴᴛ Tᴏ Cᴏɴɴᴇᴄᴛ Yᴏᴜʀ Oᴡɴ Sʜᴏʀᴛɴᴇʀ Tʜᴇɴ Jᴜsᴛ Sᴇɴᴅ Tʜᴇ Gɪᴠᴇɴ Dᴇᴛᴀɪʟs Iɴ Cᴏʀʀᴇᴄᴛ Fᴏʀᴍᴀᴛ.\n\n➥ ғᴏʀᴍᴀᴛ ↓↓↓\n<code>/shortlink sʜᴏʀᴛɴᴇʀsɪᴛᴇ sʜᴏʀᴛɴᴇʀᴀᴘɪ</code>\n\n➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓\n<code>/set_shortner tnshort.net b6aace46d40c605fff8e0cafbcd8fbe416851f4d</code>\n\nɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ᴀᴄᴄᴏᴜɴᴛ, ᴍʏ ᴏᴘᴛɪᴏɴ <a href=https://tnshort.net/ref/Bharathraj><b>ᴛɴsʜᴏʀᴛ.ɴᴇᴛ</b></a> ʙᴇᴄᴀᴜsᴇ ɪᴛs CPM ᴡᴀs 7+</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('♙ ʜᴏᴍᴇ', callback_data='home'),
                        InlineKeyboardButton('ᴄʟᴏsᴇ ⊝', callback_data='close')
                    ]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_text(
            text = f"<b>⊹ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ⊹\n\n⇒ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ\n\n⇒ ᴛʜɪs ʙᴏᴛ ᴡɪʟʟ sᴇɴᴅ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ \n\n⇒ ᴛʜɪs ʙᴏᴛ ʜᴀs /post ɴᴇᴡ ʀᴀʀᴇ ᴍᴏᴠɪᴇ ᴘᴏsᴛ ғᴇᴀᴛᴜʀᴇ, /tutorial ғᴏʀ ᴍᴏᴠɪᴇ ᴘᴏsᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ. \n\nɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ ɪɴ ᴛʜɪs ʙᴏᴛ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ\n\n⇒ ғᴏʀ ᴘᴀɪᴅ ᴅᴇᴠᴇʟᴏᴘɪɴɢ : <a href=https://t.me/NovaxTG><b>ɴᴏᴠᴀ</b></a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('♙ ʜᴏᴍᴇ', callback_data='home'),
                        InlineKeyboardButton('ᴄʟᴏsᴇ ⊝', callback_data='close')
                    ]
                ]
            )
        )
    elif data == "home":
        await query.message.edit_text(
            text = f"<b>ɪ ᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ. sᴇɴᴅ ᴀɴʏ ғɪʟᴇ ᴛᴏ ᴍᴇ, ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴅɪʀᴇᴄᴛ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ʟɪɴᴋ. ʀᴀʀᴇ ᴍᴏᴠɪᴇ ᴘᴏsᴛ ᴏᴘᴛɪᴏɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ 🥂\n\nғᴏʀ ᴘᴏsᴛ ᴏᴘᴛɪᴏɴ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ /tutorial !!</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [[
            InlineKeyboardButton('〆 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ 〆', url=f'http://t.me/{BOT_USERNAME}?startchannel=true')
            ],[
            InlineKeyboardButton('👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ​', callback_data='owner_info'),
            InlineKeyboardButton('🌿 sᴜᴘᴘᴏʀᴛ', callback_data='support')
            ],[      
            InlineKeyboardButton('🎭 ʜᴇʟᴘ 🎭', callback_data='help'),
            InlineKeyboardButton('♻️ ᴀʙᴏᴜᴛ ♻️', callback_data='about')
            ]]
            ))
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
