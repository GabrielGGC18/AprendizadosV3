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
```
## Uso do Método __str__

[!info] O método __str__ define como o objeto será representado em forma de string. É chamado quando usamos print(objeto) ou str(objeto).

Exemplo:    
    class Work:
    def __init__(self, cargo):
        self.cargo = cargo

    def __str__(self):
        return f"Meu cargo é: {self.cargo}"

trabalho = Work("Estagiário")
print(trabalho)  # Saída: Meu cargo é: Estagiário

## Diferença entre __init__ e __str__

[!warning]

__init__: inicializa os atributos do objeto.

__str__: mostra a representação textual do objeto. Não confunda: o primeiro prepara o objeto, o segundo mostra o objeto.


## Card de Estudo

Este card representa o progresso no estudo da trilha Python.



## Conclusão
Classes permitem estruturar dados e comportamentos.

__init__ organiza os atributos ao criar o objeto.

__str__ facilita a leitura e impressão dos objetos.

A prática com exemplos ajuda a consolidar o aprendizado.


---

Esse arquivo `.md` já está pronto para ser usado como documentação do seu estudo. Ele combina exemplos práticos, explicações e avisos (`info` e `warning`) para reforçar os conceitos.  

Quer que eu adicione também uma seção com exercícios práticos para treinar esses conceitos dentro do mesmo arquivo?

---