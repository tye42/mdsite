import os
import datetime


def new_post(title):
    """
    Create a new post yyyy_mm_dd_title.md under ./post
    title is joined by underscore
    """
    # check if post dir exist
    post_dir = os.path.join(os.getcwd(), 'post')
    if not os.path.exists(post_dir):
        print "Not a mdsite dir!"
        return
    # get the current date
    today = datetime.date.today().strftime("%Y_%m_%d")
    post_fname = "%s_%s.md" % (today, '_'.join(title.strip().split(' ')))
    post_fpath = os.path.join(post_dir, post_fname)
    if os.path.exists(post_fpath):
        print "File already exists!"
        return
    with open(post_fpath, 'w+'):
        print "Creating post: %s ..." % post_fname
        return post_fpath


