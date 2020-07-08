import requests


print('--------------------------------')
print('\t URL link :')
print('--------------------------------')
url = input('Enter the URl :') 

    # http://127.0.0.1 here we send the localhost as an URL

print('----------------------------------------------')
print('Enter the value the URL :',url)
print('----------------------------------------------')

pn = input('Enter Printer Name : ')
cl = input('Enter CytivaLabel : ')
co = input('Enter Company Name : ')
cy = input('Enter Cytiva : ')

myobj = {
        'PrinterName': pn,
        'CytivaLabel': cl,
        'Company': co,
        'Cytiva': cy,
        }

x = requests.post(url, data = myobj)

    #print the response text (the content of the requested file):
    
print('-------------------------------------------')
print('Print the Response from the URL :')
print('-------------------------------------------')
print('[NB] 200-OK-Standard response for successful HTTP requests.\n')
print('Here Received Response:--->',x)
print('------------------------------------------')

