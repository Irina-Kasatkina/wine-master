import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import pprint
import sys

import configargparse
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas

COMPANY_FOUNDATION_YEAR = 1920

def create_parser ():
    default_config_files = []
    if '-c' not in sys.argv and '--config' not in sys.argv:
        default_config_files = ['config/config.ini']

    parser = configargparse.ArgParser(default_config_files=default_config_files, description='Runs a website for wine shop.')
    parser.add_argument('-c', '--config', is_config_file=True, help='Config file path')
    parser.add_argument('-w', '--wines_excel_file', type=str, default='', help='Path of Excel file with wines')
    parser.add_argument('-a', '--actions_excel_file', type=str, default='', help='Path of Excel file with advertising actions')
    return parser

def create_html_file(template, wines_excel_file, actions_excel_file):
    years_count = datetime.datetime.now().year - COMPANY_FOUNDATION_YEAR
    div_hero_2_subtitle_text = f'Уже {years_count} {get_word_for_year(years_count)} с вами'
    
    wine_categories = get_wine_categories(wines_excel_file)
    actions_and_images = get_actions_and_images(actions_excel_file)

    rendered_page = template.render(
            div_hero_2_subtitle_text = div_hero_2_subtitle_text,
            wine_categories = wine_categories,
            actions_and_images = actions_and_images,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

def get_actions_and_images(actions_excel_file):
    actions_df = pandas.read_excel(actions_excel_file, na_values=['N/A', 'NA'], keep_default_na=False)
    actions_and_images = {}
    for _, row in actions_df.iterrows():
        actions_and_images[row['Акция']] = row['Картинка']
    return actions_and_images

def get_template():    
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    return env.get_template('template.html')

def get_wine_categories(wines_excel_file):
    wines_df = pandas.read_excel(wines_excel_file, na_values=['N/A', 'NA'], keep_default_na=False)
    wine_categories = collections.defaultdict(list)
    for _, row in wines_df.iterrows():
        wine = {
                'Картинка': row['Картинка'],
                'Название': row['Название'],
                'Сорт': row['Сорт'],
                'Цена': row['Цена'],
                'Акция': row['Акция'],            
        }
        wine_categories[row['Категория']].append(wine)
    return wine_categories

def get_word_for_year(years_count: int):
    years_count_string = str(years_count)

    if len(years_count_string) == 0: return ''
    if len(years_count_string) > 1 and years_count_string[-2] == '1': return 'лет'
    
    words = {'0': 'лет', '1': 'год', '2': 'года', '3': 'года', '4': 'года', '5': 'лет', '6': 'лет', '7': 'лет', '8': 'лет', '9': 'лет'}
    return words[years_count_string[-1]]

def main(wines_excel_file, actions_excel_file):
    template = get_template()
    create_html_file(template, wines_excel_file, actions_excel_file)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    parser = create_parser()
    options = parser.parse_args()

    main(options.wines_excel_file, options.actions_excel_file)