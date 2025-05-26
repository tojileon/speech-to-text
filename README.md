# Malayalam Speech to Text Converter

This project converts speech in Malayalam to Malayalam text using the sarvam.ai API. It automatically handles audio file conversion to WAV format if needed.

## Features

- Convert various audio formats to WAV
- Transcribe Malayalam speech to text using sarvam.ai API
- Automatic format conversion when needed
- Error handling and logging

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/speech-to-text.git
cd speech-to-text
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
```bash
export SARVAM_API_KEY="your-api-key-here"
```

## Usage

```python
from speech_to_text import MalayalamSpeechToText
from speech_to_text.config import get_api_key

# Initialize the converter
api_key = get_api_key()
converter = MalayalamSpeechToText(api_key)

# Convert and transcribe an audio file
text = converter.transcribe("path/to/your/audio/file.mp3")
print(text)
```

## Supported Audio Formats

The converter supports various audio formats including:
- MP3
- WAV
- OGG
- FLAC
- And more (supported by pydub)

## Error Handling

The converter includes comprehensive error handling and logging. All operations are logged with appropriate error messages when something goes wrong.

## License

MIT License

