import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        status_code = r.status_code
        body = r.json()

        return status_code, body

    def get_list_repo_commits(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
        url = r.url
        status_code = r.status_code
        body = r.json()

        return status_code, url, body

    def get_list_repo_languages(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/languages")
        status_code = r.status_code
        body = r.json()

        return status_code, body
