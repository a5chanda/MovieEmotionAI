import subprocess

command = "ffmpeg -i C:/documents/HTN/videoplayback(1).mp4 -vn -acodec copy pythaudio.wav"

subprocess.call(command, shell=True)