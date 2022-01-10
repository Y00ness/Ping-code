import subprocess
import platform

def Ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '3', host]
    return subprocess.call(command)         # return 'int',0 if it works else 1 
    # return subprocess.getoutput(command)  # return 'str', the status of ping a host

host = input('Host:')
ping_st=Ping(host)
print(ping_st)
print('\n-----\ndone :)')