import subprocess ,re

host = input('Host:')   # youtube.com, google.com and etc.
ping_st=subprocess.getoutput(['ping', host])    # ping host and get the output state in 'str' 
print(ping_st,'\n', '-'*10)          # the state of ping
loss_percentage = re.findall(r'\d+% loss', ping_st, flags=re.IGNORECASE)[0].split('%')[0]   # find the loss percentage with regex
print(float(loss_percentage), '\n', '-'*10, 'done :)')

