#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from mdsite.commands import newsite, newpost, buildsite


@click.group()
def cli():
    """
    MdSite: convert Markdown files into static site.
    """


# add subcommands
@cli.command()
@click.argument('mdsite_dir')
def new(mdsite_dir):
    """
    Create a new markdown site.
    """
    newsite.new_site(mdsite_dir)


@cli.command()
@click.option('-t', '--title', prompt=True, help='title of the new post')
def post(title):
    """
    Create a new post.
    """
    post_fpath = newpost.new_post(title)
    if post_fpath is not None:
        click.edit(filename=post_fpath)


@cli.command()
def build():
    """
    Build the markdown site.
    """
    buildsite.build_site()


if __name__ == '__main__':
    cli()
