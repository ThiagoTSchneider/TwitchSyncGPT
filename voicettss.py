from elevenlabs import generate, save
from elevenlabs import set_api_key
import sounddevice as sd
import soundfile as sf

set_api_key('')
voice_model = ""

def generate_and_send_audio(get_response):
  print("Initializing Audio Generation\n")
  audio = generate(text=get_response,
                   voice=voice_model,
                   model='eleven_multilingual_v2')
  save(audio, "Asis.wav")
  print("Audio Generated\n")
  filename = 'asis.wav'
  data, fs = sf.read(filename, dtype='float32')  
  sd.play(data, fs)
  sd.wait()  # Wait until file is done playing
