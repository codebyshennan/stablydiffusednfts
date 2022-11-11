# from audio_recorder_streamlit import audio_recorder
# import whisper
# import pathlib
# from pathlib import Path
# from tempfile import NamedTemporaryFile
# import streamlit as st
# import whisper
# import ffmpeg

# st.title("Stable Diffusion")

# st.write("Loading model...")

# model = whisper.load_model("base")

# st.write("Model loaded!")

# HERE = Path(__file__).parent
# print(HERE)

# audio_bytes = audio_recorder()

# if audio_bytes:
#     st.audio(audio_bytes, format="audio/wav")

#     st.write("Uploading audio file...")

#     with open('myfile.wav', mode='bw') as f:
#         print("Creating audio files...")
#         f.write(audio_bytes)
    
#     path = f"{HERE}\\myfile.wav"
#     st.write(path)
  
#     out = model.transcribe(path)
#     st.write(out['text'])

# audio = st.file_uploader("Upload an audio file", type=["wav"])

# if audio is not None:
#     with NamedTemporaryFile(suffix="wav") as temp:
#         temp.write(audio.getvalue())
#         temp.seek(0)
#         result = model.transcribe(temp.name)
#         st.write(result["text"])

import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

stt_button = Button(label="Speak", width=100)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
 
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        st.write(result.get("GET_TEXT"))
