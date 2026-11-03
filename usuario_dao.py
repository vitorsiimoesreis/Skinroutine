from database import Database

class UsuarioDAO:

    # 1. C (Create / Inserir)
    def inserir(self, nome, email, senha, tipo_pele):
        conexao = Database.conectar()
        if conexao is None:
            return

        try:
            cursor = conexao.cursor()
            sql = "INSERT INTO usuarios (nome, email, senha, tipo_pele) VALUES (%s, %s, %s, %s)"
            valores = (nome, email, senha, tipo_pele)
            
            cursor.execute(sql, valores)
            conexao.commit()
            print("\n[SUCESSO] Usuario inserido no banco de dados!")
        except Exception as e:
            print(f"\n[ERRO] Ao inserir usuario: {e}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    # 2. R (Read / Consultar Todos)
    def listar_usuarios(self):
        conexao = Database.conectar()
        if conexao is None:
            return

        try:
            cursor = conexao.cursor()
            sql = "SELECT id, nome, email, tipo_pele FROM usuarios"
            cursor.execute(sql)
            
            resultados = cursor.fetchall()
            print("\n--- LISTAGEM DE USUARIOS DO BANCO DE DADOS ---")
            for linha in resultados:
                print(f"ID: {linha[0]} | Nome: {linha[1]} | E-mail: {linha[2]} | Tipo de Pele: {linha[3]}")
            print("---------------------------------------------")
        except Exception as e:
            print(f"\n[ERRO] Ao consultar usuarios: {e}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    # 2.1 R (Read / Buscar por ID Específico)
    def buscar_por_id(self, id_usuario):
        conexao = Database.conectar()
        if conexao is None:
            return

        try:
            cursor = conexao.cursor()
            sql = "SELECT id, nome, email, tipo_pele FROM usuarios WHERE id = %s"
            cursor.execute(sql, (id_usuario,))
            
            linha = cursor.fetchone()
            if linha:
                print(f"\n--- USUARIO ENCONTRADO ---")
                print(f"ID: {linha[0]} | Nome: {linha[1]} | E-mail: {linha[2]} | Tipo de Pele: {linha[3]}")
                print("--------------------------")
            else:
                print(f"\n[AVISO] Nenhum usuario encontrado com o ID {id_usuario}.")
        except Exception as e:
            print(f"\n[ERRO] Ao buscar usuario: {e}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    # 3. U (Update / Atualizar)
    def atualizar(self, id_usuario, novo_nome):
        conexao = Database.conectar()
        if conexao is None:
            return

        try:
            cursor = conexao.cursor()
            sql = "UPDATE usuarios SET nome = %s WHERE id = %s"
            valores = (novo_nome, id_usuario)
            
            cursor.execute(sql, valores)
            conexao.commit()
            print("\n[SUCESSO] Usuario atualizado com sucesso!")
        except Exception as e:
            print(f"\n[ERRO] Ao atualizar usuario: {e}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    # 4. D (Delete / Deletar)
    def deletar(self, id_usuario):
        conexao = Database.conectar()
        if conexao is None:
            return

        try:
            cursor = conexao.cursor()
            sql = "DELETE FROM usuarios WHERE id = %s"
            valores = (id_usuario,)
            
            cursor.execute(sql, valores)
            conexao.commit()
            print("\n[SUCESSO] Usuario deletado com sucesso!")
        except Exception as e:
            print(f"\n[ERRO] Ao deletar usuario: {e}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()