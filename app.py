from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
# from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
    Hello User. I am DIO, the artificial intelligence paired to you. I have multiple functionalities, all you need do is ask.
"""
audio_array = generate_audio(text_prompt, history_prompt="v2/en_speaker_6")

# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

# # play text in notebook
# Audio(audio_array, rate=SAMPLE_RATE)

