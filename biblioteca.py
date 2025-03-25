funcionarios = []
proximo_id = 1
livros = []
historico_emprestimos = []

livros.extend([
    {"titulo": "A Guerra dos Tronos", "disponivel": True},
    {"titulo": "Sapiens", "disponivel": True},
    {"titulo": "O Senhor dos Anéis", "disponivel": True},
    {"titulo": "1984", "disponivel": True},
    {"titulo": "Dom Quixote", "disponivel": True},
    {"titulo": "Moby Dick", "disponivel": True},
    {"titulo": "Cem Anos de Solidão", "disponivel": True},
    {"titulo": "Ulisses", "disponivel": True},
    {"titulo": "Em Busca do Tempo Perdido", "disponivel": True},
    {"titulo": "O Grande Gatsby", "disponivel": True},
])

def exibir_menu():
    print("-" * 50)
    print("Bem-vindo ao Portal do Administrador")
    print("-" * 50)
    print("\nAs seguintes funcionalidades estão disponíveis:\n")
    print("1- Adicionar Atendente")
    print("2- Adicionar Bibliotecário")
    print("3- Visualizar Histórico de Livros Emprestados")
    print("4- Visualizar Todos os Livros na Biblioteca")
    print("5- Emprestar Livro")
    print("6- Remover Usuário")
    print("7- Listar Usuários Ativos")
    print("8- Sair")
    print("-" * 50)

def obter_escolha():
    while True:
        try:
            escolha = int(input("\nDigite a sua escolha: "))
            if 1 <= escolha <= 8:
                return escolha
            else:
                print("Escolha inválida. Digite um número entre 1 e 8.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def adicionar_funcionario(tipo):
    global proximo_id

    while True:
        nome = input("Digite o Nome (apenas letras): ")
        if nome.isalpha() or " " in nome:
            break
        else:
            print("Nome inválido. Digite apenas letras.")

    while True:
        endereco = input("Digite o Endereço (apenas letras): ")
        if endereco.isalpha() or " " in endereco:
            break
        else:
            print("Endereço inválido. Digite apenas letras.")

    while True:
        telefone = input("Digite o Número de Telefone (9 dígitos): ")
        if telefone.isdigit() and len(telefone) == 9:
            break
        else:
            print("Número de telefone inválido. Digite 9 dígitos numéricos.")

    while True:
        salario = input("Digite o Salário (apenas números): ")
        if salario.isdigit():
            break
        else:
            print("Salário inválido. Digite apenas números.")

    funcionario = {
        "id": proximo_id,
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "salario": salario,
        "tipo": tipo
    }

    funcionarios.append(funcionario)
    print(f"\n{tipo} com o nome {nome} criado com sucesso.")
    print(f"Seu ID é: {proximo_id}")
    print(f"Sua Senha é: {proximo_id}")

    proximo_id += 1

def visualizar_historico_emprestimos():
    print("\nHistórico de Livros Emprestados:")
    if historico_emprestimos:
        for emprestimo in historico_emprestimos:
            print(f"Título: {emprestimo['titulo_livro']}, Usuário: {emprestimo['id_usuario']}, Data: {emprestimo['data_emprestimo']}")
    else:
        print("Nenhum empréstimo registrado.")

def visualizar_todos_livros():
    print("\nTodos os Livros na Biblioteca:")
    if livros:
        for livro in livros:
            print(f"Título: {livro['titulo']}, Disponível: {livro['disponivel']}")
    else:
        print("Nenhum livro disponível.")

def emprestar_livro():
    print("\nLivros disponíveis:")
    for livro in livros:
        if livro["disponivel"]:
            print(f"- {livro['titulo']}")

    titulo_livro = input("\nDigite o título do livro a ser emprestado: ")
    id_usuario = int(input("Digite o ID do usuário: "))

    livro_encontrado = None
    for livro in livros:
        if livro["titulo"] == titulo_livro and livro["disponivel"]:
            livro_encontrado = livro
            break

    if livro_encontrado:
        livro_encontrado["disponivel"] = False
        emprestimo = {
            "titulo_livro": titulo_livro,
            "id_usuario": id_usuario,
            "data_emprestimo": "2024-06-22"
        }
        historico_emprestimos.append(emprestimo)
        print(f"Livro '{titulo_livro}' emprestado com sucesso para o usuário {id_usuario}.")
    else:
        print("Livro não encontrado ou não disponível.")

def remover_usuario():
    print("\nLista de Usuários Ativos:")
    if funcionarios:
        for usuario in funcionarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Tipo: {usuario['tipo']}")
    else:
        print("Nenhum usuário ativo.")
        return

    id_usuario = int(input("\nDigite o ID do usuário a ser removido ou pause a assinatura: "))
    usuario_encontrado = None

    for usuario in funcionarios:
        if usuario["id"] == id_usuario:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        nome_usuario = usuario_encontrado["nome"]  # Armazena o nome do usuário
        acao = input("Digite 'R' para remover ou 'P' para pausar a assinatura: ").upper()
        if acao == "R":
            usuario_encontrado["nome"] = "Removido"
            print(f"Usuário {nome_usuario} removido com sucesso.")  # Exibe o nome
        elif acao == "P":
            usuario_encontrado["nome"] = "Assinatura Pausada"
            print(f"Assinatura do usuário {nome_usuario} pausada com sucesso.")  # Exibe o nome
        else:
            print("Ação inválida.")
    else:
        print("Usuário não encontrado.")

def listar_usuarios_ativos():
    print("\nLista de Usuários Ativos:")
    if funcionarios:
        for usuario in funcionarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Tipo: {usuario['tipo']}")
    else:
        print("Nenhum usuário ativo.")

def main():
    while True:
        exibir_menu()
        escolha = obter_escolha()

        if escolha == 1:
            adicionar_funcionario("Atendente")
        elif escolha == 2:
            adicionar_funcionario("Bibliotecário")
        elif escolha == 3:
            visualizar_historico_emprestimos()
        elif escolha == 4:
            visualizar_todos_livros()
        elif escolha == 5:
            emprestar_livro()
        elif escolha == 6:
            remover_usuario()
        elif escolha == 7:
            listar_usuarios_ativos()
        elif escolha == 8:
            print("Saindo...")
            break

        input("\nPressione qualquer tecla para continuar..")

if __name__ == "__main__":
    main()