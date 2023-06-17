#!/usr/bin/env python3
# This script looks for ./languages.toml file and generates ./grammar-sources.json from it

import tomllib
import json
import requests
import hashlib

def create_archive_source(archive_url, name):
    archive = requests.get(archive_url)
    sha256sum = hashlib.sha256(archive.content).hexdigest()

    return {
        'type': 'archive',
        'url': archive_url,
        'sha256': sha256sum,
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
        archive_url = f'{url}/archive/{commit}.tar.gz'
        print(f'[GITHUB]: {archive_url}')
        sources.append(create_archive_source(archive_url, name))
        
    elif url.startswith('https://gitlab.'):
        archive_url = f'{url}/-/archive/{commit}/archive.tar.gz'
        print(f'[GITLAB]: {archive_url}')
        sources.append(create_archive_source(archive_url, name))
        
    elif url.startswith('https://git.sr.ht'):
        archive_url = f'{url}/archive/{commit}.tar.gz'
        print(f'[SOURCEHUT]: {archive_url}')
        sources.append(create_archive_source(archive_url, name))

    elif url.startswith('https://codeberg.org'):
        archive_url = f'{url}/archive/{commit}.tar.gz'
        print(f'[CODEBERG]: {archive_url}')
        sources.append(create_archive_source(archive_url, name))
        
    else:
        print(f'[GIT]: {url} @ {commit}')
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