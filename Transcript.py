import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from deep_translator import GoogleTranslator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import threading
import numpy as np
from datetime import datetime
import queue

# Save directory
SAVE_DIR = r"\\del3-file01-p\Planning\1- Power BI\Transcript"
os.makedirs(SAVE_DIR, exist_ok=True)

# Globals
fs = 44100
recording = True
audio_queue = queue.Queue()
audio_data = []

# Start Recording
def start_recording():
    global recording, audio_data
    recording = True
    audio_data = []

    status_label.config(text="🎙️ Recording...", fg="blue")
    record_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

    threading.Thread(target=record_stream).start()

def record_stream():
    with sd.InputStream(samplerate=fs, channels=1, callback=audio_callback):
        while recording:
            sd.sleep(100)

def audio_callback(indata, frames, time, status):
    if recording:
        audio_queue.put(indata.copy())

# Stop Recording
def stop_recording():
    global recording
    recording = False
    stop_button.config(state=tk.DISABLED)

    while not audio_queue.empty():
        audio_data.append(audio_queue.get())

    full_recording = np.concatenate(audio_data, axis=0)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    audio_filename = f"output_{timestamp}.wav"
    audio_path = os.path.join(SAVE_DIR, audio_filename)

    sf.write(audio_path, full_recording, fs, subtype='PCM_16')
    status_label.config(text="✅ Recording saved. Transcribing...", fg="green")

    threading.Thread(target=process_audio, args=(audio_path, timestamp)).start()

# Transcription + Translation
def process_audio(audio_path, timestamp):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        translated = GoogleTranslator(source='auto', target='en').translate(text)

        # Save plain transcript
        plain_path = os.path.join(SAVE_DIR, f"transcript_plain_{timestamp}.txt")
        with open(plain_path, "w", encoding="utf-8") as f:
            f.write(translated)

        # Save timestamped transcript (approx. 2-second groups)
        words = translated.split()
        total_time = len(audio_data) * 1024 / fs  # Approx time in seconds
        group_duration = 2
        words_per_group = max(1, round(len(words) / (total_time / group_duration)))

        formatted_lines = ""
        for i in range(0, len(words), words_per_group):
            start = round((i / len(words)) * total_time)
            end = round(((i + words_per_group) / len(words)) * total_time)
            group_text = ' '.join(words[i:i+words_per_group])
            formatted_lines += f"{start} to {end} sec: {group_text}\n"

        transcript_path = os.path.join(SAVE_DIR, f"transcript_timed_{timestamp}.txt")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(formatted_lines)

        status_label.config(text="✅ Transcription completed.", fg="green")
        generate_wordcloud(translated, timestamp)
        messagebox.showinfo("Done ✅", f"Saved in:\n{SAVE_DIR}")

    except sr.UnknownValueError:
        status_label.config(text="❌ Could not understand audio.", fg="red")
    except sr.RequestError as e:
        status_label.config(text=f"⚠️ API error: {e}", fg="red")

# Word Cloud
def generate_wordcloud(text, timestamp):
    wordcloud = WordCloud(width=1000,
    height=500,
    background_color='white',
    colormap='coolwarm',  # Classy color scheme
    max_words=200,
    contour_color='steelblue',
    contour_width=1,
    prefer_horizontal=0.9,
    font_path=None,  # Use a Hindi font if needed
    collocations=False ).generate(text)
    wordcloud_path = os.path.join(SAVE_DIR, f"wordcloud_{timestamp}.png")
    wordcloud.to_file(wordcloud_path)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Word Cloud from MoM", fontsize=16)
    plt.tight_layout()
    plt.show()

# GUI
app = tk.Tk()
app.title("🎤 Meeting MoM Maker")
app.geometry("400x250")
app.resizable(False, False)

title_label = tk.Label(app, text="Meeting MoM Maker", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

record_button = tk.Button(app, text="Start Recording", font=("Helvetica", 12), command=start_recording, bg="green", fg="white")
record_button.pack(pady=5)

stop_button = tk.Button(app, text="Stop Recording", font=("Helvetica", 12), command=stop_recording, bg="red", fg="white", state=tk.DISABLED)
stop_button.pack(pady=5)

status_label = tk.Label(app, text="Status: Waiting to record", font=("Helvetica", 11), fg="gray")
status_label.pack(pady=20)

app.mainloop()
