# excel_tools.py
A command line utility for manipulating and processing Excel files.

It aims to automate normalization processes on excel files, preparing them for further automation such as batch processing.

Currently Contains one tool:
- **split-sheet:**
    
    Splits each sheet in an Excel file into individual files.

    A folder with the same name as the input file will be created.
    Each Excel sheet is exported as an individual file, with a name matching the name of the Excel sheet

## Installing

This project requires Python 3.8.0
```
$ git clone https://github.com/perlcloud/excel-tools.git
$ cd excel_tools/
$ pip install -r requirements.txt
```
## Running
```
$ python3 excel_tools.py split-sheet some_excel_file.xlsx
```
## Help
```
$ python3 excel_tools.py --help

Usage: excel_tools.py [OPTIONS] COMMAND [ARGS]...

  A command line utility for manipulating and processing Excel files

Options:
  --help  Show this message and exit.

Commands:
  split-sheet  Splits each sheet in an Excel file into individual files.
```
```
$ python3 excel_tools.py split-sheet --help

Usage: excel_tools.py split-sheet [OPTIONS] INPUT_FILE

  Splits each sheet in an Excel file into individual files.

  A folder with the same name as the input file will be created. Each Excel
  sheet is exported as an individual file, with a name matching the name of
  the Excel sheet

Options:
  -o, --output-dir PATH      Alternate directory to place exports.
  -f, --file-type [csv|txt]  File type used for export files.  [default: csv]
  -r, --raw-sheet-names      Stop script from stripping leading and trailing
                             spaces from sheet names before saving files.
                             [default: False]

  -s, --suppress-prompt      Suppress user prompt for which sheets to export.
                             Exports all when True.  [default: False]

  --help                     Show this message and exit.
```