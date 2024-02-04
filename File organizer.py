import os
import shutil
import tkinter as tk
from tkinter import filedialog

def rename_files(directory):
    os.chdir(directory)

    for index, file in enumerate(os.listdir()):
         
        if os.path.isfile(file):

        
          _, file_extension = os.path.splitext(file)
        
        new_name = f"{index + 1}_file{file_extension}"

        
        os.rename(file, new_name)

def organize_files(directory):
    os.chdir(directory)

    
    audio_directory = os.path.join(directory, "audio")
    video_directory = os.path.join(directory, "video")
    image_directory = os.path.join(directory, "image")
    text_directory = os.path.join(directory, "txt")

    
    for subdirectory in [audio_directory, video_directory, image_directory, text_directory]:
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)

   
    seen_files = set()

    for file in os.listdir():
        
        
        if os.path.isfile(file):
            
            if file in seen_files:
                
                os.remove(file)
            else:
                seen_files.add(file)


               
                if is_audio(file):
                    shutil.move(file, audio_directory)
                elif is_video(file):
                    shutil.move(file, video_directory)
                elif is_text(file):
                    shutil.move(file, text_directory)
                elif is_image(file):
                    if is_screenshot(file):
                        shutil.move(file, image_directory)
                    else:
                        shutil.move(file, image_directory)

def is_audio(file):
    return os.path.splitext(file)[1] in audio_extensions

def is_text(file):
    return os.path.splitext(file)[1] in text_extensions

def is_video(file):
    return os.path.splitext(file)[1] in video_extensions

def is_image(file):
    return os.path.splitext(file)[1] in image_extensions

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in image_extensions) and "screenshot" in name.lower()

def organize_files_with_ui():
    directory = filedialog.askdirectory()
    if directory:
        
        rename_files(directory)

        
        organize_files(directory)
        result_label.config(text="Files organized successfully!")

        
        update_directory_paths(directory)

def update_directory_paths(directory):
    global audio_directory, video_directory, image_directory, text_directory
    audio_directory = os.path.join(directory, "audio")
    video_directory = os.path.join(directory, "video")
    image_directory = os.path.join(directory, "image")
    text_directory = os.path.join(directory, "txt")


text_extensions = (".txt",)
audio_extensions = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
                   ".alac", ".amr", ".ape", ".au", ".dss",
                   ".flac", ".flv", ".m4a", ".m4b", ".m4p",
                   ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
                   ".opus", ".qcp", ".tta", ".voc", ".wav",
                   ".wma", ".wv")
video_extensions = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
                   ".mp4", ".m4p", ".m4v", ".mxf")
image_extensions = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
                   ".gif", ".webp", ".svg", ".apng", ".avif")

#GUI


root = tk.Tk()
root.title("File Organizer")


organize_button = tk.Button(root, text="Organize Files", command=organize_files_with_ui)
organize_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()
