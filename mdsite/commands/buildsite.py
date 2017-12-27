import os
from mdsite.utils import postparser, homebuilder

config = {
    'site_url': None,  # if has site_url, use absolute url
    'site_dir': 'site',
    'permalink': ':year:/:month:/:day:/:title:.html',
    'template': None
}


def build_site():
    post_dir = os.path.join(os.getcwd(), 'post')
    # check if post dir exists
    if not os.path.exists(post_dir):
        print "Not a mdsite dir!"
        return
    # get post list
    # ordered by date, start from latest
    # record the current path depth, start with . (site_dir)
    path_depth = postparser.PathDepth()
    posts = postparser.get_post_list(post_dir, path_depth, config)
    # for post in posts:
    #     print post.title, post.date, post.url
    #     path_depth.set_base_path(post.html_path)
    if posts is not None:
        homebuilder.home_builder(posts, config)
