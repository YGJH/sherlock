import subprocess
import sys
from tqdm import *
for user in sys.argv[1:]:
    print("finding "+user)
    result = set()
    for _ in tqdm(range(3)):
        output = subprocess.run(f'sudo docker run sherlock/sherlock {user} --nsfw' ,capture_output=True, text=True, shell=True, check=True, encoding='utf-8')
        output = output.stdout

        output = output[output.find(f'[*] Checking username {user} on:'):output.find('[*] Search completed with ')]
        for i in output.split('[+] '):
            result.add(i)


    for i in result:
        if "Checking username" in i:
            continue
        print("[*]\t"+i.strip())

    print("total "+str(len(result))+" results")
