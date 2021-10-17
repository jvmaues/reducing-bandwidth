import os
from os import listdir
from os.path import isfile, join


def readFilesInDict(path, extension):
    onlymtxComp = [os.path.join(path, file) for file in os.listdir(path) if file.endswith(extension)]
    return onlymtxComp

# def encontraArquivosEmPastaRecursivamente(pasta='.', extensao):
#     arquivos = []
#     caminhoAbsoluto = os.path.abspath(pasta)
#     for pastaAtual, subPastas, arquivos  in os.walk(caminhoAbsoluto):
#         arquivos.extend([os.path.join(pastaAtual,arquivo) for arquivo in arquivos if arquivo.endswith(extensao)])
#     return arquivos
