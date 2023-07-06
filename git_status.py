import subprocess
from time import sleep

# Executa o comando de commit
subprocess.run('git add .', shell=True)
sleep(1)

# Executa o comando de commit
subprocess.run('git commit -m "teste commit"', shell=True)
sleep(1)

# Executa o comando de commit
subprocess.run('git push origin main', shell=True)