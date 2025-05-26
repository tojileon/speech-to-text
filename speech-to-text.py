from speech_to_text import MalayalamSpeechToText
from speech_to_text.config import get_api_key

# Initialize the converter
api_key = get_api_key()
converter = MalayalamSpeechToText(api_key)

# Transcribe the audio file and save to text file
input_file = "/Users/tojileon/Downloads/test1.m4a"
text = converter.transcribe(input_file, save_to_file=True)
print(f"Transcription saved to: {input_file.rsplit('.', 1)[0] + '.txt'}")
print(f"Transcribed text: {text}")
