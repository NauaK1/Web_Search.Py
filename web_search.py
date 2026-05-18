import sys
import webcrawlerr



if __name__ == "__main__":
    if len(sys.argv) > 1:
    
        print("""
    _ _ _ _____ ___     _____ _____ _____ _____ _____ _____     _____ __ __ 

    | | | |   __| __|   |   __|   __|  _  | __  |     |  |  |   |  _  |  |  |
    | | | |   __|__ |   |__   |   __|     |    _|-   -|  |  |   |   __|_   _|
    |_____|_____|___|   |_____|_____|__|__|__|__|_____|_____|   |__|    |_|  
                                                                            
    """)
        print("              ┌──────────────────────────────────┐")
        print("              │          web.search.py           │")
        print("              │        Developed by Nauak        │")
        print("              └──────────────────────────────────┘")
        print()
        print("Selecione uma opção:")
        print("(0) --> Buscar links")
        print("(1) --> Buscar telefones")
        print("(2) --> Buscar e-mails")
        print("(3) --> Buscar CPFs")
        print("(4) --> Buscar CNPJs")
        print()

        try:
            op = int(input("Digite sua escolha: "))
        except ValueError:
            print("Digite um numero")
        except Exception as e:
            print(e)

        if op == 0:
            t1 = webcrawlerr.threading.Thread(webcrawlerr.buscar_links(sys.argv[1]))
            t2 = webcrawlerr.threading.Thread(webcrawlerr.buscar_links(sys.argv[1]))

            t1.start()
            t2.start()

            t1.join()
            t2.join()
        
        elif op == 1:
            webcrawlerr.buscar_telefone(sys.argv[1])

        elif op == 2:
            webcrawlerr.buscar_email(sys.argv[1])

        elif op == 3:
            webcrawlerr.buscar_cpf(sys.argv[1])
        
        elif op == 4:
            webcrawlerr.buscar_cnpj(sys.argv[1])

    else:
        print("Usage: python3 web_search.py <url>")
        print("Ex: python3 web_search.py http://example.com")


