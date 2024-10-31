
---
- Libro: *Dennis Zill cap. 11 pag. 397*
---
# Definición

Las **series de Fourier** surgen de la necesidad de descomponer **funciones periódicas** complejas en componentes más simples y manejables. La idea central es que cualquier función periódica, sin importar su forma, puede representarse como una suma infinita de funciones seno y coseno, que son fáciles de manipular matemáticamente, y permiten analizar y entender el comportamiento de señales y fenómenos periódicos de manera más clara y eficiente.

Son un caso específico de **[Series Ortogonales](obsidian://open?vault=Apunte-AM2&file=1%20-%20Series%20Ortogonales)** donde las funciones ortogonales son funciones trigonométricas (seno y coseno).

**Coeficientes de Fourier:** Los coeficientes **a0​, an​ y bn**​ son esenciales para determinar cómo se descompone la función **𝑓(x)** en términos de senos y cosenos:

- **a0​**​ representa el valor medio de la función.
- **an​ y bn** determinan la amplitud de las funciones seno y coseno correspondientes para cada frecuencia **n**.
## Desarrollo de Fourier

![[img_def_series_de_Fourier.png]]

El miembro derecho de la ecuación (8) tiene periodo **2p**; en realidad, **2p** es el **periodo fundamental** de la suma. Entonces, una **serie de Fourier** no sólo representa la función en el intervalo **(-p, p)**, sino que también da la **extensión periódica** de **𝑓(x)** fuera de este intervalo.
### Desarrollo para funciones con periodo 2π

Cuando la función **𝑓(x)** es periódica con un período de **2π**, la serie de Fourier se reduce a:

![[img_formula_serie_de_Fourier_periodo_dos_pi.png]]
![[img_formula_a0_periodo_dos_pi.png]]![[img_formula_an_periodo_dos_pi.png]]![[img_formula_bn_periodo_dos_pi.png]]
### Desarrollo de series de Cosenos y Senos

El calculo de los coeficientes a0, an y bn al desarrollar una función **𝑓(x)** en una serie de Fourier se reduce significativamente cuando **𝑓(x)** es par o impar.

* Par si **𝑓(-x) = 𝑓(x)**
* Impar si **𝑓(-x) = -𝑓(x)**

En un intervalo simétrico tal como (-p, p), la gráfica de una función par tiene simetría respecto al eje y, mientras que la de una función impar tiene simetría respecto al origen.

El siguiente listado de propiedades nos ayuda a simplificar los cálculos de los coeficientes:

![[img_propiedades_funciones_pares_impares.png]]

![[img_serie_de_cosenos.png]]
![[img_serie_de_senos.png]]
## Convergencia de la serie de Fourier

![[img_condiciones_convergencia_serie_de_fourier.png]]
### Ejemplo

![[img_funcion_ejemplo_convergencia_fourier.png]]

La función satisface las condiciones del teorema. Así, para todo x del intervalo **(-π, π)** excepto en **x = 0**, la serie convergerá a **𝑓(x)**. En **x = 0** la función es discontinua, por lo que la serie convergerá a:

![[img_funcion_ejemplo_convergencia_fourier_punto_medio.png]]
![[img_funcion_ejemplo_convergencia_fourier_grafico.png]]

![[img_funcion_ejemplo_convergencia_fourier_grafico_serie.png]]
## Interpretación Geométrica

Tomando como ejemplo la siguiente función definida en el intervalo **(-π, π)**:

![[img_funcion_ejemplo_convergencia_fourier.png]]
![[img_funcion_ejemplo_interpretacion_fourier_grafico.png]]

Donde, luego de realizar los cálculos, resulta que la serie de Fourier que aproxima esta función es:

![[img_funcion_ejemplo_interpretacion_fourier_serie.png]]

Vemos cómo se aproxima la sucesión de sumas parciales de una serie de Fourier a esta función:

![[img_funcion_ejemplo_interpretacion_fourier_grafico_series.png]]
## Aplicaciones

* **Análisis de señales**: Para descomponer señales complejas en frecuencias simples.

+ **Ecuaciones diferenciales**: Especialmente en problemas de condiciones de frontera.

+ **Física y Electrotecnia**: Para modelar fenómenos periódicos como vibraciones, ondas y señales eléctricas.
---
## Ejemplos
### Ejemplo 1

Aproximación de la función 𝑓(x) = x definida en los intervalos **\[-pi, pi]**.

![[img_serie_de_fourier_ejemplo1.png]]
### Ejemplo 2

Aproximación de una función por tramos.

![[img_serie_de_fourier_ejemplo2.png]]

---

#### Enlaces
- 