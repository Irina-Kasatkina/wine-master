import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import pprint

from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas

COMPANY_FOUNDATION_YEAR = 1920

def get_word_for_year(age: int):
    age_string = str(age)

    if len(age_string) == 0: return ''
    if len(age_string) > 1 and age_string[-2] == '1': return 'лет'
    
    words = {'0': 'лет', '1': 'год', '2': 'года', '3': 'года', '4': 'года', '5': 'лет', '6': 'лет', '7': 'лет', '8': 'лет', '9': 'лет'}
    return words[age_string[-1]]

def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    years_count = datetime.datetime.now().year - COMPANY_FOUNDATION_YEAR
    hero2_subtitle = f'Уже {years_count} {get_word_for_year(years_count)} с вами'

    excel_data_df = pandas.read_excel('data/wine3.xlsx', na_values=['N/A', 'NA'], keep_default_na=False)
    wine_categories = collections.defaultdict(list)
    for _, row in excel_data_df.iterrows():
        wine = {
                'Картинка': row['Картинка'],
                'Название': row['Название'],
                'Сорт': row['Сорт'],
                'Цена': row['Цена'],
                'Акция': row['Акция'],            
        }
        wine_categories[row['Категория']].append(wine)

    rendered_page = template.render(
            hero2_subtitle = hero2_subtitle,
            wine_categories = wine_categories
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()