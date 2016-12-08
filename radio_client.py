import pyaudio
import socket
import threading
import time
import wave

CHUNK = 4410 * 2 

p = pyaudio.PyAudio()

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr = ("192.168.0.110",35000)
s.sendto("my secret key",server_addr)

#song_header, addr = s.recvfrom(1024)

#formatt = int(song_header[0])
#channelss = int(song_header[2])
#ratee = int(song_header[4:9])

stream = p.open(format=8,
                channels=2,
                rate=44100,
                output=True)

while True:
    data , addr = s.recvfrom(CHUNK)
    stream.write(data)
