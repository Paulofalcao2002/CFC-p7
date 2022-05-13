#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""

#Importe todas as bibliotecas
import sounddevice as sd
import numpy as np
from suaBibSignal import signalMeu
import time 
import matplotlib.pyplot as plt
import peakutils

#funcao para transformas intensidade acustica em dB
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)


def main():
 
    #declare um objeto da classe da sua biblioteca de apoio (cedida)  
    signal_meu = signalMeu()
    #declare uma variavel com a frequencia de amostragem, sendo 44100
    fs = 44100
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    
    sd.default.samplerate = fs #taxa de amostragem
    sd.default.channels = 2  #voce pode ter que alterar isso dependendo da sua placa
    duration_capt = 2 #tempo em segundos que ira aquisitar o sinal acustico captado pelo mic


    #faca um print na tela dizendo que a captacao comecará em n segundos. e entao 
    #use um time.sleep para a espera
    print("Começando a captação em 2 segundos...")
    time.sleep(2)
   
    #faca um print informando que a gravacao foi inicializada
    print("Gravação inicializada")
   
    #declare uma variavel "duracao" com a duracao em segundos da gravacao. poucos segundos ...
    duracao_gravacao = 5 
    #calcule o numero de amostras "numAmostras" que serao feitas (numero de aquisicoes)

    numAmostras = fs * duration_capt
   
    audio = sd.rec(int(numAmostras), fs, channels=1)
    sd.wait()
    print("...     FIM")
    
    # print(audio)
    # print(type(audio))
    # print(audio)
    #analise sua variavel "audio". pode ser um vetor com 1 ou 2 colunas, lista ...
    #grave uma variavel com apenas a parte que interessa (dados)
    dados = []
    for listinha in audio:
        dados.append(listinha[0])
    
    # print(dados)

    # use a funcao linspace e crie o vetor tempo. Um instante correspondente a cada amostra!
    t = np.linspace(0, duration_capt, numAmostras)

    # plot do gravico  áudio vs tempo!
    signal_meu.plotFreqTempo(dados, t)
    
    ## Calcula e exibe o Fourier do sinal audio. como saida tem-se a amplitude e as frequencias
    xf, yf = signal_meu.calcFFT(dados, fs)
    plt.figure("F(y)")
    plt.plot(xf,yf)
    plt.grid()
    plt.title('Fourier audio')
    plt.show()

    #esta funcao analisa o fourier e encontra os picos
    #voce deve aprender a usa-la. ha como ajustar a sensibilidade, ou seja, o que é um pico?
    #voce deve tambem evitar que dois picos proximos sejam identificados, pois pequenas variacoes na
    #frequencia do sinal podem gerar mais de um pico, e na verdade tempos apenas 1.
   
    index = peakutils.indexes(yf,thres=0.5,min_dist=20)
    print(yf[index])
    
    #printe os picos encontrados! 
    
    #encontre na tabela duas frequencias proximas às frequencias de pico encontradas e descubra qual foi a tecla
    #print a tecla.
    
  
    ## Exibe gráficos
    # plt.show()

if __name__ == "__main__":
    main()
