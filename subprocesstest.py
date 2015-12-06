import subprocess
from subprocess import PIPE
cmd = 'cat'
popen = subprocess.Popen(cmd.strip().split(' '),stdin=PIPE,stdout=PIPE)
output = popen.communicate('hogehogehoge'.encode('utf-8'))
print(output[0].decode('utf-8'))
