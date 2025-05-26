# Malayalam Speech to Text Converter

This project converts speech in Malayalam to Malayalam text using the sarvam.ai API. It automatically handles audio file conversion to WAV format if needed.

## Features

- Convert various audio formats to WAV
- Transcribe Malayalam speech to text using sarvam.ai API
- Automatic format conversion when needed
- Error handling and logging
- Save transcriptions to text files

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tojileon/speech-to-text.git
cd speech-to-text
```

2. Set up your environment:

   **Using Conda (Recommended):**
   ```bash
   conda create -n wave_env python=3.11
   conda activate wave_env
   conda install python-dotenv
   pip install -r requirements.txt
   ```

   **Using pip:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up your API key (Required):

   **Option 1: Environment Variable**
   ```bash
   export SARVAM_API_KEY="your-api-key-here"
   ```

   **Option 2: .env file (Recommended)**
   Create a `.env` file in the project root:
   ```
   SARVAM_API_KEY=your-api-key-here
   ```

Note: The API key must be set either as an environment variable or in the `.env` file. There is no fallback or default key.

## About sarvam.ai API

This project uses the sarvam.ai Speech-to-Text API for Malayalam transcription. The API provides high-quality speech recognition specifically trained for Malayalam language. To use this project, you'll need to:

1. Sign up for a sarvam.ai account at [https://sarvam.ai](https://sarvam.ai)
2. Get your API key from the sarvam.ai dashboard
3. Set the API key using one of the methods above

The API supports:
- Malayalam language (ml-IN)
- Various audio formats (converted to WAV)
- Real-time transcription
- High accuracy speech recognition

## Usage

### Basic Usage

```python
from speech_to_text import MalayalamSpeechToText
from speech_to_text.config import get_api_key
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the converter
api_key = get_api_key()  # Will raise ValueError if SARVAM_API_KEY is not set
converter = MalayalamSpeechToText(api_key)

# Transcribe the audio file and save to text file
input_file = "/path/to/your/audio/file.m4a"  # Supports various formats like .m4a, .mp3, etc.
text = converter.transcribe(input_file, save_to_file=True)
print(f"Transcription saved to: {input_file.rsplit('.', 1)[0] + '.txt'}")
print(f"Transcribed text: {text}")
```

### Save Transcription to File

The converter automatically saves the transcription to a text file with the same name as your audio file (but with .txt extension):

```python
# This will save the transcription to "path/to/your/audio/file.txt"
text = converter.transcribe("path/to/your/audio/file.mp3", save_to_file=True)
```

### Convert Audio to WAV Only

If you just want to convert an audio file to WAV format without transcription:

```python
wav_file = converter.convert_to_wav("path/to/your/audio/file.mp3")
print(f"Converted file saved to: {wav_file}")
```

### Save Text Manually

You can also save the transcribed text manually:

```python
text = converter.transcribe("path/to/your/audio/file.mp3", save_to_file=False)
converter.save_text(text, "custom_output.txt")
```

## Supported Audio Formats

The converter supports various audio formats including:
- MP3
- WAV
- OGG
- FLAC
- M4A
- And more (supported by pydub)

## Error Handling

The converter includes comprehensive error handling and logging. All operations are logged with appropriate error messages when something goes wrong. You can adjust the logging level by modifying the logging configuration in the code.

## API Response Format

The API returns a JSON response with the following structure:
```json
{
    "request_id": "unique_request_id",
    "transcript": "മലയാളം ടെക്സ്റ്റ്",
    "language_code": "ml-IN"
}
```

## License

MIT License

