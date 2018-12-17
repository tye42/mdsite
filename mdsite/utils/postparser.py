import os
import datetime


ERROR_FILENAME_MSG = """Wrong file name format!
The file name should be yyyy_mm_dd_title.md"""


def _is_markdown(fname):
    fext = os.path.splitext(fname)[1]
    return fext.lower() in ['.md', '.markdown', '.mdown']


# TODO add category
# DONE customize permalink
def _get_html_path(title, date, config):
    """
    Given permalink format, generate html path
    valid permalink format
        e.g. :year:/:month:/:day:/:title:.html
    """
    html_path = config['permalink']
    replace_format = {
        ':year:': str(date.year),
        ':month:': str(date.month),
        ':day:': str(date.day),
        ':title:': '-'.join(title.split(' '))
    }
    for key in replace_format:
        html_path = html_path.replace(key, replace_format[key])
    html_path = html_path.strip('/')
    if not html_path.endswith('.html'):
        html_path += '.html'
    return os.path.join('post', html_path)


def get_post_list(post_dir, path_depth, config):
    """
    Walk through the posts in post dir
    return a list of valid post instances, sorted by date
    """
    posts = []
    for post_fname in os.listdir(post_dir):
        # check if is markdown file
        if _is_markdown(post_fname):
            post_split = post_fname.rsplit('.', 1)[0].split('_')
            if len(post_split) > 3:
                try:
                    date = datetime.datetime.strptime('_'.join(post_split[:3]), '%Y_%m_%d').date()
                    title = ' '.join(post_split[3:])
                    # check if title is empty
                    if len(title) - title.count(' ') > 0:
                        post_fpath = os.path.join(post_dir, post_fname)
                        posts.append(Post(title, date, post_fpath, path_depth, config))
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


class PathDepth(object):
    def __init__(self):
        self.base_path = '.'

    def set_base_path(self, path):
        self.base_path = os.path.dirname(path)

    def relative_path(self, path):
        if self.base_path == '.':
            return path
        return os.path.relpath(path, start=self.base_path)


class Post(object):
    def __init__(self, title, date, path, path_depth, config):
        self.title = title
        self.date = date
        self.path_depth = path_depth
        self.path = path  # input path: post_dir/post_fname
        # html path relative to site_dir/
        self.html_path = _get_html_path(title, date, config)
        # absolute html file path (to write file)
        self.abs_html_path = os.path.join(config['site_dir'], self.html_path)
        # absolute url if has site_url
        self.abs_url = None
        if config['site_url'] is not None:
            self.abs_url = os.path.join(config['site_url'], self.html_path)
        self.prev_post = None
        self.next_post = None

    @property
    def url(self):
        if self.abs_url is not None:
            return self.abs_url
        return self.path_depth.relative_path(self.html_path)



