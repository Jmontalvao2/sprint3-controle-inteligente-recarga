from machine import Pin
from time import sleep
import gc


# ==========================================
# CONFIGURACAO DOS LEDs
# ==========================================

led_verde = Pin(2, Pin.OUT)
led_amarelo = Pin(3, Pin.OUT)
led_vermelho = Pin(4, Pin.OUT)


# ==========================================
# MEMORIA NO INICIO DO PROGRAMA
# ==========================================

gc.collect()

memoria_inicio = gc.mem_free()

print("================================")
print("CONTROLE INTELIGENTE DE RECARGA")
print("================================")
print()
print("MEMORIA LIVRE NO INICIO:", memoria_inicio, "bytes")
print()


# ==========================================
# FUNCAO PRINCIPAL
# ==========================================

def controlar_recarga(geracao, consumo):

    # Calcula a energia disponivel
    disponivel = geracao - consumo

    # Desliga todos os LEDs
    led_verde.off()
    led_amarelo.off()
    led_vermelho.off()

    # Determina o estado da recarga
    if disponivel >= 2000:
        status = "RECARGA AUTORIZADA"
        led_verde.on()

    elif disponivel > 0:
        status = "RECARGA REDUZIDA"
        led_amarelo.on()

    else:
        status = "RECARGA BLOQUEADA"
        led_vermelho.on()

    # ======================================
    # DADOS DA SESSAO
    # ======================================

    print("--------------------------------")
    print("GERACAO:", geracao, "W")
    print("CONSUMO:", consumo, "W")
    print("DISPONIVEL:", disponivel, "W")
    print("STATUS:", status)
    print("--------------------------------")
    print()


# ==========================================
# SITUACAO 1
# ==========================================

print("SITUACAO 1 - ENERGIA SUFICIENTE")

controlar_recarga(4000, 1500)

sleep(5)


# ==========================================
# SITUACAO 2
# ==========================================

print("SITUACAO 2 - ENERGIA LIMITADA")

controlar_recarga(1800, 1500)

sleep(5)


# ==========================================
# SITUACAO 3
# ==========================================

print("SITUACAO 3 - ENERGIA INSUFICIENTE")

controlar_recarga(1000, 1800)

sleep(5)


# ==========================================
# REPRESENTACAO DE DADOS
# ==========================================

# Escolhemos a potencia disponivel de 2500 W
# para demonstrar as tres bases numericas.

valor = 2500

print("================================")
print("REPRESENTACAO DE DADOS")
print("================================")

print("Potencia disponivel:", valor, "W")
print("Decimal:", valor)
print("Binario:", bin(valor))
print("Hexadecimal:", hex(valor))

print()


# ==========================================
# MEMORIA NO FINAL
# ==========================================

gc.collect()

memoria_final = gc.mem_free()

print("================================")
print("MEMORIA")
print("================================")

print("Memoria livre no inicio:", memoria_inicio, "bytes")
print("Memoria livre no final:", memoria_final, "bytes")

diferenca = memoria_inicio - memoria_final

print("Diferenca:", diferenca, "bytes")
print("================================")

# ==============================
# SIMULACAO DAS TRES SITUACOES
# ==============================

# Situacao 1 - Energia suficiente
controlar_recarga(4000, 1500)
sleep(5)

# Situacao 2 - Energia limitada
controlar_recarga(1800, 1500)
sleep(5)

# Situacao 3 - Energia insuficiente
controlar_recarga(1000, 1800)
sleep(5)
