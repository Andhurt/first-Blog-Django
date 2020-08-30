if 5 < 2:
    print('5 is indeed greater than 2')
else:
    print('5 is not greater than 2')

name = 'Andrés'
if name == 'Ola':
    print('Hey Ola!')
elif name == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey '+name+'!')

volume = 1000
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("Me duelen las orejas! :(")

# Cambiar el volumen si esta muy alto o muy bajo
if volume < 20 or volume > 80:
    volume = 50
    print("Mucho mejor!")

def hi():
    print('Hi there!')
    print('How are you?')

hi()

def imprime_Saludo(nombre):
    print("Hola! "+nombre)

imprime_Saludo("Andrés Huertas")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for girlName in girls:
    imprime_Saludo(girlName)

for i in range(1, 6):
    print(i)