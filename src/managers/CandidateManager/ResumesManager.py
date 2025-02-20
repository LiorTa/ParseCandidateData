import requests

def fetch_resumes(url: str) -> list[dict] | None:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching resumes from {url}: {e}")
        return None

