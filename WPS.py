import subprocess
import re

data = subprocess.check_output('netsh wlan show profiles', shell=True).decode()
results = re.findall(r'(Profile\s*[:]\s*)(.*)', data)
for result in results:
    print('[+] Found A Network!\n   - SSID :- '+result[1])
    data = subprocess.check_output('netsh wlan show profile name=\"'+result[1]+'\" key=clear', shell=True).decode()
    statuses = re.findall(r'(Security\skey\s*[:]\s*)(.*)', data)
    for status in statuses:
        if 'Present' in status[1]:
            print('   - Password Status :- Present')
            data = subprocess.check_output('netsh wlan show profile name=\"' + result[1] + '\" key=clear',
                                           shell=True).decode()
            passwords = re.findall(r'(Key\sContent\s*[:]\s*)(.*)', data)
            AuthenticationTypes = re.findall(r'(Authentication\s*[:]\s*)(.*)', data)
            CipherTypes = re.findall('(Cipher\s*[:]\s*)(.*)', data)
            print('   - Authentication Type :- '+AuthenticationTypes[0][1])
            print('   - Cipher :- '+CipherTypes[0][1])
            print('   - Password :- '+passwords[0][1])
        else:
            print('   - No Password Present! This is a Open Network!')
    print('\n')