from pyModbusTCP.client import ModbusClient
from time import sleep
from random import randint

# Connessione al server

client = ModbusClient(host="192.168.1.25", port=12345)
client.open()

lubrificante = 100

while True:

    # Parametri sega a nastro
    tensione = randint(1395, 1505) # 1400-1500
    allineamento = randint(23, 52) # 0.025-0.05 (valori moltiplicati per 1000)
    avanzamento = randint(49, 61) # 50-60
    rotazione = randint(295, 405) # 300-400
    lubrificante = lubrificante - randint(1, 3)


    potenza = randint(740, 960) # 750-950


    client.write_multiple_registers(1, [tensione, allineamento, avanzamento, rotazione, lubrificante, potenza])

    if (lubrificante < 30):
        lubrificante = 100

    sleep(5)
