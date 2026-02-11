nome = "Guilherme"
idade = 28
profissao = "Programado"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s. " % (nome, idade, profissao, linguagem))



################Metodo format###############
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}. " . format(nome, idade, profissao, linguagem))



print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}. " .format(linguagem, profissao, idade, nome))



########################OPÇAO--MAIS--USADO############################
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))


#########################OPÇÃO#############################
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")