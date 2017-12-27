import os
from jinja2 import TemplateNotFound


def home_builder(posts, config, template):
    context = {
        'base_url': '.',
        'posts': posts,
        'config': config
    }
    try:
        home_template = template.env.get_template('home.html')
    except TemplateNotFound:
        print "No HOME template found!"
        return
    home_html = home_template.render(context)
    if not os.path.exists(config['site_dir']):
        os.mkdir(config['site_dir'])
    # write home html
    with open(os.path.join(config['site_dir'], 'index.html'), 'w') as fh:
        fh.write(home_html)
