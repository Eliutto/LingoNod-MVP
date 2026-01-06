# LingoNod MVP
**Plataforma de Asistencia Multilingüe para Retail y Hostelería**

### Autores
**Proyecto realizado por:**
* **Jhonny Alberto Cotrina Buitrago**
* **Gerson Eliut Torrado Guerrero**

**Asignatura:** Creatividad y Pensamiento Innovador (Código 55597)
**Docente:** Hugo Herley Malaver Guzmán
**Institución:** Corporación Unificada Nacional de Educación Superior (CUN)

Este proyecto es un prototipo funcional (MVP) desarrollado como parte de la **Actividad de Construcción Aplicada (ACA 3)**. Permite la traducción bidireccional en tiempo real entre Cajeros (Español) y Clientes (Inglés) utilizando Python y Servicios Cognitivos.

## Características
- **Traducción en Tiempo Real:** Comunicación fluida usando `deep-translator`.
- **Modo Walkie-Talkie:** Lógica anti-eco para evitar repeticiones.
- **Gestión de Roles:** Acceso diferenciado para Cajeros y Supervisores.
- **Reportes:** Historial de traducciones exportable en pantalla.
- **Interfaz Web:** Diseño responsivo con Bootstrap.

## Tecnologías Usadas
- **Backend:** Python 3.10+, FastAPI.
- **Frontend:** HTML5, JavaScript (Web Speech API), Bootstrap 5.
- **Librerías:** `deep-translator`, `uvicorn`, `jinja2`.

## ¿Cómo ejecutarlo localmente?

Sigue estos pasos para probar el proyecto en tu máquina:

## Prerrequisitos: Asegúrate de tener Python instalado.

1. Clonar el repositorio
Descarga el código o usa git:

Bash
https://github.com/Eliutto/LingoNod-MVP.git

2. Crear y activar un entorno virtual (Recomendado)
Esto aísla las librerías del proyecto para evitar errores con tu sistema.

En Windows:

PowerShell

python -m venv venv
.\venv\Scripts\activate

(Si ves (venv) al inicio de la línea, ya está activo).

En macOS / Linux:

Bash

python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias
Una vez activado el entorno virtual, instala lo necesario:

Bash

pip install -r requirements.txt
4. Ejecutar el servidor

Inicia la aplicación:

Bash

python main.py

5. Abrir en el navegador

Ingresa a: http://localhost:8000
