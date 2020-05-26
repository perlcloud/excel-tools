"""Command line tool for splitting excel sheets into individual files"""

import click
from utils.inquirer import Inquire
import pandas as pd

from tools.excel_file_tools import ExcelFile

inquire = Inquire()
pd.set_option('display.max_rows', None)


@click.command()
@click.argument(
    "input_file", type=click.Path(exists=True, resolve_path=True),
)
@click.option(
    "-n",
    "--names-only",
    is_flag=True,
    show_default=True,
    help="Output sheet names only.",
    type=click.BOOL,
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    show_default=True,
    help="Adds additional information about each sheet to output.",
    type=click.BOOL,
)
@click.option(
    "-f",
    "--filter",
    is_flag=True,
    show_default=False,
    help="Prompts user to select from a list of the files sheets to get sheet info for.",
    type=click.BOOL,
)
@click.option(
    "-r",
    "--raw-sheet-names",
    is_flag=True,
    show_default=True,
    help="Stop script from stripping leading and trailing spaces from sheet names.",
    type=click.BOOL,
)
def list_sheets(input_file, names_only, verbose, filter, raw_sheet_names):
    """
    Lists the names of sheets in an excel file.
    Sheet metadata available with '-v/--verbose' flag!
    """
    file = ExcelFile(input_file)
    if not filter:
        sheet_names = file.sheet_names
    else:
        sheet_names = file.select_sheets(strip_names=False)

    if names_only and not verbose:
        for sheet_name in sheet_names:
            sheet_name = sheet_name if raw_sheet_names else sheet_name.strip()
            print(sheet_name)
    else:
        if verbose:
            # Asking to view names only but also show verbose information makes no sense
            if names_only:
                click.echo(
                    click.style(
                        "'--names-only' and '--verbose' is an illegal combination, ignoring '--names-only'.",
                        fg='red'
                    )
                )

            data = file.get_metadata(filter=sheet_names, raw_sheet_names=raw_sheet_names)
            print(data)
        else:
            for index, sheet_name in enumerate(sheet_names):
                sheet_name = sheet_name if raw_sheet_names else sheet_name.strip()
                print(index, sheet_name)


cli = list_sheets

if __name__ == '__main__':
    cli()
