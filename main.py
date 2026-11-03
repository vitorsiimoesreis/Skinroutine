from usuario_dao import UsuarioDAO

def main():
    dao = UsuarioDAO()

    while True:
        print("\n=== SISTEMA SKINROUTINE (PYTHON DAO) ===")
        print("1. Cadastrar Usuario (Create)")
        print("2. Listar Todos os Usuarios (Read)")
        print("3. Buscar Usuario por ID (Read Específico)")
        print("4. Atualizar Usuario (Update)")
        print("5. Deletar Usuario (Delete)")
        print("0. Sair")
        
        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            tipo_pele = input("Tipo de Pele: ")
            
            if not nome or not email:
                print("\n[ERRO] Nome e E-mail sao obrigatorios!")
            else:
                dao.inserir(nome, email, senha, tipo_pele)
            
        elif opcao == '2':
            dao.listar_usuarios()
            
        elif opcao == '3':
            id_usuario = input("Digite o ID do usuario que deseja buscar: ")
            dao.buscar_por_id(id_usuario)
            
        elif opcao == '4':
            id_usuario = input("ID do usuario que deseja atualizar: ")
            novo_nome = input("Novo nome: ")
            dao.atualizar(id_usuario, novo_nome)
            
        elif opcao == '5':
            id_usuario = input("ID do usuario que deseja deletar: ")
            dao.deletar(id_usuario)
            
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opcao invalida!")

if __name__ == "__main__":
    main()