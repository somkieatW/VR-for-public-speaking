#!/usr/bin/env python
# coding: utf-8

# In[98]:


import pyaudio
import sys
import wave

mysp=__import__("my-voice-analysis")
print(55555)


# In[67]:


import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


# In[21]:


p="output" # Audio File title
c=r"C:\Users\Asus\Python" # Path to the Audio_File directory (Python 3.7)
mysp.myspgend(p,c)
mysp.mysppaus(p,c)
print(555)


# In[106]:


import speech_recognition as sr

r = sr.Recognizer()
with sr.WavFile("output.wav") as source:              # ใช้ "test.wav"  เป็นแหล่งให้ข้อมูลเสียง
    audio = r.record(source)                        # ส่งข้อมูลเสียงจากไฟล์
try:
    print("Transcription: " + r.recognize_google(audio))   # แสดงข้อความจากเสียงด้วย Google Speech Recognition
except sr.RequestError as e:                                 # ประมวลผลแล้วไม่รู้จักหรือเข้าใจเสียง
    print("Could not understand audio")
text = r.recognize_google(audio)
storeText = text


data = text
words = data.split()

unwanted_chars = ".,-_"
wordfreq = {}
for raw_word in words:
    word = raw_word.strip(unwanted_chars)
    if word not in wordfreq:
        wordfreq[word] = 0 
    wordfreq[word] += 1
    num = wordfreq[word]
    
    
print(sorted(wordfreq.items(), key = 
             lambda kv:(kv[1], kv[0]))) 
    

    


#def freq(str): 
  
    # break the string into list of words  
  #  str = str.split()          
 #   str2 = [] 
  
    # loop till string values present in list str 
   # for i in str:              
  
        # checking for the duplicacy 
        #if i not in str2: 
  
            # insert value in str2 
  #          str2.append(i) 
        
   # print(str2)
            
       # str2.sort()
    #hashtable = {}
    #for i in range(len(str2)):
     #   hashtable[i] = str2[i]
        
    #print(hashtable)
    
    
    #for word in str2: 
        #print(word)
     #   try:
      #      hashtable[word] = hashtable[word] + 1
       # except KeyError:
        #    hashtable.setdefault(word,0)
        # count the frequency of each word(present  
        # in str2) in str and print 
        #str2.sort()
        #print('Frequency of', str2[i], 'is :', str.count(str2[i]))
        #hashj = {str2[i] : str.count(str2[i])}
        #hashj = sorted(hashj.items(), key=lambda x: x[1], reverse=True)
        #print(hashj)
        
        #print(hashj)
    
    
    #print(sorted(hashj.items(), key = lambda kv:(kv[1], kv[0])))
    #print(hashj)
        
#freq(text)


# In[ ]:




