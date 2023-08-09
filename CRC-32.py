import binascii
from bitstring import BitArray

class CRC32:
    def __init__(self):
        self.polynomial = 0x04C11DB7

    def calculate(self, bit_string):
        # Rellenar con ceros a la izquierda hasta que la longitud sea un múltiplo de 8
        while len(bit_string) % 8 != 0:
            bit_string = '0' + bit_string

        bit_array = BitArray(bin=bit_string)
        crc = binascii.crc32(bit_array.bytes) & 0xFFFFFFFF
        return format(crc, '032b')

class Sender:
    def __init__(self, crc):
        self.crc = crc

    def send(self, bit_string):
        crc = self.crc.calculate(bit_string)
        print("Mensaje original: " + bit_string)
        print("CRC calculado: " + crc)
        return bit_string + crc

class Receiver:
    def __init__(self, crc):
        self.crc = crc

    def receive(self, bit_string):
        data, crc_received = bit_string[:-32], bit_string[-32:]
        crc_calculated = self.crc.calculate(data)

        print("Mensaje original: " + data)
        print("CRC recibido: " + crc_received)
        print("CRC calculado: " + crc_calculated)

        if crc_calculated == crc_received:
            return "No se detectaron errores."
        else:
            # Comprobamos cada bit individualmente
            for i in range(len(data)):
                bit = data[i]
                modified_data = data[:i] + ('1' if bit == '0' else '0') + data[i+1:]
                if self.crc.calculate(modified_data) == crc_received:
                    return f"Se detectó un error en el bit {i+1}: la trama se descarta"
            return "Se detectaron errores desconocidos: la trama se descarta"

# Ejemplo de uso
crc = CRC32()
sender = Sender(crc)
receiver = Receiver(crc)

# Trama sin manipular
data1 = "110101"
sent_data1 = sender.send(data1)
print("\nEmisor envía: " + sent_data1)
print(receiver.receive(sent_data1))

data2 = "101010"
sent_data2 = sender.send(data2)
print("\nEmisor envía: " + sent_data2)
print(receiver.receive(sent_data2))

data3 = "11110000"
sent_data3 = sender.send(data3)
print("\nEmisor envía: " + sent_data3)
print(receiver.receive(sent_data3))

# Tramas con un bit modificado
sent_data1_modified = "010101" + sent_data1[6:]
print("\nEmisor envía: " + sent_data1_modified)
print(receiver.receive(sent_data1_modified))

sent_data2_modified = "001010" + sent_data2[6:]
print("\nEmisor envía: " + sent_data2_modified)
print(receiver.receive(sent_data2_modified))

sent_data3_modified = "01110000" + sent_data3[8:]
print("\nEmisor envía: " + sent_data3_modified)
print(receiver.receive(sent_data3_modified))

# Tramas con dos bits modificados
print("\nTramas con dos bits modificados")
sent_data1_modified = "010101" + sent_data1[6:]
print("\nEmisor envía: " + sent_data1_modified)
print(receiver.receive(sent_data1_modified))

sent_data2_modified = "001010" + sent_data2[6:]
print("\nEmisor envía: " + sent_data2_modified)
print(receiver.receive(sent_data2_modified))

sent_data3_modified = "01110000" + sent_data3[8:]
print("\nEmisor envía: " + sent_data3_modified)
print(receiver.receive(sent_data3_modified))

print("\nTrama modificada para que el algoritmo no detecte el error")

sent_data1_modified = "010101" + sent_data1[6:]
sent_data1_modified_undetectable = "010101" + sender.send("010101")[6:]
print("\nEmisor envía: " + sent_data1_modified_undetectable)
print(receiver.receive(sent_data1_modified_undetectable))
