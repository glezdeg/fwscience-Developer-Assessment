# fwscience-Developer-Assessment

This project is developed to show the skills as a developer requested in:
[CloserIQ Developer Assessment](https://docs.google.com/document/d/1NFwKtv0FXtTsZuaWmiGI5jQzFgouOA9zEk7WVywGSNE/edit)

## Architecture proposal

According to the given background. The database has a lot of interactions every day so a periodic duplicate identification system would be the best option. Duplicate cleanup should be done at a time where the database has the fewest number of interactions. Generating a report and updating after removing duplicate data.
The proposed system is to generate the methods to connect and select the data from mysql or a csv file. Subsequently, a duplicate data report will be made for updating. In this system only the data report will be carried out as well as the interaction with mysql or csv.
The file package structure will have an example for csv main_csv_report() and another for mysql main_sql_report() in the main file called application.py the rest of the functions will be generated in separate modules in the rest of the package.
File structure (the corresponding \_\_init\_\_ files will be skipped):

|--application.py

|--companies_example_data.csv

|--dbhandlers

| |--mysqlhandler.py

| |--duplicatehandler.py

A report.json file will be generated as output

## Installation and creation of the virtual environment

To generate an independent and portable system, a virtual environment "env" will be created, generating a requirements.txt file for the necessary dependencies. Review documentation in [Creation of virtual environments](https://docs.python.org/3/library/venv.html).

## MySQL handlers

Inside the dbhandlers folder a file is generated with the methods to create the database and the companies table as well as the insertion of a record and the selection of all the records as a query. These functions were copied and modified from the official MySQL-Python [documentation](https://dev.mysql.com/doc/connector-python/en/)

## Duplicate handler

To remove duplicate names, use the csv file as an example to generate a json report using the report_duplicates method. In order to do it efficiently, a research was carried out and the [difflib](https://docs.python.org/3/library/difflib.html) library was found as a quick solution. reviewed several examples of using difflib.get_close_matches

## Main app

Finally, the duplicate report is performed using the code generated for the example csv file. we also proceed to test its operation using the data to interact with MySQL locally.

## Time spent on each task

(35 min) Documentary review of the Assessment.
(45 min) Interaction with MySQL.
(30 min) difflib revision to remove duplicates.
(45 min) Generation of the final application, git repository, documentation comments and README.
