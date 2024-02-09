import os,sys
import argparse
import requests as r
from colorama import Fore

os.system("clear")
print('''

    _   __    __________  _                _  __       __      _ __ 
   / | / /___/_  __/ __ \(_)___  ____     | |/ /____  / /___  (_) /_
  /  |/ / __ \/ / / /_/ / / __ \/ __ \    |   // __ \/ / __ \/ / __/
 / /|  / /_/ / / / ____/ / / / / /_/ /   /   |/ /_/ / / /_/ / / /_  
/_/ |_/\____/_/ /_/   /_/_/ /_/\____/   /_/|_/ .___/_/\____/_/\__/  
                                            /_/                     
                                       
Recode By ./NoTPino 
Create By ./RedSec
inspiration by https://github.com/varelsecurity/
''')     
parser = argparse.ArgumentParser()
parser.add_argument('-u','--url', type=str, required=True, help="Masukan URL")
parser.add_argument('-o','--output', type=str, required=True, help="Masukan Output (eg: output.txt)")
parser.add_argument('-w','--wordlist', type=str, required=True,default="main/wordlist.txt", help="Masukan Wordlist (default: main/wordlist.txt)")
args = parser.parse_args()
if args.wordlist:
    with open(args.wordlist, 'r') as file:
        wordlist = file.readlines()
else:
    wordlist = open("main/wordlist.txt").readlines()
   
os.system("clear")
print (Fore.LIGHTCYAN_EX, '''

    _   __    __________  _                _  __       __      _ __ 
   / | / /___/_  __/ __ \(_)___  ____     | |/ /____  / /___  (_) /_
  /  |/ / __ \/ / / /_/ / / __ \/ __ \    |   // __ \/ / __ \/ / __/
 / /|  / /_/ / / / ____/ / / / / /_/ /   /   |/ /_/ / / /_/ / / /_  
/_/ |_/\____/_/ /_/   /_/_/ /_/\____/   /_/|_/ .___/_/\____/_/\__/  
                                            /_/                     
                                                                                                                 
Admin Login Finder 
Recode By ./NoTPino
Create By ./RedSec
inspiration by https://github.com/varelsecurity/
''')

print (f"Website : {args.url}")
print (f"Output file : {args.output}")
print (f"Wordlist : {args.wordlist}")
if not os.path.isfile(args.wordlist):
    print(f"{args.wordlist} not found!")
    sys.exit()
print()
for i in list:
    line = i.strip()
    req = r.get(f'{args.url}{line}')
    if req.status_code ==200:
        print (Fore.LIGHTGREEN_EX, f"(status: {req.status_code}) (size: {len(req.content)}) {args.url}{line}")
        f = open(f"{args.output}", "a")
        f.write(f"(status: {req.status_code}) (size: {len(req.content)}) {args.url}{line}\n")
        f.close()
