import os


def post_builder(post, path_depth, config, template):
    # set path depth to the current post
    path_depth.set_base_path(post.html_path)
    # content =