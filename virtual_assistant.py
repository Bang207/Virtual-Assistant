import speech_recognition
import pyttsx3
from datetime import date, datetime
import random
import pywhatkit as kit
import snake
import flappybird


def listen(text):
	robot_ear = speech_recognition.Recognizer()
	with speech_recognition.Microphone() as mic:
		speak(text)
		print("Mike:...")
		audio = robot_ear.record(mic, duration=3)
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("You:", you)
	return you


def speak(text):
	robot_mouth = pyttsx3.init()
	print("Mike:", text)
	robot_mouth.say(text)
	robot_mouth.runAndWait()


def main():
	while True:
		playing = True

		you = listen("How can I help you")

		if you == "":  # Recursion until the computer hear something
			robot_brain = "I can't hear you, try again"
		elif "your name" in you:
			robot_brain = "My name is Mike"
		elif "hi" in you:
			robot_brain = "hi"
		elif "hello" in you:
			robot_brain = "Hello"
		elif "today" in you:  # Return the date
			today = date.today()
			robot_brain = today.strftime("%B %d %Y")
		elif "time" in you:  # Return time
			now = datetime.now()
			robot_brain = now.strftime("Now is %H hours %M minutes %S seconds")
		elif "fact" in you:  # Output a ramdom fact
			with open("facts.txt", "r") as f:
				fact_list = f.read().split("\n")
			robot_brain = random.choice(fact_list)
		elif "game" in you:
			while playing:
				print("1.Snake")
				print("2.Flappy Bird")
				choice = listen("Choose a game(Say exit to return)")
				if "snake" in choice:
					speak("Loading Snake")
					snake.main()
				elif "flappy bird" in choice:
					speak("Loading Flappy Bird")
					flappybird.main()
				elif "exit" in choice:
					speak("Exit game")
					playing = False
				else:
					speak("I can't hear you, try again")
			continue
		elif "YouTube" in you:  # Search on Youtube
			kit.playonyt(you.replace("YouTube", ""))
		elif "search" in you:  # Search on Google
			kit.search(you.replace("search", ""))
		elif "bye" in you:
			speak("Goodbye")
			break
		else:
			robot_brain = "I'm not programed to answer this"
		speak(robot_brain)


if __name__ == '__main__':
	main()
