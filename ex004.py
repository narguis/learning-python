# Check the primitive type of a string and get some info about it

algo = input("Digite algo: ")
limpa = "\033[m"
print(f"O tipo primitivo desse valor é \033[35m{type(algo)}{limpa}\n"
      f"É só espaços? \033[31m{algo.isspace()}{limpa}\n"
      f"É numérico? \033[1;30;107m{algo.isnumeric()}{limpa}\n"
      f"É alfabético? \033[1;97;40m{algo.isalpha()}{limpa}\n"
      f"É alfanumérico? \033[4;34m{algo.isalnum()}{limpa}\n"
      f"É maiúsculo? \033[4;33m{algo.isupper()}{limpa}\n"
      f"É minúsculo? \033[7;32;107m{algo.islower()}{limpa}\n"
      f"Está capitalizado? \033[1;36;45m{algo.istitle()}{limpa}")
