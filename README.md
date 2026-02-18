# Vision Transformer (ViT) — Trabajo de Fin de Máster

**Autor:** Diego Del Río Rodríguez  
**Repositorio:** [diegoodelrio/ViT-Master-Tesis](https://github.com/diegoodelrio/ViT-Master-Tesis)

---

## 📄 Descripción

Este repositorio contiene todo el material asociado al Trabajo de Fin de Máster (TFM) de Diego Del Río Rodríguez, centrado en el estudio, implementación y evaluación de **Vision Transformers (ViT)** aplicados a tareas de visión por computador.

Los Vision Transformers son arquitecturas basadas en el mecanismo de atención (*self-attention*) originalmente propuesto para procesamiento de lenguaje natural (NLP), adaptadas para trabajar directamente sobre imágenes dividiéndolas en parches (*patches*) que son tratados como secuencias de tokens.

---

## 📁 Estructura del Repositorio

```
ViT-Master-Tesis/
│
├── Diego_DelRio_Rodriguez_TesisColab/   # Notebooks de Google Colab con los experimentos
├── main/                                # Scripts Python principales del proyecto
│
├── Diego_DelRio_Rodriguez_Tesis.pdf           # Documento completo de la tesis
├── Diego_DelRio_Rodriguez_PresentacionCorta.pptx  # Presentación resumida
├── Diego_DelRio_Rodriguez_PresentacionLarga.pptx  # Presentación detallada
└── README.md
```

---

## 🧪 Contenido Principal

### Notebooks (Google Colab)
La carpeta `Diego_DelRio_Rodriguez_TesisColab/` contiene los cuadernos Jupyter con los experimentos realizados a lo largo de la investigación. Están diseñados para ejecutarse en Google Colab, aprovechando el acceso a GPUs para el entrenamiento de modelos.

### Scripts Python
La carpeta `main/` incluye los scripts Python con la implementación modular del proyecto, permitiendo entrenar y evaluar los modelos de forma reproducible.

### Documento de Tesis
El archivo `Diego_DelRio_Rodriguez_Tesis.pdf` contiene la memoria completa del TFM, incluyendo el marco teórico, la metodología, los experimentos y las conclusiones.

### Presentaciones
Se incluyen dos versiones de la presentación del trabajo:
- **Presentación Corta:** versión condensada para defensas o exposiciones breves.
- **Presentación Larga:** versión extendida con mayor detalle técnico y experimental.

---

## 🛠️ Tecnologías Utilizadas

- **Python** — lenguaje de programación principal
- **Jupyter Notebooks** — entorno de experimentación interactivo
- **Google Colab** — plataforma de ejecución con soporte GPU
- **PyTorch / TensorFlow** *(según implementación)* — frameworks de deep learning
- **Vision Transformer (ViT)** — arquitectura principal investigada

---

## 🚀 Cómo Usar

### Requisitos Previos

```bash
pip install torch torchvision timm numpy matplotlib scikit-learn
```

### Ejecutar los Notebooks en Google Colab

1. Abre [Google Colab](https://colab.research.google.com/)
2. Ve a **Archivo → Subir notebook**
3. Sube el notebook deseado desde la carpeta `Diego_DelRio_Rodriguez_TesisColab/`
4. Conecta el entorno de ejecución con GPU: **Entorno de ejecución → Cambiar tipo de entorno de ejecución → GPU**
5. Ejecuta las celdas en orden

### Ejecutar los Scripts Python

```bash
# Clonar el repositorio
git clone https://github.com/diegoodelrio/ViT-Master-Tesis.git
cd ViT-Master-Tesis/main

# Ejecutar el script principal
python main.py
```

---

## 📚 Referencias

- Dosovitskiy, A. et al. (2020). *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*. [arXiv:2010.11929](https://arxiv.org/abs/2010.11929)
- Vaswani, A. et al. (2017). *Attention Is All You Need*. [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)

---

## 📬 Contacto

**Diego Del Río Rodríguez**  
GitHub: [@diegoodelrio](https://github.com/diegoodelrio)

---

## 📝 Licencia

Este repositorio ha sido creado con fines académicos como parte de un Trabajo de Fin de Máster. Para cualquier uso del código o contenido, por favor contacta al autor.
