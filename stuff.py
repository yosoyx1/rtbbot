import os, datetime, sys, json
from pyrogram.types import ReplyKeyboardMarkup


token = os.getenv("token", "") #telegram bot token
app_id = os.getenv("app_id", "")
app_hash = os.getenv("app_hash", "")
logGroup =  os.getenv("logGroup", False) # change this to group id

x = datetime.datetime.utcnow()
i = x + datetime.timedelta(hours=3)
y = i.strftime("%Y-%m-%d_%I:%M%P")
print(y)
print("My PID is:", os.getpid())


if len(str(token)) < 5: print("пожалуйста, поместите свой токен в env"); sys.exit(1)


keybd = ReplyKeyboardMarkup([
     ['🤖 Пинг', '⁉️ Помощь', '👀 Что это?'],
     ['⚠️ Репорт', '😊 Спасибо']], resize_keyboard=True)


stk0 = "CAADBAADrgcAAnILQFPgjUtxHDj-oQI"
stk1 = "CAADBAADlQoAAo8RQFOWkvFydBKJlwI"
stk2 = "CAADBAADSAsAAn_eOFPurvLfXO2hzAI"
stk3 = "CAADBAAD0QoAAkKSOFND8vqd0dBlhQI"
stk4 = "CAADBAADRgkAAhzwOFMQTCV2uQABp4wC"
stk5 = "CAADBAADHwoAAgTjOFPwcaIN8VE3uQI"
stk6 = "CAADBAAD2AgAAv1sOFOBvhMuUqdpVgI"
stk7 = "CAADBAAD_AkAAzI4U1zm0zS8ZmfzAg"
stk8 = "CAADBAADZQoAAvmvQFN_0Kq6nbL7IAI"
fthl = "CAACAgEAAxkBAAEDhMhhv1eWCc2bLbg8V5ZW2w7v5lVz0QAClQEAAjT0-UWjXL_zWuG_FiME"

start_msg0 = "Привет! Я очень быстро скачиваю видео с **RUTUBE** \nПросто пришлите мне любую ссылку на видео, чтобы его скачать.\n\nПоддержка: @dlph1n"

help_text = """ Hi %s,

Welcome to **PLACE_HOLDER** 👋

I can download rutube links with instant speed
just send a link and grab a coffee

🔴🔴 **Notes** 🔴🔴
┏━━━━━━━━━━━━━━━━━━━━━━
• **Bot** is completely free for use,
• So please don't abuse/spam the bot
• After **Download Finshes** you can save to your downloads directory,
• Directly by long pressing a song then **Click save to Downloads**
• Reply to **/report** to report any bugs
• Make sure you report the error link too
• Check out **/about**
┗━━━━━━━━━━━━━━━━━━━━━━━

** ⚠️ REPORT any bugs at @xd2222 ⚠️ **"""

about_text = """
╭────[🔅Rutube Bᴏᴛ🔅]───⍟
│
├<b>🤖 Bot Name : Rutube</b>
│
├<b>💢 Source : <a href='https://github.com/Justxd22/rutubeXD'>Justxd22/rutubeXD</a></b>
│
├<b>🌐 Server : <a href='https://heroku.com'>Heroku</a></b>
│
├<b>📕 Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>
│
├<b>㊙ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>
│
├<b>👨‍💻 Developer : <a href='https://github.com/Justxd22'>Justxd22</a></b>
│
╰──────[Thanks 😊]───⍟"""

msg0 = "**Получение ссылки...**"
msg1=  "**Извините, но я не могу скачать это видео, оно приватное**"
msg2 = "**Скачивание...**"
msg3 = "**Загрузка завершена**\n\n**Отправка**..."
msg4 = "**Пожалуйста, выберите качество видео**, которое вы хотели бы скачать"
msg5 = "**Пожалуйста, выберите качество звука** для выбранного видео."
msg6 = "**Получили ошибку 429 (HTTP Too many reqests)** \nпожалуйста, отправьте эту проблему в поддержу: @dlph1in \n Я перезагружусь сейчас, пожалуйста, повторите попытку через 1 мин."
msg7 = "**Видео скачано, скачивание аудио....**"
msg8 = "**Код ошибки %s** Пожалуйста, сообщите об этом в поддержку: @dlph1in"
msg9 = "**Объединение видео с аудио вы выбрали...**"
msg10 = "**А?** Вы не хотите видео или аудио,\nтогда что вы хотите???"
msg11 = "**Пожалуйста, пришлите действующую ссылку на видео**"
msg12 = "**Извините, запрашиваемая вами ссылка ограничена по возрасту**"
msg13 = "**Извините, это видео является приватным**"
msg14 = "**Извините, это видео заблокировано в регионе**"
msg16 = "**Regex Error, пожалуйста, сообщите об этой проблеме вместе со ссылкой в поддержку: @dlph1in"

logger1 = "**Новый пользователь**"
logger2 = "**Пользователь отправил**:\n\n"
logger3 = "**Пользователь хочет сообщить** \n\n"
logger4 = "Вы должны сказать что-то вроде**: отчет видео не воспроизводится**\n или ответить на сообщение\n\n** ⚠️ Отправляйте ошибки в поддержку @dlph1in  ⚠️ **"
logger5 = "**Пользователь счастлив** говорит спасибо"


headers = {
       'Connection': 'keep-alive',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
       'cache-control': 'max-age=0',
       'Content-Type': 'application/json',
       'Accept': '*/*',
       'Origin': 'https://rutube.ru',
       'Sec-Fetch-Site': 'same-site',
       'Sec-Fetch-Mode': 'cors',
       'Sec-Fetch-Dest': 'empty',
       'Accept-Language': 'en-US,en;q=0.9'}
