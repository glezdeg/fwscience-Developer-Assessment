# fwscience-Developer-Assessment

This project is developed to show the skills as a developer requested in:
[CloserIQ Developer Assessment](https://docs.google.com/document/d/1NFwKtv0FXtTsZuaWmiGI5jQzFgouOA9zEk7WVywGSNE/edit)

## Architecture proposal

According to the given background. The database has a lot of interactions every day so a periodic duplicate identification system would be the best option. Duplicate cleanup should be done at a time where the database has the fewest number of interactions. Generating a report and updating after removing duplicate data.
The proposed system is to generate the methods to connect and select the data from mysql or a csv file. Subsequently, a duplicate data report will be made for updating. In this system only the data report will be carried out as well as the interaction with mysql or csv.
The file package structure will have an example for csv main_csv_report() and another for mysql main_sql_report() in the main file called application.py the rest of the functions will be generated in separate modules in the rest of the package.
File structure (the corresponding \_\_init\_\_ files will be skipped):

> application.py
> companies_example_data.csv
> dbhandlers
>
> > mysqlhandler.py
> > duplicatehandler.py

A report.json file will be generated as output

## Installation and creation of the virtual environment

To generate an independent and portable system, a virtual environment "env" will be created, generating a requirements.txt file for the necessary dependencies. Review documentation in [Creation of virtual environments](https://docs.python.org/3/library/venv.html).
