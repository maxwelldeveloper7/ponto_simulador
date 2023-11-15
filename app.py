import modelo
import visao

class PontoController:
    def __init__(self):
        self.modelo = modelo.PontoModel()
        self.visao = visao.PontoView()

    def run(self):
        while True:
            self.visao.mostrar_menu()
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Digite o seu nome: ")
                self.modelo.registrar_entrada(nome)
            elif opcao == '2':
                nome = input("Digite o seu nome: ")
                self.modelo.registrar_saida(nome)
            elif opcao == '3':
                registros = self.modelo.registros
                for registro in registros:
                    registro['horas_trabalhadas'] = self.modelo.calcular_horas_trabalhadas(registro)
                self.visao.exibir_registros(registros)
            elif opcao == '4':
                print("Encerrando o aplicativo.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    controller = PontoController()
    controller.run()
