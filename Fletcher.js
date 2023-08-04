function Fletcher(blocksize, message){

    //blocksizes
    const sizes = [8,16,32]

    //Add padding depending on the blocksize wanted
    function padding(blocksize, message){
        let new_message = message
        let remainder = message.length%blocksize
        if(remainder!=0){
            new_message +="0".repeat(blocksize-remainder)

        }
        return new_message
        
    }
 
    if (!sizes.includes(blocksize)){
        console.log("El tamaño de bloque especificado no es posible ")
        return
    }
    
    const new_message = padding(blocksize, message)
    let tramas = []

    //Create tramas in blockSizes
    for(let i = 0; i<new_message.length; i+=blocksize){
        tramas.push(new_message.slice(i, i+blocksize))
    }
    //convert from each trama from binary to decimal
    const numbers = tramas.map(element =>{
        return parseInt(element, 2)
    })

    //compute checksum
    let c1 = 0
    let c2 = 0

    for(let i = 0; i<numbers.length; i++){
        c1+=numbers[i]
        c2+=c1
    }

    let checksum1 = c1%Math.pow(2, blocksize)
    let checksum2 = c2%Math.pow(2, blocksize)

    checksum1 = checksum1.toString(2)
    checksum2 = checksum2.toString(2)

    checksum1 = '0'.repeat(8-checksum1.length)+checksum1
    checksum2 = '0'.repeat(8-checksum2.length)+checksum2
    

    return checksum1+checksum2
}

function sendMessage(blockSize, message){
    adder = Fletcher(blockSize, message)
    console.log('- SENDER')
    console.log('- input: ', message)
    console.log('- output: ', message+adder)

    return [message+adder, blockSize]
}

function receiveMessege(message){
    let new_message = message[0]
    let blockSize = message[1]

    console.log('Input: ', new_message)

    index = new_message.length- (blockSize*2)

    checksum = new_message.slice(index)
    clean_message = new_message.slice(0, index)

    console.log('Original Message: ', clean_message)

    check = Fletcher(blockSize, clean_message)

    if(check===checksum){
        console.log('* Sin errores * ')
    }
    else{
        console.log('* Se ha encontrado un error * ')
        console.log('Checksum recibido: ')
        console.log('- ', checksum)
        console.log('-', checksum.slice(0,blockSize),'->',parseInt(checksum.slice(0,blockSize), 2))
        console.log('-', checksum.slice(blockSize,) ,'->',parseInt(checksum.slice(blockSize,),2))
        console.log('')
        console.log('Checksum encontrado: ')
        console.log('- ', check)
        console.log('-', check.slice(0,blockSize),'->',parseInt(check.slice(0,blockSize), 2))
        console.log('-', check.slice(blockSize,) ,'->',parseInt(check.slice(blockSize,), 2))
    }

    return check===checksum
}


const block = 8
const prueba = "00000000"


mensaje = sendMessage(block, prueba)
//mensaje = ['01110100000001000000',block]
//console.log('- RECEPTOR')
//receiveMessege(mensaje)