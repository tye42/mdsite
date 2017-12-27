import jinja2
import os
import shutil


class Template:
    def __init__(self, config):
        if config['template_dir'] is not None:
            self.template_dir = config['template_dir']
        else:
            mdsite_dir = os.path.abspath(os.path.dirname(__file__))
            mdsite_dir = mdsite_dir.rstrip('/').rsplit('/', 1)[0]
            mdsite_template = os.path.join(mdsite_dir, 'templates')
            self.template_dir = mdsite_template
        loader = jinja2.FileSystemLoader(self.template_dir)
        self.env = jinja2.Environment(loader=loader)
        self.copy_assets(config)

    def copy_assets(self, config):
        # clean the site_dir
        if os.path.exists(config['site_dir']):
            shutil.rmtree(config['site_dir'])
        shutil.copytree(self.template_dir, config['site_dir'], ignore=shutil.ignore_patterns('*.html'))
