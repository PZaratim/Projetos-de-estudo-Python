from machine import Pin

led_par = Pin(2, Pin.OUT)    # ajuste o pino
led_impar = Pin(18, Pin.OUT)  # ajuste o pino

while True:
    entrada = input("Digite um número: ")

    numero = int(entrada)

    if numero % 2 == 0:
        led_par.value(1)     # liga LED par
        led_impar.value(0)   # desliga LED ímpar
        print("Par")
    else:
        led_par.value(0)
        led_impar.value(1)
        print("Ímpar")
