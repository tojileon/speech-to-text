"""
Configuration settings for the speech-to-text converter.
"""

import os
from typing import Optional

def get_api_key() -> str:
    """
    Get the sarvam.ai API key from environment variables.
    
    Returns:
        str: The API key
        
    Raises:
        ValueError: If API key is not found in environment variables
    """
    api_key = os.getenv('SARVAM_API_KEY')
    if not api_key:
        raise ValueError("SARVAM_API_KEY environment variable is not set. Please set it using: export SARVAM_API_KEY='your-api-key'")
    return api_key 