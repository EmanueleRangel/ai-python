import time
import random
import math

pessoas = [('Amanda', 'CWB'), 
           ('Bruno', 'GIG'), 
           ('Carlos', 'POA'), 
           ('Diana', 'FLN'), 
           ('Elaine','CNF'),
           ('Hugo', 'GYN')]

destino = 'GRU'

voos = {}
for linha in open('voos.txt'):
    _origem, _destino, _saida, _chegada, _preco = linha.strip().split(',')
    voos.setdefault((_origem, _destino), [])
    voos[(_origem, _destino)].append((_saida, _chegada, int(_preco)))

