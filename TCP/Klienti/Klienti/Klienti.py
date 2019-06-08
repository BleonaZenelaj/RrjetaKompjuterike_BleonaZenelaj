import socket
import string
import sys

print('**********************************MENU*********************************')
print('')
print('Shtypni njeren nga komandat e meposhtme ne menyren e shfaqur ne manual!')
print('IPADRESA - \t\tIP adresa e klientit')
print('NUMRI I PORTIT - \t\tPorti i klientit') 
print('BASHKETINGELLORE - \tNumri i bashketingelloreve ne tekst') 
print('PRINTIMI - \tFjalia e derguar') 
print('EMRIIKOMPJUTERIT - \t\tEmri i kompjuterit') 
print('KOHA- \t\tKoha aktuale ne server') 
print('LOJA - \t\t7 numra nga rangu[1,49]') 
print('FIBONACCI - \tGjen numrin perkates nga seria Fibonacci ku parametri hyres paraqet indeksin e atij numri')
print('KONVERTIMI - \tKonvertimi i temperatures varesisht opsionit te zgjedhur: \n\t\t\t1.KilowattToHorsepower\n\t\t\t2.HorsepowerToKilowatt\n\t\t\t3.DegreesToRadians\n\t\t\t4.RadiansToDegrees\n\t\t\t5.GallonsToLiters\n\t\t\t6.LitersToGallons')
print('TEMPKONVERTO- \tKonvertimi nga Kelvin ne Celsius dhe anasjelltas sipas opsionit te zgjedhur: \n\t\t\t1.KelvinToCelsius(per konvertimin nga kelvin ne celsius)\n\t\t\t2.CelsiusToKelvin(per konvertimin nga celsius ne kelvin)')
print('RRETHI- \tGjetja e perimetrit dhe siperfaqes se rrethit me rreze te dhene si parameter')
print('')

change=input("Deshironi te percaktoni portin e komunikimit me serverin?\nPergjigjuni me PO ose JO: ")

if(change.lower()=="po"):
    while True:
        serverPort=input("Jepni numrin per portin: ")
        try:
            serverPort=int(serverPort)
            break
        except ValueError:
            print("Vlera e dhene per portin duhet te jete numer integjer (i plote)")
elif(change.lower()=="jo"):
    serverPort = 12000
    print("Vlera e nenkuptuar per portin do te jete 12000")


serverName = "localhost"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((serverName,int(serverPort)))

a=True
while a:
    

    var = input("Jeni lidhur me serverin.\nPer te mbyllur linjen shtypni C. Perndryshe zgjidhni ndonje nga opsionet e menuse me larte: ")
    if(var.lower()=="c"):
        print('Lidhja eshte mbyllur')
        a=False
        s.close()
    else:
        if(var==""):
            print("Nuk keni specifikuar asnje kerkese.")
        else:
            s.sendall(str(var).encode())
            data = s.recv(128).decode()
            print('Te dhenat e pranuara nga serveri: '+ repr(data))
            
    
