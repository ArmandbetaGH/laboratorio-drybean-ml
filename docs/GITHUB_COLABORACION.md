# Colaboración y reproducibilidad — Windows y macOS

**Repositorio privado:** `ArmandbetaGH/laboratorio-drybean-ml`.

GitHub permite sincronizar versiones del proyecto, pero **no comparte el entorno Python local**. Cada integrante clona el repositorio y crea su propio entorno `.venv`, excluido mediante `.gitignore`.

## 1. Acceso y clonación

Una vez aceptada la invitación al repositorio privado, ejecutar:

```bash
git clone https://github.com/ArmandbetaGH/laboratorio-drybean-ml.git
cd laboratorio-drybean-ml
```

## 2. Configuración en Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/verificar_modelo_guardado.py
```

## 3. Configuración en macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/verificar_modelo_guardado.py
```

El proyecto se ha probado en Windows con Python 3.12.7 y `scikit-learn 1.6.1`. La ejecución integral en Mac debe comprobarse. Las rutas usadas por el notebook son relativas al proyecto.

## 4. Abrir el notebook

En VS Code, abrir `notebooks/01_laboratorio_drybean.ipynb`, seleccionar el intérprete de `.venv` como kernel y ejecutar de principio a fin. La carga inicial de UCI requiere conexión a Internet.

## 5. Flujo de cambios con ramas

```bash
git switch main
git pull origin main
git switch -c feature/ajuste-documentacion
# Editar los archivos correspondientes
git add .
git commit -m "Mejorar documentación"
git push -u origin feature/ajuste-documentacion
```

Crear un *pull request*, revisar los cambios y fusionarlos en `main`. Conviene acordar previamente quién modifica el `.ipynb`, ya que los conflictos al editar notebooks en paralelo pueden ser difíciles de resolver.

## 6. Buenas prácticas

- No subir `.venv`, cachés, credenciales ni rutas personales.
- Conservar dependencias en `requirements.txt` y validar las pruebas antes de publicar.
- Comprobar formatos, modelos y resultados después de cambios importantes.
- Cargar archivos `.joblib` solo de fuentes confiables; su deserialización puede ejecutar código.
- Separar el registro de tareas Scrum de los hechos personales todavía no acordados.
