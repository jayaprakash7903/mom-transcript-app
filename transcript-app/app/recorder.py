from datetime import datetime
import os
import queue
import sounddevice as sd
import soundfile as sf
import threading

# Save directory
SAVE_DIR = r"\\del3-file01-p\Planning\1- Power BI\Transcript"
os.makedirs(SAVE_DIR, exist_ok=True)

# Globals
fs = 44100
recording = False
audio_queue = queue.Queue()
audio_data = []

def start_recording():
    global recording, audio_data
    recording = True
    audio_data = []

    threading.Thread(target=record_stream).start()

def record_stream():
    with sd.InputStream(samplerate=fs, channels=1, callback=audio_callback):
        while recording:
            sd.sleep(100)

def audio_callback(indata, frames, time, status):
    if recording:
        audio_queue.put(indata.copy())

def stop_recording():
    global recording
    recording = False

    while not audio_queue.empty():
        audio_data.append(audio_queue.get())

    full_recording = np.concatenate(audio_data, axis=0)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    audio_filename = f"output_{timestamp}.wav"
    audio_path = os.path.join(SAVE_DIR, audio_filename)

    sf.write(audio_path, full_recording, fs, subtype='PCM_16')
    return audio_path, timestamp