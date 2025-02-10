from colorama import Fore, init, Back
from random import randint
import os

init()

BASE_PATH = "algorithms"

algos = os.listdir(BASE_PATH)

FILES = {}
for i in range(len(algos)):
    FILES[i + 1] = [algos[i], os.path.splitext(algos[i])[0]]


def generate_algorithm_filler(algoTextFile: str, blanks=3):
    """
    :param: `algoTextFile` is the path to the .txt file containing the pseudoCode/python-like 
            code for the specific algorithm
    :param: `blanks` is the number of blank lines to show (*default = 3*)
    """
    answers = {}
    selectedLines = []
    length = 0
    with open(os.path.join(BASE_PATH, algoTextFile), "r") as f:
        l = f.readlines()
        length = len(l)

        lines = {i: l[i] for i in range(len(l))}

        # Generate Unique Random Line numbers to show as blanks
        while blanks:
            r = randint(1, len(lines) - 1)
            if r not in selectedLines:
                selectedLines.append(r)
                selectedLines.sort()
                answers[r] = lines[r]
                del lines[r]
                blanks -= 1

        keys = list(answers.keys())
        keys.sort()
        returnAnswers = {i:answers[i] for i in keys}
        return lines, returnAnswers, length

def display_blanks():
    print(Fore.RED + "<" + "_" * 30 + ">")
    

def equal_ignore_whitespace(s1, s2):
    return "".join(s1.split()) == "".join(s2.split())

def play():
    print(Fore.CYAN + """
    :::'###::::'##::::::::'######::::'#######::'########::'####:'########:'##::::'##:'##::::'##::'######:::'##::::'##:'########::'######:::'######::'########:'########::
    ::'## ##::: ##:::::::'##... ##::'##.... ##: ##.... ##:. ##::... ##..:: ##:::: ##: ###::'###:'##... ##:: ##:::: ##: ##.....::'##... ##:'##... ##: ##.....:: ##.... ##:
    :'##:. ##:: ##::::::: ##:::..::: ##:::: ##: ##:::: ##:: ##::::: ##:::: ##:::: ##: ####'####: ##:::..::: ##:::: ##: ##::::::: ##:::..:: ##:::..:: ##::::::: ##:::: ##:
    '##:::. ##: ##::::::: ##::'####: ##:::: ##: ########::: ##::::: ##:::: #########: ## ### ##: ##::'####: ##:::: ##: ######:::. ######::. ######:: ######::: ########::
     #########: ##::::::: ##::: ##:: ##:::: ##: ##.. ##:::: ##::::: ##:::: ##.... ##: ##. #: ##: ##::: ##:: ##:::: ##: ##...:::::..... ##::..... ##: ##...:::: ##.. ##:::
     ##.... ##: ##::::::: ##::: ##:: ##:::: ##: ##::. ##::: ##::::: ##:::: ##:::: ##: ##:.:: ##: ##::: ##:: ##:::: ##: ##:::::::'##::: ##:'##::: ##: ##::::::: ##::. ##::
     ##:::: ##: ########:. ######:::. #######:: ##:::. ##:'####:::: ##:::: ##:::: ##: ##:::: ##:. ######:::. #######:: ########:. ######::. ######:: ########: ##:::. ##:
    ..:::::..::........:::......:::::.......:::..:::::..::....:::::..:::::..:::::..::..:::::..:::......:::::.......:::........:::......::::......:::........::..:::::..::
    """)

    choice = 0
    while not choice:
        print(Fore.BLUE + "Choose an algorithm")
        for f in list(FILES.keys()):
            print(f"[{f}]\t{FILES[f][1]}")

        choice = int(input(Fore.WHITE + "Choose: "))
        try:
            global blanks
            blanks = int(input("Enter the number of Blank Lines: "))
            lines, answers, length = generate_algorithm_filler(FILES[choice][0], blanks = blanks)
        except:
            print(Fore.RED + "Please choose a valid value")
            choice = 0


    while True:
        for i in range(length):
            if i in list(answers.keys()):
                print(Fore.RED + f"{i}\t", end="")
                display_blanks()
            else:
                print(Fore.GREEN + f"{i}\t", end="")
                print(Fore.GREEN + lines[i], end='')
        for a in list(answers.keys()):
            ans = answers[a]
            inp = input(Fore.WHITE + f"Enter answer for line {a}: ")
            if equal_ignore_whitespace(inp, ans):
                print(Fore.GREEN + "Thats Correct!")
                lines[a] = ans
                del answers[a]
            else:
                print(Fore.RED + "That's incorrect :(")
            break
        if not bool(answers):
            print(Fore.WHITE + Back.BLACK + "Noice, Genius!")
            for i in range(length):
                print(Fore.GREEN + f"{i}\t", end="")
                print(Fore.GREEN + lines[i], end='')
            ch = input(Fore.WHITE + "Do you wanna go again?? (0/1)")
            if ch == "0":
                break
            else:
                os.system('clear')
                lines, answers, length = generate_algorithm_filler(FILES[choice][0], blanks = blanks)


    print(Fore.BLACK + Back.WHITE + "Good Job, to-be Bjarne")

play()
