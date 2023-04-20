import os
import shutil

# define the directory where the csv files are located
csv_dir = "D:\\esc"

# loop through each csv file in the directory
for csv_file in os.listdir(csv_dir):
    if csv_file.endswith(".csv"):
        
        # create a folder for the csv file
        folder_name = csv_file[:-4] # remove the .csv extension
        folder_path = os.path.join(csv_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        # read the csv file
        csv_path = os.path.join(csv_dir, csv_file)
        with open(csv_path, 'r') as f:
            lines = f.readlines()
            
        # loop through each line in the csv file
        for line in lines:
            line = line.strip() # remove any whitespace
            
            # extract the filename from the csv line
            filename = line.split(",")[0].strip()
            
            # move the wav file to the new folder
            wav_path = os.path.join("D:\\audio", filename)
            if os.path.exists(wav_path):
                dest_path = os.path.join(folder_path, filename)
                shutil.move(wav_path, dest_path)
