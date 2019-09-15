import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud import speech_v1p1beta1


client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname('~'),
    'resources',
    '30 Second Conversations.wav')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
    

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    audio_channel_count=2,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)


for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))


def sample_long_running_recognize(local_file_path):
    """
    Print confidence level for individual words in a transcription of a short audio
    file
    Separating different speakers in an audio file recording

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    client = speech_v1p1beta1.SpeechClient()

    # local_file_path = 'resources/commercial_mono.wav'

    # If enabled, each word in the first alternative of each result will be
    # tagged with a speaker tag to identify the speaker.
    enable_speaker_diarization = True

    # Optional. Specifies the estimated number of speakers in the conversation.
    diarization_speaker_count = 2

    # The language of the supplied audio
    language_code = "en-US"
    config = {
        "enable_speaker_diarization": enable_speaker_diarization,
        "diarization_speaker_count": diarization_speaker_count,
        "language_code": language_code,
    }


    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    for result in response.results:
        # First alternative has words tagged with speakers
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
        # Print the speaker_tag of each word
        for word in alternative.words:
            print(u"Word: {}".format(word.word))
            print(u"Speaker tag: {}".format(word.speaker_tag))


sample_long_running_recognize(file_name)