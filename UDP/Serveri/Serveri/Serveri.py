from math import pi
import socket
import time
import datetime
import random
import string

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Serveri u startua ne localhost:'+str(serverPort))
print('Miresevini ne Serverin FIEK UDP!!!')
print('Serveri eshte i gatshem te pranoj kerkesa!')

while True:
    fjalia, addr = serverSocket.recvfrom(1024);
    print("Te dhenat e pranuara nga klienti: " + fjalia.decode())
    farray=fjalia.decode().split(" ")


    def IPADRESA():
        ip=str(addr[0])
        serverSocket.sendto(str("IP adresa e klientit eshte: "+ip).encode(),addr)
        

    def NUMRIIPORTIT():
        ip=str(addr[1])
        serverSocket.sendto(str("Numri i portit eshte: "+ip).encode(),addr)
        

    def BASHKETINGELLORE(text):
        nrBashketingelloreve = 0
        bashketingelloret = ['b','B','c', 'C', 'd', 'D', 'f','F', 'g', 'G', 'h', 'H', 'i', 'I','j', 'J', 'k', 'K', 'l', 'L', 'm','M', 'n', 'N', 'p', 'P', 'q', 'Q','r', 'R', 's', 'S', 't', 'T', 'v','V', 'x', 'X', 'z', 'Z']
        for ch in text:
            if ch in bashketingelloret:
                nrBashketingelloreve=nrBashketingelloreve+1
        serverSocket.sendto(str("Numri i zanoreve ne tekst eshte: "+str(nrBashketingelloreve)).encode(),addr)
        

    def PRINTIMI(text):
        text=text.strip()
        serverSocket.sendto(str("Teksti i formatuar: "+text).encode(),addr)
        

    def EMRIIKOMPJUTERIT():
            emriikompjuterit=socket.gethostname() 
            serverSocket.sendto(emriikompjuterit.encode(),addr)
        

    def KOHA():
        date = datetime.datetime.now().strftime('%Y/%m/%d %I:%M:%S%p')
        serverSocket.sendto(str("Koha e serverit eshte: "+str(date)).encode(),addr)
        

    def LOJA():
        loja=[random.randint(1,49) for i in range(7)]
        serverSocket.sendto(str("7 numra random nga rangu 1-49: "+str(loja)).encode(),addr)
        

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
                serverSocket.sendto(str(str(temp)+" Kilowatt = "+ str(tempK)+" Horsepower").encode(),addr)
                
            elif(opt=="HorsepowerToKilowatt"):
                tempK = float(temp)/1.36
                serverSocket.sendto(str(str(temp)+" Horsepower = "+ str(tempK)+" Kilowatt").encode(),addr)
                
            elif(opt=="DegreesToRadians"):
                tempK = float(temp)*(pi/180)
                serverSocket.sendto(str(str(temp)+" Degrees = "+ str(tempK)+" Radians").encode(),addr)
                
            elif(opt=="RadiansToDegrees"):
                tempK = float(temp)*(180/pi)
                serverSocket.sendto(str(str(temp)+" Radians = "+ str(tempK)+" Degrees").encode(),addr)
                
            elif(opt=="GallonsToLiters"):
                tempK = float(temp)*3.78541
                serverSocket.sendto(str(str(temp)+" Gallons = "+ str(tempK)+" Liters").encode(),addr)
                
            elif(opt=="LitersToGallon"):
                tempK = float(temp)/3.78541
                serverSocket.sendto(str(str(temp)+" Liters = "+ str(tempK)+" Gallons").encode(),addr)
                
        
                
        except ValueError:
            serverSocket.sendto(str("Parametri i dhene duhet te jete numer ne menyre qe te mund te konvertohet").encode(),addr)
    
    def TEMPKONVERTO(fromTo,var):
        try:
            var=float(var)
            if(fromTo=="CelsiusToKelvin"):
                celsius = float(var)+(273.15)
                serverSocket.sendto(str(str(var)+" Celsius = "+ str(celsius)+" Kelvin").encode(),addr)
                            
            elif(fromTo=="KelvinToCelsius"):
                kelvin = float(var)-(273.15)
                serverSocket.sendto(str(str(var)+" Kelvin = "+ str(kelvin)+" Celsius").encode(),addr)
                
        except ValueError:
            serverSocket.sendto(str("Parametri i dhene duhet te jete numer").encode(),addr)

    def RRETHI(rrezja):
        try:
            rr=float(rrezja)
            serverSocket.sendto(str("Perimetri i rrethit me rreze: "+str(rr)+" eshte "+str(2*pi*rr)+" ndersa siperfaqja e tij eshte "+str(pi*rr*rr)).encode(),addr)
            
        except ValueError:
            serverSocket.sendto(str("Parametri i dhene per rrezen duhet te jete numer.").encode(),addr)



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
            serverSocket.sendto(str("Ne nuk e ofrojme kete lloj sherbimi ose nuk e keni specifikuar mire kerkesen tuaj").encode(),addr)
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
                        serverSocket.sendto(str("Numri i serise Fibonacci me indeks: "+str(x)+" eshte: "+str(rez)).encode(),addr)
                        
                    except ValueError:
                        serverSocket.sendto(str("Parametri i dhene duhet te jete numer integjer").encode(),addr)
                if(funks=="RRETHI"):
                    RRETHI(x)                    
            else:
                serverSocket.sendto(str("Nuk keni dhene parametrin shoqerues per funksionin").encode(),addr)
        else:
            serverSocket.sendto(str("Ne nuk e ofrojme kete lloj sherbimi ose nuk e keni specifikuar mire kerkesen tuaj").encode(),addr)
       
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
                        serverSocket.sendto(str("Parametri qe do te konvertohet duhet te jete numer").encode(),addr)
                else:
                    serverSocket.sendto(str("Nuk keni dhene parametrin shoqerues per funksionin").encode(),addr)
            else:
                serverSocket.sendto(str("Nuk ofrojme kete opsion per funksionin perkates ose nuk keni specifikuar si duhet emrin e tij.").encode(),addr)
        else:
            serverSocket.sendto(str("Ne nuk e ofrojme kete lloj sherbimi ose nuk e keni specifikuar mire kerkesen tuaj").encode(),addr)
    else:
        serverSocket.sendto(str("Mund te zgjedhni vetem opsionet ekzistuese ne menu").encode(),addr)

