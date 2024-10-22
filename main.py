import pandas as pd
from scrapper import scrape_and_analyze

if __name__ == "__main__":
    # Solicitar al usuario los nombres de los productos
    product_names = input("Ingrese los nombres de los productos separados por comas: ").split(',')

    # Llamar a la función scrape_and_analyze con la lista de nombres de productos
    resultados = scrape_and_analyze([product_name.strip() for product_name in product_names])

    # Crear un DataFrame con los resultados
    df_resultados = pd.DataFrame(resultados)

    # Guardar el DataFrame en un archivo Excel
    df_resultados.to_excel("mercadolibre_price_analysis.xlsx", index=False)

    print("Análisis de precios guardado en 'mercadolibre_price_analysis.xlsx'.")
