import time

def exibir_mensagem(texto, tempo):
  for i in range(tempo, 0 ,-1):
    print(f"{i}")
    time.sleep(1)
  print(texto)


# programa principal
msg = input("Digite a mensagem a ser exibida: ")
exibir_mensagem(msg, 5)
