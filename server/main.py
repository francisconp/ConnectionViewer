from flask import Flask
from queue import queue

app = Flask(__name__)

remote = queue(hostname='localhost',queue='data')
remote.connect()

@app.route("/v1/receiver/<data>", methods=['GET'])
def v1_receiver(data):
    remote.send(data)
    return ('', 201)

if __name__ == '__main__':
    app.run()