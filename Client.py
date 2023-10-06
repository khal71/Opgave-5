import socket
import json

Client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Client.connect(('localhost',1234))
operation= input ("Enter Operation(Random/Add/Subtract):")
num1= int (input ("Enter first number:"))
num2= int (input("Enter second number:"))
request = {"method": operation, "Tal1": num1, "Tal2": num2}
Client.send(json.dumps(request).encode())
server_response=Client.recv(1024).decode()
response= (json.loads(server_response))
if "error"in response: 
 print(f"error on server:{response['error']}")
elif "Result" in response:
 print(f"response :{response['Result']}")

 
 
