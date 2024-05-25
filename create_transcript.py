# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai
import os
from typing import List, Dict, Any


def generate_transcript(link: str) -> Any:
    aai.settings.api_key = os.environ.get("ASSEMBLYAI_API_KEY")
    transcriber = aai.Transcriber()

    # TODO - Supply this link through streamlit UI
    transcript = transcriber.transcribe(link)
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")

    return transcript.text


if __name__ == "__main__":
    text = generate_transcript(
        "https://karnatakabank.com/sites/default/files/2024-05/tkb0220240524153240_1.mp3"
    )
    with open("transcripts/transcript.txt", "wb") as f:
        f.write(text)
