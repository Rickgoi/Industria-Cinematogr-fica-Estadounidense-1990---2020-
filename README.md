# 🎬 Análisis de Inversión y ROI en la Industria Cinematográfica (1990-2020)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg) 
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Data](https://img.shields.io/badge/Source-BoxOfficeMojo-orange.svg)

## 📌 Executive Summary
Este proyecto analiza el ecosistema financiero de la industria cinematográfica de EE.UU. para identificar patrones de rentabilidad. Mediante el uso de **Machine Learning y Estadística Avanzada**, se determinaron los factores que maximizan el ROI, permitiendo a los estudios mitigar riesgos en producciones de alto presupuesto.

## 🛠️ Tech Stack & Herramientas
* **Data Wrangling:** `Pandas`, `NumPy`, `DateTime`.
* **Visualización:** `Seaborn`, `Matplotlib`, `Plotly Express` (Gráficos interactivos).
* **Estadística:** `Scipy.stats` (ANOVA, Tukey HSD, Shapiro-Wilk).
* **Machine Learning:** `XGBoost`, `Random Forest`, `LightGBM`, `K-Means Clustering`.

## 📊 Hallazgos Crave (Business Insights)
* **Rentabilidad por Riesgo:** El género **Horror** presenta el ratio de retorno más alto frente a presupuestos modestos, mientras que **Acción/Aventura** domina el volumen total de ingresos pero con mayor riesgo financiero.
* **Poder de Distribución:** Disney lidera la recaudación doméstica, evidenciando el impacto de la consolidación de franquicias.
* **Predictibilidad:** Se logró reducir el error de predicción de ingresos (MAE) a **36.3M USD** utilizando modelos de ensamble (Random Forest), superando significativamente a la regresión lineal simple.
* **Segmentación de Mercado:** Mediante **K-Means**, se identificaron 3 nichos claros: *Blockbusters de alto riesgo*, *Éxitos rentables de bajo presupuesto* y *Cine independiente/nicho*.

## 🏗️ Fases del Proyecto
1.  **Data Engineering:** Limpieza de +3000 registros, imputación de nulos mediante investigación externa y normalización de variables financieras.
2.  **Análisis Estadístico:** Validación de hipótesis sobre el impacto de la calificación MPAA y el género en la recaudación.
3.  **Modelado Predictivo:** Comparativa de algoritmos de regresión para estimar taquilla.
4.  **Clustering:** Agrupación estratégica de películas para análisis de competencia.

## 🚀 Instalación y Uso
1. Clonar: `git clone https://github.com/Rickgoi/movie-industry-analysis.git`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `jupyter notebook notebooks/Analisis_Cinematografico.ipynb`

---
📫 **Contacto:** (https://www.linkedin.com/in/ricardo-goitia-659a5895/) - goitiaricardo@gmail.com
