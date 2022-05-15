import random
data = {
    "Hi": ["HI THERE!", "HOW ARE YOU?", "HI!"],
    "How are you" : ["FINE","I'M OK"],
    "What is you name" : ["MY NAME IS CHATBOT.", "YOU CAN CALL ME CHATBOT."],    
}
print("Chatbot")

run = True
while run:
    query = input("You : ")
    for i,j in data.items():
        if query.lower() == i.lower():
            print("Bot : ",random.choice(j))
        if query == 'end':
            print("Bot : Nice to chat with you!!")
            run = False