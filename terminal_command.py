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
