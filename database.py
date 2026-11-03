import mysql.connector
from mysql.connector import Error

class Database:
    @staticmethod
    def conectar():
        try:
            conexao = mysql.connector.connect(
                host='localhost',
                database='skinroutine_db',  # Altere para o nome do seu banco criado na Entrega 4
                user='root',                # Seu usuário do MySQL
                password='sua_senha'        # Sua senha do MySQL
            )
            if conexao.is_connected():
                return conexao
        except Error as e:
            # Tratamento inicial de erros exigido pelo requisito 1
            print(f"Erro de Conexao com o MySQL: {e}")
            print("Dica: Verifique se o servico do MySQL esta ativo e as credenciais estao corretas.")
            return None
            