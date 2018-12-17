import yaml

config = {
    'site_url': None,  # if has site_url, use absolute url
    'site_dir': 'site',
    'permalink': ':year:/:month:/:day:/:title:.html',
    'template_dir': None,
    'site_name': 'Your Site Name',
    'author': 'Your Name'
}


def load_config(config_file, config):
    with open(config_file, 'r') as fh:
        config_fromfile = yaml.load(fh)
    for key in config_fromfile:
        if key in config and config_fromfile[key]:
            config[key] = config_fromfile[key]