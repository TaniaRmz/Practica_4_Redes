import socket
import sys

def processArguments():
    host_server = sys.argv[1]

    arguments = [host_server]
    return arguments 


def constructHTTPRequest(host_server):
    http_method = sys.argv[2]
    url = sys.argv[3]
    version = "HTTP/1.1"
    request_line = http_method + " " + url + " " + version + "\r\n"

    options =   ["Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"] + \
                ["Chrome/51.0.2704.103 Safari/537.36"] + \
                ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"] + \
                ["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"]
    user_agent = "User-Agent: " + options[int(sys.argv[4])-1]
    host = "Host: " + host_server
    
    accept = "Accept: */*"
    accept_charset = "Accept-Charset: *"
    accept_encoding = "Accept-Encoding: " + sys.argv[5]
    accept_language = "Accept-Language: *"
    connection = "Connection: "+ sys.argv[6]
    header_lines =  host + "\r\n" + \
                    user_agent + "\r\n" + \
                    accept + "\r\n" + \
                    accept_charset + "\r\n" + \
                    accept_encoding + "\r\n" + \
                    accept_language + "\r\n" + \
                    connection + "\r\n"

    HTTP_request =  request_line + \
                    header_lines + "\r\n"
    
    return HTTP_request

def TCPconnection(host_server, HTTP_request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host_server, 80))
        s.send(HTTP_request.encode())

        while True:
            HTTP_response = s.recv(1024)
            if not HTTP_response:
                break
            print (HTTP_response.decode())

        s.close()
        print ("\n\nConexion con el servidor finalizada\n")

    except socket.timeout:
        print("No response :(")
    except socket.error as socket_error:
        print("Error: ", socket_error)

arguments = processArguments()
HTTP_request = constructHTTPRequest(*arguments)
TCPconnection(arguments[0], HTTP_request)


