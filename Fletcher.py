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
    
    print('checksum1: ', checksum1, len(checksum1), int(checksum1, 2))
    print('checksum2: ', checksum2, len(checksum2), int(checksum2, 2))
    return checksum1+checksum2
      
    
    
#Add checksum to message
def SendMessage(blockSize, message):
    adder = Fletcher(blockSize, message)
    return (message+adder, blockSize)

#check if checksum is correct
def ReceiveMessage(message):
    new_message, blockSize = message
    
    print(new_message, blockSize)
    index = len(new_message)-(blockSize*2)
    
    checksum = new_message[index:]
    clean_message = new_message[:index]

    check = Fletcher(blockSize,clean_message)
    
    return check==checksum

blockSize = 8
prueba = "00000000111111111"
print('prueba', len(prueba), prueba)
print(bin(255))


mensaje = SendMessage(blockSize, prueba)
print(ReceiveMessage(mensaje))

