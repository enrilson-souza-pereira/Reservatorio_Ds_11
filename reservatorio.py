import random
import colorama
from colorama import Fore, Style

# Inicializa o colorama (necessário em alguns terminais Windows)
colorama.init()

situacao = random.randint(1, 5)

niveis = {
    1: (Fore.RED, "Nível 1\t\t\t| Muito baixo\t|"),
    2: (Fore.YELLOW, "Nível 2\t\t\t| Baixo\t\t\t|"),
    3: (Fore.GREEN, "Nível 3\t\t\t| Médio\t\t\t|"),
    4: (Fore.CYAN, "Nível 4\t\t\t| Alto\t\t\t|"),
    5: (Fore.BLUE, "Nível 5\t\t\t| Muito alto\t|")
}

def situacao_reservatorio(situacao):
    cor, texto = niveis[situacao]
    print(cor + texto + Style.RESET_ALL)

print("Nível do reservatório\t| Situação\t\t|")
situacao_reservatorio(situacao)