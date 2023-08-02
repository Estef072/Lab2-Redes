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
        
    print(c1, c2)
    print(checksum1, checksum2)
    
    print(tramas)  
    print(numbers)  
    
    

blockSize = 8
prueba = "00000000111111111"

Fletcher(blockSize, prueba)
    