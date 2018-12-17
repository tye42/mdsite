import os

# DONE template config

CONFIG_TEMPLATE = """
site_name: Your Site Name
author: Your Name
site_url:
permalink: :year:/:month:/:day:/:title:.html
template_dir:
"""


def new_site(mdsite_dir):
    """
    Create a new markdown site.
    Initialize with an template configuration file: config.yml
    and an empty directory: post to store all posts
    """
    config_fpath = os.path.join(mdsite_dir, 'config.yml')
    post_dir = os.path.join(mdsite_dir, 'post')
    if os.path.exists(config_fpath) and os.path.exists(post_dir):
        print "Site already exists!"
        return
    if not os.path.exists(mdsite_dir):
        print "Creating mdsite: %s ..." % mdsite_dir
        os.mkdir(mdsite_dir)
    if not os.path.exists(post_dir):
        print "Creating post dir: %s ..." % post_dir
        os.mkdir(post_dir)
    if not os.path.exists(config_fpath):
        print "Creating template config: %s ..." % config_fpath
        with open(config_fpath, 'w') as fh:
            fh.write(CONFIG_TEMPLATE)
