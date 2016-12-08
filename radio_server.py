try :
    import pyaudio
    import socket
    import threading
    import time
    import pydub
    import sys
except ImportError as e:
    print "unable to import modules"
    print e
    sys.exit(1)
    

CLIENT_LIST = []
CHUNK = (4410 * 3) - 2000

SERVER_ADDR = ("192.168.0.110",35000)



def int_to_string(integer):
    string = str(integer) + '\n'
    return string

def clientHandler():

    try:
        while True:
            if len(CLIENT_LIST) == 0:
                time.sleep(0.02)
            else:
                print "server sending song"
                i = 100
                frame = song_data[i*CHUNK:(i+1)*CHUNK]
                while(frame):
                    for client_addr in CLIENT_LIST:
                        SOCKET.sendto(frame,client_addr)
                    i += 1
                    frame = song_data[i*CHUNK:(i+1)*CHUNK]
                    time.sleep(0.05)
    except KeyboardInterrupt:
        SOCKET.close()
        sys.exit(1)




p = pyaudio.PyAudio()
#wf = wave.open("music_test.wav","rb")
#song_header = int_to_string(p.get_format_from_width(wf.getsampwidth())) +int_to_string(wf.getnchannels()) +int_to_string(wf.getframerate())
#wf.close()


song_file = pydub.AudioSegment.from_mp3("music_test2.mp3")
song_data = song_file.raw_data
print len(song_data)
print len(song_data)/(1024)
try:
    SOCKET = socket.socket(socket.AF_INET,socket.SO5 /y0CK_DGRAM)
except socket.error as e:
    print "unable to create socket"
    print e
    sys.exit(1)

try:    
    SOCKET.bind(SERVER_ADDR)
except socket.error as e:
    print "unable to bind addr"
    print e
    sys.exit(1)
    
SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client_thread = threading.Thread(target=clientHandler)
#print dir(client_thread)
client_thread.setDeamon = True
client_thread.daemon = True

client_thread.start()


while True:
    data, addr = SOCKET.recvfrom(1024)
    if data == "my secret key":
        print str(addr) + " connected"
        #SOCKET.sendto(song_header,addr)
        #time.sleep(0.5)
        CLIENT_LIST.append(addr)


SOCKET.close()
p.terminate()
s.close()
wf.close()
