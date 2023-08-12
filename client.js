

const Hamming = require('./jshamming.js');
const {sendMessage, receiveMessage} = require('./Fletcher.js');

const {io} = require('socket.io-client');
const socket = io("ws://127.0.0.1:3001")

function toBinary(message) {
    return [...message]
      .map((char) => char.charCodeAt(0).toString(2).padStart(8, '0'))
      .join('');
}

function binaryToText(binaryString) {
    console.log("Binary String",binaryString)
    const binaryChunks = binaryString.match(/.{1,8}/g);
    const textArray = binaryChunks.map(chunk => String.fromCharCode(parseInt(chunk, 2)));
    return textArray.join('');
  }
  


socket.on("connnect", "Conectado al servidor")

socket.on("message", (arg)=>{

    let encoding = arg.encoding
    let message = arg.message
    let args = arg.args
    let output;
    let decoded = "";
    let valid = true

    if (encoding == "1") { //Hamming
        let hamming = new Hamming(args.n, args.m)
        decoded = hamming.decode(message)


    } else if (encoding == "2") { //CRC

    } else if (encoding == "3") { //Fletcher
        let correct = receiveMessage([message, 8])
        if (correct ==true){
            console.log("Ningun error detectado");
            decoded = message.slice(0, message.length-16)
        }
        else{
            valid = false;
        }

    } else { console.log("WTF") }

    if (valid==true){
        console.log(decoded)
        output = binaryToText(decoded)
        console.log("\nMensaje recibido", output);
    }



})


function countPowersOfTwo(cadenaz) {
    const result = [1];
    for (let x = 1; x <= cadenaz; x++) {
        if ((x & (x - 1)) === 0 && x !== 1) {
            result.push(x);
        }
    }

    return result.length;
}

function addRandomNoise(message, probability) {
    console.log(message);
    const messageArray = message.split('');
    const length = messageArray.length
    for (let i = 0; i < length; i++) {
      if (Math.random() < probability) {
        messageArray[i] = String((parseInt(messageArray[i]) + 1) % 2);
      }
    }
  
    const modifiedMessage = messageArray.join('');
    console.log(modifiedMessage);
    return modifiedMessage;
  }

  const readline = require('readline');

  const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
  });
  
  function getInput(question) {
      return new Promise((resolve) => {
          rl.question(question, (answer) => {
              resolve(answer);
          });
      });
  }

  (async () => {
    while (true) {
        let message = await getInput("Ingrese un mensaje: ");
        let encoding = 0;

        while (!['1', '2', '3'].includes(encoding)) {
            console.log("Tipo de codificación:\n");
            console.log("(1) - Hamming");
            console.log("(2) - CRC-32");
            console.log("(3) - Fletcher");
            encoding = await getInput("Ingrese el tipo de codificación: ");
        }

        const messageBinary = toBinary(message);
        const length = messageBinary.length;
        const args = {};

        if (encoding === "1") {
            console.log("Longitud del mensaje: ", length, countPowersOfTwo(length));
            const hamming = new Hamming(length + countPowersOfTwo(length), length);
            const encodedMessage = hamming.encode(messageBinary);
            args.n = hamming.n;
            args.m = hamming.m;
            message = encodedMessage;
        } else if (encoding === "2") {
            // Agregar CRC-32
        } else {
            const [encodedMessage] = SendMessage([8, message]);
            message = encodedMessage;
        }

        message = addRandomNoise(message, 0.001);

        socket.emit('message', { encoding, message, args });
    }

    rl.close();
})();



