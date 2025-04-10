from tkinter import Tk, Label, Button, messagebox
from app.recorder import start_recording, stop_recording
from app.transcription import process_audio
import os

class TranscriptApp:
    def __init__(self, master):
        self.master = master
        master.title("🎤 Meeting MoM Maker")
        master.geometry("400x250")
        master.resizable(False, False)

        self.title_label = Label(master, text="Meeting MoM Maker", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.record_button = Button(master, text="Start Recording", font=("Helvetica", 12), command=self.start_recording, bg="green", fg="white")
        self.record_button.pack(pady=5)

        self.stop_button = Button(master, text="Stop Recording", font=("Helvetica", 12), command=self.stop_recording, bg="red", fg="white", state='disabled')
        self.stop_button.pack(pady=5)

        self.status_label = Label(master, text="Status: Waiting to record", font=("Helvetica", 11), fg="gray")
        self.status_label.pack(pady=20)

    def start_recording(self):
        self.status_label.config(text="🎙️ Recording...", fg="blue")
        self.record_button.config(state='disabled')
        self.stop_button.config(state='normal')
        start_recording(self.status_label, self.stop_button)

    def stop_recording(self):
        self.stop_button.config(state='disabled')
        self.record_button.config(state='normal')
        stop_recording(self.status_label)

if __name__ == "__main__":
    root = Tk()
    app = TranscriptApp(root)
    root.mainloop()