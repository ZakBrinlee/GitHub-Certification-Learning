import os
import eyed3
import yaml
import datetime

# Function to read all mp3 files in the 'audio' directory
def read_mp3_files():
    mp3_files = []
    # Loop through all files in the 'audio' directory
    for file in os.listdir('audio'):
        # Check if the file is an mp3 file
        if file.endswith('.mp3'):
            # Load the audio file using eyed3
            audiofile = eyed3.load(os.path.join('audio', file))
            # Get the duration of the audio file in seconds and convert it to HH:MM:SS format
            duration = str(datetime.timedelta(seconds=int(audiofile.info.time_secs)))
            # Get the size of the file in bytes
            size = os.path.getsize(os.path.join('audio', file))
            # Format the size with commas as thousand separators
            size_with_commas = "{:,}".format(size)
            # Append the audio file information to the mp3_files list
            mp3_files.append({
                'title': audiofile.tag.title,
                'description': [comment.text for comment in audiofile.tag.comments],
                'filename': '/audio/' + file,
                'duration': duration,
                'length': size_with_commas
            })
    # Return the list of mp3 files
    return mp3_files

# Function to write data to a yaml file
def write_to_yaml(data, filename):
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Dump the data to the file
        yaml.dump(data, file, sort_keys=False)

# Call the read_mp3_files function and store the result in mp3_files
mp3_files = read_mp3_files()
# Write the mp3_files data to 'episodes.yaml'
write_to_yaml(mp3_files, 'episodes.yaml')