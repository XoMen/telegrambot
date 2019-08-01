from telegram import ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, Job, InlineQueryHandler
from uuid import uuid4
from random import randint
import requests
url = "https://api.telegram.org/bot840337808:AAGlf-0La9tWrY7bJrvZ68GQoHCwo7_R6I8"

updater = Updater('840337808:AAGlf-0La9tWrY7bJrvZ68GQoHCwo7_R6I8')

def start(bot, update,	args):
  chat_id = update.message.chat_id
  # ReplyKeyboard_method(bot, update)
  bot.sendChatAction(chat_id, "TYPING")
  bot.sendMessage('-1001324862919', f"{args[0]} {args[1]} ")

# def send_mess(text):
#     params = {'chat_id':1337638187, 'text': text}
#     response = requests.post(url + 'sendMessage', data=params)
#     return response


# send_mess("hello") 

def hello(bot, update):
  chat_id = update.message.chat_id
  bot.sendMessage(chat_id, "hello how are you?")
 

def send_photo_method(bot, update):
  chat_id = update.message.chat_id
  bot.sendChatAction(chat_id, "UPLOAD_PHOTO")
  photo = open("C:/Users/ASUS/Desktop/e.jpg" ,'rb')
  bot.sendPhoto(chat_id, photo, "see you at startup reality event :)")
  photo.close()

def send_document_method(bot, update):
  chat_id = update.message.chat_id
  bot.sendChatAction(chat_id, "UPLOAD_DOCUMENT")
  document = open("C:/Users/ASUS/Desktop/Ework/ErfanEsmCV.pdf" , "rb")
  bot.sendDocument(chat_id, document, caption = "download it")


def send_location_method(bot, update):
  chat_id = update.message.chat_id
  bot.sendChatAction(chat_id, "FIND_LOCATION")
  bot.sendLocation(chat_id ,'35.68.65.18', '51.39.02.991')


# jobqueue = updater.job_queue

# def myFirstJob_method(bot, update):
#   bot.sendMessage('@ebot1', 'bot message')

# myFirstJob = Job(myFirstJob_method , 0.5)
# jobqueue._put(myFirstJob, next_t = 0.0)



def ReplyKeyboard_method(bot, update):
  chat_id = update.message.chat_id
  Inline_List = [['My First Name', 'My Last Name'],
  ['My Phone Number','My E-mail'],
  ['اطلاعات بیشتر']] 
  MyList = Inline_List
  bot.sendMessage(chat_id, "please select the button" , reply_markup=ReplyKeyboardMarkup(MyList, resize_keyboard=True, one_time_keyboard=False, selective=False))
  


def inline_query_method(bot, update):
  query = update.inline_query.query
  results = list()
  results.append(InlineQueryResultArticle(id = uuid4() , title="UperCase" , input_message_content = InputTextMessageContent(f"UpperCase of {query} is = {query.upper()}")))
  results.append(InlineQueryResultArticle(id = uuid4() , title="LowerCase" , input_message_content = InputTextMessageContent(f"LowerCase of {query} is = {query.lower()}")))
  # results.append(InlineQueryResultArticle(id = uuid4() , title="Random" , input_message_content = InputTextMessageContent(f"Random between 0 to {query} is = { randint(0, query)}")))
  bot.answerInlineQuery(update.inline_query.id , results = results)
  # my commandss


def SendMessage_method(bot,update):
    text = "بچه ها بیایین بازی 😙\n\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{} \n\n Saleh Sage :/"
    text = text.format("💁‍♂️ @eerfan" , "💁‍♂️ @mohammadsalehsaeidi" , "💁‍♂️ @iamalibabaei" , "💁‍♂️ @ScorpionWoW" , "💁‍♂️ @m_javad_azima" , "💁‍♀️ @Minw_d" , "👩 @yoohahahahaaa" , "️💁‍♀️ @Romina_tl" , "💁‍♀️ @im_z01" , "💁‍♂️ @Mohammad_ba97" , "💁‍♀️ @Mig_Mig79" , "💁‍♀️ @atossamia") 
    bot.send_message('-1001324862919', text)

start_command = CommandHandler('start',	start,	pass_args=True)
hello_command = CommandHandler('hello',	hello)
photo_command = CommandHandler('photo',	send_photo_method)
document_command = CommandHandler('document',	send_document_method)
location_command = CommandHandler('location',	send_location_method)
send_message_command = CommandHandler('tagall', SendMessage_method)
# reply_command = CommandHandler('reply',	ReplyKeyboard_method)




updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(hello_command)
updater.dispatcher.add_handler(photo_command)
updater.dispatcher.add_handler(document_command)
updater.dispatcher.add_handler(location_command)
updater.dispatcher.add_handler(InlineQueryHandler(inline_query_method))
updater.dispatcher.add_handler(send_message_command)





updater.start_polling()

updater.idle()