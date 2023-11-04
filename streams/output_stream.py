from entities.pessoa import Pessoa
from typing import List
from io import BufferedWriter as OutputStream
import sys


class PessoasOutputStream(OutputStream):
    def __init__(self, pessoas: List[Pessoa], out: OutputStream):
        self.pessoas = pessoas
        self.out = out

    def write_system(self):
        self.out.write("Quantidade de pessoas:"+str(len(self.pessoas))+"\n")
        for pessoa in self.pessoas:
            self.out.write("Bytes do nome: "+str(sys.getsizeof(pessoa.nome))+"\n")
            self.out.write("nome da pessoa: "+pessoa.nome+"\n")
            self.out.write("cpf da pessoa: "+str(pessoa.cpf)+"\n")
            self.out.write("idade da pessoa: "+str(pessoa.idade)+"\n\n")

    def write_file(self):
        with open(self.out, "w") as f:
            f.write("Quantidade de pessoas:"+str(len(self.pessoas))+"\n")
            for pessoa in self.pessoas:
                f.write("Bytes do nome: "+str(sys.getsizeof(pessoa.nome))+"\n")
                f.write("nome da pessoa: "+pessoa.nome+"\n")
                f.write("cpf da pessoa: "+str(pessoa.cpf)+"\n")
                f.write("idade da pessoa: "+str(pessoa.idade)+"\n\n")

    def write_tcp(self):
        with self.out as sock:
            sock.sendall(("Quantidade de pessoas:"+str(len(self.pessoas))+"\n").encode())
            for pessoa in self.pessoas:
                sock.sendall(("Bytes do nome: "+str(sys.getsizeof(pessoa.nome))+"\n").encode())
                sock.sendall(("nome da pessoa: "+pessoa.nome+"\n").encode())
                sock.sendall(("cpf da pessoa: "+str(pessoa.cpf)+"\n").encode())
                sock.sendall(("idade da pessoa: "+str(pessoa.idade)+"\n\n").encode())
