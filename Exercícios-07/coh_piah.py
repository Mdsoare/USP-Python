'''
Data: 05/05/2023
Autor: Marcelo Soares
Descrição: Escreva um programa que simule um detector de cópia. Para isso, complete as funções abaixo:
def compara_assinatura(as_a, as_b):
    pass

def calcula_assinatura(texto):
    pass

def avalia_textos(textos, ass_cp):
    pass
'''
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa função recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(len(as_a)):
        soma += abs(as_a[i] - as_b[i])
    return soma / 6

def calcula_assinatura(texto):
    '''Essa função recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    for sentenca in sentencas:
        frases += separa_frases(sentenca)
    for frase in frases:
        palavras += separa_palavras(frase)

    tam_palavras = sum(len(p) for p in palavras)
    n_palavras = len(palavras)
    type_token = n_palavras_diferentes(palavras) / n_palavras
    hapax_legomana = n_palavras_unicas(palavras) / n_palavras
    tam_sentencas = sum(len(s) for s in sentencas) / len(sentencas)
    comp_sentencas = len(frases) / len(sentencas)
    tam_frases = sum(len(f) for f in frases) / len(frases)

    return [tam_palavras/n_palavras, type_token, hapax_legomana, tam_sentencas, comp_sentencas, tam_frases]


def avalia_textos(textos, ass_cp):
    '''Essa função recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))
    similaridades = []
    for assinatura in assinaturas:
        similaridades.append(compara_assinatura(assinatura, ass_cp))
    return similaridades.index(min(similaridades)) + 1