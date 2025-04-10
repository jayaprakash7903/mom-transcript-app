# Transcript App

This project is a Python application designed to record audio, transcribe it, translate the text, and generate a word cloud from the transcribed text. It provides a user-friendly GUI for easy interaction.

## Features

- **Audio Recording**: Start and stop audio recording with a simple button click.
- **Transcription**: Convert recorded audio into text using speech recognition.
- **Translation**: Translate the transcribed text into English.
- **Word Cloud Generation**: Create a visual representation of the most common words in the transcribed text.

## Project Structure

```
transcript-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── gui.py
│   ├── recorder.py
│   ├── transcription.py
│   ├── wordcloud_generator.py
│   └── utils.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd transcript-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python app/main.py
   ```

2. Use the GUI to start recording audio. Once you stop the recording, the application will automatically transcribe and translate the audio, and generate a word cloud.

## Dependencies

- tkinter
- sounddevice
- soundfile
- speech_recognition
- deep_translator
- wordcloud
- matplotlib

## License

This project is licensed under the MIT License - see the LICENSE file for details.