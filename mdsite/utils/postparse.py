import os
import datetime


ERROR_FILENAME_MSG = """Wrong file name format!
The file name should be yyyy_mm_dd_title.md"""


def get_post_list(post_dir):
    """
    Walk through the posts in post dir
    return a list of valid post instances, sorted by date
    """
    posts = []
    for post_fname in os.listdir(post_dir):
        # check if is markdown file
        if post_fname.endswith('.md'):
            post_split = post_fname.rsplit('.', 1)[0].split('_')
            if len(post_split) > 3:
                try:
                    date = datetime.datetime.strptime('_'.join(post_split[:3]), '%Y_%m_%d').date()
                    title = ' '.join(post_split[3:])
                    # check if title is empty
                    if len(title) - title.count(' ') > 0:
                        posts.append(Post(title, date, os.path.join(post_dir, post_fname)))
                    else:
                        print 'Empty title!'
                except ValueError:
                    print ERROR_FILENAME_MSG
            else:
                print ERROR_FILENAME_MSG
    # sort by date
    if len(posts) > 0:
        sorted_posts = sorted(posts, key=lambda x: x.date, reverse=True)
        # walk through posts to link previous and next post
        prev_post = None
        for post in sorted_posts:
            if prev_post is not None:
                post.prev_post = prev_post
                prev_post.next_post = post
            prev_post = post
        return sorted_posts
    else:
        print 'No valid posts found!'
        return None


class Post:
    def __init__(self, title, date, path):
        self.title = title
        self.date = date
        self.path = path
        self.url = None
        self.prev_post = None
        self.next_post = None