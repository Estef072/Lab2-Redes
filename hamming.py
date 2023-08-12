class Hamming:
    
    def __init__(self, n, m):
        """Inicializa el código de Hamming.

        Args:
            n (int): Numero de bits en el codigo codificado. 
            m (int): Bits originales en el codigo sin codificar.

        Raises:
            ValueError: Si n + m + 1 > 2**n.
        """
        
        if n + m + 1 > 2**n:
            raise ValueError(f"Invalid parameters: {n} + {m} + 1 > 2**{n}")
        
        self.n = n
        self.m = m
        
        self.ps = [x for x in range(1, self.n+1) if x & (x-1) == 0]
    
    def get_parity_bits(self, cadena) -> list:
        return [cadena[i-1] for i in self.ps]
    
    def get_data_bits(self, cadena:str or list) -> list:
        return [cadena[i-1] for i in range(1, self.n+1) if i not in self.ps]
        
    def encode(self, cadena:str) -> str:
        
        if len(cadena) != self.m:
            raise ValueError("Invalid data length")
        
        data_bits = list(map(int, list(cadena)))
        code = data_bits.copy()

        lista = [0] * len(self.ps)
        
        #print(data_bits, self.ps, code, lista)
        
        for x in self.ps:
            code.insert(x-1, 0)
            
        for i in range(1, self.n+1):
            for x in self.ps:
                if i & x == x:
                    #print(i, x, lista[self.ps.index(x)], code[i-1])
                    lista[self.ps.index(x)] = (lista[self.ps.index(x)] + code[i-1]) % 2
                
        for i, x in enumerate(lista):
            code[self.ps[i]-1] = x
        
        return ''.join(map(str, code))
    
    def check_hamming(self, cadena:str):
        
        if len(cadena) != self.n:
            raise ValueError("Invalid code length", cadena, len(cadena))
        
        # Convert code to list of bits
        code_bits = list(map(int, list(cadena)))
        code = code_bits.copy()
        
        code = self.get_data_bits(code)
                
        original = self.encode(''.join(map(str, code)))
        original_parity = self.get_parity_bits(original)  
        cadena_parity = self.get_parity_bits(cadena)
        
        original_parity = int("".join(original_parity[::-1]),2)
        cadena_parity = int("".join(cadena_parity[::-1]),2)
        
        index = original_parity^cadena_parity
        
        if index:
            code_bits[index-1] = int(not code_bits[index-1])
                    
        return ''.join(map(str, code_bits)), index
    
    def decode(self, cadena:str) -> str:
        
        cadena, index = self.check_hamming(cadena)
        cadena = list(map(int, list(cadena)))
        
        #print(cadena, index)
              
        
        #print(cadena)
        cadena = self.get_data_bits(cadena)
                
        return ''.join(map(str, cadena))
        
        
x = Hamming(7, 4)
#print(x.encode('1011'))

#print(x.decode('0110110'))
