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

1. **Clonar el repositorio:**
   Descarga el código como ZIP o usa git:
   ```bash
   git clone [https://github.com/TU_USUARIO/LingoNod-MVP.git](https://github.com/TU_USUARIO/LingoNod-MVP.git)

2 ## Instalar dependencias: Abre la terminal en la carpeta del proyecto y ejecuta:
Bash
pip install -r requirements.txt

3 ## Ejecutar el servidor:
Bash
python main.py

Abrir en el navegador: Ingresa a: http://localhost:8000
