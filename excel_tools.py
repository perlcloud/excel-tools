# excel_tools.py
# """A command line utility for manipulating and processing Excel files"""

from pathlib import Path

from utils.lazy_load import MyCLI


if __name__ == '__main__':
    plugin_folder = Path(__file__).parents[0].joinpath("commands")
    cli = MyCLI(plugin_folder, help="A command line utility for manipulating and processing Excel files")
    cli()
