def saluto_nome_cognome(nome, cognome):
    saluto = "buongiorno prof sono, " + nome + " " + cognome + "!"
    return saluto

nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
saluto = saluto_nome_cognome(nome, cognome)
print(saluto)
