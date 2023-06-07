#!/usr/bin/env python3
# This script looks for ./languages.toml file and generates ./grammar-sources.json from it

import tomllib
import json
import requests
import hashlib

def create_guthub_source(name, url, commit):
    archive_url = f'{url}/archive/{commit}.tar.gz'

    print(f'downloading {archive_url}...')
    archive = requests.get(archive_url)
    sha256sum = hashlib.sha256(archive.content)

    return {
        'type': 'archive',
        'url': archive_url,
        'sha256': sha256sum.hexdigest(),
        'dest': f'grammars/{name}'
    }

with open('languages.toml', 'rb') as languages_toml:
    toml = tomllib.load(languages_toml)

sources = []
paths = ''

for grammar in toml['grammar']:
    name: str = grammar['name']
    url: str = grammar['source']['git']
    commit: str = grammar['source']['rev']

    if 'subpath' in grammar['source']:
        subpath = grammar['source']['subpath']
        paths += f'{name} grammars/{name}/{subpath}\n'
    else:
        paths += f'{name} grammars/{name}\n'

    if url.startswith('https://github.com'):
        sources.append(create_guthub_source(name, url, commit))
    else:
        sources.append({
            'type': 'git',
            'url': url,
            'commit': commit,
            'dest': f'grammars/{name}'
        })


sources.append({
    'type': 'inline',
    'dest-filename': 'paths.txt',
    'contents': paths
})

with open('grammar-sources.json', 'w') as grammar_sources_json:
    json.dump(sources, grammar_sources_json, indent=4)