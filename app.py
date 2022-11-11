# import streamlit as st
# from PIL import Image
# from audio_recorder_streamlit import audio_recorder
# import whisper
# import pathlib
# from pathlib import Path

# st.title("Stable Diffusion")

# st.write("Loading model...")

# model = whisper.load_model("tiny")

# st.write("Model loaded!")

# HERE = Path(__file__).parent
# print(HERE)

# audio_bytes = audio_recorder()

# if audio_bytes:
# 	st.audio(audio_bytes, format="audio/wav")

# 	with open('myfile.wav', mode='bw') as f:
# 		f.write(audio_bytes)

# 	path = f"{HERE}\\myfile.wav"

# 	st.write(path)

# 	out = model.transcribe(path)
# 	st.write(out['text'])

from tempfile import NamedTemporaryFile

import streamlit as st
import whisper

import ffmpeg
st.write("ffmpeg imported")

audio = st.file_uploader("Upload an audio file", type=["wav"])

if audio is not None:
    with NamedTemporaryFile(suffix="wav") as temp:
        temp.write(audio.getvalue())
        temp.seek(0)
        model = whisper.load_model("base")
        result = model.transcribe(temp.name)
        st.write(result["text"])
