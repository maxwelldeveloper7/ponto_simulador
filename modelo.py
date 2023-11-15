import json
from datetime import datetime

class PontoModel:
    def __init__(self):
        self.registros = []

    def registrar_entrada(self, nome):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.registros.append({'nome': nome, 'entrada': data_hora, 'saida': None})
    def registrar_saida(self, nome):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for registro in self.registros:
            if registro['nome'] == nome and registro['entrada'] and not registro['saida']:
                registro['saida'] = data_hora

    def calcular_horas_trabalhadas(self, registro):
        if registro['entrada'] and registro['saida']:
            entrada = datetime.strptime(registro['entrada'], "%Y-%m-%d %H:%M:%S")
            saida = datetime.strptime(registro['saida'], "%Y-%m-%d %H:%M:%S")
            diferenca = saida - entrada
            return str(diferenca)
        return "Horas não calculadas"
