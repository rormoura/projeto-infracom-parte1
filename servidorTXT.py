from socket import * # importando todas as funções da biblioteca socket
portaServidor = 12000
socketServidor = socket(AF_INET, SOCK_DGRAM) # criando o socket do servidor
# AF_INET é uma constante definida em socket e representa as famílias de endereços e protocolos
# SOCK_DGRAM é outra constante definida em socket e representa o tipo de socket que utiliza o protocolo UDP
socketServidor.bind(("", portaServidor)) # aqui vinculamos ao socket do servidor a porta do servidor
print("O servidor está pronto.")
while (True): #servidor always on
    contrecebido, endCliente = socketServidor.recvfrom(34)  # recebe do socket algum conteúdo enviado por algum cliente
                                                            # o arquivo TesteTXT.txt tem tamanho de 34 bytes
    e1, e2 = endCliente # e1 é o endereço IP do cliente e e2 a porta pela qual ele se comunica com o servidor
    print("Endereço IP e porta do cliente:")
    print(e1,e2)
    print("Arquivo recebido do cliente: "+contrecebido.decode()) # printando o que recebemos em formato de string
    arquivo = open("recebido_servidor.txt", "wt") # criando o arquivo que guarda o conteúdo recebido
    arquivo.write(contrecebido.decode()) # guardando o conteúdo
    arquivo.close() # fechando o arquivo após guarda o conteúdo
    socketServidor.sendto(contrecebido, endCliente) # enviamos o que lemos para o endereço do cliente (IP:porta)