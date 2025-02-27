from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv
import os
import talk_lkj as tk 
import gemini

#.env 파일 로드
load_dotenv()
TOKEN = os.getenv('TTOKEN')

#TRIGGER_WORDS = {
#    "안녕":"안녕하세요 ! 저는 chat880_bot입니다👻 ",
#     "정보":"어떤 정보가 필요하세요??😈 ",
#     "기분":"저는 기분이 좋아요👾 "
#}

async def start(update,context) : #비동기 처리(thread)
    await update.message.reply_text("안녕하세요! 저는 chat880_bot입니다.무엇을 도와드릴까요?")

async def send_photo(update,context):
    photo_url = "https://th.bing.com/th/id/OIP.S6YGTko6BCK_TPs3ZlwifQHaLH?w=203&h=304&c=7&r=0&o=5&pid=1.7"
    await update.message.reply_photo(photo=photo_url,caption="사진이미지 불러왔어요~")

async def monitor_chat(update,context) : 
    user_text = update.message.text #감지된 메세지들  #택배 알맹이 
    chat_id = update.message.chat_id #메세지가 온 채팅방 # 택배 주소지

    if "gpt" in user_text :
        res = gemini.aiai(user_text.replace("gpt",""))
        await context.bot.send_message(chat_id = chat_id,text=res,parse_mode ="MarkdownV2")    
    elif "영화정보" in user_text :
        # await 영화정보크롤링() 함수를 실행 
        pass
    elif "사진줘" in user_text :
        await send_photo(update,context)
    else:    
        for key,res in tk.TRIGGER_WORDS.items():
            if key in user_text :  
                await context.bot.send_message(chat_id = chat_id,text=res)
                break # 한 개의 키워드에만 반응 
def main():
    app = Application.builder().token(TOKEN).build()

    #명령어 핸들러 추가 
    app.add_handler(CommandHandler("start",start))

    # 응답 핸들러 추가 
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,monitor_chat))
   
    print("텔레그램 봇이 실행중입니다. 모니터링 중...")
    app.run_polling()

if __name__ == "__main__":
    main()
