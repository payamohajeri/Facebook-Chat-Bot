# Chatbot Hacker News
## Facebook ChatBot

Facebook Messenger Bot (ChatBot)

https://www.facebook.com/ChatbotHackerNews/
http://m.me/ChatbotHackerNews

## For virtualizatoin:

vagrant up

## For deploying to heroku you should have an application on heroku: 

./manage.sh init

## To test it locally you can do:

./manage.sh test

## Development and Deployment:

For development, I used Python programming 
language with Flask framework and Redis database.

Since the database class is defined separatly we can change it easily and use
other databases.

I used Heroku to deploy this bot, there is a few env variables that should define
in you Heroku project, please take a look at manage.sh to find them.

if Heroku could not build the project, you should set buildpack manually:

./manage.sh set:buildpack