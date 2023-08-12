"""import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3000  # Port to listen on (non-privileged ports are > 1023)
print('Mounted server')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connection accepted')
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)"""
            
import socketio
import logging

logging.basicConfig(level=logging.ERROR)
sio = socketio.Server(cors_allowed_origins="*")
sio.logger.setLevel(logging.ERROR)
app = socketio.WSGIApp(sio)
users = {'py':None,
         'js':None}

@sio.on("start")
def start():
    print("Se ha iniciado la comunicacion")

@sio.on("connect")
def connect(sid, environ):
    
    if environ["HTTP_USER_AGENT"].startswith("python"):
        users['py'] = sid
        print("Python client connected")
    else:
        users['js'] = sid
        print("JS client connected")
            
    print("Se han conectado")

@sio.on("message")
def message(sid, data):
    if data["encoding"] == "stop":
        print("Done")
        return False
    if sid == users['py']:
        sio.emit("message", data, room=users['js'])
    elif sid == users['js']:
        sio.emit("message", data, room=users['py'])
    else:
        print("Usuario no encontrado")
    #print("Mensaje recibido: ", data)

@sio.on("disconnect")
def disconnect(sid):
    print("Se han desconectado")

if __name__ == "__main__":
    import eventlet
    eventlet.wsgi.server(eventlet.listen(("127.0.0.1", 3001)), app)


#python : 5555
#js: 