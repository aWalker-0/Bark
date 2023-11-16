from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
    Fuck... I - I don't know. [laughs] Like'a sentence? [clears throat] I don't know... I am the LORAX and I speak for the trees. But for some reason, the trees speak VIETNAMESE!
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

# # play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)

