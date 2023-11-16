import modelo
import visao

class PontoController:
    def __init__(self):
        self.modelo = modelo.PontoModel()
        self.visao = visao.PontoView()

    def run(self):
        while True:
            self.visao.limpar_tela()
            self.visao.mostrar_menu()
            opcao = input("Escolha uma opção: ")
            print() # Print utulizado para saltar uma linha 

            if opcao == '1':
                nome = input("Digite o seu nome: ")
                self.modelo.registrar_entrada(nome)
                self.visao.apagar_resultado()
            elif opcao == '2':
                nome = input("Digite o seu nome: ")
                self.modelo.registrar_saida(nome)
                self.visao.apagar_resultado()
            elif opcao == '3':
                self.modelo.registros = self.modelo.carregar_registros_salvos()
                registros = self.modelo.registros                
                for registro in registros:
                    registro['horas_trabalhadas'] = self.modelo.calcular_horas_trabalhadas(registro)
                self.visao.exibir_registros(registros)
                self.visao.apagar_resultado()
            elif opcao == '4':
                self.visao.limpar_tela()
                break
            else:
                print("Opção inválida. Tente novamente.")
                self.visao.apagar_resultado()

if __name__ == "__main__":
    controller = PontoController()
    controller.run()
