from pyrogram import filters, Client as Mbot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import DUMP_GROUP

subscribed_users = set()

@Mbot.on_message(filters.incoming & filters.private, group=-1)
async def monitor(client, message):
    if DUMP_GROUP:
        await message.forward(DUMP_GROUP)

@Mbot.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    channel_link = "https://t.me/FilmPrimiere"  
    
    if message.from_user.id not in subscribed_users:
        
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Подписаться", url=channel_link)
                ]
            ]
        )
        await message.reply("Подпишитесь на наш канал, чтобы продолжить.", reply_markup=keyboard)
        subscribed_users.add(message.from_user.id)

    else:
        await message.reply(f"Привет 👋👋 {message.from_user.mention()}\n Я простой бот Telegram, который может загружать из нескольких социальных сетей. В настоящее время поддерживает Instagram, TikTok, Twitter, Facebook, YouTube (музыка и шорты) и так далее....!")
        

@Mbot.on_message(filters.command("help") & filters.incoming)
async def help(Mbot, message):
          await message.reply("Это удобный бот, поэтому вы можете просто отправить сюда свой ролик из Instagram и разместить ссылки :) \n например: `https://www.instagram.com/reel/CZqWDGODoov/?igshid=MzRlODBiNWFlZA==`\n `post: ` `https://www.instagram.com/reel/CuCTtORJbDj/?igshid=MzRlODBiNWFlZA==`")
