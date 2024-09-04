# 5)
# Você está em uma sala com três interruptores, cada um conectado a uma lâmpada
# em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas
# pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é
# descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir,
# usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla
# cada lâmpada?

import time
import random

def simulate_lights():
    lights = {
        'Lampada1': {'estado': 'apagada', 'temperatura': 'fria'},
        'Lampada2': {'estado': 'apagada', 'temperatura': 'fria'},
        'Lampada3': {'estado': 'apagada', 'temperatura': 'fria'},
    }
    return lights

def ligar_interruptor(lights, interruptor):
    for lampada in lights:
        if interruptor == 'A':
            lights[lampada]['estado'] = 'acesa'
            lights[lampada]['temperatura'] = 'quente'
        elif interruptor == 'B':
            lights[lampada]['estado'] = 'acesa'
            lights[lampada]['temperatura'] = 'quente'
        elif interruptor == 'C':
            pass

def main():
    lights = simulate_lights()

    print("Ligando Interruptor A...")
    ligar_interruptor(lights, 'A')
    time.sleep(10)

    print("Desligando Interruptor A e ligando Interruptor B...")
    lights = simulate_lights()
    ligar_interruptor(lights, 'B')

    print("Verificando as lâmpadas:")
    for lampada, estado in lights.items():
        print(f"{lampada}: Estado = {estado['estado']}, Temperatura = {estado['temperatura']}")

if __name__ == "__main__":
    main()