import speech_recognition
import pyttsx3
from datetime import date, datetime
# import snake
def speak(text):
	print("Robot: ", text)
	robot_mouth.say(text)
	robot_mouth.runAndWait()
while True:
	robot_ear = speech_recognition.Recognizer()
	robot_mouth = pyttsx3.init()
	robot_brain = ""
	playing = True

	with speech_recognition.Microphone() as mic:
		speak("I'm listening...")
		audio =robot_ear.record(mic, duration=3)
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("You: ", you)

	if you == "":
		robot_brain = "I can't hear you, try again"
	elif "hello" in you:
		robot_brain = "Hello"
	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("Now is %H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain = "Goodbye"
		print("Robot: ", robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	elif "game" in you:
		while playing:
			speak("Chose a game")
			print("1.Snake")
			print("2.Flappy Bird")
			print("3.Love")
			choice = input("Enter a number(0 to return)")
			if choice == "1":
				speak("Loading Snake")
				import snake
			elif choice == "2":
				speak("Loading Flappy Bird")
				import flappybird
			elif choice == "3":
				speak("Loading Love")
				import love
			elif choice == "0":
				speak("Exit game")
				playing = False
			else:
				speak("You must enter a number from 0 to 3")
		continue
	else:
		robot_brain = "I'm not programed to answer this"
	speak(robot_brain)
