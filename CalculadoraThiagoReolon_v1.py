# Calculadora em Python

print("\n******************* Calculadora em Python *******************")

print("\nDesenvolvido por Thiago Reolon"
      "\n46 99110 0201"
      "\n"
      "\nSelecione o número da operação desejada:"
      "\n1 - Soma"
      "\n2 - Subtração"
      "\n3 - Multiplicação"
      "\n4 - Divisão\n\n")
opcao = input("Digite sua opção (1,2,3,4): ")
num1 = input("\nDigite o primeiro número: ")
num2 = input("Digite o segundo número: ")
"\n\n"

if opcao == "1":
      if int(num1)+int(num2) == 4:
            print("\nA soma de ("+num1+"+"+num2+") é = " + str(int(num1)+int(num2)))
            print("\nDesenvolvido por Thiago Reolon"
                  "\nguitahudson@gmail.com")
      else:
            print("\nA soma de (" + num1 + "+" + num2 + ") é = " + str(int(num1) + int(num2)))
elif opcao == "2":
      print("\nA subtração de ("+num1+"-"+num2+") é = " + str(int(num1)-int(num2)))
elif opcao == "3":
      print("\nA multiplicação de ("+num1+"*"+num2+") é = " + str(int(num1)*int(num2)))
elif opcao == "4":
      print("\nA divisão de ("+num1+"/"+num2+") é = " + str(int(num1)/int(num2)))
else:
      print("Opção seleciona inválida")

