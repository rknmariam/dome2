import requests

def verify_shodan_api_key(api_key):
    url = f'https://api.shodan.io/account/profile?key={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if 'error' in data:
            print(f"Invalid API key {api_key}: {data['error']}")
            return False
        else:
            print(f"API key {api_key} is valid. Remaining credits: {data['credits']}")
            return True

    except requests.exceptions.RequestException as e:
        print(f"Error while verifying API key {api_key}: {e}")
        return False

# Replace 'your_api_key_here' with your actual Shodan API keys
api_keys = ['aSerusL0GjGzwCneaHEy6bwY7ix6aWPp']

for key in api_keys:
    verify_shodan_api_key(key)

