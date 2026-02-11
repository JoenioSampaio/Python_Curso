nome = "Joenio"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " Olá mundo!      "

print(texto) #mantem os espaços 
print(texto.strip())  #retira os espaços da String

#remove os espaços laterais
print(texto.rstrip() + "...")
print(texto.lstrip() + "...")


#Concatenação com String
menu = "Python"

print("###" + menu + "###") 
print(menu.center(14) + ".") # colocar espaço nas laterais
print(menu.center(20, "#"))  #colocar numero igual de #