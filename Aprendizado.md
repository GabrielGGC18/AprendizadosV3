# Aplicação dos Conhecimentos em Python

Este documento reúne conceitos fundamentais de **classes**, **métodos especiais** e **estruturação de dados** em Python, aplicados durante o estudo.

---

## Estruturação de Classes

```python
class SobreMim:
    def __init__(self, nome, idade, altura, estudante):
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
