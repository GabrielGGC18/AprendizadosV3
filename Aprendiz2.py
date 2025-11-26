"""Aplicação dos Conhecimentos em Python"""

class Sobre_mim(): #Estruturação de dados e Classes
    def __init__(self,nome, idade, altura, estudante):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.estudante = estudante

    def sobre(self):    
       nome = f"My name is {self.nome}"
       idade = f", I am {self.idade} years old"
       altura = f", my height is {self.altura} meters"
       estudante = f", it is {self.estudante}, that I am a student"
       return nome + idade + altura + estudante

instance_class = Sobre_mim("Gabriel", 19, 1.92, "Estagiário")


print ("Informações Sobre Mim:", instance_class.sobre())