# Meeting MoM Maker

## Overview
The Meeting MoM Maker is a Python application designed to record meetings, transcribe the audio, translate the text, and generate a word cloud from the transcribed content. This tool is useful for creating minutes of meetings (MoM) efficiently.

## Features
- **Audio Recording**: Start and stop recording audio during meetings.
- **Transcription**: Convert recorded audio into text using speech recognition.
- **Translation**: Translate the transcribed text into English.
- **Word Cloud Generation**: Visualize the most frequently used words in the meeting using a word cloud.

## Requirements
To run this project, you need to install the following dependencies:

- tkinter
- sounddevice
- soundfile
- speech_recognition
- deep_translator
- wordcloud
- matplotlib

You can install these dependencies using the following command:

```
pip install -r requirements.txt
```

## Setup
1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required packages using the command mentioned above.
4. Run the application by executing the `Transcript.py` script located in the `src` directory.

## Usage
- Launch the application.
- Click on "Start Recording" to begin capturing audio.
- Click on "Stop Recording" to finish and process the audio.
- The application will transcribe the audio, translate it, and generate a word cloud.
- The results will be saved in the specified directory.

## License
This project is licensed under the MIT License. Feel free to modify and use it as per your requirements.