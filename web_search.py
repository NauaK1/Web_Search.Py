import sys
import webcrawlerr

def deseja_salvar(retorno,nome):
    while True:
                print("Deseja salvar em um arquivo?")
                esco = input("y/n: ")
                if esco != 'y' and esco != 'n':
                    print("Escolha invalida. Tente novamente.")
                    continue
                elif esco == 'y':
                    webcrawlerr.salvar(retorno,nome)
                    break
                elif esco == 'n':
                    break


if __name__ == "__main__":
    CIANO = "\033[1;36m"
    AMARELO = "\033[1;33m"
    VERDE = "\033[1;32m"
    RESET = "\033[0m"

    if len(sys.argv) > 1:
        print(f"""{CIANO}
 _ _ _ _____ ___     _____ _____ _____ _____ _____ _____     _____ __ __ 

| | | |   __| __|   |   __|   __|  _  | __  |     |  |  |   |  _  |  |  |
| | | |   __|__ |   |__   |   __|     |    _|-   -|  |  |   |   __|_   _|
|_____|_____|___|   |_____|_____|__|__|__|__|_____|_____|   |__|    |_|  
{RESET}""")

        print(f"{AMARELO}" + "┌──────────────────────────────────┐".center(77))
        print(f"│          web.search.py           │".center(77).replace("web.search.py", f"{VERDE}web.search.py{AMARELO}"))
        print(f"│               v1.0               │".center(77))
        print(f"                     │   Developed by Kauan dos Santos  │{RESET}")
        print(f"{AMARELO}" + "└──────────────────────────────────┘".center(77) + f"{RESET}")
        
        print()
        print()

        print("Selecione uma opção:")
        print("(0) --> Buscar links")
        print("(1) --> Buscar telefones")
        print("(2) --> Buscar e-mails")
        print("(3) --> Buscar CPFs")
        print("(4) --> Buscar CNPJs")


        try:
            op = int(input("Digite sua escolha: "))
        except ValueError:
            print("Digite um numero")
        except Exception as e:
            print(e)

        if op == 0:
            retorno = webcrawlerr.buscar_links(sys.argv[1])
            if retorno:
                deseja_salvar(retorno,'Links')
        
        elif op == 1:
            retorno = webcrawlerr.buscar_telefone(sys.argv[1])
            if retorno:
                deseja_salvar(retorno, 'Telefones')

        elif op == 2:
            retorno = webcrawlerr.buscar_email(sys.argv[1])
            if retorno:
                deseja_salvar(retorno,'E-mails')

        elif op == 3:
           retorno = webcrawlerr.buscar_cpf(sys.argv[1])
           if retorno:
            deseja_salvar(retorno,'CPFs')
        
        elif op == 4:
            retorno = webcrawlerr.buscar_cnpj(sys.argv[1])
            if retorno:
                deseja_salvar(retorno,'CNPJs')

    else:
        print("Usage: python3 web_search.py <url>")
        print("Ex: python3 web_search.py http://example.com")


