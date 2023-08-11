def Fletcher(blockSize: int, message:str):
    
    sizes = [8, 16, 32]
    
    #Add padding depending on the blocksize wanted
    def padding(blockSize: int, message:str):
        new_message = message
        remainder = len(message)%blockSize
        if remainder !=0:
            new_message += "0"*(blockSize-remainder)
            
        return new_message
    
    
    if blockSize not in sizes:
        print("El tamaño de bloque especificado no es posible ")
        return
    #Get new message with padding if necessary
    new_message = padding(blockSize, message)
    
    #create tramas
    tramas = [new_message[i:i+blockSize] for i in range(0,len(new_message),blockSize)]
    numbers = [int(i,2) for i in tramas] 
    
    #Compute checksum
    c1 = 0
    c2 = 0
    for i in numbers:
        c1 +=i
        c2 += c1
        
    checksum1 = c1%pow(2,blockSize)
    checksum2 = c2%pow(2,blockSize)
    
    checksum1 = str(bin(checksum1))[2:]
    checksum2 = str(bin(checksum2))[2:]
    
    checksum1 = '0'*(8-len(checksum1))+checksum1
    checksum2 = '0'*(8-len(checksum2))+checksum2

    return checksum1+checksum2
      
    
    
#Add checksum to message
def SendMessage(blockSize, message):
    adder = Fletcher(blockSize, message)
    return (message+adder, blockSize)

#check if checksum is correct
def ReceiveMessage(message):
    new_message, blockSize = message
    
    print('Input: ', new_message)
        
    index = len(new_message)-(blockSize*2)
    
    checksum = new_message[index:]
    clean_message = new_message[:index]
    
    print('Original Message: ', clean_message)

    check = Fletcher(blockSize,clean_message)
    
    if checksum==check:
        print('* Sin errores *')
    else:
        print('* Se ha encontrado un error *')
        print('Checksum recibido: ')
        print('-', checksum)
        print('-', checksum[0:blockSize], '->', int(checksum[0:blockSize], 2))
        print('-', checksum[blockSize:], '->', int(checksum[blockSize:], 2))
        print('')
        print('Checksum encontrado: ')
        print('-', check)
        print('-', check[0:blockSize], '->', int(check[0:blockSize], 2))
        print('-', check[blockSize:], '->', int(check[blockSize:], 2))
    
    return check==checksum

blockSize = 8
#prueba = "0100"
#mensaje = SendMessage(blockSize, prueba)
mensaje = ('1000000001000000000000000', blockSize)
#ReceiveMessage(mensaje)
#000001111 -> 0000000111000011110001110
#1001011 -> 10010111001000010010110
#0100 ->  01110100000001000000
numbers = []

a = "AB"
print(''.join(format(i, 'b') for i in bytearray(a, encoding='utf-8'))
)

''' for i in range(1024):
    mensaje = Fletcher(blockSize, str(bin(i))[2:])
    if mensaje not in numbers:
        numbers.append(mensaje)
    else:
        print(i, mensaje)
        break '''
