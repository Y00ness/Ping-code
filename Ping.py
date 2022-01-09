import subprocess
import platform

def Ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '3', host]
    # return subprocess.call(command)
    return subprocess.getoutput(command)

host = input('url:')
res=Ping(host)
# print(type(res))
print(res)
print('\n-----\ndone :)')