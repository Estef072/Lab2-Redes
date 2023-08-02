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

    const checksum1 = c1%Math.pow(2, blocksize)
    const checksum2 = c2%Math.pow(2, blocksize)

    console.log(c1, c2)
    console.log(checksum1, checksum2)
    console.log(tramas)
    console.log(numbers)

    
}

const block = 8
const prueba = "00000000111111111"
Fletcher(block, prueba)