import speech_recognition as sr
import os

recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            print("Could not understand")
            return ""

def execute_command(command):
    if "list files" in command:
        os.system("dir")   # use 'ls' for Linux/Mac

    elif "current directory" in command:
        os.system("cd")

    elif "make folder" in command:
        folder_name = command.replace("make folder", "").strip()
        os.system(f"mkdir {folder_name}")

    elif "remove file" in command:
        file_name = command.replace("remove file", "").strip()
        os.system(f"del {file_name}")

    elif "exit" in command:
        print("Exiting...")
        exit()

    else:
        print("Command not recognized")

while True:
    cmd = listen_command()
    execute_command(cmd)