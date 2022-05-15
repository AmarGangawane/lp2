import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i'm" : "you are",
    "i am" : "you are",
    "my" : "your",
    "i'v":"you have",
    "i have":"you have",
    "i":"you",
    "me":"you",
    "i'll": "you will",
    "i was":"you were",
    "i'd":"you would",
    "you":"me",
    "yours":"mine",
    "you'll":"i will",
    "you'd":"i would",
    "you were":"i was",
    "your":"my",
    "you've":"i have"    
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1 nice to have chat with you!!"]
    ],
    [
        r"i am (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"i am fine",
        ["Glad to hear that!"]
    ],
    [
        r"what is your name",
        ["You can call me Chatterbox:)"]
    ],
    [
        r"who created you",
        ["Apeksha created me using nltk libraries from python"]
    ],
    [
        r"hi|hey|hello",
        ["Hey there!","Hello!!!"]
    ],
    [
        r"how are you?",
        ["Great as always! what about you?"]
    ],
    [
        r"(.*) (location|city)?",
        ["Pune, Maharashtra"]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1"]
    ],
    [
        r"i study in (.*)?",
        ["%1 is an Amazing college, I have heard about it.",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony","M.S.Dhoni","Virat Kohli"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt","RDJ"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]
def chat():
    print("Hello I am Chatterbox, Created by Apeksha for your service!")
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chat()

