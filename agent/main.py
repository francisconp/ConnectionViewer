
import socket
import urllib2
from time import time

network_file = '/proc/net/tcp'
server = 'http://127.0.0.1'

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
        for data in fd:
            parse_data(timestamp,data)
        fd.close()

def parse_data(timestamp,data):
    value = data.split()
    network = timestamp + ':' + hostname + ':' + ipaddr + ':' +value[1]+':'+value[2]+':'+value[3]
    print(server + "/" + api_version + "/" + context +"/" + network)
    req = urllib2.Request(server + "/" + api_version + "/" + context +"/" + network)
    urllib2.urlopen(req)
    print(network)

def send_data(data):
    pass

if __name__ == '__main__':
    read_file()