# lazy_load.py
"""Classes for lazy-loading click groups"""

import click


class MyCLI(click.MultiCommand):
    """
    A class to lazy load the python files in a folder as click command groups
    Adapted from the click documentation: https://click.palletsprojects.com/en/7.x/commands/#custom-multi-commands
    """

    def __init__(self, plugin_folder, **attrs):
        super().__init__(**attrs)
        self.plugin_folder = plugin_folder
        self.plugin_files = [x for x in self.plugin_folder.glob('**/*') if x.is_file() and x.suffix == '.py']

    def list_commands(self, ctx):
        rv = []
        for filename in self.plugin_files:
            rv.append(filename.stem)
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = self.plugin_folder.joinpath(name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']
