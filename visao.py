class PontoView:
    def mostrar_menu(self):
        print("\nMenu Principal:")
        print("1. Registrar Entrada")
        print("2. Registrar Saída")
        print("3. Exibir Registros")
        print("4. Sair")

    def exibir_registros(self, registros):
        for registro in registros:
            print(f"Nome: {registro['nome']}, Entrada: {registro['entrada']}, Saída: {registro['saida']}, Horas Trabalhadas: {registro['horas_trabalhadas']}")
