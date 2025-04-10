import streamlit as st
import soundfile as sf
import speech_recognition as sr
from deep_translator import GoogleTranslator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime
import os
import io

# Save location
SAVE_DIR = r"\\del3-file01-p\Planning\1- Power BI\Transcript"
os.makedirs(SAVE_DIR, exist_ok=True)

st.set_page_config(page_title="Meeting MoM Maker", layout="centered")
st.title("🎤 Meeting MoM Maker (Web Version)")
st.markdown("1. Record your audio in Hindi<br>2. Upload the file<br>3. Get transcription, translation, and a word cloud", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload your recorded `.wav` file", type=["wav"])

if uploaded_file:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    audio_path = os.path.join(SAVE_DIR, f"output_{timestamp}.wav")

    # Save uploaded audio
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"✅ Audio saved as {audio_path}")

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        st.info("Transcribing...")
        text = recognizer.recognize_google(audio, language="hi-IN")
        translated = GoogleTranslator(source='auto', target='en').translate(text)

        # Save plain transcript
        plain_path = os.path.join(SAVE_DIR, f"transcript_plain_{timestamp}.txt")
        with open(plain_path, "w", encoding="utf-8") as f:
            f.write(translated)

        # Save timestamped transcript (approx. 2s chunks)
        words = translated.split()
        total_time = len(audio.frame_data) / audio.sample_rate
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

        st.success("📝 Transcription complete")
        st.text_area("📃 Translated Transcript", translated, height=200)

        # Word Cloud
        wordcloud = WordCloud(
            width=1000,
            height=500,
            background_color='white',
            colormap='coolwarm',
            max_words=200,
            contour_color='steelblue',
            contour_width=1,
            prefer_horizontal=0.9,
            collocations=False
        ).generate(translated)

        wordcloud_path = os.path.join(SAVE_DIR, f"wordcloud_{timestamp}.png")
        wordcloud.to_file(wordcloud_path)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

    except sr.UnknownValueError:
        st.error("❌ Could not understand the audio.")
    except sr.RequestError as e:
        st.error(f"⚠️ API error: {e}")
