# Web Layout for pythonist - We sell elite wine

This tutorial project demonstrates how to work with HTML and Jinja2 library templates on the example of the website of the author's wine store "New Russian Wine".

### How to install

To install the project, copy it to your local drive.

You should already have Python3 installed.<br>
It's best to work in a virtual environment to avoid conflicts with your installed library versions.<br>
Then use `pip` (or `pip3`, there is a conflict with Python2) to install the dependencies:
```
pip install -r requirements.txt
```

### How to start

- Run cmd, then on the command line change to the program directory: 
```
cd <program_directory_on_your_local_disk>
```
- Then start the site with 
```
python main.py
```
or
```
python3 main.py
```
- Go to the website at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### How to change the data on the website

If you want to change the data on the html page, copy the `data/wine3.xlsx` file as a sample and fill it with your data (do not change the column headings).

You can also set a different path to the file with your data.
This can be done using the `-f` option on the command line (example file path: `data1/wine4.xlsx`):
```
python main.py -f path_to_your_data_file
```
or you can set the path to your file in the configuration file (see the example in `config/config.ini`).
If you wish, you can change the path to the configuration file. Then specify it in the `-c` command line option (example of the file path: `config1/config2.ini`):
```
python main.py -c path_to_your_config_file
```

### Project Goals

The code was written for educational purposes in the process of learning in an online course on web layout for Python developers.



# Вёрстка для питониста - Продаём элитное вино

Этот учебный проект демонстрирует работу с HTML и шаблонами библиотеки Jinja2 на примере сайта магазина авторского вина "Новое русское вино".

### Как установить

Для установки проекта скопируйте его на свой локальный диск.

У вас уже должен быть установлен Python3.<br>
Лучше работать в виртуальном окружении, чтобы избежать конфликта с установленными у вас версиями библиотек.<br>
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

- Запустите cmd, в командной строке перейдите в каталог программы: 
```
cd <каталог_программы_на_вашем_локальном_диске>
```
- Затем запустите сайт командой 
```
python main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Как поменять данные на сайте

Если вы хотите поменять данные на html-странице, скопируйте как образец файл `data/wine3.xlsx` и заполните его своими данными (не меняйте заголовки столбцов).

Вы также можете задать другой путь к файлу со своими данными.
Это можно сделать с помощью параметра `-f` в командной строке (пример пути к файлу: `data1/wine4.xlsx`):
```
python main.py -f путь_к_вашему_файлу_с_данными
```
либо можно задать путь к вашему файлу в конфигурационном файле (см. образец в `config/config.ini`).
При желании вы также можете поменять путь к конфигурационному файлу. Тогда задайте его в параметре `-c` командной строки (пример пути к файлу: `config1/config2.ini`):
```
python main.py -c путь_к_вашему_конфигурационному_файлу
```

### Цель проекта

Код написан в учебных целях в процессе обучения на онлайн-курсе по вёрстке для Python-разработчиков.
