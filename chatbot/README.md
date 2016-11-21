# Chatbot Module

in this module the design and structure of chatbot is defined.

## Data Strucutres
different data strucutures are defined in separate classes:
    Elements -> element.py
    Buttons -> button.py
    templates -> template.py
    attachment -> attachment.py

TODO: it's better that the we move the data structure files to a new folder.

## Database
the information about the db is located in db.py and it's change based on the 
bot enviroment which currently can be "development" or "production"

## User
user information is defined and collected in user.py, currently we use only
the firstname. We should implement more reach interfaces with user using his/her
profile and also we can store information in db.

## Message
The structure of recieved message and related functionality are defined in message.py

## Response
The strucuture of response message and related functionality as well as send function
are defined in response.py

## Design
The interactions of chatbot based on the user's message and activities are defined
in the design.py
This file contains the flow and design of our chatbot

TODO: since the design can be more complex, we should defined some strucutres in
a new classes

## Notification
notifing the subscribers is defined in notification.py and it uses the db.py functions
to get the related subscribers.
Currently, since we have one source, we should notify all the subscribers. 

## Utilities
Utility functions which is common in different classes and files are defined here.
Currently we just have log() function as common 

## Constants
Constants variables which may be dependent to the chatbot environments are defined
in the file constant.py 