import json, os, random, shutil, sys
from distutils.dir_util import copy_tree
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown
from argparse import Namespace

env = Environment(loader=PackageLoader('ssg', 'templates'))

def write_to_file(path, content):
    with open(path, 'w', encoding='utf8') as f:
        f.write(content)

def create_directory(path):
    cartella = os.path.dirname(path)
    if not os.path.exists(cartella):
        os.makedirs(cartella)

def get_markdown_files():
    POSTS = {}

    file_path = 'content/'

    for md_file in os.listdir(file_path):
        md_file_path = os.path.join(file_path, md_file)

        # if it's not a directory, read it
        if not os.path.isdir(md_file_path):
            with open(md_file_path, 'r') as f:
                POSTS[md_file] = markdown(f.read(), extras=['metadata'])

    return POSTS


def articles(POSTS, post_template):
    for post in POSTS:
        post_metadata = POSTS[post].metadata
        post_data = {
            'content': POSTS[post],
            'slug': post_metadata['slug'],
            'title': post_metadata['title'],
            'summary': post_metadata['summary'],
            'category': post_metadata['category'],
            'date': post_metadata['date']
        }
        post_html_content = post_template.render(post=post_data)
        post_file_path = 'output/posts/{slug}.html'.format(slug=post_metadata['slug'])
        create_directory(post_file_path)
        write_to_file(post_file_path, post_html_content)

"""
Collect metadata of all the posts
for home page and sort them in reversed order

@param:
POSTS => Dictionary
"""
def get_posts_metadata(POSTS):
    posts_metadata = []
    for k,v in sorted(POSTS.items(), reverse=True):
        posts_metadata.append(v.metadata)
    return posts_metadata

"""
@params:
POSTS => Dictionary
template => jinja template
"""
def index(POSTS):
    posts_metadata = get_posts_metadata(POSTS)

    template = env.get_template('index.html')
    html_content = template.render(posts=posts_metadata)
    index_path = 'output/index.html'
    write_to_file(index_path, html_content)

def index_bici():
    bici_template = env.get_template('index_bici.html')
    # per ogni file nella directory track_data
    track_dir = 'track_data/'
    lista_tracce = []
    for track_file in os.listdir(track_dir):
        track_path = os.path.join(track_dir, track_file)
        with open(track_path, 'r') as f:
            data = json.load(f)
            lista_tracce.append(data)
    html_content = bici_template.render(listaTracce=lista_tracce)
    write_to_file('output/pages/bici.html', html_content)

def main(sec):
    # copy static files
    copy_tree('static/css', 'output/css')
    copy_tree('static/img', 'output/img')
    shutil.copyfile('static/favicon.ico', 'output/favicon.ico')

    # create directory structure
    create_directory('output/pages')

    sections = ['articles']
    for section in sections:
        POSTS = get_markdown_files()
        if section == "articles":
            posts_template = env.get_template('article.html')
            index(POSTS)
            articles(POSTS, posts_template)
        else:
            print("This section does not exist")

    index_bici()
