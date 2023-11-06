import requests

def download_resource(remote, local):
    r = requests.get(remote)
    r.raise_for_status()
    with open(local, 'w') as f:
        f.write(r.text)
