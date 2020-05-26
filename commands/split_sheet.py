"""Command line tool for splitting excel sheets into individual files"""

import click
from pathlib import Path
from utils.inquirer import Inquire

from tools.excel_file_tools import ExcelFile

inquire = Inquire()


@click.command()
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
    file = ExcelFile(input_file)
    output_path = (Path.cwd().joinpath(file.path.stem) if not output_dir else Path(output_dir))
    output_path.mkdir(exist_ok=True)  # Create output directory if it does not exist

    sheet_names = file.stripped_sheet_names if not raw_sheet_names else file.sheet_names
    sheets_for_export = file.select_sheets() if not suppress_prompt else sheet_names

    with click.progressbar(
        file.sheet_names,
        label=f"Exporting {len(sheets_for_export)} sheets as .{file_type} files",
    ) as sheet_names:
        for sheet_name in sheet_names:
            output_file_stem = sheet_name.strip() if not raw_sheet_names else sheet_name
            if output_file_stem in sheets_for_export:
                print(f"Processing: '{sheet_name}'", end=" ")
                output_file = output_path.joinpath(f"{output_file_stem}.{file_type}")

                df = file.get_sheet(sheet_name)
                if file_type == "csv":
                    df.to_csv(output_file)
                elif file_type == "txt":
                    df.to_csv(output_file)
                print(":: DONE!")


cli = split_sheet


if __name__ == '__main__':
    cli()
