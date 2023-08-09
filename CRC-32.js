const crc32 = require('buffer-crc32');

class CRC32 {
    constructor() {
        this.polynomial = 0x04C11DB7;
    }

    calculate(bitString) {
        while (bitString.length % 8 !== 0) {
            bitString = '0' + bitString;
        }

        let bitArray = Buffer.from(bitString, 'binary');
        let crc = crc32.unsigned(bitArray);
        return crc.toString(2).padStart(32, '0');
    }
}

class Sender {
    constructor(crc) {
        this.crc = crc;
    }

    send(bitString) {
        let crc = this.crc.calculate(bitString);
        console.log("Mensaje original: " + bitString);
        console.log("CRC calculado: " + crc);
        return bitString + crc;
    }
}

class Receiver {
    constructor(crc) {
        this.crc = crc;
    }

    receive(bitString) {
        let data = bitString.slice(0, -32);
        let crcReceived = bitString.slice(-32);
        let crcCalculated = this.crc.calculate(data);

        console.log("Mensaje original: " + data);
        console.log("CRC recibido: " + crcReceived);
        console.log("CRC calculado: " + crcCalculated);

        if (crcCalculated === crcReceived) {
            return "No se detectaron errores.";
        } else {
            for (let i = 0; i < data.length; i++) {
                let bit = data[i];
                let modifiedData = data.slice(0, i) + (bit === '0' ? '1' : '0') + data.slice(i + 1);
                if (this.crc.calculate(modifiedData) === crcReceived) {
                    return `Se detectó un error en el bit ${i + 1}: la trama se descarta`;
                }
            }
            return "Se detectaron errores desconocidos: la trama se descarta";
        }
    }
}

// Ejemplo de uso
let crc = new CRC32();
let sender = new Sender(crc);
let receiver = new Receiver(crc);

// Trama sin manipular
let data1 = "110101";
let sentData1 = sender.send(data1);
console.log("\nEmisor envía: " + sentData1);
console.log(receiver.receive(sentData1));

let data2 = "101010";
let sentData2 = sender.send(data2);
console.log("\nEmisor envía: " + sentData2);
console.log(receiver.receive(sentData2));

let data3 = "11110000";
let sentData3 = sender.send(data3);
console.log("\nEmisor envía: " + sentData3);
console.log(receiver.receive(sentData3));

// Tramas con un bit modificado
let sentData1Modified = "010101" + sentData1.slice(6);
console.log("\nEmisor envía: " + sentData1Modified);
console.log(receiver.receive(sentData1Modified));

let sentData2Modified = "001010" + sentData2.slice(6);
console.log("\nEmisor envía: " + sentData2Modified);
console.log(receiver.receive(sentData2Modified));

let sentData3Modified = "01110000" + sentData3.slice(8);
console.log("\nEmisor envía: " + sentData3Modified);
console.log(receiver.receive(sentData3Modified));

// Tramas con dos bits modificados
console.log("\nTramas con dos bits modificados");
sentData1Modified = "010101" + sentData1.slice(6);
console.log("\nEmisor envía: " + sentData1Modified);
console.log(receiver.receive(sentData1Modified));

sentData2Modified = "001010" + sentData2.slice(6);
console.log("\nEmisor envía: " + sentData2Modified);
console.log(receiver.receive(sentData2Modified));

sentData3Modified = "01110000" + sentData3.slice(8);
console.log("\nEmisor envía: " + sentData3Modified);
console.log(receiver.receive(sentData3Modified));

console.log("\nTrama modificada para que el algoritmo no detecte el error");

sentData1Modified = "010101" + sentData1.slice(6);
let sentData1ModifiedUndetectable = "010101" + sender.send("010101").slice(6);
console.log("\nEmisor envía: " + sentData1ModifiedUndetectable);
console.log(receiver.receive(sentData1ModifiedUndetectable));
