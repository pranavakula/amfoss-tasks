import os
import telebot
import requests
import json
import csv, io
#here we had imported the required modules to run the cinebot sucessfully, io is added for handling input and output values


yourkey = "afcc42dd"
bot_id = "5583870663:AAH9WeUrxXYDGhMZsk67ffvdFzVSYuBDy60"
#api key and bot id are stored in this variables respectively

bot = telebot.TeleBot(bot_id)

s = io.StringIO()
buf = io.BytesIO()
#these s and io are used for handling string and binary data, respectively


@bot.message_handler(commands=['start','hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(message, 'Hello there! I am a bot that will show  movie information for you and export it in a csv file.\n\n' )
#This handler will kick start when the user sends '/start' or '/hello' command to the tele bot
@bot.message_handler(commands=['stop','bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message,'Bye!\nHave a good time')
    #this handler ensures the chat is dead when the user sends '/stop' or '/bye'
   
@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message,'1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')
#this handler helps or give suitable instructions when the message command '/help' is sent
@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    movieName = message.text.replace('/movie ', "")
    bot.reply_to(message,'Getting movie info...')
    api_url = f"https://www.omdbapi.com/?i=tt3896198&apikey=afcc42dd"
    #http://www.omdbapi.com/?apikey={yourkey}&t={movieName}
    movieDetails = requests.get(api_url).json()
    moviePoster = movieDetails['Poster']
    movieTitle = movieDetails['Title']
    movieYear = movieDetails['Year']
    movieRating = movieDetails['Rated']

    bot.reply_to(message,'/movie')

    csv.writer(s).writerow([movieTitle,movieYear,movieRating])
    s.seek(0)

    buf.write(s.getvalue().encode())
    buf.seek(0)

    buf.name = f'datas.csv'
    
    bot.send_photo(message.chat.id, moviePoster , f'Title: {movieTitle} \nReleased_Year: {movieYear}\nRating: {movieRating}')
#this set of code is used to send the movie details from the OMDB app to the csv file(s) when the command '/movie' is sent

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
   bot.reply_to(message,'Generating the data file')
   bot.send_document(message.chat.id,buf) 
   #when '/export' command is sent the csv file which contains details of the movie is sent in the tele chat.

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
#this function is just used to say that the bot didn't understand the user input.
bot.infinity_polling()
#this ensures the bot is running always untill the user sends '/stop' or '/bye' command
