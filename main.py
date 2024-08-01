# main.py
from scrapper import scrape_and_analyze

if __name__ == "__main__":
    # Solicitar al usuario el nombre del producto
    product_name = input("Ingrese el nombre del producto: ")

    # Llamar a la función scrape_and_analyze con el nombre del producto
    resultados = scrape_and_analyze(product_name)

    # Imprimir los resultados
    print(f"Media: {resultados['mean']:.2f}")
    print(f"Mediana: {resultados['median']:.2f}")
    print(f"Mínimo: {resultados['min']:.2f}")
    print(f"Máximo: {resultados['max']:.2f}")
    print(f"Precio sugerido (mediana - 5%): {resultados['suggested_price']:.2f}")
