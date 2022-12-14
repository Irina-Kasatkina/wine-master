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

If you want to change the wines data on the html page, copy the `data/wine3.xlsx` file as a sample and fill it with your data (do not change the column headings). If you want to change the advertising actions data, copy the `data/actions.xlsx` file as a sample and fill it with your data (do not change the column headings). After that, as before, run the site with the command
```
python main.py
```

In addition, the main.py program can accept command-line options to set paths to files with information about wines and advertising actions:<br>
`-w filepath` - to set the path to the wines data file,<br>
`-a filepath` - to set the path to a file with advertising actions data.

For example, for the files `data1/wines1.xlsx` and `data2/actions2.xlsx`, the site is runned with the command:
```
python main.py -w data1/wines1.xlsx -a data2/actions2.xlsx
```

It is also possible not to specify the paths on the command line, but to set them in the configuration file (see the sample in `config/config.ini`).
If you change the path to the configuration file, then use the `-c` option to set the path to it. For example, for the configuration file `config1/config1.ini`
run the site with the command
```
python main.py -c config1/config1.ini
```

Wines images are in the `images` folder, and images for advertising actions are in the `assets` folder.

### Project Goals

The code was written for educational purposes in the process of learning in an online course on web layout for Python developers.