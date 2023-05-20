#! /bin/python3

import os
import time
import requests
import json

print()
print('OLA LAMER, USE ESSE PROGRAMA PARA HACKEAR CEPS E LOCALIZACOES PESSOAIS PARA O BEM, EU SOU O HACKER WHITE HAT, EU SOU UM CARA QUE E HEROI POR DIVERSAO. ')
print()
print('USE ESSE PROGRAMA E COPIE E COLE NA MAQUINA OU NUM ANDROID OU PC PARA KALI LINUX, E TERMUX.')
print()
print(' EU SOU UM HACKER ')      
print()      
    
Hacker_cep = input('Digite o CEP Para HACKEAR: ')
if len(Hacker_cep) != 8:
    print('ERROR')
    exit()
      
requests = requests.get('https://viacep.com.br/ws/01001000/json/')
      
address_data = request.json()
      
if 'erro' not in address_data:
        print('===> CEP HACKEADO <===')
        
        print('CEP: {}'.format(address_data['cep']))
        print('LOGRADOURO: {}'.format(address_data['logradouro']))
        print('COMPLEMENTO: {}'.format(address_data['complemento']))
        print('ESTADO: {}'.format(address_data['estado']))
        print('CIDADE: {}'.format(address_data['cidade']))                                     
        print('GIA: {}'.format(address_data['gia']))
        print('SIAFI: {}'.format(address_data['siafi']))
        print('IBGE: {}'.format(address_data['ibge']))
        print('DDD: {}'.format(address_data['ddd']))
else:
        print(' ATE MAIS ENTAO ')

    
    
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
