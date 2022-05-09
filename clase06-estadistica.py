
import matplotlib.pyplot as plt
import numpy as np  
from scipy import stats 
import seaborn as sns 


#funciones de distribucion discreta


#----------------------------------------------------------------------------------------------------------------------------------------------
#? p= probabilidad de éxito.<br>
#? q= Probabilidd de fracaso.<br>
#? n= espacio muestral.<br>
#? k= número de éxitos
from math import factorial
def funcion_binomial(k,n,p):
  num_exitos = factorial(n) #Factorial de la cantidad de casos de éxito buscados.
  num_eventos = factorial (k) * factorial(n-k) #Factorial del espacio muestral.
  exitos_fracaso=pow(p,k) * pow(1-p,(n-k)) # Probabilidad de exitos y fracasos.

  binomial = (num_exitos / num_eventos) * exitos_fracaso #Aplicación de la función binomial.

  return binomial

print(funcion_binomial(4,5,0.5))

#sirve cuando tenemos un suceso que tiene cierta probabilidad y se repite un numero n de veces
# por ejemplo la probabilidad de que salga 1 cara en 5 lanzamientos de una moneda

#----------------------------------------------------------------------------------------------------------------------------------------------

from math import e,factorial

def probabilidad_poisson(lamba_np,x):
     probabilidad = (pow(e,-lamba_np) * pow(lamba_np,x))/factorial(x)
     return probabilidad

# nos sirve cuando dentro de un marco temporal, existe una media pero se desea calcular la probabilidad de otro valor
# ejemplo, en un taller llega una media de 10 autos al dia, cual es la probabilidad de que en un dia lleguen 5

print(probabilidad_poisson(5,2))


#----------------------------------------------------------------------------------------------------------------------------------------------
#hipergeometrica


from math import e,factorial

# N ES LA POBLACION
# X ES LA CANTIDAD DE CASOS FAVORABLES DE
# n es la muestra
# x es los casos favorables de la muestra



N,X,n,x= 80,30,9,2

Xx = factorial(X)/(factorial(x)*factorial(X-x))
NX_nx= factorial(N-X)/(factorial(n-x)*factorial((N-X)-(n-x)))
Nn = factorial(N)/(factorial(n)*factorial(N-n))

probabilidad_hipergeometrica = (Xx * NX_nx)/Nn

print(probabilidad_hipergeometrica)


#----------------------------------------------------------------------------------------------------------------------------------------------

# Graficando Normal
'''
mu, sigma = 0, 0.2 # media y desvio estandar
normal = stats.norm(mu, sigma)
x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
fp = normal.pdf(x) # Función de Probabilidad
plt.plot(x, fp)
plt.title('Distribución Normal')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
''' 
#estandarizacion
# z = (x-mu)/sigma
















