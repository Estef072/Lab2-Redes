import socketio
import random
import string
from hamming import Hamming
from Fletcher import SendMessage, ReceiveMessage

sio = socketio.Client()

def toBinary(message):
    return ''.join(format(ord(i), '08b') for i in message)

def binary_to_text(binary_string):
    print("Binary String:", binary_string)
    binary_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    text_array = [chr(int(chunk, 2)) for chunk in binary_chunks]
    return ''.join(text_array)


def add_random_noise(message, probability):
    print(message)
    message = list(message)
    for i in range(len(message)):
        if random.random() < probability:
            message[i] = str((int(message[i])+1)%2)
    message = ''.join(message)
    print(message)
    return message

@sio.on('connect')
def on_connect():
    print('Conectado al servidor')

@sio.on('message')
def on_chat_message(arg):
    
    print('\nMensaje recibido:', arg)
    
    encoding = arg["encoding"]
    message = arg["message"]
    args = arg["args"]
    decoded = ""
    valid = True

    if encoding == "1":  # Hamming
        print(message)
        hamming = Hamming(args["n"], args["m"])
        decoded = hamming.decode(message)

    elif encoding == "2":  # CRC
        # Implement CRC handling if needed
        pass

    elif encoding == "3":  # Fletcher
        correct = ReceiveMessage([message, 8])  # Replace with appropriate function
        if correct:
            print("Ningun error detectado")
            decoded = correct.s
        else:
            valid = False
    else:
        print("WTF")

    if valid:
        print(decoded)
        output = binary_to_text(decoded)
        print("\nMensaje recibido:", output)
    
    print('\nMensaje recibido:', arg)

def send_message(message, encoding, noise):
    
    message = toBinary(message)
    lenght = len(message)
    args = {}
    
    if encoding == "1":
        print("Largo del mensaje: ", lenght, len([x for x in range(1, lenght+1) if x & (x-1) == 0]))
        hamming = Hamming(lenght + len([x for x in range(1, lenght+1) if x & (x-1) == 0]), lenght)
        message = hamming.encode(message)
        args["n"] = hamming.n
        args["m"] = hamming.m
        
    elif encoding == "2":
        """Agregar CRC-32"""
        pass
    else:
        message = SendMessage(8, message)[0]
        
    message = add_random_noise(message, noise)

    sio.emit('message', {"encoding":encoding,"message":message,"args":args})

def generate_random_string(size):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(size))
    return random_string

def test1(size, noise):
    message = generate_random_string(size)
    lenght = len(message)
    args = {}
    message = SendMessage(8, message)[0]
    new_message = add_random_noise(new_message, noise)
    if new_message==message:
        args["noise"]=False
    else:
        args["noise"]=True
    sio.emit('message', {"encoding":3,"message":new_message,"args":args})

sio.connect('http://localhost:3001')
while True:
    for i in range(10_000):
        test1(10, 0.01)
    '''  message = input("Ingrese un mensaje: ")
    encoding = 0
    while encoding not in ['1', '2', '3']:
        print("Tipo de codificacion: \n")
        print("(1) - Hamming")
        print("(2) - CRC-32 ")
        print("(3) - Fletcher")
        encoding = input("Ingrese el tipo de codificación: ")
    
    message = toBinary(message)
    lenght = len(message)
    args = {}
    
    if encoding == "1":
        print("Largo del mensaje: ", lenght, len([x for x in range(1, lenght+1) if x & (x-1) == 0]))
        hamming = Hamming(lenght + len([x for x in range(1, lenght+1) if x & (x-1) == 0]), lenght)
        message = hamming.encode(message)
        args["n"] = hamming.n
        args["m"] = hamming.m
        
    elif encoding == "2":
        """Agregar CRC-32"""
        pass
    else:
        message = SendMessage(8, message)[0]


    message = add_random_noise(message, 0.001)
    
    sio.emit('message', {"encoding":encoding,"message":message,"args":args}) '''


