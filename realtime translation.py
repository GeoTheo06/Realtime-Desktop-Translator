import pyaudio
import wave
import speech_recognition as sr
from googletrans import Translator
import os
import threading

# in case you want to capture audio output instead of microphone:
# 1. download and install VB-CABLE and restart computer
# 2. Type "change system sounds" in search bar and go to "recording", there set "cable ouput" device as the default device.
# 3. Right click "cable output" device and go to "listen" tab, from there enable "listen to this device" option and select the device to which you want to listen the computer output to.
# 4. Set "CABLE Input" device to default output device

#i = 1

# Function to record audio using PyAudio
def record_audio(filename, duration=30):  # Listen for x seconds
	audio = pyaudio.PyAudio()
	stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
	frames = []

	#print("Listening...")

	for i in range(0, int(44100 / 1024 * duration)):
		data = stream.read(1024)
		frames.append(data)

	#print("Finished recording.")
	stream.stop_stream()
	stream.close()
	audio.terminate()

	with wave.open(filename, 'wb') as wf:
		wf.setnchannels(1)
		wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
		wf.setframerate(44100)
		wf.writeframes(b''.join(frames))

# Function to play audio on Windows
def play_audio(filename):
	os.system("start wmplayer /play /close " + filename)

# Function to perform speech recognition
def recognize_speech():
	r = sr.Recognizer()
	with sr.AudioFile("captured_voice.wav") as source:
		audio = r.record(source)
	
	try:
		text = r.recognize_google(audio, language='ru-RU') # change in case you need different language
		#print(f"Recognized text {i}: {text}")
		return text
	except sr.UnknownValueError:
		print("Speech not recognized.")
		return None
	except sr.RequestError as e:
		print(f"Could not request results; {e}")
		return None

# Function to translate text
def translate_in_background(text, dest_language):
	source_language = 'ru' # change in case you need different language
	translator = Translator()
	translated_text = translator.translate(text, src = source_language, dest=dest_language)
	print(f"\n{translated_text.text}\n") # use {i} in case you want to count
	
	file_path = "translatedText.txt"
	with open(file_path, "a") as file:
		file.write(str(translated_text.text) + '\n' + '\n')

# Infinite loop for continuous translation and playback
while True:
	
	translate_language = 'en' # change in case you need different language

	# Record audio for x seconds
	record_audio("captured_voice.wav", duration=30)

	# Perform speech recognition
	recognized_text = recognize_speech()

	if recognized_text:
		# Translate recognized text to English
		translation_thread = threading.Thread(target=translate_in_background, args=(recognized_text, translate_language))
		translation_thread.start()
		
