
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

with open('file.txt','r') as file:
    conversation = file.read()

bott = ChatBot("Sunanda's Resume ChatBot")
trainer2 = ListTrainer(bott)
trainer2.train([    "Hey",
    "Hi there!",
    "Hi",
    "Hi!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What is your name?", "My name is Resume ChatBot",
    "Who created you?", "Sunanda",
    "Tell me about yourself",
    "My name is Sunanda Somwase. I am a third year computer engineering student at PVGCOET",
    "Contact",
    "Email : sunandasomwase@gmail.com, Mobile number : +91 9021393816 Location : Pune, Maharashtra",
    "Education",
    "Bachelor of Engineering (B.E), Computer Science & Engineering\n Pune Vidyarthi Grihas College Of Engineering And Technology Pune '\n'2018 - 2022 '\n'CGPA: 8.84/10 '\n'Senior Secondary (XII), Science Sir Parashurambhau College Pune Maharashtra (MAHARASHTRA STATE BOARD board) Year of completion: 2018 Percentage: 88.40% Secondary (X) Sant Meera School Aurangabad (MAHARASHTRA STATE BOARF board) Year of completion: 2016 Percentage: 96.20%",
    "Projects",
    ])
trainer = ChatterBotCorpusTrainer(bott)
trainer.train("chatterbot.corpus.english")
#trainer2.train(["Thank You","Welcome"])

@app.route("/")
def home(): 
	return render_template("home.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(bott.get_response(userText))
if __name__ == "__main__":
	app.run()