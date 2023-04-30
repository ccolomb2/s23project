"""to print reference in the terminal"""

import click
from .worksproject import Works


@click.command()
@click.argument("url", nargs=1)
@click.option("--bibtex", is_flag=True, show_default=True, default=False)
@click.option("--ris", is_flag=True, show_default=True, default=False)
def terminal(url, bibtex, ris):
    """terminal"""
    result = Works(url)
    if bibtex:
        print(result.bibtex())
    if ris:
        print(result.ris())
