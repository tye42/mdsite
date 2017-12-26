#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from mdsite.commands import newsite, newpost, buildsite


@click.group()
def cli():
    pass


# add subcommands
@cli.command()
@click.argument('mdsite_dir')
def new(mdsite_dir):
    """
    create a new markdown site
    """
    newsite.new_site(mdsite_dir)


@cli.command()
@click.option('-t', '--title', prompt=True, help='title of the new post')
def post(title):
    """
    create a new post
    """
    post_fpath = newpost.new_post(title)
    if post_fpath is not None:
        click.edit(filename=post_fpath)


@cli.command()
def build():
    """
    build the markdown site
    """
    buildsite.build_site()


if __name__ == '__main__':
    cli()
