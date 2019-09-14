from __future__ import unicode_literals
import youtube_dl
import ffmpeg


url = raw_input("Enter youtube URL: ")

ydl = youtube_dl.YoutubeDL({
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
    'outtmpl': '%(title)s.%(etx)s',
    'quiet': False
    })

result = {}

with ydl:
    result = ydl.extract_info(
        #'http://www.youtube.com/watch?v=BaW_jenozKc',
        url,
        download=True # We just want to extract the info
    )

#Convert from stereo to mono    
# from pydub import AudioSegment
# sound = AudioSegment.from_wav("./" + re.match("*.wav"))
# sound = sound.set_channels(1)
# sound.export("./" + "mono" + re.match("*.wav"), format="wav")
# print(result['']);


