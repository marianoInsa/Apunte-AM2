import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Configuración
L = np.pi         # Periodo de la función (ajusta esto según la función a aproximar)
N_values = [1, 5, 10, 20]    # Número de términos en la serie de Fourier
x = np.linspace(-L, L, 500)

# Funcion con 4 tramos
def funcion_a_aproximar(x):
    return np.where(
        x < -L/2, -1,                            # Tramo 1: devuelve -1
        np.where(
            (-L/2 <= x) & (x < 0), x + 1,        # Tramo 2: devuelve x + 1
            np.where(
                (0 <= x) & (x < L/2), 1 - x,     # Tramo 3: devuelve 1 - x
                1                                # Tramo 4: devuelve 1
            )
        )
    )

# def funcion_a_aproximar(x):
#     return np.where(
#         (-L <= x) & (x < 0), x,
#         np.where(
#             (0 <= x) & (x < L), x,
#             np.nan
#         )
#     )
  
# funcion_a_aproximar_vec = np.vectorize(funcion_a_aproximar)

# Cálculo de los coeficientes a0, an, bn de Fourier
def calcular_coeficientes_fourier(func, L, num_terms):
    a0 = (1 / L) * quad(lambda x: func(x), -L, L)[0]
    an = []
    bn = []

    for n in range(1, num_terms + 1):
        an_n = (1 / L) * quad(lambda x: func(x) * np.cos(n * np.pi * x / L), -L, L)[0]
        bn_n = (1 / L) * quad(lambda x: func(x) * np.sin(n * np.pi * x / L), -L, L)[0]
        an.append(an_n)
        bn.append(bn_n)

    return a0, an, bn

# Aproximación de la función mediante la serie de Fourier
def aproximacion_fourier(x, a0, an, bn, L):
    f_aprox = a0 / 2
    for n in range(1, len(an) + 1):
        f_aprox += an[n-1] * np.cos(n * np.pi * x / L) + bn[n-1] * np.sin(n * np.pi * x / L)
    return f_aprox

# a0, an, bn = calcular_coeficientes_fourier(funcion_a_aproximar, L, num_terms)
# f_aprox = aproximacion_fourier(x, a0, an, bn, L)

# Graficar la función original y la aproximación de Fourier
plt.figure(figsize=(10, 6))
plt.plot(x, funcion_a_aproximar(x), label="Función original", color='blue')

# plt.plot(x, f_aprox, label=f'Aproximación de Fourier con {num_terms} términos', color='red')
for num_terms in N_values:
    a0, an, bn = calcular_coeficientes_fourier(funcion_a_aproximar, L, num_terms)
    f_aprox = aproximacion_fourier(x, a0, an, bn, L)
    plt.plot(x, f_aprox, label=f'Aproximación de Fourier N={num_terms}')

plt.xlabel("x")
plt.ylabel("f(x)")
# plt.xlim(-L, L)
# plt.ylim(-2, 2)
plt.legend()
plt.title("Aproximación de funciones con series de Fourier")
plt.grid(True)
plt.show()
