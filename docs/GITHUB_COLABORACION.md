# Colaboración con GitHub — Windows y macOS

## 1. Concepto
GitHub es el **repositorio compartido**, no un entorno Python compartido.
Cada persona clona los archivos y crea su propio `.venv` (excluido por `.gitignore`).
Los resultados académicos y datos versionables sí quedan en el repositorio.
Se utiliza el repositorio privado **`ArmandbetaGH/laboratorio-drybean-ml`**, independiente del Taller de Series. La invitación a la compañera se hará cuando el equipo haya terminado los ajustes.

## 2. Repositorio ya creado y publicado desde Windows
El repositorio ya fue inicializado, conectado a `origin` y publicado con el primer commit. **No repetir `git init` ni `git remote add origin` en la copia local actual.** Para la siguiente actualización, conservar la carpeta `.git` y hacer cambios sobre los archivos existentes.

Como referencia, el procedimiento inicial fue:
- Crear `laboratorio-drybean-ml` como repositorio privado y vacío.
- Desde la carpeta raíz, realizar el commit inicial y conectar el remoto:

```bash
git init
git branch -M main
git add .
git commit -m "Inicio laboratorio Dry Bean: CRISP-DM, TDSP y Scrum ML"
git remote add origin https://github.com/ArmandbetaGH/laboratorio-drybean-ml.git
git push -u origin main
```

Si se creó un repositorio con README automático, el remoto ya tendrá un commit; es preferible
crear uno vacío para evitar reconciliar historiales en este primer paso.

## 3. Aplicar actualizaciones en tu copia Windows
1. Descargar la actualización de la fase 2 y extraerla manteniendo sus rutas (`docs/`, `scripts/`, `src/`, etc.) encima de la carpeta existente, **sin borrar `.git`**.
2. En VS Code revisar cambios con `git status`, ejecutar pruebas y solo entonces confirmar y enviar al repositorio.

```powershell
python scripts/generar_reporte_calidad.py
python -m pytest -q
git status
git add .
git commit -m "CRISP-DM fase 2: analisis de calidad de datos"
git push origin main
```

Si las dependencias no están instaladas, crear el entorno virtual del apartado Windows antes de correr las pruebas.

## 4. Clonar en macOS (compañera)
1. Aceptar la invitación en *Settings > Collaborators* de GitHub si el repositorio es privado.
2. Abrir terminal y ejecutar (usar la URL real visible en GitHub > Code):

```bash
git clone https://github.com/ArmandbetaGH/laboratorio-drybean-ml.git
cd laboratorio-drybean-ml
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/verificar_estructura.py
python -m pytest -q
python -m jupyter lab
```

Se recomienda Python **3.10, 3.11 o 3.12**, no Python 3.13 sin antes verificar compatibilidades.
Con conexión a Internet, abrir `notebooks/01_laboratorio_drybean.ipynb` y ejecutar desde el inicio.
El notebook utiliza rutas relativas del proyecto, no rutas de macOS o Windows.

## 5. Windows (propietario)
En PowerShell abierto en la carpeta del proyecto:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python scripts/verificar_estructura.py
python -m pytest -q
python -m jupyter lab
```

`py -3.11` es un ejemplo: si no está instalado, usar una versión compatible disponible.
Si PowerShell impide la activación, abrir **CMD** y usar `.venv\Scripts\activate.bat`.
No subir el entorno virtual al repositorio.

## 6. Flujo para trabajar en equipo (como en Series)
Cada integrante trabaja desde una rama propia, sube los cambios y crea un Pull Request
para revisarlos antes de fusionarlos a `main`.

```bash
git switch main
git pull origin main
git switch -c feature/documentacion-crispdm
# Editar y guardar archivos
git add .
git commit -m "Documenta comprensión del negocio"
git push -u origin feature/documentacion-crispdm
```

En GitHub, abrir **Compare & pull request** > revisar > fusionar a `main`.
Para actualizar el clon local después de la fusión:

```bash
git switch main
git pull origin main
```

**Muy importante:** eviten modificar simultáneamente el mismo `.ipynb` en ramas diferentes;
los conflictos en notebooks son difíciles de resolver. Una persona puede encargarse del
notebook y otra de `docs/`, `scrum/` o `README.md`.

## 7. ¿Qué se sincroniza y qué no?

Se sincroniza: `src/`, `notebooks/`, `docs/`, `scrum/`, `data/processed/`,
`outputs/`, `README.md`, `.gitignore`, `.gitattributes`, `requirements.txt`.
No se sincroniza: `.venv/`, cachés, `.DS_Store`, archivos temporales o credenciales.

Los `.joblib` tienen riesgos de carga por usar serialización pickle: abrir solamente
artefactos de origen confiable. Para usar el modelo original se debe comprobar
compatibilidad de librerías; lo más robusto es regenerarlo ejecutando el notebook
con dependencias acordadas.

## 8. Validaciones antes del Pull Request

```bash
python scripts/verificar_estructura.py
python -m pytest -q
```

Estos comandos verifican estructura y datos almacenados, **no** sustituyen
la ejecución completa del notebook. Los integrantes deben verificar por separado
que éste pueda ejecutarse de principio a fin en el entorno elegido.
