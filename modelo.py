from datetime import datetime

import pandas as pd
from datasets import load_dataset

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# 1. Cargar el dataset desde Hugging Face
print("Cargando dataset Palmer Penguins...")

dataset = load_dataset("SIH/palmer-penguins", split="train")
df = dataset.to_pandas()

# 2. Seleccionar variables
columnas = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g"
]

X = df[columnas]
y = df["species"]

# 3. Separar entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 4. Comparar profundidades mediante validación cruzada
profundidades = [2, 3, 4, 5, None]

validacion = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

resultados = []

for profundidad in profundidades:
    pipeline = Pipeline([
        ("imputador", SimpleImputer(strategy="median")),
        ("modelo", DecisionTreeClassifier(
            max_depth=profundidad,
            random_state=42
        ))
    ])

    puntuaciones = cross_val_score(
        pipeline,
        X_train,
        y_train,
        cv=validacion,
        scoring="accuracy"
    )

    resultados.append({
        "max_depth": profundidad,
        "exactitud_promedio": puntuaciones.mean(),
        "desviacion": puntuaciones.std()
    })

# Elegir la mejor configuración:
# mayor exactitud, menor desviación y menor profundidad
mejor = sorted(
    resultados,
    key=lambda r: (
        -r["exactitud_promedio"],
        r["desviacion"],
        r["max_depth"] if r["max_depth"] is not None else float("inf")
    )
)[0]

mejor_profundidad = mejor["max_depth"]

# 5. Entrenar el modelo definitivo
modelo_final = Pipeline([
    ("imputador", SimpleImputer(strategy="median")),
    ("modelo", DecisionTreeClassifier(
        max_depth=mejor_profundidad,
        random_state=42
    ))
])

modelo_final.fit(X_train, y_train)

# 6. Evaluar el modelo
y_pred = modelo_final.predict(X_test)

exactitud = accuracy_score(y_test, y_pred)
reporte = classification_report(y_test, y_pred)
matriz = confusion_matrix(y_test, y_pred)

# 7. Obtener importancia de las variables
importancia = pd.DataFrame({
    "variable": columnas,
    "importancia": modelo_final.named_steps["modelo"].feature_importances_
}).sort_values(by="importancia", ascending=False)

# 8. Generar archivo TXT automáticamente
with open("resumen_ejecucion.txt", "w", encoding="utf-8") as archivo:

    archivo.write("RESUMEN DE EJECUCION - MACHINE LEARNING\n")
    archivo.write("=" * 45 + "\n\n")

    archivo.write("PREGUNTA DE NEGOCIO:\n")
    archivo.write(
        "¿Es posible identificar la especie de un pingüino "
        "a partir de sus características físicas?\n\n"
    )

    archivo.write("DATASET:\n")
    archivo.write("SIH/palmer-penguins\n")
    archivo.write(f"Registros: {len(df)}\n")
    archivo.write(f"Columnas: {len(df.columns)}\n\n")

    archivo.write("PREPROCESAMIENTO:\n")
    archivo.write("Variables predictoras: " + ", ".join(columnas) + "\n")
    archivo.write("Variable objetivo: species\n")
    archivo.write("Valores nulos: imputados con la mediana\n")
    archivo.write(f"Registros duplicados: {df.duplicated().sum()}\n")
    archivo.write("Separacion: 80% entrenamiento y 20% prueba\n\n")

    archivo.write("COMPARACION DE PROFUNDIDADES:\n")
    for resultado in resultados:
        archivo.write(
            f"max_depth={resultado['max_depth']}: "
            f"exactitud promedio={resultado['exactitud_promedio']:.4f}, "
            f"desviacion={resultado['desviacion']:.4f}\n"
        )

    archivo.write(f"\nProfundidad seleccionada: {mejor_profundidad}\n\n")

    archivo.write("MODELO:\n")
    archivo.write("Tipo de aprendizaje: Supervisado\n")
    archivo.write("Tipo de problema: Clasificacion multiclase\n")
    archivo.write("Algoritmo: Arbol de decision (DecisionTreeClassifier)\n")
    archivo.write(f"max_depth: {mejor_profundidad}\n")
    archivo.write("random_state: 42\n\n")

    archivo.write("CONFIGURACION DEL ENTRENAMIENTO:\n")
    archivo.write("Division de datos: 80% entrenamiento y 20% prueba\n")
    archivo.write(f"Registros de entrenamiento: {len(X_train)}\n")
    archivo.write(f"Registros de prueba: {len(X_test)}\n")
    archivo.write("Validacion cruzada: 5 particiones estratificadas\n")
    archivo.write("Criterio de evaluacion: exactitud (accuracy)\n")
    archivo.write("Criterio de seleccion: mayor exactitud promedio, "
                  "menor desviacion y menor profundidad\n\n")

    archivo.write("EVALUACION:\n")
    archivo.write(f"Exactitud: {exactitud:.4f}\n\n")
    archivo.write("Reporte de clasificacion:\n")
    archivo.write(reporte)

    archivo.write("\nMatriz de confusion:\n")
    archivo.write(str(matriz) + "\n\n")

    archivo.write("IMPORTANCIA DE LAS VARIABLES:\n")
    archivo.write(importancia.to_string(index=False))
    archivo.write("\n\n")

    archivo.write("FECHA DE EJECUCION:\n")
    archivo.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("\nProceso terminado correctamente.")
print(f"Exactitud del modelo: {exactitud:.4f}")
print(f"Profundidad seleccionada: {mejor_profundidad}")
print("Archivo resumen_ejecucion.txt actualizado.")
