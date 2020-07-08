# -*- coding: utf-8 -*-
#----[ Before execute the code Save the following XML as "note.xml"
#--------------------[XML file starts here]---------------------------
# <data>
#    <items>
#        <item name="item1">item1abc</item>
#        <item name="item2">item2abc</item>
#    </items>
# </data>
#--------------------[XML file ends here]----------------------------
#---------[ Code starts here ]--------------

import requests

xml = "<?xml version='1.0' encoding='utf-8'?>"

headers = {'Content-Type': 'note/xml'} # set what your server accepts

print('--------------------------------')
print('\t URL link :')
print('--------------------------------')

url = input('Enter the URl :') 

x=requests.post(url, data=xml, headers=headers)

print('-------------------------------------------')
print('Print the Response from the URL :')
print('-------------------------------------------')
print('[NB] 200-OK-Standard response for successful HTTP requests.\n')
print('Here Received Response:--->',x)
print('------------------------------------------')

