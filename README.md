# **ANALISIS EXPLORATORIO DE LA INDUSTRIA CINEMATOGRAFICA ESTADOUNIDENSE (1990 - 2020)**

## Introducción
Este proyecto se enfoca en el análisis y exploración de la industria cinematográfica estadounidense durante un período de 30 años, desde 1990 hasta 2020.

## Objetivo
La finalidad es limpiar, explorar y visualizar datos para identificar patrones y tendencias relevantes en la industria del cine en EE.UU. Los resultados buscan predecir el comportamiento del público en cuanto a gustos por actores, directores o géneros, lo que podría guiar a estudios y ejecutivos hacia producciones más rentables.

## Origen de los datos
El dataset proviene de Box Office Mojo, con identificadores de películas del portal IMDB. Aunque el análisis es de EE.UU., las películas incluyen producciones no exclusivamente estadounidenses pero con calificación de la MPAA, indicando su lanzamiento en Estados Unidos.

## Definición de las variables
*   **imdb_movie_id**: Identificador único de la película.
*   **title**: Título de la película.
*   **year**: Año de estreno.
*   **mpaa**: Clasificación de la MPAA.
*   **release_date**: Fecha de lanzamiento.
*   **run_time**: Duración original de la película.
*   **run_time_minutes**: Duración de la película en minutos.
*   **distributor**: Estudio o casa distribuidora.
*   **director**: Director.
*   **writer**: Escritor o guionista.
*   **producer**: Productor.
*   **composer**: Compositor.
*   **cinematographer**: Cinematógrafo o director de fotografía.
*   **main_actor_1, main_actor_2, main_actor_3, main_actor_4**: Actores principales.
*   **budget**: Presupuesto de producción.
*   **domestic**: Recaudación en el mercado doméstico.
*   **international**: Recaudación en el mercado internacional.
*   **worldwide**: Recaudación total mundial.
*   **genres**: Géneros de la película (combinación de `genre_1` a `genre_4`).
*   **html**: Enlace a la película en Box Office Mojo.

## Librerías utilizadas
Se utilizan librerías como `pandas` para manipulación de datos, `numpy` para operaciones numéricas, `matplotlib` y `seaborn` para visualización estática, `plotly.express` para visualizaciones interactivas, `wordcloud` para nubes de palabras, `datetime` para manejo de fechas y varias módulos de `scikit-learn`, `xgboost`, `lightgbm` y `scipy.stats` para modelado y análisis estadístico.

## FASES DEL PROYECTO Y HALLAZGOS CLAVE

### FASE 1: Importación, limpieza y preparación de datos
Se importaron los datos y librerías necesarias. Se realizó una exploración inicial para entender la estructura y detectar valores nulos. Los valores nulos en `release_date`, `mpaa`, `distributor`, `producer`, `composer`, `cinematographer`, `main_actor_4` y `writer` fueron tratados (rellenados con datos específicos o con 'unknown'). Los valores de recaudación (`domestic`, `international`, `worldwide`) se rellenaron con la media. Se consolidaron las columnas de géneros en una única columna `genres`. Se eliminó la columna `trivia` por no ser relevante. Los tipos de datos de `budget`, `domestic`, `international`, y `worldwide` se convirtieron a `int64`. La columna `run_time` se convirtió a minutos y se creó `run_time_minutes`. Se renombró `movie_id` a `imdb_movie_id`.

### FASE 2: Análisis Univariado
*   **Distribución MPAA**: La clasificación 'R' es la más frecuente, seguida de 'PG-13', indicando una fuerte presencia de películas con contenido maduro, aunque las PG-13 y PG recaudan más.
*   **Presupuesto (budget)**: La mayoría de las películas tienen presupuestos considerados, pero existen valores atípicos de superproducciones.
*   **Producción por año**: La cantidad de películas aumentó exponencialmente desde el 2000, con picos en 2009 y 2010. Se observa una caída drástica en 2020 debido a la pandemia.

### FASE 3: Análisis Bivariado
*   **MPAA vs. Taquilla Mundial**: Películas PG y PG-13 dominan la recaudación, aunque las de clasificación R también generan confianza.
*   **Correlación entre variables numéricas**: Fuerte correlación positiva entre `budget` y las recaudaciones (`domestic`, `international`, `worldwide`). Las recaudaciones también tienen fuertes correlaciones entre sí. El `year` tiene correlaciones bajas con el presupuesto y la taquilla.
*   **Ajuste por Inflación**: Se graficó la taquilla doméstica ajustada por inflación, mostrando que películas de años anteriores habrían recaudado más en términos actuales. Se confirmaron los grandes éxitos de 1997 (Titanic), 2009 (Avatar) y 2015 (Star Wars: The Force Awakens).
*   **Duración (run_time_minutes) vs. Taquilla**: La correlación es débil, sugiriendo que la duración no es un factor determinante en la recaudación.
*   **Presupuesto vs. Taquilla**: Existe una clara tendencia: a mayor presupuesto, mayor ganancia, aunque con riesgos significativos. Se identificaron casos de éxitos masivos (Avatar) y fracasos costosos.
*   **Distribución porcentual de recaudación**: La taquilla internacional representa la mayor parte de la recaudación total, seguida por la doméstica.
*   **Cronología evolutiva**: Se observó un incremento constante tanto en el presupuesto promedio como en la recaudación doméstica promedio a lo largo de los años (excluyendo la caída de 2020), lo que indica un crecimiento y rentabilidad de la industria.
*   **Distribuidores vs. Ingresos Domésticos**: Disney lidera la recaudación doméstica, consolidando su posición a través de la adquisición de franquicias importantes.

### FASE 4: Análisis de variables categóricas
*   **Géneros (genre_1) vs. Taquilla y Presupuesto**: Los géneros de Acción y Aventura son los que generan mayores ingresos y requieren mayores presupuestos. El horror demuestra ser muy rentable con presupuestos más modestos. Se realizó un análisis del ratio `domestic/budget` por género, donde el horror destacó por su alta rentabilidad.
*   **Nubes de Palabras**: Las nubes de palabras para títulos, actores, directores y distribuidores por recaudación doméstica e internacional ilustraron la concentración de éxitos y la influencia de figuras y empresas clave.
*   **Actores y Directores**: Actores como Tom Hanks y Tom Cruise, y directores como Steven Spielberg y James Cameron, muestran alta acumulación de ingresos en taquilla, destacando la importancia de las estrellas y las franquicias.

### FASE 5: Análisis Estadístico
*   **Estadísticas Descriptivas**: Se analizaron la media, mediana, desviación estándar, asimetría y curtosis de las variables numéricas. La mayoría de las distribuciones de recaudación y presupuesto presentan asimetría positiva y alta curtosis, indicando la presencia de valores atípicos (grandes éxitos).
*   **Pruebas de Normalidad (Shapiro-Wilk, Kolmogorov-Smirnov, QQ Plot)**: Se concluyó que las variables `budget` y `domestic` no siguen una distribución normal, lo cual es esperado dada la variabilidad de la industria.
*   **Comparación de Grupos (T-test, ANOVA, Tukey HSD)**: Se encontraron diferencias significativas en los ingresos entre clasificaciones MPAA (PG-13 vs. R) y en los presupuestos entre géneros (Acción, Comedia, Drama), confirmando que las clasificaciones y géneros influyen en la inversión y el rendimiento.
*   **Regresión Lineal Simple y Múltiple**: Los modelos de regresión lineal simple y múltiple (`budget`, `year`, `main_actor_1`, `director` vs. `domestic`) mostraron un rendimiento limitado, con un R² bajo (aprox. 0.11), indicando que estas variables por sí solas no explican la mayor parte de la variabilidad en la taquilla doméstica. El MAE fue de aproximadamente 54.87 millones de dólares.
*   **Algoritmos Adicionales de Regresión (Random Forest, XGBoost, LightGBM)**: Modelos más avanzados como Random Forest y XGBoost mejoraron ligeramente la predicción (R² de 0.43 y 0.45 respectivamente, MAE de 36.3M y 37.9M). LightGBM tuvo el rendimiento más bajo. Esto subraya la complejidad y la incertidumbre inherente a la predicción del éxito cinematográfico.
*   **Análisis de Clusters (K-Means)**: Se agruparon películas en tres clusters basadas en `budget`, `worldwide` y `run_time_minutes`: bajo presupuesto/baja taquilla, bajo presupuesto/alta taquilla (éxitos rentables), y alto presupuesto/alta taquilla (blockbusters).

## Conclusiones Generales
La industria cinematográfica estadounidense es dinámica y compleja. Los géneros de acción y aventura dominan la taquilla, mientras que géneros como el horror ofrecen alta rentabilidad con menor riesgo. La taquilla internacional es crucial para el éxito de grandes producciones. El valor de las estrellas, directores y franquicias sigue siendo un factor determinante. Aunque el análisis estadístico y los modelos de ML pueden identificar tendencias, la predicción del éxito de una película sigue siendo un desafío, influenciada por factores subjetivos y externos.

## Mejoras Futuras para el Proyecto
1.  **Ampliación y actualización de la base de datos**: Incluir datos más recientes, otros mercados internacionales, inversión en marketing, críticas, puntuaciones de audiencia y presencia en streaming.
2.  **Integración de nuevas herramientas analíticas**: Aplicar técnicas avanzadas de Machine Learning (redes neuronales, series temporales) y visualización interactiva.
3.  **Análisis de sentimiento y redes sociales**: Evaluar el impacto del sentimiento en la taquilla.
4.  **Enfoque en variables externas**: Considerar factores macroeconómicos, eventos globales y competencia.
5.  **Modelos de recomendación y segmentación de audiencia**: Desarrollar sistemas de recomendación para optimizar estrategias de marketing y lanzamiento.
