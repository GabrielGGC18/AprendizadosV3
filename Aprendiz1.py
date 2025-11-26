# Criando Váriaveis 
class age:
    pass

Nome = "Gabriel" # É uma string
Idade = 19 # é um inteiro  = int
Altura = 1.92 #Do tipo float(número decimal)
Estudante = 'Estudante'  # Do tipo Booleano


class work:
    def __DOG__(self):
        return "My second work is: Banqueiro"
    
    def __str__(self):
        return "Estagiário"

my_work_is = work ()
BANQUEIRO = my_work_is.__DOG__()
#Aplicação dos conceitos aprendidos em python

print(f"My name is {Nome}, I am {Idade} years old, my height is {Altura} meters and it, is {Estudante}, that I am a student")
print ("my age is:", Idade) 
print("My function:", Estudante)
print("My work is: ", work())
print(BANQUEIRO)
