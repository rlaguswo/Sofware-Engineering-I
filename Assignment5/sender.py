import zmq

context = zmq.Context()

#  Socket to talk to server
#print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:")

#  Do 10 requests, waiting each time for a response
for request in range(1):

    print(f"Sending request {request} …")
    s = input("Send: ")
    socket.send_string(s)

    #  Get the reply.
    message = socket.recv()
print(f"Received reply {request} [ {message} ]")