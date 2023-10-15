# Realtime-Desktop-Translator
Reads mic input and outputs translated text in console. (can also capture output audio with external tool and extra configuration)

# Audio to Text Translator

This Python project is designed to capture audio from the microphone, save the last 30 seconds of recorded audio to a WAV file, transcribe the spoken words to text, translate the text into a specified language, and output the translated text to both the console and a text file. It uses several libraries and technologies to achieve this functionality.

**Note:** This project provides near-real-time translation; however, it may not offer instantaneous translation due to the processing involved in audio recording, transcription, and translation.

## Technologies Used

The project uses the following technologies and libraries:

- **Python**: The programming language used to create the project.
- **PyAudio**: A Python library used for audio input and output. It is used to capture audio from the microphone.
- **Wave**: A module in Python's standard library for reading and writing WAV files.
- **SpeechRecognition**: A Python library for performing speech recognition. It's used to transcribe the audio to text.
- **Googletrans**: A Python library that interfaces with Google Translate for language translation.
- **Threading**: The threading module in Python is used for parallel execution of translation and audio recording.

## How It Works

The project follows these main steps:

1. Record Audio: It uses PyAudio to capture audio from the microphone for 30 seconds. The audio is saved to a WAV file temporarily.

2. Speech Recognition: The recorded audio is transcribed into text using the SpeechRecognition library, specifically the Google Web Speech API.

3. Translation: The transcribed text is then translated from its source language (e.g., Russian) into the target language (e.g., English) using the Googletrans library.

4. Output: The translated text is printed to the console, and it is also appended to a text file called "translatedText.txt."

## Capturing Audio Output (Optional)

If you want to capture audio output from your computer instead of using a microphone, follow these steps:

1. Download and install VB-CABLE and restart your computer.

2. Type "change system sounds" in the search bar and go to the "recording" tab. Set the "cable output" device as the default recording device.

3. Right-click on the "cable output" device and go to the "listen" tab. Enable the "listen to this device" option and select the device to which you want to listen for computer audio output.

## Running the Project

To run the project, simply execute the Python script. It will continuously record audio from your microphone or the selected audio output, transcribe it, translate it, and output the translation to the console and the "translatedText.txt" file.

**Note:** Make sure to install the required libraries (PyAudio, SpeechRecognition, and googletrans) using pip before running the script.

This project can be useful for various applications such as real-time translation, language learning, or transcription of spoken content.
