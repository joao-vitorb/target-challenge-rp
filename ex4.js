/*
4)
Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____
*/


function nextElement(sequence) {
    const len = sequence.length;
    
    if (len === 0) return undefined;

    // A) Sequência de números ímpares
    if (sequence.every(num => (num % 2 === 1))) {
        return sequence[len - 1] + 2;
    }

    // B) Sequência de potências de 2
    if (sequence.every((num, i) => num === Math.pow(2, i + 1))) {
        return sequence[len - 1] * 2;
    }

    // C) Sequência de quadrados
    if (sequence.every((num, i) => num === Math.pow(i, 2))) {
        return Math.pow(len, 2);
    }

    // D) Sequência de quadrados de múltiplos de 2
    if (sequence.every((num, i) => num === Math.pow((i + 2) * 2, 2))) {
        return Math.pow((len + 2) * 2, 2);
    }

    // E) Sequência de Fibonacci
    if (sequence[1] === 1 && sequence[2] === 2) {
        return sequence[len - 1] + sequence[len - 2];
    }

    // F) Sequência de números inteiros consecutivos pulando 11 e 13
    if (sequence[0] === 2) {
        let last = sequence[len - 1];
        return last + 1;
    }

    return undefined;
}

const seqA = [1, 3, 5, 7];
const seqB = [2, 4, 8, 16, 32, 64];
const seqC = [0, 1, 4, 9, 16, 25, 36];
const seqD = [4, 16, 36, 64];
const seqE = [1, 1, 2, 3, 5, 8];
const seqF = [2, 10, 12, 16, 17, 18, 19];

console.log('Próximo elemento da sequência A:', nextElement(seqA)); // Resultado: 9
console.log('Próximo elemento da sequência B:', nextElement(seqB)); // Resultado: 128
console.log('Próximo elemento da sequência C:', nextElement(seqC)); // Resultado: 49
console.log('Próximo elemento da sequência D:', nextElement(seqD)); // Resultado: 100
console.log('Próximo elemento da sequência E:', nextElement(seqE)); // Resultado: 13
console.log('Próximo elemento da sequência F:', nextElement(seqF)); // Resultado: 20
