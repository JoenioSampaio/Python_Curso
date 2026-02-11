nome = "Guilherme"
idade = 28
profissao = "Programado"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Joenio", "idade": 28}

print("nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade,nome))
print("Nome: {1} Idade: {0} nome: {1} {0}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}") 