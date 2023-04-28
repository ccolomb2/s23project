<<<<<<< HEAD
"""to print reference in the terminal"""

import click
from s23project import Works

@click.command()
@click.option('--bibtex')
@click.option('--ris')

def terminal(bibtex, ris):
    """terminal"""
    if bibtex:
        result = Works(bibtex)
        click.echo(result.bibtex())
    if ris:
        result = Works(ris)
        click.echo(result.ris())
=======
"""for command that print in the terminal"""
>>>>>>> ea9841f2e16228fa57c9b1eb6d51695e8cb49407
