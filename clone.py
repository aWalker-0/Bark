from TTS.tts.configs.bark_config import BarkConfig
from TTS.tts.models.bark import Bark
from scipy.io.wavfile import write as write_wav

from TTS.api import TTS

# Load the model to GPU
# Bark is really slow on CPU, so we recommend using GPU.
tts = TTS("tts_models/multilingual/multi-dataset/bark", gpu=True)


# Cloning a new speaker
# This expects to find a mp3 or wav file like `bark_voices/new_speaker/speaker.wav`
# It computes the cloning values and stores in `bark_voices/new_speaker/speaker.npz`
tts.tts_to_file(text="Hello, my name is Manmay , how are you?",
                file_path="output.wav",
                voice_dir="bark_voices/",
                speaker="speaker")


# When you run it again it uses the stored values to generate the voice.
tts.tts_to_file(text="Hello, my name is Manmay , how are you?",
                file_path="output.wav",
                voice_dir="bark_voices/",
                speaker="speaker")


# random speaker
tts = TTS("tts_models/multilingual/multi-dataset/bark", gpu=True)
tts.tts_to_file("hello world", file_path="out.wav")


# config = BarkConfig()
# model = Bark.init_from_config(config)
# model.load_checkpoint(config, checkpoint_dir="bark/", eval=True)
# model.to("cuda")

# text = "This is a sentence. Please Ignore!"

# output_dict = model.synthesize(
#     text,
#     config,
#     speaker_id="speaker",
#     voice_dirs="bark_voices",
#     temperature=0.95
# )

# write_wav("output.wav", 24000, output_dict["wav"])