# Función que calcula el seno hiperbolico de un ángulo
# Autor: Felix M. Pormachi Jimenez

def fact(n: int) -> int:
    '''Calcula el factorial de un número entero positivo utilizando recursión.
    
    Args:
        n (int): El número entero positivo del que se desea calcular el factorial.
        
    Returns:
        int: El factorial de n.'''
    
    if n == 0:
        return 1
    
    else:
        return n * fact(n - 1)


def senh(x: float) -> str:
    """
        Calcula el seno hiperbólico de un número utilizando la serie de Taylor.

        Args:
            x (float): El número para el cual se desea calcular el seno hiperbólico.

        Returns:
            str: Una cadena que indica el resultado del cálculo del seno hiperbólico y el error relativo.

        Example:
            >>> senh(1.5)
            'El senh(1.5) = 2.129, con un error de 0.021 %'
        """

    n = int(input('Ingrese la cantidad de iteraciones: '))
    suma_actual = 0
    suma_anterior = 0

    for i in range(n+1):

        #Utilizamos serie de Taylor
        suma_actual += x ** (2 * i + 1) / fact(2 * i + 1) 
        err = abs((suma_actual - suma_anterior) * 100 / suma_actual)

        if i > 0:
            suma_anterior += x ** (2 * (i - 1) + 1) / fact(2 * (i - 1) + 1)

        else:
            suma_anterior = 0

    print(f'El senh({x}) = {suma_actual:.3f}, con un error de {err}')


x = float(input('Ingrese un angulo: '))
senh(x)


