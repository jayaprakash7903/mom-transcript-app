# Meeting MoM Maker

## Overview
The Meeting MoM Maker is a web application designed to facilitate the creation of meeting minutes (MoM) by transcribing audio recordings, translating the transcripts, and generating visual word clouds. This tool is particularly useful for users who conduct meetings in Hindi and need an English translation of the discussions.

## Features
- Upload audio files in `.wav` format.
- Automatic transcription of audio using speech recognition.
- Translation of the transcript from Hindi to English.
- Generation of a word cloud from the translated text.

## Requirements
To run this project, you need to have the following Python packages installed:

- Streamlit
- SpeechRecognition
- DeepTranslator
- WordCloud
- Matplotlib

You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Usage
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the application using Streamlit:

```
streamlit run src/mom_web_upload.py
```

4. Upload your recorded `.wav` file when prompted.
5. Wait for the transcription and translation to complete.
6. View the translated transcript and the generated word cloud.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.