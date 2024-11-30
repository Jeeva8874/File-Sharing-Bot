#(©)NovaXTG



import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import *
from helper_func import subscribed, encode, decode, get_messages
from database.database import *





@Bot.on_message(filters.command('start') & filters.private)
async def start_command(client: Client, message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    text = message.text
    if len(text)>7:
        if client.link_one is not None and message.from_user.id not in ADMINS and not await is_requested_one(message):
            btn = [[
                InlineKeyboardButton(
                    "⇔ ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1 ⇔", url=client.link_one)
            ]]
            try:
                if client.link_two is not None and message.from_user.id not in ADMINS and not await is_requested_two(message):
                    btn.append(
                          [
                        InlineKeyboardButton(
                            "⇔ ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2 ⇔", url=client.link_two)
                          ]
                    )
            except Exception as e:
                print(e)
            try:
                btn.append(
                      [
                        InlineKeyboardButton(
                             text = 'Try Again',
                             url = f"https://t.me/{client.username}?start={message.command[1]}"
                        )
                    ]
                    )
            except (IndexError, ValueError):
                pass
            await client.send_message(
                chat_id=message.from_user.id,
                text="**‼ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ ᴏɴ ʙᴇʟᴏᴡ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴄʟɪᴄᴋ ᴛʀʏ ᴀɢᴀɪɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs ‼**",
                reply_markup=InlineKeyboardMarkup(inline_keyboard=btn),
                parse_mode=ParseMode.MARKDOWN
            )
            return
        if client.link_two is not None and message.from_user.id not in ADMINS and not await is_requested_two(message):
            btn = [[
                InlineKeyboardButton(
                    "⇔ ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ⇔", url=client.link_two)
            ]]
            try:
                if client.link_one is not None and message.from_user.id not in ADMINS and not await is_requested_one(message):
                    btn.append(
                          [
                        InlineKeyboardButton(
                            "⇔ ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ⇔", url=client.link_one)
                          ]
                    )
            except Exception as e:
                print(e)
            try:
                btn.append(
                      [
                        InlineKeyboardButton(
                             text = 'Try Again',
                             url = f"https://t.me/{client.username}?start={message.command[1]}"
                        )
                    ]
                    )
            except (IndexError, ValueError):
                pass
            await client.send_message(
                chat_id=message.from_user.id,
                text="**Please request Join the Following Channels to use this Bot!**",
                reply_markup=InlineKeyboardMarkup(inline_keyboard=btn),
                parse_mode=ParseMode.MARKDOWN
            )
            return
            
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Please wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if DISABLE_CHANNEL_BUTTON:
                reply_markup = msg.reply_markup
            else:
                reply_markup = None

            try:
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, caption = caption, parse_mode = ParseMode.HTML, reply_markup = reply_markup, protect_content=PROTECT_CONTENT)
            except:
                pass
        return
    else:
        await client.send_photo(
            chat_id=message.chat.id,
            photo=PIC,
            caption=START_MSG,
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton('👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ​', callback_data='owner_info'),
                    InlineKeyboardButton('🌿 sᴜᴘᴘᴏʀᴛ', callback_data='support')
                ], [
                    InlineKeyboardButton('🎭 ʜᴇʟᴘ 🎭', callback_data='help'),
                    InlineKeyboardButton('♻️ ᴀʙᴏᴜᴛ ♻️', callback_data='about')
                ]]
            )
        )
        return
#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##


@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)

    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()

        
        
#---------------------------------------------
def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]  


@Bot.on_message(filters.command('purge_one') & filters.private & filters.user(ADMINS))
async def purge_req_one(bot, message):
    r = await message.reply("`processing...`")
    await delete_all_one()
    await r.edit("**Req db Cleared**" )


@Bot.on_message(filters.command('purge_two') & filters.private & filters.user(ADMINS))
async def purge_req_two(bot, message):
    r = await message.reply("`processing...`")
    await delete_all_two()
    await r.edit("**Req db Cleared**" )
