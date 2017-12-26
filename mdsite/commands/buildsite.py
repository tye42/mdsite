import os
from mdsite.utils import postparse


def build_site():
    post_dir = os.path.join(os.getcwd(), 'post')
    # check if post dir exists
    if not os.path.exists(post_dir):
        print "Not a mdsite dir!"
        return
    # get post list
    # ordered by date, start from latest
    posts = postparse.get_post_list(post_dir)

