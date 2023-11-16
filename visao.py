import os

class PontoView:
    def apagar_resultado(self):
        input("Pressione 'Enter' para contitnuar...")
        os.system('clear')

    def limpar_tela(self):
        os.system('clear')
    
    def mostrar_menu(self):
        print("\nMenu Principal:")
        print("1. Registrar Entrada")
        print("2. Registrar Saída")
        print("3. Exibir Registros")
        print("4. Sair")

    def exibir_registros(self, registros):
        for registro in registros:
            saida = registro['saida']
            if saida == None:
                saida = "Não registrada"
            print(f"Nome: {registro['nome']}, Entrada: {registro['entrada']}, Saída: {saida}, Horas Trabalhadas: {registro['horas_trabalhadas']}")
