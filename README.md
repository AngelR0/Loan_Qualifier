# Loan Qualifier Application

# Description

This application saves any loans the user qualifies for, by extracting from the file `data_rate_sheet` and doing calculations of month debt ratio and loan to value ratio. The application asks for the user's information to compare it with other loans offered by different banks. Then printing the loans the user qualifies for onto `qualified_loans.csv`.

---
## Installations

Runs on python 3.7 with the following packages:

* [Fire](https://github.com/google/python-fire) - Used for the command line interface help page and entry point.

* [Questionary](https://github.com/tmbo/questionary) - This is used as our interactive user prompts and dialogs.
  
---

### How to install:

To install the following packages we need to use terminal or git bash and type in the command line:

* Fire
    ```python
    pip install Fire
    ```
* Questionary
    ```python
    pip install questionary
    ```
---
## Running the Application
To execute the application:
* Clone the repository.
* Open the file containing the application.
* Run the **app.py** file by typing in the command line:
    ```python
   python app.py
    ```
* There will be prompts asking for the file path being extracted, type:
  ```python 
  ./data/daily_rate_sheet.csv
  ``` 
  ![File Path Extraction](Pictures/File%20Path%20Extraction.png)

* These are the prompts:
  
  ![App Prompts](Picture/../Pictures/App%20Prompts.png)

* At the end of the application it will ask you if you want to save the file. 
  * If 'Yes' then you will be prompted to save the file. Include '.csv' after the title of the file to save it correctly.
  * if 'No' then you will be prompted "Did not save qualified loans." Do nothing further the application will exit.
## Contributors
Brought to you by Angel Reyes.
