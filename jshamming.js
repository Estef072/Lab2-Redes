class Hamming {
    constructor(n, m) {
        if (n + m + 1 > Math.pow(2, n)) {
            throw new Error(`Invalid parameters: ${n} + ${m} + 1 > 2**${n}`);
        }
        
        this.n = n;
        this.m = m;
        
        this.ps = [...Array(this.n).keys()].map(x => x + 1).filter(x => (x & (x - 1)) == 0);
    }
    
    get_parity_bits(cadena) {
        return this.ps.map(i => cadena[i-1]);
    }
    
    encode(cadena) {
        if (cadena.length != this.m) {
            throw new Error("Invalid data length");
        }
    
        const data_bits = Array.from(cadena, Number);
        let code = data_bits;
        let lista = Array(this.ps.length).fill(0);
    
        console.log(`Data bits: ${data_bits}`);
        console.log(`Parity bits: ${this.ps}`);
        console.log(`Code bits: ${code}`)
        console.log(`Lista: ${lista}`)

        for (let x of this.ps) {
            code.splice(x-1, 0, 0);
        }

        for (let i = 1; i < this.n+1; i++) {
            for (let x of this.ps) {
                if ((i & x) === x) {
                    lista[this.ps.indexOf(x)] = (lista[this.ps.indexOf(x)] + code[i-1]) % 2;
                }
            }
        }

        for (let x of lista) {
            code[this.ps[lista.indexOf(x)]-1] = x;
        }
    
        return code.join('');
    }
    
    check_hamming(cadena) {
        if (cadena.length != this.n) {
            throw new Error("Invalid code length");
        }
        
        let code_bits = Array.from(cadena, Number);
        let code = [...code_bits];
        
        for (let x of this.ps.slice().reverse()) {
            code.splice(x-1, 1);
        }

        let original = this.encode(code.join(''));
        let original_parity = this.get_parity_bits(original);
        let cadena_parity = this.get_parity_bits(cadena);
        
        original_parity = parseInt(original_parity.reverse().join(''),2);
        cadena_parity = parseInt(cadena_parity.reverse().join(''),2);
        
        let index = original_parity^cadena_parity;
        
        if (index) {
            code_bits[index-1] = Number(!code_bits[index-1]);
        }
                    
        return [code_bits.join(''), index];
    }
}

// Creating an instance of the Hamming class
let hamming = new Hamming(7, 4);

// Encode a string
let cadena = '1011';
let encoded = hamming.encode(cadena);
console.log(`Encoded: ${encoded}`);

// Check the Hamming code
let checked = hamming.check_hamming('0110011');
console.log(`Checked: ${checked[0]}, index: ${checked[1]}`);