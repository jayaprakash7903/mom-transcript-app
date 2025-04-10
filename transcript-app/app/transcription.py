def process_audio(audio_path, timestamp, save_dir):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        translated = GoogleTranslator(source='auto', target='en').translate(text)

        # Save plain transcript
        plain_path = os.path.join(save_dir, f"transcript_plain_{timestamp}.txt")
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

        transcript_path = os.path.join(save_dir, f"transcript_timed_{timestamp}.txt")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(formatted_lines)

    except sr.UnknownValueError:
        return "❌ Could not understand audio."
    except sr.RequestError as e:
        return f"⚠️ API error: {e}"