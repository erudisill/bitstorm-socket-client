'''
Created on Dec 29, 2014

@author: ericrudisill
'''
import socket

# HOST, PORT = "72.3.250.117", 1878
#HOST, PORT = "72.3.250.117", 30006
HOST, PORT = "72.3.250.117", 1878

        
def client(ip, port):
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        try:
            while True:
                response = sock.recv(1024)
                if not response: 
                    print "[EMPTY RESPONSE]"
                    break

            	lines = response.split('\n')
               	for oneLine in lines:
                    parts = oneLine.split('|', 9)
                    #print parts
                    if (len(parts) >= 9):
                        try:
                            print parts[2] + "  " + parts[4].zfill(8) + "\t" + parts[8].rstrip()
                        except Exception as ex:
                            print str(ex)
                            print parts
                    
        except Exception as ex:
            print "[EXCEPTION] " + ex
        finally:
            print "[CLOSING SOCKET]"
            sock.close()
    
    
if __name__ == '__main__':
    print "\r\n\r\nBitStorm Socket Client"
    print "Press Ctrl-C to exit.\r\n"
    client(HOST, PORT)