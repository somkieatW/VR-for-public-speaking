#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyaudio
import sys
import wave
import requests
import json
import speech_recognition as sr
mysp=__import__("my-voice-analysis")


# In[2]:


import pyaudio
import wave
 
def record_audio(RECORD_SECONDS, WAVE_OUTPUT_FILENAME):
    #--------- SETTING PARAMS FOR OUR AUDIO FILE ------------#
    FORMAT = pyaudio.paInt16    # format of wave
    CHANNELS = 2                # no. of audio channels
    RATE = 44100                # frame rate
    CHUNK = 1024                # frames per audio sample
    #--------------------------------------------------------#
 
    # creating PyAudio object
    audio = pyaudio.PyAudio()
 
    # open a new stream for microphone
    # It creates a PortAudio Stream Wrapper class object
    stream = audio.open(format=FORMAT,channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
 
    #----------------- start of recording -------------------#
    print("Listening...")
 
    # list to save all audio frames
    frames = []
 
    for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
        # read audio stream from microphone
        data = stream.read(CHUNK)
        # append audio data to frames list
        frames.append(data)
 
    #------------------ end of recording --------------------#
    print("Finished recording.")
 
    stream.stop_stream()    # stop the stream object
    stream.close()          # close the stream object
    audio.terminate()       # terminate PortAudio
 
    #------------------ saving audio ------------------------#
 
    # create wave file object
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
 
    # settings for wave file object
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
 
    # closing the wave file object
    waveFile.close()
 
def read_audio(WAVE_FILENAME):
    # function to read audio(wav) file
    with open(WAVE_FILENAME, 'rb') as f:
        audio = f.read()
    return audio


# In[3]:


import requests
import json
 
# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'
 
# Wit.ai api access token
wit_access_token = 'BBL4UDNORDRPGH5V5RDDHT5WRRQMWQQ7'
 
def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
 
    # record audio of specified length in specified audio file
   # record_audio(num_seconds, AUDIO_FILENAME)
 
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
 
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}
 
    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
 
    # converting response content to JSON format
    data = json.loads(resp.content)
 
    # get text from data
    text = data['_text']
 
    # return the text
    return text


# record_audio(10,'Doctor.wav')

# text = RecognizeSpeech("Doctor.wav")

# print(text)

# In[4]:



'''recorder.py
Provides WAV recording functionality via two approaches:

Blocking mode (record for a set duration):
>>> rec = Recorder(channels=2)
>>> with rec.open('blocking.wav', 'wb') as recfile:
...     recfile.record(duration=5.0)

Non-blocking mode (start and stop recording):
>>> rec = Recorder(channels=2)
>>> with rec.open('nonblocking.wav', 'wb') as recfile2:
...     recfile2.start_recording()
...     time.sleep(5.0)
...     recfile2.stop_recording()
'''
import pyaudio
import wave

class Recorder(object):
    '''A recorder class for recording audio to a WAV file.
    Records in mono by default.
    '''

    def __init__(self, channels=1, rate=44100, frames_per_buffer=1024):
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer

    def open(self, fname, mode='wb'):
        return RecordingFile(fname, mode, self.channels, self.rate,self.frames_per_buffer)

class RecordingFile(object):
    def __init__(self, fname, mode, channels, 
                rate, frames_per_buffer):
        self.fname = fname
        self.mode = mode
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self._pa = pyaudio.PyAudio()
        self.wavefile = self._prepare_file(self.fname, self.mode)
        self._stream = None

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def record(self, duration):
        # Use a stream with no callback function in blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.frames_per_buffer)
        for _ in range(int(self.rate / self.frames_per_buffer * duration)):
            audio = self._stream.read(self.frames_per_buffer)
            self.wavefile.writeframes(audio)
        return None

    def start_recording(self):
        # Use a stream with a callback in non-blocking mode
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.frames_per_buffer,
                                        stream_callback=self.get_callback())
        self._stream.start_stream()
        return self

    def stop_recording(self):
        self._stream.stop_stream()
        return self

    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wavefile.writeframes(in_data)
            return in_data, pyaudio.paContinue
        return callback


    def close(self):
        self._stream.close()
        self._pa.terminate()
        self.wavefile.close()

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.channels)
        wavefile.setsampwidth(self._pa.get_sample_size(pyaudio.paInt16))
        wavefile.setframerate(self.rate)
        return wavefile


# In[5]:


import time

sentence = ""
i = 1
while i <= 2:
    name = "nonblocking" + str(i) + ".wav"
    rec = Recorder(channels=2)
    with rec.open(name, 'wb') as recfile2:
        recfile2.start_recording()
        time.sleep(3.0)
        recfile2.stop_recording()
        print 'finish_record: '+name
        a = RecognizeSpeech(name) + " "
        print a
    sentence = sentence + a
    i = i+1


# In[5]:


def recording():
    status = True
    while status:
        recfile2.start_recording()
        if(Input.GetKeyDown(KeyCode.Space)):
            recfile2.stop_recording()
            status = False


# In[6]:


print sentence


# In[7]:


record_audio(10,'Doctor.wav')


# In[9]:



RecognizeSpeech("Doctor.wav")


# In[ ]:




