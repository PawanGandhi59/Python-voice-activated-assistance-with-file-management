# Voice-Controlled File Management System

This is a Python-based voice-controlled system that allows users to interact with their computer through voice commands. It integrates with the `speech_recognition` library to recognize speech and execute commands to open/close files, open applications like YouTube, Chrome, Calculator, and more. It also supports the ability to replace words within files using voice commands.

## Features

- **Voice Commands**: Recognizes voice commands to perform actions such as:
  - Create and open new/existing text files
  - Close opened files
  - Open/close applications like YouTube, Chrome, Calculator
  - Replace words inside files
- **Multi-Language Support**: The program can recognize speech in different languages. By default, it supports English and Gujarati.
  
## Prerequisites

To run this project, you need the following:

- Python 3.x
- `speech_recognition` library
- `pyttsx3` (optional, for text-to-speech functionality)
- `pyaudio` (for microphone input)
