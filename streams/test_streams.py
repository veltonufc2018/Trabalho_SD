from entities.pessoa import Pessoa
from streams.input_stream import PessoasInputStream
from streams.output_stream import PessoasOutputStream
import sys

class TestStreams:
	def main(self):
		pessoas = [Pessoa('João', '123.456.789-00', 30), Pessoa('Maria', '987.654.321-00', 25)]
		pis = PessoasInputStream(pessoas, sys.stdin)
		pessoas = pis.readSystem()
		pis.close()        
		
		pos = PessoasOutputStream(pessoas, sys.stdout)
		pos.writeSystem()
		pos.close()
