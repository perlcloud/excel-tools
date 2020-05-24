# excel_tools.py
"""A command line utility for manipulating and processing Excel files"""

from __future__ import print_function, unicode_literals
from pathlib import Path, PurePath

import click
import pandas as pd

from PyInquirer import prompt


@click.group()
def main():
    """A commandline utility with tools for manipulating Excel files"""
    pass


@main.command()
@click.option(
    "-i",
    "--input-file",
    help="Valid path to an Excel file",
    prompt="Please enter a path to a valid file",
    type=click.Path(exists=True, resolve_path=True),
)
@click.option(
    "-f",
    "--file-type",
    default="csv",
    help="File type to export Excel sheets as",
    type=click.Choice(["csv", "txt"]),
)
@click.option(
    "-t",
    "--strip-sheet-names",
    default=True,
    show_default=True,
    help="Strip leading and trailing spaces from sheet names before saving files",
    type=click.BOOL,
)
def sheet_conversion(input_file, file_type, strip_sheet_names):
    """Convert excel sheets to individual files"""
    input_file = Path(input_file)
    output_path = Path(input_file.parents[0]).joinpath(input_file.stem)
    output_path.mkdir(exist_ok=True)  # Create output directory if it does not exist

    excel_file = pd.ExcelFile(input_file)
    sheet_names = [
        x.strip() if strip_sheet_names else x for x in excel_file.sheet_names
    ]

    select_sheets_for_export = [
        {
            "type": "checkbox",
            "message": "Select sheets to export as files",
            "name": "sheets",
            "choices": [{"name": x, "checked": True} for x in sheet_names],
        }
    ]

    sheets_for_export = prompt(select_sheets_for_export)["sheets"]

    for sheet_name in excel_file.sheet_names:
        output_file_stem = sheet_name.strip() if strip_sheet_names else sheet_name
        if output_file_stem in sheets_for_export:
            output_file = output_path.joinpath(f"{output_file_stem}.{file_type}")

            df = excel_file.parse(sheet_name)
            if file_type == "csv":
                df.to_csv(output_file)
            elif file_type == "txt":
                df.to_csv(output_file)


if __name__ == "__main__":
    main()
