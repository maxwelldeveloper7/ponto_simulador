#!/usr/bin/env python3
import json
from datetime import datetime


class PontoModel:
    def __init__(self):
        self.registros = []


    def registrar_entrada(self, nome):
        # Recebe a data e hora atual para adicionar ao registro
        data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        # Tenta abrir o arquivo JSON existente ou cria um novo se não existir
        try:
            with open('registro_ponto.json', 'r') as arquivo:
                self.registros = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            self.registros = []
            
        # Adiciona o novo registro
        self.registros.append({'nome': nome, 'entrada': data_hora, 'saida': None})
        
        # Salva os registros de volta no arquivo JSON
        with open('registro_ponto.json', 'w') as arquivo:
            json.dump(self.registros, arquivo, indent=2)
        print(f'Entrada registrada para {nome} às {data_hora}')


    def registrar_saida(self, nome):
        data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        try:
            with open('registro_ponto.json', 'r') as arquivo:
                self.registros = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nenhum registro de entrada encontrado para o nome fornecido.")

        encontrado = False        
        for registro in self.registros:
            if registro['nome'] == nome and registro['entrada'] and not registro['saida']:
                registro['saida'] = data_hora
                encontrado = True

        if encontrado:
            with open('registro_ponto.json', 'w') as arquivo:
                json.dump(self.registros, arquivo, indent=2)
            print(f'Saída registrada para {nome} às {data_hora}')
        else:
            print("Registro de entrada não encontrado para o nome fornecido ou saída já registrada.")


    def calcular_horas_trabalhadas(self, registro):
        if registro['entrada'] and registro['saida']:
            entrada = datetime.strptime(registro['entrada'], "%d-%m-%Y %H:%M:%S")
            saida = datetime.strptime(registro['saida'], "%d-%m-%Y %H:%M:%S")
            diferenca = saida - entrada
            return str(diferenca)
        return "Horas não calculadas"


    def carregar_registros_salvos(self):
        registros = []
        try:
            with open('registro_ponto.json', 'r') as arquivo:
                registros = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nenhum registro encontrado.")
        return registros
