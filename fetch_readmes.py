import base64
import requests

GITHUB_API_URL = 'https://api.github.com/'

RUNME = False

def fetch_repo_readmes(username):
    resp = requests.get(GITHUB_API_URL + 'users/' + username + '/repos')
    repo_list = resp.json()
    readmes = []

    for repo in repo_list:
        readme_url = GITHUB_API_URL + 'repos/' + repo['full_name'] + '/contents/README.md'
        repo_resp = requests.get(readme_url)
        readme_json = repo_resp.json()
        if 'content' in readme_json:
            readme_text = base64.b64decode(readme_json['content'])
            readmes.append(readme_text)

    import pdb
    pdb.set_trace()
    return readmes


if RUNME:
    fetch_repo_readmes('octocat')