def save_transcript_to_file(transcript, timestamp, save_dir):
    plain_path = os.path.join(save_dir, f"transcript_plain_{timestamp}.txt")
    with open(plain_path, "w", encoding="utf-8") as f:
        f.write(transcript)

def save_timed_transcript_to_file(formatted_lines, timestamp, save_dir):
    transcript_path = os.path.join(save_dir, f"transcript_timed_{timestamp}.txt")
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(formatted_lines)

def create_save_directory(save_dir):
    os.makedirs(save_dir, exist_ok=True)