# excel_tools.py
A command line utility for manipulating and processing Excel files.

It aims to automate normalization processes on excel files, preparing them for further automation such as batch processing.

Current Tools:
- **split:**
    
    Splits each sheet in an Excel file into individual files.

    A folder with the same name as the input file will be created.
    Each Excel sheet is exported as an individual file, with a name matching the name of the Excel sheet
- **list:**
    
    Lists the names of sheets in an excel file.
    Sheet metadata available with '-v/--verbose' flag! 
    
## Installing

This project requires Python 3.8.0
```
$ git clone https://github.com/perlcloud/excel-tools.git
$ cd excel_tools/
$ pip install -r requirements.txt
```
## Running
```
$ python3 excel_tools.py split_sheet some_excel_file.xlsx
$ python3 excel_tools.py list_sheets some_excel_file.xlsx
```
## Help
```
$ python3 excel_tools.py --help

Usage: excel_tools.py [OPTIONS] COMMAND [ARGS]...

  A command line utility for manipulating and processing Excel files

Options:
  --help  Show this message and exit.

Commands:
  list   Lists the names of sheets in an excel file.
  split  Splits each sheet in an Excel file into individual files.
```
```
$ python3 excel_tools.py split --help

Usage: excel_tools.py split_sheet [OPTIONS] INPUT_FILE

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
```
$ python3 excel_tools.py list --help

Usage: excel_tools.py list [OPTIONS] INPUT_FILE

  Lists the names of sheets in an excel file. Sheet metadata available with
  '-v/--verbose' flag!

Options:
  -n, --names-only                Output sheet names only.  [default: False]
  -f, --filter                    Prompts user to select from a list of the
                                  files sheets to get sheet info for.

  -r, --raw-sheet-names           Stop script from stripping leading and
                                  trailing spaces from sheet names.  [default:
                                  False]

  -v, --verbose                   Adds additional information about each sheet
                                  to output.  [default: False]

  -t, --table-style [plain|simple|github|grid|fancy_grid|pipe|orgtbl|jira|presto|pretty|psql|rst|mediawiki|moinmoin|youtrack|html|latex|latex_raw|latex_booktabs|textile]
                                  Sets the style of table output for verbose
                                  output. Use 'plain' for none.  [default:
                                  github]

  --help                          Show this message and exit.
```