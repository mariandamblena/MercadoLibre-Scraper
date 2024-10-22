import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_analyze(product_names):
    base_url = 'https://listado.mercadolibre.com.ar/'
    all_data = []

    for product_name in product_names:
        cleaned_name = product_name.replace(" ", "-").lower()
        urls = [base_url + cleaned_name]

        page_number = 50
        for i in range(0, 10000, 50):
            urls.append(f"{base_url}{cleaned_name}_Desde_{page_number + 1}_NoIndex_True")
            page_number += 50

        data = []
        for i, url in enumerate(urls, start=1):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find_all('li', class_='ui-search-layout__item')

            if not content:
                break

            for post in content:
                title = post.find('h2').text
                price = post.find('span', class_='andes-money-amount__fraction').text.replace('.', '')
                post_link = post.find("a")["href"]
                try:
                    img_link = post.find("img")["data-src"]
                except:
                    img_link = post.find("img")["src"]

                post_data = {
                    "title": title,
                    "price": float(price),
                    "post link": post_link,
                    "image link": img_link,
                    "product": product_name
                }
                data.append(post_data)

        all_data.extend(data)

    df = pd.DataFrame(all_data)
    results = []

    for product_name in product_names:
        product_prices = df[df['product'] == product_name]['price']
        mean_price = product_prices.mean()
        median_price = product_prices.median()
        min_price = product_prices.min()
        max_price = product_prices.max()
        suggested_price = median_price * 0.95

        results.append({
            "product": product_name,
            "mean": mean_price,
            "median": median_price,
            "min": min_price,
            "max": max_price,
            "suggested_price": suggested_price
        })

    return results
