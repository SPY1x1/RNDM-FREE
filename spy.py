import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from SpY import menu
 
        menu()
 
 
 
elif bit == "32bit":
 
        from SpY32 import menu
        
        menu()
        


 
 
 
