import requests

def fetch_resumes(url: str) -> list[dict] | None:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching resumes from {url}: {e}")
        return None
    
irmas_url = "https://recruiting-test-resume-data.hiredscore.com/allcands-full-api_hub_b1f6-acde48001122.json"
print(fetch_resumes(irmas_url))