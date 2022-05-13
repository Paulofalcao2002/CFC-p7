
#importe as bibliotecas
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

#funções a serem utilizadas
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)




def main():
    
   
    #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias corresposndentes à tecla pressionada, segundo a tabela DTMF
    # se voce quiser, pode usar a funcao de construção de senoides existente na biblioteca de apoio cedida. Para isso, você terá que entender como ela funciona e o que são os argumentos.
    # essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # o tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Seja razoável.
    # some as senoides. A soma será o sinal a ser emitido.
    # utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumento.
    # grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal
    
    print("Inicializando encoder")
    inpt = ''

    teclas = {
        '1': [697, 1206], '2': [697, 1339], '3': [697, 1477], 'A': [697, 1633],
        '4': [770, 1206], '5': [770, 1339], '6': [770, 1477], 'B': [770, 1633],
        '7': [852, 1206], '8': [852, 1339], '9': [852, 1477], 'C': [852, 1633],
        'X': [941, 1206], '0': [941, 1339], '#': [941, 1477], 'D': [941, 1633],
    }

    while inpt not in teclas:
        print("Aguardando usuário")
        inpt = input('Digite a tecla que deseja transmitir: ')
        if inpt not in teclas:
            print('Input invalido')
            print(inpt)

    print("Gerando Tons base")
    freq1, freq2 = teclas[inpt]
    fs = 44100

    signal_meu = signalMeu()
    tempo1, sin1 = signal_meu.generateSin(freq1, 1, 2, fs)
    tempo2, sin2 = signal_meu.generateSin(freq2, 1, 2, fs)

    sinT = sin1 + sin2

    # print(sin1)
    # print(sin2)
    # print(sinT)
   

    print("Executando as senoides (emitindo o som)")
    print("Gerando Tom referente ao símbolo : {}".format(inpt))
    
    sd.play(sinT, fs)
    # Exibe gráficos
    # aguarda fim do audio
    sd.wait()
    signal_meu.plotFFT(sinT, fs)
    signal_meu.plotFreqTempo(sinT, tempo1)
    plt.show()
    

if __name__ == "__main__":
    main()
