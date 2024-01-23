import shodan

SHODAN_API_KEY = "pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM"

def shodan_search(api, query):
    try:
        # Search Shodan
        results = api.search(query)

        # Show the results
        print('Results found: {}'.format(results['total']))
        return results['matches']
    except shodan.APIError as e:
        print('Error: {}'.format(e))
        return None

def get_domain_details(api, ip):
    try:
        # Lookup the host
        host = api.host(ip)

        # Extract relevant details
        details = {
            'IP': host['ip_str'],
            'Organization': host.get('org', 'n/a'),
            'Operating System': host.get('os', 'n/a'),
            'Banners': [{'Port': item['port'], 'Banner': item['data']} for item in host['data']]
        }

        return details
    except shodan.APIError as e:
        print('Error: {}'.format(e))
        return None

if __name__ == "__main__":
    api = shodan.Shodan(SHODAN_API_KEY)

    # Read domains from wordlist.txt
    with open('wordlist.txt', 'r') as file:
        domains = [line.strip() for line in file.readlines()]

    for domain_to_search in domains:
        print(f"\nSearching Shodan for: {domain_to_search}")

        # Perform Shodan search
        matches = shodan_search(api, domain_to_search)

        if matches:
            # Extract details for the first match
            first_match_ip = matches[0]['ip_str']
            details = get_domain_details(api, first_match_ip)

            if details:
                # Print the details
                print("\nSHODAN RESULTS:")
                for key, value in details.items():
                    if isinstance(value, list):
                        print(f"{key.upper()}:")
                        for item in value:
                            print(f"  - {item}")
                    else:
                        print(f"{key.upper()}: {value}")
            else:
                print("No details found.")
