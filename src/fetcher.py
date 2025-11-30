import requests

def fetch(url):
    try:
        response = requests.get(url, timeout=5)
        return {
            "html": response.text,
            "headers": response.headers,
            "status_code": response.status_code
        }
    except Exception as e:
        return {
            "error": str(e)
        }