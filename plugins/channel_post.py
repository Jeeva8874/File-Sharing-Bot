#(©)NovaXTG

import asyncio
import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from bot import Bot
from config import *
from pyromod import Client
from helper_func import encode



#--------------------------------
import re
import os
import io
from shortzy import Shortzy
from helper_func import get_message_id
import requests
from telethon.tl import types
from urllib.parse import quote_plus
from utils.human_readable import humanbytes
from utils.database import Database
from asyncio import TimeoutError
from utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(DB_URI, name)
CMD = ["/", "."]
from imdb import IMDb
from io import BytesIO
from PIL import Image
imdb = IMDb()
from imdb._exceptions import IMDbDataAccessError
#--------------------------------



@Bot.on_message(filters.private & (filters.document | filters.video) & ~filters.command(['start','users','post','broadcast','batch','genlink','stats','imdb','saami']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    media = message.document or message.video or message.audio or message.photo
    filesize = humanbytes(media.file_size) if media.file_size else ""
    filename = media.file_name if media.file_name else ""
    link = await get_shortlink(f"{RXL}/{base64_string}")
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("💸 Yᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴛʜɪs ᴛᴏ ᴀɴʏ ᴄʜᴀᴛs 💸", url=f'https://telegram.me/share/url?url={link}')]])
    await reply_text.edit(f"<b>💎 ғɪʟᴇ ɴᴀᴍᴇ : </b> {filename} \n\n<b>💫 ғɪʟᴇ sɪᴢᴇ : </b> {filesize} \n\n<b>🦋 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ : </b><i><b>{link}</b></i>\n\n<i>© @Nova_Botz</i>", reply_markup=reply_markup, disable_web_page_preview = True)
    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)



#--------------------------------SHORTENER------------------------------------------------#

async def get_shortlink(link):
    url = 'https://tnshort.net/api'
    params = {'api': SHORTENER_API, 'url': link}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            return data["shortenedUrl"]


#--------------------------------SHORTENER------------------------------------------------#


#----------------------------------POST------------------------------------------------------#





@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('post'))
async def post(client: Client, message: Message):
    try:
        num_files = await client.ask(
            text="<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴜsᴇ ᴏᴜʀ ʀᴀʀᴇ ᴍᴏᴠɪᴇ ᴘᴏsᴛ ғᴇᴀᴛᴜʀᴇ :) ᴄᴏᴅᴇᴅ ʙʏ <a href=https://t.me/NovaXTG>ɴᴏᴠᴀxᴛɢ</a> 👨🏼‍💻\n\n👉🏻 sᴇɴᴅ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ғɪʟᴇs ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ 👈🏻\n\n‼️ ɴᴏᴛᴇ : ᴏɴʟʏ ɴᴜᴍʙᴇʀ</b>",
            chat_id=message.from_user.id, filters=filters.text, timeout=60,
            disable_web_page_preview=True
        )
        num_files = int(num_files.text)
    except Exception as e:
        print(f"Error in getting number of files: {e}")
        return
    media_list = []
    for i in range(num_files):
        try:
            forward_message = await client.ask(
                text=f"<b>⏩ ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ɴᴏ : {i+1} ғɪʟᴇ</b>",
                chat_id=message.from_user.id, filters=(filters.video | filters.document), timeout=60
            )
        except Exception as e:
            print(f"Error in getting forward message: {e}")
            return
        
        post_message1 = await forward_message.copy(chat_id=CHANNEL_ID, disable_notification=True)
        post_message = await forward_message.copy(chat_id=BIN_CHANNEL, disable_notification=True)
        media = forward_message.document or forward_message.video
        media_list.append((media, post_message1.id, forward_message, post_message.id))
        await forward_message.delete()
        await forward_message.sent_message.delete()

    filename_message = await client.ask(
        text="<b>ɴᴏᴡ sᴇɴᴅ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ ᴍᴏᴠɪᴇ\n\nᴇx : ᴀɴʙᴇ sɪᴠᴀᴍ (2003) ᴛᴀᴍɪʟ ʜᴅʀɪᴘ</b>",
        chat_id=message.from_user.id, filters=filters.text, timeout=60
    )
    filename = filename_message.text.strip() if filename_message else "Unknown Filename"
    await filename_message.sent_message.delete()
    await filename_message.delete()
    
    direct_telegram_links = []
    stream_links = []
    online_links = []

    for i, (media, msg_id, forward_message, post_message_id) in enumerate(media_list):
        string = f"get-{msg_id * abs(CHANNEL_ID)}"
        base64_string = await encode(string)
        file_size = humanbytes(media.file_size) if media.file_size else ""
        linkk = await get_shortlink(f"{RXL}/{base64_string}")
        link = f"<b>{file_size} :</b> {linkk}\n"
        direct_telegram_links.append(link)
        direct_telegram_lines = '\n'.join(direct_telegram_links)

    # Construct unique stream links for each file
        online_linkk = await get_shortlink(f"{URL}{str(post_message_id)}/{quote_plus(get_name(forward_message))}?hash={get_hash(forward_message)}")  # Using post_message_id
        stream_linkk = await get_shortlink(f"{URL}watch/{str(post_message_id)}/{quote_plus(get_name(forward_message))}?hash={get_hash(forward_message)}")  # Using post_message_id
        stream_link = f"<b>{file_size} :</b> {stream_linkk}\n"
        online_link = f"<b>{file_size} :</b> {online_linkk}\n"
        stream_links.append(stream_link)
        online_links.append(online_link)
        stream_lines = '\n'.join(stream_links)
        online_lines = '\n'.join(online_links)

# Join all links outside the loop after constructing all links


    

    imdb_info = await get_poster(extract_movie_name(filename))
    
    # Check if IMDb info is found
    if imdb_info:
        # Download the IMDb poster image
        imdb_image_response = requests.get(imdb_info['poster'])
        imdb_image_data = io.BytesIO(imdb_image_response.content)
    else:
        # Use a default image if IMDb info is not found
        # Replace 'common_image_url' with the URL of the common image you want to use
        common_image_url = 'https://telegra.ph/file/74707bb075903640ed3f6.jpg'
        imdb_image_data = io.BytesIO(requests.get(common_image_url).content)
    # Send the IMDb poster image as a photo along with other details
    await client.send_photo(
        chat_id=message.chat.id,
        photo=imdb_image_data,
        caption=f'<b>🎬 {filename}\n\n'
                f'✅ Note : [ <a href=https://t.me/tnlinkdown/9>How to download</a> ]\n\n'
                f'🔻 Direct Telegram Files 🔻\n\n{direct_telegram_lines}\n'
                f'🔻 Stream / Fast Download 🔻\n\n{stream_lines}\n'
                f'@RX_LinkZz || @RolexMoviesOXO\n\n'
                f'Share and Support Us 🫶🏻</b>'
    )




#---------------------------------IMDB--------------------------------------#

async def get_poster(query, bulk=False, id=False, file=None):
    if not id:
        query = query.strip().lower()
        title = query
        year = re.findall(r'[1-2]\d{3}$', query, re.IGNORECASE)
        if year:
            year = list_to_str(year[:1])
            title = (query.replace(year, "")).strip()
        elif file is not None:
            year = re.findall(r'[1-2]\d{3}', file, re.IGNORECASE)
            if year:
                year = list_to_str(year[:1])
        else:
            year = None
        movieid = imdb.search_movie(title.lower(), results=10)
        if not movieid:
            return None
        if year:
            filtered = list(filter(lambda k: str(k.get('year')) == str(year), movieid))
            if not filtered:
                filtered = movieid
        else:
            filtered = movieid
        movieid = list(filter(lambda k: k.get('kind') in ['movie', 'tv series'], filtered))
        if not movieid:
            movieid = filtered
        if bulk:
            return movieid
        movieid = movieid[0].movieID
    else:
        movieid = query
    movie = imdb.get_movie(movieid)
    if movie.get("original air date"):
        date = movie["original air date"]
    elif movie.get("year"):
        date = movie.get("year")
    else:
        date = "N/A"
    plot = ""
    if not True:  # Replace True with the condition you want
        plot = movie.get('plot')
        if plot and len(plot) > 0:
            plot = plot[0]
    else:
        plot = movie.get('plot outline')
    if plot and len(plot) > 800:
        plot = plot[0:800] + "..."

    return {
        'title': movie.get('title'),
        'votes': movie.get('votes'),
        "aka": list_to_str(movie.get("akas")),
        "seasons": movie.get("number of seasons"),
        "box_office": movie.get('box office'),
        'localized_title': movie.get('localized title'),
        'kind': movie.get("kind"),
        "imdb_id": f"tt{movie.get('imdbID')}",
        "cast": list_to_str(movie.get("cast")),
        "runtime": list_to_str(movie.get("runtimes")),
        "countries": list_to_str(movie.get("countries")),
        "certificates": list_to_str(movie.get("certificates")),
        "languages": list_to_str(movie.get("languages")),
        "director": list_to_str(movie.get("director")),
        "writer": list_to_str(movie.get("writer")),
        "producer": list_to_str(movie.get("producer")),
        "composer": list_to_str(movie.get("composer")),
        "cinematographer": list_to_str(movie.get("cinematographer")),
        "music_team": list_to_str(movie.get("music department")),
        "distributors": list_to_str(movie.get("distributors")),
        'release_date': date,
        'year': movie.get('year'),
        'genres': list_to_str(movie.get("genres")),
        'poster': movie.get('full-size cover url'),
        'plot': plot,
        'rating': str(movie.get("rating")),
        'url': f'https://www.imdb.com/title/tt{movieid}'
    }


@Bot.on_message(filters.command('imdb') & filters.private)
async def imdb_command(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply("Please provide a movie name with the /imdb command.")
        return

    movie_name = ' '.join(message.command[1:])
    
    try:
        poster_info = await get_poster(movie_name)
        
        if poster_info:
            # Download the poster image
            image_response = requests.get(poster_info['poster'])
            image_data = io.BytesIO(image_response.content)

            # Send the poster image as a photo along with other details
            await client.send_photo(
                chat_id=message.chat.id,
                photo=image_data,
                caption=f'Movie Poster for {poster_info["title"]}\n'
                        f'Rating: {poster_info["rating"]}\n'
                        f'Genres: {poster_info["genres"]}\n'
                        f'Plot: {poster_info["plot"]}\n'
                        f'IMDb URL: {poster_info["url"]}'
            )

        else:
            await message.reply_text('Movie not found. Please check the movie name and try again.')

    except Exception as e:
        print(f"An error occurred: {e}")
        await message.reply_text('An error occurred while fetching movie information.')

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


def list_to_str(input_list):
    if not input_list:
        return "N/A"
    return ', '.join(str(element) for element in input_list)

def extract_movie_name(filename):
    # Updated pattern to capture movie name along with year and exclude anything after it
    pattern = r'(.+?\(\d{4}\)).*'
    match = re.match(pattern, filename)
    return match.group(1) if match else filename
