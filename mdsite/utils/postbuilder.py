import os
import markdown
from jinja2 import TemplateNotFound

# TODO replace links in markdown
# TODO copy files recursively to dest
# TODO render math
# TODO render code highlight


def post_builder(post, path_depth, config, template):
    # set path depth to the current post
    path_depth.set_base_path(post.html_path)
    with open(post.path, 'r') as fh:
        md_source = fh.read()
    content = markdown.markdown(md_source, extensions=['markdown.extensions.fenced_code', 'mdx_math'])
    context = {
        'base_url': path_depth.relative_path('.'),
        'post': post,
        'config': config,
        'content': content
    }
    try:
        post_template = template.env.get_template('post.html')
    except TemplateNotFound:
        print "No POST template found!"
        return
    post_html = post_template.render(context)
    post_dir = os.path.dirname(post.abs_html_path)
    if not os.path.exists(post_dir):
        os.makedirs(post_dir)
    # write post html
    with open(post.abs_html_path, 'w') as fh:
        fh.write(post_html)
