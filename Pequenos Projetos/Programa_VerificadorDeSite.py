import urllib
from urllib import request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mO site desejado está fora do ar neste momento.\033[m')
else:
    print('\033[32mO site digitado está ativo neste momento.\033[m')
