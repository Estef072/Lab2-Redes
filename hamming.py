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
        
    def encode(self, cadena):
        
        if len(cadena) != self.m:
            raise ValueError("Invalid data length")
        
        data_bits = list(map(int, list(cadena)))
        code = data_bits.copy()
        ps = [x for x in range(1, self.n+1) if x & (x-1) == 0]        
        
        lista = [0] * len(ps)
        
        
        for x in ps:
            code.insert(x-1, 0)
            
        for i in range(1, self.n+1):
            for x in ps:
                if i & x == x:
                    print(i, x, lista[ps.index(x)], code[i-1])
                    lista[ps.index(x)] = (lista[ps.index(x)] + code[i-1]) % 2
        
        for x in lista:
            code[ps[lista.index(x)]-1] = x
        
        return ''.join(map(str, code))
    
    def check_hamming(self, cadena):
        
        if len(cadena) != self.n:
            raise ValueError("Invalid code length")
        
        # Convert code to list of bits
        code_bits = list(map(int, list(cadena)))
        
        # Check parity bits
        error_bit = 0
        for i in range(1, self.n+1):
            if i & (i-1) == 0:  # i is a power of 2
                if sum(code_bits[j] for j in range(i-1, self.n, i*2)) % 2 != 0:
                    error_bit += i
        
        # Correct error if any
        if error_bit != 0:
            code_bits[error_bit-1] ^= 1
        
        # Extract data bits
        data_bits = [code_bits[i-1] for i in range(1, self.n+1) if i & (i-1) != 0]
        
        return ''.join(map(str, data_bits))
        
        

