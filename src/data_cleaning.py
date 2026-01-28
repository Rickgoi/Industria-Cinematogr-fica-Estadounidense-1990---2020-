import pandas as pd

def clean_movie_data(df):
    """
    Esta función toma el dataset sucio y lo devuelve limpio.
    Es la que usaremos en nuestro portafolio para demostrar orden.
    """
    df_clean = df.copy()
    
    # 1. Limpiamos las columnas de dinero (eliminamos $ y comas)
    for col in ['budget', 'domestic', 'international', 'worldwide']:
        if col in df_clean.columns and df_clean[col].dtype == 'object':
            df_clean[col] = df_clean[col].str.replace('$', '').str.replace(',', '').astype(float)
    
    # 2. Manejo de nulos básicos
    df_clean['distributor'] = df_clean['distributor'].fillna('Independent')
    
    # 3. Crear métrica de éxito (ROI)
    # Filtramos presupuestos > 0 para evitar errores matemáticos
    df_clean = df_clean[df_clean['budget'] > 0]
    df_clean['roi'] = df_clean['worldwide'] / df_clean['budget']
    
    return df_clean
