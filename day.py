curso="FCT NAHID" 
dias=20
print( "Bienvenido al curso",curso ,"Duracion",dias)
'''anio_nacimiento=input("cuantos años tienes ?")
anio_num_nac=int(anio_nacimiento)
anio_estamos=input("En que año estamos ?")
anio_num_est=int(anio_estamos)
edad=anio_num_est-anio_num_nac
print("Tienes",edad,"años")'''
'''if(anio_num_nac <18):
   print("Lo siento eres un menor de edad no puedes pasar")

elif(anio_num_nac>65):
    print("Adelante,pase vip gratis")
    
else:
    print("Adelante eres mayor de edad")  ''' 
    
pizza=[] 
precio=10
ingrediente=""
while(ingrediente!="fin") :  
    ingrediente= input("Que ingrediente quieres añadir:")
    if(ingrediente!="fin"):
      pizza.append(ingrediente)  
      precio=precio+2   
print("Añadido",",".join(pizza),".PrecioActual:",precio) 