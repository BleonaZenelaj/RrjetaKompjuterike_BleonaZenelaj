from math import pi
import socket
import time
import datetime
import random
import string
from _thread import *


serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
print('Serveri u startua ne localhost:'+str(serverPort))
serverSocket.listen(15)
print('Miresevini ne Serverin FIEK TCP!!!')
print('Serveri eshte i gatshem te pranoj kerkesa!')


def klientiThread(connectionSocket):
    while 1:
        try:
            fjalia = connectionSocket.recv(1024)
        except Exception:
            print("Lidhja u shkeput ")
            break
        
        
        farray=fjalia.decode().split(" ")
        
        def IPADRESA():
            ip=str(addr[0])
            connectionSocket.send(str("IP adresa e klientit eshte: "+ip).encode())
        

        def NUMRIIPORTIT():
            ip=str(addr[1])
            connectionSocket.send(str("Numri i portit eshte: "+ip).encode())
        

        def BASHKETINGELLORE(text):
            nrBashketingelloreve = 0
            bashketingelloret = ['b','B','c', 'C', 'd', 'D', 'f','F', 'g', 'G', 'h', 'H', 'i', 'I','j', 'J', 'k', 'K', 'l', 'L', 'm','M', 'n', 'N', 'p', 'P', 'q', 'Q','r', 'R', 's', 'S', 't', 'T', 'v','V', 'x', 'X', 'z', 'Z']
            for ch in text:
                if ch in bashketingelloret:
                    nrBashketingelloreve=nrBashketingelloreve+1
            connectionSocket.send(str("Numri i bashketingelloreve ne tekst eshte: "+str(nrBashketingelloreve)).encode())
        

        def PRINTIMI(text):
            text=text.strip()
            connectionSocket.send(str("Teksti i formatuar: "+text).encode())
        

        def EMRIIKOMPJUTERIT():
            emriikompjuterit=socket.gethostname() 
            connectionSocket.send(emriikompjuterit.encode())
        

        def KOHA():
            date = datetime.datetime.now().strftime('%Y/%m/%d %I:%M:%S%p')
            connectionSocket.send(str("Koha e serverit eshte: "+str(date)).encode())
        

        def LOJA():
            loja=[random.randint(1,49) for i in range(7)]
            connectionSocket.send(str("7 numra random nga rangu 1-49: "+str(loja)).encode())
        

        def FIBONACCI(n):
            nr=int(n)
            if nr == 0:
                return 0;
            elif nr == 1:
                return 1
            else:
                return FIBONACCI(nr-1)+FIBONACCI(nr-2)
    
        def KONVERTIMI(opt,temp):
            try:
                temp=float(temp)
                if(opt=="KilowattToHorsepower"):
                    tempK = 1.36*int(temp)
                    connectionSocket.send(str(str(temp)+" Kilowatt = "+ str(tempK)+" Horsepower").encode())
                
                elif(opt=="HorsepowerToKilowatt"):
                    tempK = float(temp)/1.36
                    connectionSocket.send(str(str(temp)++" Horsepower = "+ str(tempK)+" Kilowatt").encode())
                
                elif(opt=="DegreesToRadians"):
                    tempK = float(temp)*(pi/180)
                    connectionSocket.send(str(str(temp)+" Degrees = "+ str(tempK)+" Radians").encode())
                
                elif(opt=="RadiansToDegrees"):
                    tempK = float(temp)*(180/pi)
                    connectionSocket.send(str(str(temp)+" Radians = "+ str(tempK)+" Degrees").encode())
                
                elif(opt=="GallonsToLiters"):
                    tempK =float(temp)*3.78541
                    connectionSocket.send(str(str(temp)+" Gallons = "+ str(tempK)+" Liters").encode())
                
                elif(opt=="LitersToGallon"):
                    tempK = float(temp)/3.78541
                    connectionSocket.send(str(str(temp)+" Liters = "+ str(tempK)+" Gallons").encode())
                
      
            except ValueError:
                connectionSocket.send(str("Parametri i dhene duhet te jete numer ne menyre qe te mund te konvertohet").encode())
    
        def TEMPKONVERTO(fromTo,var):
            try:
                var=float(var)
                if(fromTo=="KelvinToCelsius"):
                    celsius = float(var)-(273.15)
                    connectionSocket.send(str(str(var)+" Celsius = "+ str(celsius)+" Kelvin").encode())
                            
                elif(fromTo=="CelsiusToKelvin"):
                    kelvin = float(var)+(273.15)
                    connectionSocket.send(str(str(var)+" Kelvin = "+ str(kelvin)+" Celsius").encode())
                
            except ValueError:
                connectionSocket.send(str("Parametri i dhene duhet te jete numer").encode())

        def RRETHI(rrezja):
            try:
                rr=float(rrezja)
                connectionSocket.send(str("Perimetri i rrethit me rreze: "+str(rr)+" eshte "+str(2*pi*rr)+" ndersa siperfaqja e tij eshte "+str(pi*rr*rr)).encode())
            
            except ValueError:
                connectionSocket.send(str("Parametri i dhene per rrezen duhet te jete numer.").encode())



        if(str(farray[0])=="PRINTIMI"):
            t=fjalia.decode().split(" ",1)
            x=t[1]
            PRINTIMI(x)
        elif(str(farray[0])=="BASHKETINGELLORE"):
            t=fjalia.decode().split(" ",1)
            x=t[1]
            BASHKETINGELLORE(x)
        
        elif(len(farray)==1):
            if(str(farray[0]) in {'IPADRESA','NUMRIIPORTIT','EMRIIKOMPJUTERIT','KOHA','LOJA'}):
                funks = farray[0]
                if (funks=="IPADRESA"):
                    IPADRESA()
                if (funks=="NUMRIIPORTIT"):
                    NUMRIIPORTIT()
                if (funks=="EMRIIKOMPJUTERIT"):
                    EMRIIKOMPJUTERIT()
                if (funks=="KOHA"):
                   KOHA()
                if(funks=="LOJA"):
                   LOJA()
            else:
                connectionSocket.send(str("Ne nuk e ofrojme kete lloj sherbimi ose nuk e keni specifikuar mire kerkesen tuaj").encode())
        elif(len(farray)==2):
            if(str(farray[0]) in {'PRINTIMI','BASHKETINGELLORE','FIBONACCI','RRETHI'}):
                if(str(farray[1])!=""):
                    funks = farray[0]
                    x = farray[1]
                    if(funks=="BASHKETINGELLORE"):
                        BASHKETINGELLORE(x)
                    if(funks=="FIBONACCI"):
                        try:
                            x=int(x)
                            rez=FIBONACCI(x)
                            connectionSocket.send(str("Numri i serise Fibonacci me indeks: "+str(x)+" eshte: "+str(rez)).encode())
                        
                        except ValueError:
                            connectionSocket.send(str("Parametri i dhene duhet te jete numer integjer").encode())
                    if(funks=="RRETHI"):
                        RRETHI(x)                    
                else:
                    connectionSocket.send(str("Nuk keni dhene parametrin shoqerues per funksionin").encode())
            else:
                connectionSocket.send(str("Ne nuk e ofrojme kete lloj sherbimi ose nuk e keni specifikuar mire kerkesen tuaj").encode())
       
        elif(len(farray)==3):
            if(str(farray[0]) in {'KONVERTIMI','TEMPKONVERTO'}):
                if(str(farray[1]) in {'KilowattToHorsepower','HorsepowerToKilowatt','DegreesToRadians','RadiansToDegrees','GallonsToLiters','LitersToGallons'}):
                    if(str(farray[2])!=""):
                        try:
                            x=float(farray[2])
                            funks=farray[0]
                            opt=farray[1]
                            if(funks=="KONVERTIMI"):
                                KONVERTIMI(opt,x)
                            if(funks=="TEMPKONVERTO"):
                                TEMPKONVERTO(opt,x)
                        except ValueError:
                            connectionSocket.send(str("Parametri qe do te konvertohet duhet te jete numer").encode())
                    else:
                        connectionSocket.send(str("Nuk keni dhene parametrin shoqerues per funksionin").encode())
                else:
                    connectionSocket.send(str("Nuk ofrojme kete opsion per funksionin perkates ose nuk keni specifikuar si duhet emrin e tij.").encode())
            else:
                connectionSocket.send(str("Ne nuk e ofrojme kete lloj sherbimi ose nuk e keni specifikuar mire kerkesen tuaj").encode())
        else:
            connectionSocket.send(str("Mund te zgjedhni vetem opsionet ekzistuese ne menu").encode())

        

    

while 1:
    connectionSocket, addr = serverSocket.accept()
    print('Klienti u lidh ne serverin %s me port %s' % addr)
    start_new_thread(klientiThread,(connectionSocket,))

