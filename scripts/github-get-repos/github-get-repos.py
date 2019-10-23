#!/usr/bin/env python3
from github import Github

github = Github()

github_org = github.get_organization('opennms-config-modules')
github_repos = github_org.get_repos()

git_urls = list()

for repository in github_repos:
    if not repository.full_name.endswith('/meta'):
        git_urls.append(repository.clone_url)

for clone_url in sorted(git_urls):
    print("git submodule add -b master " + clone_url)
