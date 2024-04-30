
#CALCULADORA -> Módulo padrão ; sem bibliotecas auxiliares.
def main():
    def add (x,y):
        return x+y
    def sub (x,y):
        return x-y
    def mult (x,y):
        return x*y
    def div (x,y):
        return x/y
    def expo (x,y):
        return x**y
    calc = True
    while calc:
        print(
            "\n1 - Adição\n"
            "2 - Subtração\n"
            "3 - Multiplicação\n"
            "4 - Exponenciação\n"
            "5 - Divisão\n"
        )
        entrada = input("Escolha uma opção:")
        if entrada.lower() == "sair":
            break
        elif entrada == "1":
        
            val1 = int(input("Primeiro valor: "))
            val2 = int(input("Segundo valor: "))
            print(f"Resultado: {add(val1,val2)}")
            while True:
                print(
                    "\n Deseja usar a calculadora novamente?"
                )
                res = input("> ")
                if res.lower() in ["ss", "s", "si","yes","sim"]:
                    break
                elif res.lower() in ["nn","no","n","nope","não","nao"]:
                    calc = False
                    break
                else:
                    print("Desculpe, não entendi!\n Repita por favor.")
        elif entrada == "2":
        
            val1 = int(input("Primeiro valor: "))
            val2 = int(input("Segundo valor: "))
            print(f"Resultado: {sub(val1,val2)}")
            while True:
                print(
                    "\n Deseja usar a calculadora novamente?"
                )
                res = input("> ")
                if res.lower() in ["ss", "s", "si","yes","sim"]:
                    break
                elif res.lower() in ["nn","no","n","nope","não","nao"]:
                    calc = False
                    break
                else:
                    print("Desculpe, não entendi!\n Repita por favor.")
        elif entrada == "3":
        
            val1 = int(input("Primeiro valor: "))
            val2 = int(input("Segundo valor: "))
            print(f"Resultado: {mult(val1,val2)}")
            while True:
                print(
                    "\n Deseja usar a calculadora novamente?"
                )
                res = input("> ")
                if res.lower() in ["ss", "s", "si","yes","sim"]:
                    break
                elif res.lower() in ["nn","no","n","nope","não","nao"]:
                    calc = False
                    break
                else:
                    print("Desculpe, não entendi!\n Repita por favor.")
        elif entrada == "4":
        
            val1 = int(input("Numero: "))
            val2 = int(input("elevado à: "))
            print(f"Resultado: {expo(val1,val2)}")
            while True:
                print(
                    "\n Deseja usar a calculadora novamente?"
                )
                res = input("> ")
                if res.lower() in ["ss", "s", "si","yes","sim"]:
                    break
                elif res.lower() in ["nn","no","n","nope","não","nao"]:
                    calc = False
                    break
                else:
                    print("Desculpe, não entendi!\n Repita por favor.")
        elif entrada == "5":
        
            val1 = int(input("Numero: "))
            val2 = int(input("dividido por: "))
            print(f"Resultado: {div(val1,val2)}")
            while True:
                print(
                    "\n Deseja usar a calculadora novamente?"
                )
                res = input("> ")
                if res.lower() in ["ss", "s", "si","yes","sim"]:
                    break
                elif res.lower() in ["nn","no","n","nope","não","nao"]:
                    calc = False
                    break
                else:
                    print("Desculpe, não entendi!\n Repita por favor.")
        else:
            print("Desculpe, não entendi. \n Repita por favor!")

if __name__=='__main__':
    main()
                
        






