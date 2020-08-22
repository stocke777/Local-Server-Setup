import sys
import socket
from _thread import *

server = "192.168.43.215"
port = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def read_pos(s):
    s = s.split(",")
    return int(s[0]), int(s[1])

pos = [(0, 0), (100, 100)]

def threaded_client(conn, player):
    print(player, pos, make_pos(pos[player]))
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            if not data:
                print("DISCONNECTED")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending: ", reply)
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("Lost Connection")
    conn.close()

currentplayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to::", addr)
    start_new_thread(threaded_client, (conn, currentplayer))
    currentplayer+=1 