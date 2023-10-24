def escreverNoSql(comando):
    f = open('SQL.txt', 'a+')
    f.write(comando+"\n")
    f.close()

def criarPessoa(nome, idade, cpf):
    escreverNoSql(f'INSERT INTO Pessoa (Nome, Idade, CPF) VALUES ({nome}, {idade}, {cpf})')
    

def editarPessoa(nome, idade, cpf):
    escreverNoSql(f'UPDATE Pessoa SET Nome={nome} Idade={idade} CPF={cpf} WHERE ID={id}')


def excluirPessoa(id):
    escreverNoSql(f'DELETE FROM Pessoa WHERE ID ={id}')
