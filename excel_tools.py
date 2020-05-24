# excel_tools.py
"""A command line utility for manipulating and processing Excel files"""

from pathlib import Path

import click
import pandas as pd

from PyInquirer import prompt


@click.group()
def main():
    """A command line utility for manipulating and processing Excel files"""
    pass


@main.command()
@click.argument(
    "input_file", type=click.Path(exists=True, resolve_path=True),
)
@click.option(
    "-o",
    "--output-dir",
    help="Alternate directory to place exports.",
    type=click.Path(resolve_path=True),
)
@click.option(
    "-f",
    "--file-type",
    default="csv",
    show_default=True,
    help="File type used for export files.",
    type=click.Choice(["csv", "txt"]),
)
@click.option(
    "-r",
    "--raw-sheet-names",
    is_flag=True,
    show_default=True,
    help="Stop script from stripping leading and trailing spaces from sheet names before saving files.",
    type=click.BOOL,
)
@click.option(
    "-s",
    "--suppress-prompt",
    is_flag=True,
    show_default=True,
    help="Suppress user prompt for which sheets to export. Exports all when True.",
    type=click.BOOL,
)
def split_sheet(input_file, output_dir, file_type, raw_sheet_names, suppress_prompt):
    """
    Splits each sheet in an Excel file into individual files.

    A folder with the same name as the input file will be created.
    Each Excel sheet is exported as an individual file, with a name matching the name of the Excel sheet
    """
    input_file = Path(input_file)

    output_path = (
        Path.cwd().joinpath(input_file.stem) if not output_dir else Path(output_dir)
    )
    output_path.mkdir(exist_ok=True)  # Create output directory if it does not exist

    excel_file = pd.ExcelFile(input_file)
    sheet_names = [
        x.strip() if not raw_sheet_names else x for x in excel_file.sheet_names
    ]

    if not suppress_prompt:
        # Assemble question for PyInquirer
        select_sheets_for_export = [
            {
                "type": "checkbox",
                "message": "Select sheets to export as files",
                "name": "sheets",
                "choices": [{"name": x, "checked": True} for x in sheet_names],
            }
        ]
        sheets_for_export = prompt(select_sheets_for_export)["sheets"]
    else:
        sheets_for_export = sheet_names

    with click.progressbar(
        excel_file.sheet_names,
        label=f"Exporting {len(sheets_for_export)} sheets as .{file_type} files",
    ) as sheet_names:
        for sheet_name in sheet_names:
            output_file_stem = sheet_name.strip() if not raw_sheet_names else sheet_name
            if output_file_stem in sheets_for_export:
                print(f"Processing: '{sheet_name}'", end=" ")
                output_file = output_path.joinpath(f"{output_file_stem}.{file_type}")

                df = excel_file.parse(sheet_name)
                if file_type == "csv":
                    df.to_csv(output_file)
                elif file_type == "txt":
                    df.to_csv(output_file)
                print(":: DONE!")


if __name__ == "__main__":
    main()
