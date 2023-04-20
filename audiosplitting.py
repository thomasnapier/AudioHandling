import os
from pydub import AudioSegment

# define the directory containing the subdirectories
parent_dir = "D:\\PhD-data\\Wambiana"

# loop through each subdirectory
for subdir in os.listdir(parent_dir):
    # construct the path to the subdirectory
    subdir_path = os.path.join(parent_dir, subdir)
    
    # check if the subdirectory is a directory
    if os.path.isdir(subdir_path):
        # loop through each .wav file in the subdirectory
        for filename in os.listdir(subdir_path):
            # construct the path to the .wav file
            filepath = os.path.join(subdir_path, filename)
            
            # check if the file is a .wav file
            if filename.endswith(".wav"):
                # load the audio file using pydub
                audio = AudioSegment.from_file(filepath, format="wav")
                
                # check if the audio file is at least 4.5 seconds long
                if len(audio) >= 4500:
                    # split the audio file into 4.5 second non-overlapping chunks
                    chunks = audio[::4500]
                    
                    # loop through each chunk and save it as a new .wav file
                    for i, chunk in enumerate(chunks):
                        chunk_filename = f"{os.path.splitext(filename)[0]}_{i+1}.wav"
                        chunk_filepath = os.path.join(subdir_path, chunk_filename)
                        chunk.export(chunk_filepath, format="wav")
                        
                # remove the file if it's less than 4.5 seconds long
                else:
                    os.remove(filepath)
