"""
Core functionality for converting Malayalam speech to text.
"""

import os
from typing import Optional, Union, Dict, Any
import requests
from pydub import AudioSegment
import logging
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MalayalamSpeechToText:
    """Main class for converting Malayalam speech to text."""
    
    def __init__(self, api_key: str):
        """
        Initialize the converter with API credentials.
        
        Args:
            api_key (str): The sarvam.ai API key
        """
        self.api_key = api_key
        self.api_url = "https://api.sarvam.ai/speech-to-text"
        
    def convert_to_wav(self, input_file: str, output_file: Optional[str] = None) -> str:
        """
        Convert an audio file to WAV format.
        
        Args:
            input_file (str): Path to the input audio file
            output_file (str, optional): Path for the output WAV file
            
        Returns:
            str: Path to the converted WAV file
            
        Raises:
            Exception: If conversion fails
        """
        try:
            # Load the audio file
            audio = AudioSegment.from_file(input_file)
            
            # If no output file specified, create one based on input filename
            if output_file is None:
                output_file = os.path.splitext(input_file)[0] + '.wav'
            
            # Export as WAV
            audio.export(output_file, format='wav')
            logger.info(f"Successfully converted {input_file} to {output_file}")
            return output_file
            
        except Exception as e:
            logger.error(f"Error converting file: {str(e)}")
            raise
    
    def save_text(self, text: str, output_file: str) -> None:
        """
        Save transcribed text to a file.
        
        Args:
            text (str): The text to save
            output_file (str): Path where to save the text file
            
        Raises:
            Exception: If saving fails
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text)
            logger.info(f"Successfully saved transcription to {output_file}")
        except Exception as e:
            logger.error(f"Error saving text to file: {str(e)}")
            raise
    
    def transcribe(self, audio_file: str, save_to_file: bool = True) -> str:
        """
        Transcribe Malayalam speech to text using sarvam.ai API.
        
        Args:
            audio_file (str): Path to the audio file
            save_to_file (bool): Whether to save the transcription to a file
            
        Returns:
            str: Transcribed text
            
        Raises:
            Exception: If transcription fails
        """
        try:
            # Ensure file is WAV format
            if not audio_file.lower().endswith('.wav'):
                audio_file = self.convert_to_wav(audio_file)
            
            # Prepare the request
            headers = {
                "api-subscription-key": self.api_key,
                "Accept": "application/json"
            }
            
            data = {
                'language_code': "ml-IN",
                'model': "saarika:v2",
            }
            
            # Open the file in binary mode
            with open(audio_file, 'rb') as audio:
                files = {
                    'file': (os.path.basename(audio_file), audio, 'audio/wav')
                }
                
                # Make API request
                response = requests.post(
                    self.api_url,
                    headers=headers,
                    data=data,
                    files=files
                )
                
                # Log the response details for debugging
                logger.debug(f"API Response Status: {response.status_code}")
                logger.debug(f"API Response Headers: {response.headers}")
                
                try:
                    response.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    error_msg = f"API Error: {str(e)}"
                    if response.text:
                        try:
                            error_details = response.json()
                            error_msg += f"\nAPI Response: {json.dumps(error_details, indent=2)}"
                        except json.JSONDecodeError:
                            error_msg += f"\nAPI Response: {response.text}"
                    logger.error(error_msg)
                    raise Exception(error_msg)
                
                # Log the full response for debugging
                logger.debug(f"API Response Content: {response.text}")
                
                result = response.json()
                logger.debug(f"Parsed JSON Response: {json.dumps(result, indent=2)}")
                
                # Get the transcript from the response
                text = result.get('transcript', '')
                
                if not text:
                    logger.warning("No transcription text found in API response")
                    logger.debug(f"Full response structure: {json.dumps(result, indent=2)}")
                
                # Save to file if requested
                if save_to_file and text:
                    output_file = os.path.splitext(audio_file)[0] + '.txt'
                    self.save_text(text, output_file)
                
                return text
            
        except Exception as e:
            logger.error(f"Error transcribing file: {str(e)}")
            raise 