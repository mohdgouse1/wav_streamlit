import streamlit as st
import pandas as pd
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import os


st.title('Wav File Creator')

fs = 16000  # Sample rate
# seconds = st.text_input("Approx length of the recording.", 4)
# print(seconds)
seconds = 4

filename = st.text_input("Choose a filename: ")
if st.button(f"Click to Record"):
    if filename == "":
        st.warning("Choose a filename.")
    else:
        record_state = st.text("Recording...")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype="int16")
        sd.wait(seconds)  # Wait until recording is finished
        write(f'{filename}.wav', fs, myrecording)  # Save as WAV file 

        if os.path.exists(f"{filename}.wav"):
            audio_file = open(f'{filename}.wav', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/wav", start_time=0)

        st.download_button("Download wav file", audio_bytes, file_name=f"{filename}.wav", mime="audio/wav", on_click=None)


