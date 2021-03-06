from pathlib import Path
import pandas as pd

from utils.inquirer import Inquire

inquire = Inquire()


class ExcelFile:
    """Excel file class with helper functions for parsing Excel files"""

    def __init__(self, excel_file):
        self.path = Path(excel_file)
        self.excel_file = pd.ExcelFile(self.path)

    @property
    def stripped_sheet_names(self):
        """
        Returns the names of the Excel files sheets, with leading and trailing spaces removed
        :return list:
        """
        return [x.strip() for x in self.excel_file.sheet_names]

    @property
    def sheet_names(self):
        """
        Returns the names of the Excel files sheets
        :return list:
        """
        return self.excel_file.sheet_names

    def get_sheet(self, sheet_name):
        """
        Returns a data frame for the selected excel sheet
        :param sheet_name:
        :return:
        """
        return self.excel_file.parse(sheet_name)

    def select_sheets(self, strip_names=True):
        """
        Prompts the user to select from a list of the files sheet names
        :param strip_names:
        :return:
        """
        sheet_names = self.stripped_sheet_names if strip_names else self.sheet_names

        # Ask user for input via PyInquirer
        inquire.question(
            inquire.CHECKBOX,
            message="Select sheets to export as files",
            name="sheets",
            choices=[{"name": x, "checked": True} for x in sheet_names],
        )
        return inquire.ask()["sheets"]

    def get_metadata(self, filter=None, raw_sheet_names=False):
        """
        Returns a data frame of metadata about the sheets
        :param filter: List of sheets to return data for
        :param raw_sheet_names: Do not strip sheet names
        :return: Data frame
        """
        sheet_names = (
            self.sheet_names
            if not filter
            else [x for x in self.sheet_names if x in filter]
        )

        data = {"Sheet Name": [], "Rows": [], "Columns": []}
        for sheet_name in sheet_names:
            sheet = self.get_sheet(sheet_name)
            data["Sheet Name"].append(
                sheet_name if raw_sheet_names else sheet_name.strip()
            )
            data["Rows"].append(len(sheet))
            data["Columns"].append(len(sheet.columns))

        return pd.DataFrame(data=data)
