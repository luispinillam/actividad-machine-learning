Clasificación de especies de pingüinos con Machine Learning

1. Descripción del proyecto

Este proyecto busca desarrollar un modelo de Machine Learning que permita identificar la especie de un pingüino a partir de sus características físicas. Para esto se utiliza el dataset Palmer Penguins, obtenido directamente desde Hugging Face mediante Python.

El proyecto utiliza un algoritmo de aprendizaje supervisado llamado Árbol de Decisión, que permite clasificar los pingüinos en tres especies: Adelie, Chinstrap y Gentoo.

2. Pregunta de negocio

¿Es posible identificar la especie de un pingüino a partir de sus características físicas para apoyar el trabajo de investigadores y equipos de monitoreo de fauna silvestre?

3. Dataset utilizado

    Nombre: Palmer Penguins.
    Identificador: SIH/palmer-penguins.
    Fuente: Hugging Face - Palmer Penguins.
    Cantidad de registros: 344.
    Cantidad de columnas: 8.

El dataset contiene información sobre diferentes características de los pingüinos, como las dimensiones de sus picos, la longitud de sus aletas, su masa corporal y su especie.

4. Variables utilizadas

Se seleccionaron cuatro variables predictoras:

    bill_length_mm: longitud del pico.
    bill_depth_mm: profundidad del pico.
    flipper_length_mm: longitud de las aletas.
    body_mass_g: masa corporal.

La variable objetivo es species, que representa la especie del pingüino. Las demás columnas no se utilizaron en esta primera versión del modelo.

5. Preprocesamiento de los datos

Durante el análisis exploratorio se encontraron valores nulos en algunas características físicas y no se encontraron registros duplicados.

Para preparar los datos se realizaron los siguientes procedimientos:

    Se seleccionaron las cuatro características físicas.
    Los valores nulos se reemplazaron utilizando la mediana.
    Se dividieron los datos en 80 % para entrenamiento y 20 % para prueba.
    Se utilizó una semilla aleatoria de 42 para mantener la reproducibilidad.
    No se aplicó normalización, debido a que los árboles de decisión no requieren escalado de las variables.

6. Algoritmo utilizado: Árbol de Decisión

Se utilizó el algoritmo DecisionTreeClassifier de la biblioteca Scikit-learn.

Este algoritmo pertenece al aprendizaje supervisado y permite clasificar información mediante una estructura de decisiones. Funciona realizando preguntas sobre las características de los datos y dividiéndolos en grupos hasta obtener una clasificación.

En este proyecto, el árbol analiza las dimensiones del pico, la longitud de las aletas y la masa corporal para determinar a qué especie pertenece cada pingüino.

Parámetros del modelo

    max_depth=4: limita la profundidad del árbol para controlar su complejidad.
    random_state=42: permite reproducir los resultados.

Se compararon diferentes profundidades mediante validación cruzada de cinco particiones. Se seleccionó una profundidad de 4, que obtuvo una exactitud promedio de 95.64 % y una desviación de 0.0272. Esta profundidad permite mantener un buen rendimiento y controlar la complejidad del árbol.

Ventajas

    Es fácil de comprender e interpretar.
    Permite trabajar con variables de diferentes escalas.
    Puede identificar relaciones entre las características y las especies.

Limitaciones

    Puede presentar sobreajuste si el árbol crece demasiado.
    Sus resultados pueden variar dependiendo de los datos utilizados.
    Una clasificación incorrecta puede ocurrir cuando dos especies tienen características físicas similares.

Funcionamiento del árbol de decisión paso a paso

    El modelo recibe las características físicas de cada pingüino: longitud y profundidad del pico, longitud de las aletas y masa corporal.
    El algoritmo analiza estas características y busca divisiones que permitan separar los datos según la especie.
    Organiza las decisiones en nodos y ramas, creando diferentes caminos de clasificación.
    Se establece una profundidad máxima de 4 para limitar el crecimiento del árbol.
    Finalmente, cada hoja representa una predicción de la especie: Adelie, Chinstrap o Gentoo.

7. Resultados de la evaluación

El modelo definitivo obtuvo una exactitud de 98.55 % sobre los datos de prueba, clasificando correctamente 68 de los 69 registros.

Métricas por especie

Especie                 Precision               Recall              F1-score

Adelie                  1.00                    0.97                0.98

Chinstrap               1.00                    1.00                1.00

Gentoo                  0.96                    1.00                0.98

Matriz de confusión

[[29  0  1]
 [ 0 14  0]
 [ 0  0 25]]

La matriz muestra que el modelo clasificó correctamente 29 pingüinos Adelie, 14 Chinstrap y 25 Gentoo. Solamente un pingüino Adelie fue clasificado incorrectamente como Gentoo.

8. Importancia de las variables

El análisis de importancia permitió identificar cuáles características aportaron más información para la clasificación:

Variable e Importancia

    Longitud de las aletas: 53.91 %

    Longitud del pico: 35.42 %

    Profundidad del pico: 7.06 %

    Masa corporal: 3.61 %

La longitud de las aletas fue la variable más importante, seguida por la longitud del pico.

9. Conclusiones

Los resultados muestran que es posible identificar las especies de pingüinos utilizando sus características físicas y un modelo de Árbol de Decisión. La exactitud obtenida fue de 98.55 %, lo que representa un buen desempeño en los datos de prueba.

También se encontró que la longitud de las aletas y la longitud del pico fueron las características que más contribuyeron a la clasificación. Sin embargo, el modelo no es completamente infalible y sería conveniente probarlo con más datos para comprobar su comportamiento en otros registros.

10. Tecnologías utilizadas

    Python.
    Jupyter Notebook.
    Pandas.
    NumPy.
    Matplotlib.
    Seaborn.
    Hugging Face Datasets.
    Scikit-learn.
    Git y GitHub.

11. Ejecución del proyecto

    Clonar el repositorio.
    Crear y activar un entorno virtual.
    Instalar las dependencias.
    Abrir el notebook actividad-machine-learning.ipynb.
    Ejecutar las celdas en orden.

Para instalar las dependencias se utilizará:

    pip install -r requirements.txt

El archivo resumen_ejecucion.txt contiene los resultados de la ejecución del modelo y se genera mediante código Python.