from entities.pessoa import Pessoa
from io import BufferedReader as InputStream
from typing import List
import socket


class PessoasInputStream(InputStream):
    def __init__(self, entrada):
        self.entrada = entrada

    def read_system(self):
        nome = self.entrada.readline()[:-1]
        cpf = self.entrada.readline()[:-1]
        idade = self.entrada.readline()[:-1]

        person = Pessoa(nome, cpf, idade)
        return person

    def read_file(self):
        with open("entrada.txt", "r") as f:
            nome = f.readline()[:-1]
            cpf = f.readline()[:-1]
            idade = f.readline()
            person = Pessoa(nome, cpf, idade)
        return person

    def read_tcp(self):
        with self.entrada as sock:
            sock.connect(("localhost", 7896))
            dados = sock.recv(1024).decode().split("\n")
            nome = dados[0]
            cpf = dados[1]
            idade = dados[2]
            person = Pessoa(nome, cpf, idade)
        return person
