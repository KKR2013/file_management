from os import scandir
from pathlib import Path
from time import sleep
from shutil import move

def NewFileChecker(directory, rest_time):
    initial_files = set(scandir(directory))

    # You may add more file extensions if you like, but follow the same syntax. I just added the ones I need.
    documents_filetypes = [".jpg", ".png", ".jpeg", ".pdf", ".docx", ".txt", ".py"]
    video_filetypes = [".mp4"]
    large_filetypes = [".iso", ".dmg", ".pkg", ".zip"]
    music_filetypes = [".mp3"]
    sound_effects = [".sfx"]

    # Enter you directories where you want to move your files to.
    docs_dir = ""
    video_dir = ""
    large_dir = "" 
    music_dir = "" 
    sound_dir = "" 
    extra_dir = ""

    while True:
        current_files = set(scandir(directory))
        new_files = current_files - initial_files
        sleep(rest_time)

        if new_files:
            for file in new_files:
                file_path = Path(file)
                extension = file_path.suffix
                if extension in documents_filetypes:
                    move(directory + "/" + file, docs_dir + file)
                    print(f"Successfully moved {file} to downloaded images")
                elif extension in video_filetypes:
                    move(directory + "/" + file, video_dir + file)
                    print(f"Successfully moved {file} to downloaded videos")
                elif extension in large_filetypes:
                    move(directory + "/" + file, large_dir + file)
                    print(f"Successfully moved {file} to large files")
                elif extension in music_filetypes:
                    move(directory + "/" + file, music_dir + file)
                    print(f"Successfully moved {file} to music files")
                elif extension in sound_effects:
                    move(directory + "/" + file, sound_dir + file)
                    print(f"Successfully moved {file} to sound effects")
                else:
                    move(directory + "/" + file, extra_dir + file)
                    print(f"Successfully moved {file} to others")
            
            initial_files = current_files

# Enter the directory where you want to check for new files
NewFileChecker("", 3)