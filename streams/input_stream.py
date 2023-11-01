import io
from entities.pessoa import Pessoa
from typing import List


class PessoaInputStream(io.IOBase):
    def __init__(self, pessoas, entrada):
        self.pessoas = pessoas
        self.entrada = entrada

    def read_system(self):
        name = input("Enter the person's name:")
        cpf = input("Enter the person's cpf:")
        age = int(input("Enter the person's age:"))

        self.people[0] = Pessoa(name, cpf, age)
        return self.people

    def read_file(self):
        return self.people

    def read_tcp(self):
        return self.people

    def read(self):
        return 0
        # Implement this method if needed, but it's not clear how it should behave in your context.

# Exemplo de uso:

if __name__ == "__main__":
    pessoas = [{}]
    entrada = io.BytesIO(b'Sua Entrada Aqui')  # Substitua pela sua entrada

    stream = PessoasInputStream(pessoas, entrada)
    stream.read_system()

    print("Dados lidos:")
    print(stream.read_file())
