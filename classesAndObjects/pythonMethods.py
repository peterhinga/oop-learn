# A Method is a function that is bound to an instance of a class

class Request:
    def send():
        print("sent")

class Response:
    def receive(*args):
        print("Receive", args)
# to call the function you have to call it via the class
Request.send()

# the send() function is an instance of the function class

print(Request.send)

# the type of send is a function

print(type(Request.send))

httpRequest = Request()

# This is a method
print(httpRequest.send)

# So httpRequest.send is a method while Request.send is a function

print(type(httpRequest.send))
print(type(Request.send))

# When you access a function via an object, the function becomes a method

Response.receive()

httpResponse = Response()

httpResponse.receive()