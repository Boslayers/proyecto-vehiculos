# Cuadro de Mando de Inventario de Vehículos

Este proyecto es una aplicación interactiva desarrollada en **Python** utilizando **Streamlit**. El objetivo principal es proporcionar una herramienta visual para analizar un conjunto de datos sobre anuncios de venta de vehículos en los Estados Unidos.

## Propósito del Proyecto
La aplicación permite a los usuarios explorar rápidamente las tendencias de los datos de vehículos, como la distribución del kilometraje (odómetro) y la relación entre el kilometraje y el precio, facilitando la identificación de patrones y valores atípicos.

## Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Librerías:**
    * `streamlit`: Para la creación de la interfaz web interactiva.
    * `pandas`: Para la manipulación y limpieza de los datos del archivo CSV.
    * `plotly.express`: Para la generación de gráficos dinámicos.

## Datos
El proyecto utiliza el archivo `vehicles_us.csv`, el cual contiene información detallada sobre vehículos, incluyendo:
* **Price:** Precio de venta.
* **Model year:** Año del modelo.
* **Condition:** Estado del vehículo.
* **Odometer:** Kilometraje registrado.
* **Fuel:** Tipo de combustible.

## Instrucciones de Funcionamiento
Para ejecutar este proyecto de forma local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Boslayers/proyecto-vehiculos.git](https://github.com/tu_usuario/proyecto-vehiculos.git)

   ¡Felicidades! Tienes una revisión **excelente**. El revisor prácticamente te dio el visto bueno en todo el código y la estructura, solo te falta un "empujoncito" final con el archivo **README.md**.

Básicamente, el README es la cara de tu proyecto. Quieren que cualquier persona que entre a tu GitHub entienda qué hiciste sin tener que leer todo el código.

Aquí tienes una estructura lista para copiar y pegar en tu archivo `README.md` en VS Code. He incluido los puntos que te pidió el revisor:

---

### Instrucciones:
1. Abre tu archivo `README.md` en VS Code.
2. Borra lo que tenga y pega el siguiente contenido:

```markdown
# Cuadro de Mando de Inventario de Vehículos

Este proyecto es una aplicación interactiva desarrollada en **Python** utilizando **Streamlit**. El objetivo principal es proporcionar una herramienta visual para analizar un conjunto de datos sobre anuncios de venta de vehículos en los Estados Unidos.

## Propósito del Proyecto
La aplicación permite a los usuarios explorar rápidamente las tendencias de los datos de vehículos, como la distribución del kilometraje (odómetro) y la relación entre el kilometraje y el precio, facilitando la identificación de patrones y valores atípicos.

## Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Librerías:**
    * `streamlit`: Para la creación de la interfaz web interactiva.
    * `pandas`: Para la manipulación y limpieza de los datos del archivo CSV.
    * `plotly.express`: Para la generación de gráficos dinámicos.

## Datos
El proyecto utiliza el archivo `vehicles_us.csv`, el cual contiene información detallada sobre vehículos, incluyendo:
* **Price:** Precio de venta.
* **Model year:** Año del modelo.
* **Condition:** Estado del vehículo.
* **Odometer:** Kilometraje registrado.
* **Fuel:** Tipo de combustible.

## Instrucciones de Funcionamiento
Para ejecutar este proyecto de forma local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu_usuario/proyecto-vehiculos.git](https://github.com/tu_usuario/proyecto-vehiculos.git)
   ```
2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   ```
3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar la aplicación:**
   ```bash
   streamlit run main.py
   ```

## Uso de la Aplicación
Una vez lanzada la aplicación en tu navegador:
* Haz clic en el botón **"Construir histograma"** para visualizar la distribución del odómetro de los vehículos.
* Haz clic en el botón **"Construir gráfico de dispersión"** para analizar cómo afecta el kilometraje al precio de venta.

---
Desarrollado por [Juan Felipe Bermúdez Calderón] como parte del Sprint 7 de Tripleten.
```

---

### ¿Qué hacer después de pegar esto?

1.  **Guarda el archivo** (`Ctrl + S`).
2.  **Sube el cambio a GitHub:**
    * `git add README.md`
    * `git commit -m "Mejora del archivo README según revisión"`
    * `git push`
3.  **Verifica en Render:** No necesitas hacer nada más en Render, pero como actualizaste GitHub, Render hará un "deploy" automático. El link seguirá siendo el mismo.

**¡Con esto ya puedes enviar de nuevo tu proyecto y quedarías aprobado!** ¿Hay alguna parte del README que quieras que personalicemos más?