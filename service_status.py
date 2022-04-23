import sys
import os
import subprocess
import requests
import shlex
def status(args):
        a = args[1]
        b = args[2]
        c = args[3]
        if a == 'status' and c == 'http_prd':
                with open("interfacelist.txt") as f:
                        lines = f.read().splitlines()
                        b = args[2]
                        for i in lines:
                                if b == i:
                                        print(i)
                                        #ssh = subprocess.Popen(cmd,
                                        ssh = subprocess.Popen(["curl", "http://abc-{}.format(b)-.com/actuator/health"],
                                        shell=False,
#                                        stdout=subprocess.PIPE)
                                        stderr=subprocess.PIPE)
                                        result = ssh.stderr.readlines()
                                        print(result)
if __name__ == '__main__':
#    import sys
        status(sys.argv)
