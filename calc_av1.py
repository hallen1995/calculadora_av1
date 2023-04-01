class Calculadora:
    def __init__(self): 
        self.n1 = 0
        self.n2 = 0 
        self.resultado = 0

    def somar(self, n1, n2):  #definção da calc. de adição
        self.n1 = n1
        self.n2 = n2
        self.resultado = self.n1 + self.n2
        return self.resultado
        
    def subtrair(self, n1, n2):  #definção da calc. de subtração
        self.n1 = n1
        self.n2 = n2
        self.resultado = self.n1 - self.n2
        return self.resultado
    
    def multiplicar(self, n1, n2):  #definção da calc. de multiplicação
        self.n1 = n1
        self.n2 = n2
        self.resultado = self.n1 * self.n2
        return self.resultado
    
    def dividir(self, n1, n2):  #definção da calc. de divisão
        self.n1 = n1
        self.n2 = n2
        self.resultado = self.n1 / self.n2
        return self.resultado
    
    def expoente(self, n1, n2):  #definção da calc. de exponenciação
        self.n1 = n1
        self.n2 = n2
        self.resultado = self.n1 ** self.n2
        return self.resultado
    
    def resto(self, n1, n2):  #definção da calc. de módulo(resto)
        self.n1 = n1
        self.n2 = n2
        self.resultado = self.n1 % self.n2
        return self.resultado

def continuar(entrada):
    if entrada:
        return True
    else:
        return False

def menu():
    opc = {1: 'Adição',
           2: 'Subtração',
           3: 'Multiplicação',
           4: 'Divisão',
           5: 'Exponenciação',
           6: 'Módulo (resto)'}
    
    calc = Calculadora()
    print(""" Qual é a operação matemática deseja fazer?
    1 -> Adição
    2 -> Subtração
    3 -> Multiplicação
    4 -> Divisão
    5 -> Exponenciação
    6 -> Módulo (resto)
    Digite o número desejado e aperte ENTER:""")
    
    calcular = True
    while calcular:
        opcao = input("\nEscolha a opção de cálculo desejada (1, 2, 3, 4, 5 ou 6)")
        if not(opcao in '1 2 3 4 5 6'):
            print("Opção escolhida é inválida!!!")
            continue
        else:
            opcao = int(opcao)
            print(f"A operação matemática escolhida é {opc[opcao]}")
            print("Apenas números inteiros serão aceitou nas operações!!!")
              
        if opcao == 1:
            n1 = int(input("Digite o penúltimo número de seu RU:"))
            n2 = int(input("Digite o último número de seu RU:"))
            resultado = calc.somar(n1,n2)
            print(f"O valor da operação adição é {resultado}")
            calcular = continuar(input("Digite algum valor para continuar ou aperte ENTER para sair da Calculadora."))
            if opcao != ("1","2","3","4","5","6"):
                print("Você apertou ENTER, calculadora encerrada!")
                
        elif opcao == 2:
            n1 = int(input("Digite o penúltimo número de seu RU:"))
            n2 = int(input("Digite o último número de seu RU:"))
            resultado = calc.subtrair(n1,n2)
            print(f"O valor da operação subtração é {resultado}")
            calcular = continuar(input("Digite algum valor para continuar ou aperte ENTER para sair da Calculadora."))
            if opcao != ("1","2","3","4","5","6"):
                print("Você apertou ENTER, calculadora encerrada!")
          
        elif opcao == 3:
            n1 = int(input("Digite o penúltimo número de seu RU:"))
            n2 = int(input("Digite o último número de seu RU:"))
            resultado = calc.multiplicar(n1,n2)
            print(f"O valor da operação multiplicação é {resultado}")
            calcular = continuar(input("Digite algum valor para continuar ou aperte ENTER para sair da Calculadora."))
            if opcao != ("1","2","3","4","5","6"):
                print("Você apertou ENTER, calculadora encerrada!")
                
        elif opcao == 4:
            n1 = int(input("Digite o penúltimo número de seu RU:"))
            n2 = int(input("Digite o último número de seu RU:"))
            resultado = calc.dividir(n1,n2)
            print(f"O valor da operação divisão é {resultado}")
            calcular = continuar(input("Digite algum valor para continuar ou aperte ENTER para sair da Calculadora."))
            if opcao != ("1","2","3","4","5","6"):
                print("Você apertou ENTER, calculadora encerrada!")
                
        elif opcao == 5:
            n1 = int(input("Digite o penúltimo número de seu RU:"))
            n2 = int(input("Digite o último número de seu RU:"))
            resultado = calc.expoente(n1,n2)
            print(f"O valor da operação exponenciação é {resultado}")
            calcular = continuar(input("Digite algum valor para continuar ou aperte ENTER para sair da Calculadora."))
            if opcao != ("1","2","3","4","5","6"):
                print("Você apertou ENTER, calculadora encerrada!")
                
        elif opcao == 6:
            n1 = int(input("Digite o penúltimo número de seu RU:"))
            n2 = int(input("Digite o último número de seu RU:"))
            resultado = calc.resto(n1,n2)
            print(f"O valor da operação módulo (resto) é {resultado}")
            calcular = continuar(input("Digite algum valor para continuar ou aperte ENTER para sair da Calculadora."))
            if opcao != ("1","2","3","4","5","6"):
                print("Você apertou ENTER, calculadora encerrada!")
                

        
menu()