
try:
    veces = int( input (" Cuántas veces quieres repetir la serie: " ) )

    if veces <= 0:
        raise Exception("El número debe ser mayor que cero")

    resultado = 0
    signo = 1
    i = 1

    for x in range(veces):
        resultado =  resultado  +  signo  *  ( 1 / i )
        i  =  i  +  2
        signo = signo * -1

    pi_aprox = 4 * resultado
    print ( " Aproximación de pi:", pi_aprox)

except ValueError:
    print (" Error: Ingresa un número válido" )

except Exception as  e :
    print( " Ocurrió un error: ", e)

