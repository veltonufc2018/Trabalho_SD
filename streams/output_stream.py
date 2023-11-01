from io import BufferedWriter as OutputStream
from entities.pessoa import Pessoa
from typing import List


class PessoasOutputStream(OutputStream):
    def __init__(self, people: List[Pessoa], out: OutputStream):
        self.people = people
        self.outS = out

    def read_system(self):
        name = input("Enter the person's name:")
        cpf = float(input("Enter the person's cpf:"))
        age = int(input("Enter the person's age:"))

        self.people[0] = Pessoa(name, cpf, age)
        return self.people

    def read_file(self):
        return self.people

    def read_tcp(self):
        return self.people

    def read(self, size=-1):
        return self.people.__str__()
        # Implement this method if needed, but it's not clear how it should behave in your context.
