import socket # to import to socket programming
import threading # multiple clinets 
import random # random number 
import json 



def handle_CLient(Client_socket): 
    try: 
        data=Client_socket.recv(1024).decode()
        request=json.loads(data)


        if "method" in request: 
            method= request["method"]
            if method== "Random" and "Tal1" in request and "Tal2" in request: 
                num1=request ["Tal1"]
                num2=request["Tal2"]
                randomnr= random.randint(num1,num2)
                response={"Result":randomnr}
            elif method== "Add" and "Tal1" in request and "Tal2" in request: 
                num1=request ["Tal1"]
                num2=request["Tal2"]
                Addnr= num1+num2 
                response={"Result":Addnr}
            elif method== "Subtract" and "Tal1" in request and "Tal2" in request: 
                num1=request ["Tal1"]
                num2=request["Tal2"]
                subnr= num1-num2
                response={"Result":subnr}
            else:
                response= {"error": "not found"}
        else: 
             response= {"error": "not found"}
        Client_socket.send(json.dumps(response).encode())
    except Exception as exception:
        print(f"Error in client:{str(exception)}")
    finally:
        Client_socket.close()
        
            

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM) # to connect witht the socket stream 
server.bind(('localhost', 1234)) # port connection 
server.listen(7) # the specific channal to listen to 
print("Server is listening on port 1234")
while True: #while the socket is runing execute the code below 
    Client, addr= server.accept()
    print(f"accept address from{addr[0]}:{addr[1]}")
    Client_handler= threading.Thread(target=handle_CLient, args=(Client,))
    Client_handler.start()

