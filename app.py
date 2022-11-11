from audiorecorder import audiorecorder
import whisper
import pathlib
from pathlib import Path
from tempfile import NamedTemporaryFile
import streamlit as st
import whisper
import ffmpeg

st.title("Stable Diffusion")

st.write("Loading model...")

model = whisper.load_model("base")

st.write("Model loaded!")

HERE = Path(__file__).parent
print(HERE)

audio = audiorecorder("Click to record", "Recording...")

if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio)

    # To save audio to a file:
    wav_file = open(f"{HERE}/myfile.wav", "wb")
    wav_file.write(audio.tobytes())

    path = f"{HERE}/myfile.wav"
#     st.write(path)

    out = model.transcribe(path, language='en')
    st.write(out['text'])

audio = st.file_uploader("Upload an audio file", type=["wav"])

if audio is not None:
    with NamedTemporaryFile(suffix="wav") as temp:
        temp.write(audio.getvalue())
        temp.seek(0)
        result = model.transcribe(temp.name)
        st.write(result["text"])
