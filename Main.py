from colorama import Fore, Style, init
import json
import os

init()

ascii_art = """  _____                                            __        __ 
 / ___/__  ______  ___  _________ ___  ____ ______/ /_____  / /_
 \__ \/ / / / / __ \/ _ \/ ___/ __ `__ \/ __ `/ ___/ //_/ _ \/ __/
___/ / /_/ / /_/ /  __/ /  / / / / / / / /_/ / /  / ,< /  __/ /_  
/____/\__,_/ .___/\___/_/  /_/ /_/ /_/\__,_/_/  /_/|_|\___/\__/  
          /_/                                                 """

ARQUIVO = 'data/produtos.json'
historico = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_tela():
    limpar_tela()
    print(Fore.RED + ascii_art + Style.RESET_ALL)
    print("Create by " + Fore.RED + "ExtremeCodeX" + Style.RESET_ALL)
    print("=" * 60)
    for msg in historico[-10:]:  
        print(msg)
    print("=" * 60)

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open(ARQUIVO, 'w') as f:
        json.dump(dados, f, indent=4)

def ADD():
    dados = carregar_dados()
    nome = input("Digite o nome do produto: ")
    try:
        preco = float(input("Digite o preço do produto: "))
        dados.append({"nome": nome, "preco": preco})
        salvar_dados(dados)
        historico.append(Fore.GREEN + f"[OK] Produto '{nome}' adicionado com sucesso!" + Style.RESET_ALL)
    except ValueError:
        historico.append(Fore.RED + "[ERRO] Preço inválido!" + Style.RESET_ALL)

def ALT():
    dados = carregar_dados()
    nome = input("Digite o nome do produto que deseja alterar: ")
    for item in dados:
        if item['nome'].lower() == nome.lower():
            try:
                novo_preco = float(input("Digite o novo preço: "))
                item['preco'] = novo_preco
                salvar_dados(dados)
                historico.append(Fore.YELLOW + f"[OK] Preço de '{nome}' alterado com sucesso!" + Style.RESET_ALL)
                return
            except ValueError:
                historico.append(Fore.RED + "[ERRO] Preço inválido!" + Style.RESET_ALL)
                return
    historico.append(Fore.RED + f"[ERRO] Produto '{nome}' não encontrado." + Style.RESET_ALL)

def VER():
    dados = carregar_dados()
    if not dados:
        historico.append("Nenhum produto cadastrado.")
    else:
        historico.append("Visualização de produtos:")
        historico.append("+==========================+=============+")
        historico.append("| Nome do Produto          | Preço (R$)  |")
        historico.append("+==========================+=============+")
        for item in dados:
            nome_formatado = item['nome'].ljust(26)[:26]
            preco_formatado = f"R$ {item['preco']:.2f}".rjust(11)
            historico.append(f"| {nome_formatado} | {preco_formatado} |")
        historico.append("+==========================+=============+")

def PESQUISAR():
    dados = carregar_dados()
    termo = input("Digite o nome ou parte do nome do produto: ").lower()
    resultados = [item for item in dados if termo in item['nome'].lower()]
    if resultados:
        historico.append(f"Resultados da pesquisa por '{termo}':")
        for item in resultados:
            historico.append(f"- {item['nome']} | R$ {item['preco']:.2f}")
    else:
        historico.append(Fore.RED + "[INFO] Nenhum item encontrado." + Style.RESET_ALL)

def APAGAR():
    dados = carregar_dados()
    nome = input("Digite o nome do produto que deseja apagar: ")
    novo_dados = [item for item in dados if item['nome'].lower() != nome.lower()]
    if len(novo_dados) < len(dados):
        salvar_dados(novo_dados)
        historico.append(Fore.GREEN + f"[OK] Produto '{nome}' apagado com sucesso!" + Style.RESET_ALL)
    else:
        historico.append(Fore.RED + "[ERRO] Produto não encontrado." + Style.RESET_ALL)

def ORDENAR():
    dados = carregar_dados()
    dados.sort(key=lambda x: x['nome'].lower())
    salvar_dados(dados)
    historico.append("[OK] Lista de produtos ordenada por nome.")

def EXPORTAR_TXT():
    dados = carregar_dados()
    with open('produtos.txt', 'w', encoding='utf-8') as f:
        f.write("Nome do Produto | Preço (R$)\n")
        f.write("-" * 30 + "\n")
        for item in dados:
            f.write(f"{item['nome']} | R$ {item['preco']:.2f}\n")
    historico.append(Fore.CYAN + "[OK] Arquivo produtos.txt criado com sucesso!" + Style.RESET_ALL)

def EXPORTAR_EXCEL():
    try:
        import pandas as pd
        dados = carregar_dados()
        df = pd.DataFrame(dados)
        df.to_excel("produtos.xlsx", index=False)
        historico.append(Fore.CYAN + "[OK] Arquivo produtos.xlsx criado com sucesso!" + Style.RESET_ALL)
    except ImportError:
        historico.append(Fore.RED + "[ERRO] pandas não instalado. Use: pip install pandas openpyxl" + Style.RESET_ALL)

def MENU():
    while True:
        exibir_tela()
        try:
            opcao = int(input(
                "Menu:\n"
                "1 - Adicionar item\n"
                "2 - Alterar valor\n"
                "3 - Visualizar lista\n"
                "4 - Pesquisar por item\n"
                "5 - Apagar item\n"
                "6 - Ordenar lista\n"
                "7 - Criar documento TXT\n"
                "8 - Criar documento EXCEL\n"
                "9 - Encerrar programa\n"
                "Escolha uma opção: "
            ))
        except ValueError:
            historico.append(Fore.RED + "[ERRO] Entrada inválida. Digite um número." + Style.RESET_ALL)
            continue

        if opcao == 1:
            ADD()
        elif opcao == 2:
            ALT()
        elif opcao == 3:
            VER()
        elif opcao == 4:
            PESQUISAR()
        elif opcao == 5:
            APAGAR()
        elif opcao == 6:
            ORDENAR()
        elif opcao == 7:
            EXPORTAR_TXT()
        elif opcao == 8:
            EXPORTAR_EXCEL()
        elif opcao == 9:
            historico.append(Fore.CYAN + "[SAINDO] Encerrando o programa..." + Style.RESET_ALL)
            exibir_tela()
            break
        else:
            historico.append(Fore.RED + "[ERRO] Opção inválida." + Style.RESET_ALL)

MENU()
