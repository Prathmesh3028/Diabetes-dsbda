import requests

def test_api():
    urls_to_test = [
        "http://127.0.0.1:8000/",
        "http://localhost:8000/",
        "http://127.0.0.1:8000/api/health",
        "http://localhost:8000/api/health"
    ]
    
    for url in urls_to_test:
        try:
            print(f"\nTesting connection to: {url}")
            response = requests.get(url)
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text}")
        except Exception as e:
            print(f"Error with {url}: {e}")

if __name__ == "__main__":
    test_api() 