import os
print(':::IMPORTANTE:::   USE AS LETRAS CORRESPONDENTES => C (CESIUS), K (KELVIN) OU F (FIRENHEIT)\n\n')
temp = input('Qual temperatura quer saber? ')
tv = float(input('Digite o valor da temperatura: '))

if(temp == 'c'):
    fah = ((tv * 1.8) + 32)
    kel = (tv + 273.15)
    cel = tv
    print('Fahrenheit {}\nKelvin {}\nCelsius {:.0f}' . format(fah,kel,cel))

if(temp == 'k'):
    fahk = ((tv * 1.8) - 459.7)
    kelk = (tv - 273.15)
    celk = tv
    print('Fahrenheit {}\nCelsius {}\nKelvin {:.0f}' . format(fahk,kelk,celk))

if(temp == 'f'):
    fpk = ((tv + 459.67) * 5/9)
    fpc = ((tv - 32) / 1.8)
    celf = tv
    print('Kelvin {}\nCelsius {}\nFahrenheit {:.0f}' . format(fpk,fpc,celf))
    
os.system('Pause')
