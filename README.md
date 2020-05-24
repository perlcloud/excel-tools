# excel_tools.py
A command line utility for manipulating and processing Excel files.

It aims to automate normalization processes on excel files, preparing them for further automation such as batch processing.

Currently Contains one tool:
- **split_sheet:**
    
    Splits each sheet in an Excel file into individual files.

    A folder with the same name as the input file will be created.
    Each Excel sheet is exported as an individual file, with a name matching the name of the Excel sheet

##Installing
This project requires Python 3.8.0
```
$ git clone https://github.com/perlcloud/excel-tools.git
$ cd excel_tools/
$ pip install -r requirements.txt
```
##Running
```
$ python3 excel_tools.py split-sheet some_excel_file.xlsx
```
##Help
```
$ python3 excel_tools.py --help
$ python3 excel_tools.py split-sheet --help
```