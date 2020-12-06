import os.path
import os
from os import listdir
from os.path import isfile, join
from os import walk


def getFiles(connectionSocket):
    # arr = os.listdir()

    global dirpath, dirnames, filenames
    f = []
    for (dirpath, dirnames, filenames) in walk(os.getcwd()):
        f.extend(filenames)
        break

    print(dirpath)
    print(dirnames)
    print(filenames)

    data = '<ul>'
    for x in filenames:
        data += '<h3><a href="/file/' + x + '"><li>' + x + '</li></a></h3>'
    data += '</ul>'
    print(data)

    response = b'HTTP/1.1 200 OK\r\n'
    response += b'Server: Myserver/1.0\r\n'
    response += b'Content-type: text/html\r\n'
    response += b'Connection: Closed\r\n\r\n'

    response_body = '''
    <html>
    <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    </head>
    <body>
    <div class="container"><br>
    <h1>List of Files</h1><br>
    ''' + data + '''
    </div>
    </body>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
    </html> '''

    response_body = response_body.encode()

    response = b''.join([response, response_body])

    connectionSocket.sendall(response)
