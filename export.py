from pydub import AudioSegment
import sys
import os

def convert_to_wav(input_file, output_file=None):
    """
    Convert an audio file to WAV format.
    
    Args:
        input_file (str): Path to the input audio file
        output_file (str, optional): Path for the output WAV file. If not provided,
                                   will use the input filename with .wav extension
    """
    try:
        # Load the audio file
        audio = AudioSegment.from_file(input_file)
        
        # If no output file specified, create one based on input filename
        if output_file is None:
            output_file = os.path.splitext(input_file)[0] + '.wav'
        
        # Export as WAV
        audio.export(output_file, format='wav')
        print(f"Successfully converted {input_file} to {output_file}")
        
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python export.py <input_file> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_to_wav(input_file, output_file)
