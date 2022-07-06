#Determinar frecuencia de cada letra en la palabra
frase = " ¡Proyecto Numero 2, Principios de Comunicaciones Otoño 2022 EL4112! Modulación digital M-FSK."

print ("\n\n.....................CODIFICANDO................\n\n")
mensaje = "¡Proyecto Numero 2, Principios de Comunicaciones Otoño 2022 EL4112! Modulación digital M-FSK."
mensaje="holo"
print ("\n\nTotal de simbolos: \n\n %s"% (len(mensaje)))
simbolos=''
probabilidad=[]
msm=mensaje
d=0

for i in mensaje:
    if i in msm:
        simbolos+=i
        probabilidad.append(float(float ( msm.count(i))/float(len(mensaje))))
        msm=msm.replace(i,'')
        d+= 1

symbols=dict(zip(simbolos, probabilidad))
print ("\n\nSimbolos comprimidos: \n\n",d)
print ("\n\nPROBABILIDAD DE CADA SIMBOLO:\n\n ", symbols)
