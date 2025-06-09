import preguntas as p


def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    ##global correcto                 se probo variable correcta, comprobando que devuelve OK los False y True.
    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    if alternativas[eleccion][1] == 1:
        print("Respuesta correcta")
        correcto = True
        return correcto
    else:
        print("Respuesta incorrecta")
        correcto = False
        return correcto
    
    
    
    
    ##########################################################################################
    ####return correcto,  no me calza en esta posición el return. y al ser False la condición incorecta se termina el juego, 
    ### esto no me queda tan claro pero hay indicaciones en la pagina 4 que si es incorrecto debe retornar un False.



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)
    ## print(correcto)





