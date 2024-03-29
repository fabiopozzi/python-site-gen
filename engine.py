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


def get_markdown_pages():
    pages = {}
    file_path = 'pages/'
    e = ['code-friendly', 'cuddled-lists', 'fenced-code-blocks', 'tables',
            'footnotes', 'smarty-pants', 'numbering', 'tables', 'strike',
            'spoiler']

    for md_file in os.listdir(file_path):
        md_file_path = os.path.join(file_path, md_file)

        # if it's not a directory, read it
        if not os.path.isdir(md_file_path):
            with open(md_file_path, 'r') as f:
                pages[md_file] = markdown(f.read(), extras=e)

    return pages


def get_markdown_posts():
    posts = {}
    file_path = 'content/'

    for md_file in os.listdir(file_path):
        md_file_path = os.path.join(file_path, md_file)

        # if it's not a directory, read it
        if not os.path.isdir(md_file_path):
            with open(md_file_path, 'r') as f:
                posts[md_file] = markdown(f.read(), extras=['metadata', 'fenced-code-blocks'])
    return posts


def render_pages(page_list, page_template):
    for p in page_list:
        page_metadata = page_list[p].metadata
        if page_metadata is None:
            print("metadata vuoti")
        else:
            page_data = {
                'content': page_list[p],
                'slug': page_metadata['slug'],
                'title': page_metadata['title'],
            }
            page_html_content = page_template.render(page=page_data)
            page_file_path = 'output/pages/{slug}.html'.format(slug=page_metadata['slug'])
            write_to_file(page_file_path, page_html_content)


def render_articles(posts, post_template):
    for p in posts:
        post_metadata = posts[p].metadata
        if post_metadata is None:
            print("metadata vuoti")
        else:
            try:
                post_data = {
                    'content': posts[p],
                    'slug': post_metadata['slug'],
                    'title': post_metadata['title'],
                    'summary': post_metadata['summary'],
                    'category': post_metadata['category'],
                    'date': post_metadata['date'],
                    'image_url': post_metadata['image_url']
                }
            except TypeError:
                print(post_metadata)
                continue
            post_html_content = post_template.render(post=post_data)
            post_file_path = 'output/posts/{slug}.html'.format(slug=post_metadata['slug'])
            write_to_file(post_file_path, post_html_content)



"""
Extract datetime from metadata object.
To be used for sorting posts by date
"""
def per_data(valore):
    d = datetime.strptime(valore['date'], "%d-%m-%Y")
    return d


"""
Collect metadata of all the posts
for home page and sort them by date

@param:
POSTS => Dictionary
"""
def get_posts_metadata(POSTS):
    posts_metadata = []
    for k,v in POSTS.items():
        posts_metadata.append(v.metadata)

    sorted_posts_metadata = sorted(posts_metadata, key=per_data, reverse=True)
    return sorted_posts_metadata

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
    track_template = env.get_template('traccia.html')
    # per ogni file nella directory track_data
    track_dir = 'track_data/'
    lista_tracce = []
    for track_file in os.listdir(track_dir):
        track_path = os.path.join(track_dir, track_file)
        with open(track_path, 'r') as f:
            data = json.load(f)
            data['link'] = '/pages/bici/tracce/' + data['nome_file'] + '.html'
            track_path = 'output/pages/bici/tracce/' + data['nome_file'] + '.html'
            lista_tracce.append(data)
            # render track page
            html_content = track_template.render(traccia=data)
            write_to_file(track_path, html_content)

    html_content = bici_template.render(listaTracce=lista_tracce)
    write_to_file('output/pages/bici.html', html_content)

def main():
    # copy static files
    copy_tree('static/css', 'output/css')
    copy_tree('static/img', 'output/img')
    copy_tree('static/gpx', 'output/gpx')
    copy_tree('static/js', 'output/js')
    shutil.copyfile('static/favicon.ico', 'output/favicon.ico')

    # create directory structure
    create_directory('output/pages/')
    create_directory('output/posts/')
    create_directory('output/pages/bici/')
    create_directory('output/pages/bici/tracce/')

    # render posts
    posts = get_markdown_posts()
    post_template = env.get_template('article.html')
    index(posts)
    render_articles(posts, post_template)

    # render pages
    pages = get_markdown_pages()
    page_template = env.get_template('page.html')
    render_pages(pages, page_template)

    # render tracks
    index_bici()
