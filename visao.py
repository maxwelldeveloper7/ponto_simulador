import os

class PontoView:
    def __init__(self) -> None:
        self.AMARELO = "\033[93m"
        self.RESET = "\033[0m"
        self.AZUL = "\033[36m"
        self.VERMELHO = "\033[35m"
        self.VERDE = "\033[32m"
    
    def apagar_resultado(self):
        input(self.AMARELO+"Pressione 'Enter' para contitnuar..."+self.RESET)
        os.system('clear')

    def limpar_tela(self):
        os.system('clear')
    
    def mostrar_menu(self):
        print("\nPonto Eletrônico:")
        print("1. Registrar Entrada"+self.AZUL+" <<"+self.RESET)
        print("2. Registrar Saída"+self.VERMELHO+" >>"+self.RESET)
        print("3. Exibir Registros"+self.VERDE+" 📊"+self.RESET)
        print("4. Sair "+self.AMARELO+" 🚪"+self.RESET)

    def exibir_registros(self, registros):
        for registro in registros:
            saida = registro['saida']
            if saida == None:
                saida = "Não registrada"
            print(f"Nome: {self.VERDE}{registro['nome']}{self.RESET}, Entrada: {self.AZUL}{registro['entrada']}{self.RESET}, Saída: {self.VERMELHO}{saida}{self.RESET}, Horas Trabalhadas: {self.AMARELO}{registro['horas_trabalhadas']}{self.RESET}")
