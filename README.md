# Taller3-MLOps-MLFlow

Pasos para ejecutar el proyecto

1. Descargar el repositorio
Clona el repositorio utilizando el siguiente comando: git clone git@github.com:carmenca7/Taller3-MLOps-MLFlow.git

2. Entrar a la carpeta del proyecto
Cambia al directorio del proyecto descargado: cd Taller3-MLOps-MLFlow/

3. Crear un entorno virtual
Crea un entorno virtual para gestionar las dependencias de manera aislada: python3 -m venv mlflow

4. Activar el entorno virtual
Activa el entorno virtual creado en el paso anterior: source mlflow/bin/activate

5. Instalar dependencias
Instala todas las dependencias necesarias especificadas en el archivo requirements.txt:
pip install -r requirements.txt

6. Ejecutar los archivos del proyecto
Ejecuta cada archivo del repositorio de la siguiente forma: python nombre_archivo.py
Asegúrate de reemplazar nombre_archivo.py con el nombre del archivo que deseas ejecutar.

7. Visualizar los resultados en MLflow
Ejecuta el siguiente comando para iniciar la interfaz gráfica de MLflow y visualizar los resultados:mlflow ui
Esto abrirá un servidor local de MLflow. Puedes acceder a la interfaz a través de tu navegador en http://localhost:5000.
