
import socket
import urllib2
from time import time

network_file = '/proc/net/tcp'
server = 'http://127.0.0.1:5000'

ipaddr = socket.gethostbyname(socket.gethostname())
hostname = socket.gethostname()
api_version = 'v1'
context = 'receiver'

def read_file():
    try:
        fd = open(network_file,'r')
    except Exception as Error:
        print("Erro trying to read file: %s")
        print(Error)
    else:
        timestamp = str(time())
        tcp = fd.readlines()
        fd.close()
        for data in tcp:
            parse_data(timestamp,data)
        

def parse_data(timestamp,data):
    value = data.split()
    network = timestamp + ':' + hostname + ':' + ipaddr + ':' +value[1]+':'+value[2]+':'+value[3]
    print(server + "/" + api_version + "/" + context +"/" + network)
    try:
        req = urllib2.Request(server + "/" + api_version + "/" + context +"/" + network)
        connection = urllib2.urlopen(req)
        connection.close()
    except:
        pass

def send_data(data):
    pass

if __name__ == '__main__':
    read_file()