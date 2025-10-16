Proyecto Biblioteca – Sistema de Gestión y Pruebas Unitarias

🧠 Desarrollado como ejercicio de calidad de software con enfoque en pruebas automatizadas y cobertura de código.

🏢 Resumen 

El proyecto Biblioteca implementa un sistema modular en Python para la gestión de libros, préstamos y devoluciones.
Su objetivo es demostrar la aplicación de buenas prácticas de desarrollo, incluyendo pruebas unitarias con Pytest y la evaluación de cobertura de código mediante pytest-cov.

El resultado es una base de código confiable, mantenible y evaluable con métricas objetivas.

🎯 Objetivos

✅ Implementar un sistema funcional y escalable.
✅ Garantizar la fiabilidad del código mediante pruebas automatizadas.
✅ Medir el nivel de cobertura del sistema.
✅ Generar reportes visuales de cobertura en formato HTML.

🧰 Tecnologías Utilizadas
Categoría	Herramienta / Librería	Descripción
🐍 Lenguaje	Python 3.11+	Base del sistema
🧪 Testing	pytest	Framework principal de pruebas
📊 Cobertura	pytest-cov	Extensión para medir cobertura
🧱 Entorno	virtualenv / venv	Entorno virtual de desarrollo
🧩 Estructura del Proyecto
biblioteca/
│
├── biblioteca/          # Código fuente principal
│   ├── __init__.py
│   ├── gestor.py
│   └── modelos.py
│
├── tests/               # Carpeta de pruebas unitarias
│   ├── test_modelos.py
│   └── test_gestor.py
│
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación principal

⚙️ Instalación y Configuración
1️⃣ Clonar el Repositorio
git clone https://github.com/usuario/biblioteca.git
cd biblioteca

2️⃣ Crear y Activar el Entorno Virtual
python -m venv venv
# En Linux / macOS:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

3️⃣ Instalar Dependencias
pip install -r requirements.txt

🧪 Ejecución de Pruebas

Ejecutar todas las pruebas con salida detallada:

pytest tests/ -v

📊 Generar Reporte de Cobertura

Para obtener un reporte visual en formato HTML:

pytest tests/ -v --cov=biblioteca --cov-report=html


Abrir el reporte en navegador:

start htmlcov/index.html     # Windows
xdg-open htmlcov/index.html  # Linux
open htmlcov/index.html      # macOS


📈 El reporte muestra el porcentaje de líneas cubiertas, ayudando a identificar áreas no testeadas.

📈 Resultados Estimados
Métrica	Descripción	Objetivo
🔍 Cobertura	Porcentaje de código probado	≥ 90%
⚡ Velocidad de Pruebas	Tiempo total de ejecución	< 2s
🧩 Integridad	Consistencia entre módulos	100%