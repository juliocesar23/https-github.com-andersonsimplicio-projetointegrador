import Model.conexao as conn

class clienteBD:
    def __init__(self):
        self.banco = conn.managerdb()

    def insert(self,dados):
        lista= [tuple(dados)]
        print(type(lista))
        c = self.banco.getcursor()
        c.executemany("""INSERT INTO Cliente (cod_cliente,nome,nome_fantasia,cpf,cnpj,tipo,status,ins_estadual,ins_municipal,email,emailxml,telefone1,telefone2)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            lista)
        self.banco.fecharConexao()






