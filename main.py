import io
import socket
import sys
from entities.pessoa import Pessoa
from streams.output_stream import PessoasOutputStream
from streams.input_stream import PessoasInputStream

def main():
    # people_list = [Pessoa('Luciana', '123', 20), Pessoa('Carlos', '456', 21)]
    people_list = []

    input_stream_stdin = PessoasInputStream(sys.stdin)
    person = input_stream_stdin.read_system()
    people_list.append(person)

    input_stream_filein = PessoasInputStream('entrada.txt')
    person = input_stream_filein.read_file()
    people_list.append(person)
    
    # descomentar fragmento de código no servidor para funcionar
    # input_stream_tcp = PessoasInputStream(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    # person = input_stream_tcp.read_tcp()
    # people_list.append(person)

    output_stream_stdout = PessoasOutputStream(people_list, sys.stdout)
    output_stream_stdout.write_system()

    output_stream_fileout = PessoasOutputStream(people_list, 'saida.txt')
    output_stream_fileout.write_file()
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("localhost", 7896))
        output_stream_serverout = PessoasOutputStream(people_list, sock)
        output_stream_serverout.write_tcp()

    



if __name__ == "__main__":
    main()