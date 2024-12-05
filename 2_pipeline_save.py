# -*- coding: utf-8 -*-
"""2_pipeline_save.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15FNnGGACyLQV4RUyxZz6dU2YqAOxQoFw
"""

import mlflow.sklearn
import mlflow.pycaret
from pycaret.regression import save_model, load_model

# Guardar el modelo final con PyCaret
best_model = load_model("best_model")
model_path = "pipeline_model"

# Guardar el modelo como pipeline con MLflow
mlflow.sklearn.save_model(
    sk_model=best_model,
    path=model_path
)

print(f"Modelo guardado en la ruta: {model_path}")

# Cargar el modelo desde MLflow
loaded_model = mlflow.sklearn.load_model(model_path)
print("Modelo cargado exitosamente desde MLflow")

# Usar el modelo cargado para predicciones
example_data = [[0.5, 0.3, 0.2]]
prediction = loaded_model.predict(example_data)
print(f"Predicción del modelo: {prediction}")