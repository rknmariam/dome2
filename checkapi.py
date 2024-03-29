from shodan import Shodan, APIError
import time

def check_api_key(api_key):
    try:
        api = Shodan(api_key)
        account_info = api.info()

        print(f"API Key: {api_key}")
        print(f"Account Information:\n{account_info}")
        print("------")

    except APIError as e:
        print(f"Error: {e}")

# Replace the following list with your actual Shodan API keys
api_keys = ['OefcMxcunkm72Po71vVtX8zUN57vQtAC',
'PSKINdQe1GyxGgecYz2191H2JoS9qvgD',
'pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM',
'61TvA2dNwxNxmWziZxKzR5aO9tFD00Nj',
'xTbXXOSBr0R65OcClImSwzadExoXU4tc',
'EJV3A4Mka2wPs7P8VBCO6xcpRe27iNJu',
'mEuInz8UH1ixLGJq4oQhEiJORERVG5xc',
'lkY0ng0XMo29zEhzyw3ibQfeEBxghwPF',
'syeCnFndQ8TE4qAGvhm9nZLBZOBgoLKd',
'7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib61',
'v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik',
'dTNGRiwYNozXIDRf5DWyGNbkdiS5m3JK',
'kdnzf4fsYWQmGajRDn3hB0RElbUlIaqu',
'boYedPn8iDWi6GDSO6h2kz72VLt6bZ3S',
'FQNAMUdkeqXqVOdXsTLYeatFSpZSktdb',
'OygcaGSSq46Lg5fZiADAuFxl4OBbn7zm',
'XAbsu1Ruj5uhTNcxGdbGNgrh9WuMS1B6',
'nkGd8uVE4oryfUVvioprswdKGmA5InzZ',
'XYdjHDeJM36AjDfU1feBsyMJIj8XxGzD',
'EBeU0lGqtIO6yCxVFCWC4nUVbvovtjo5',
'LCDrehJT6fDnDpWTEamTdogkgCXDw8mw'
]

for key in api_keys:
    check_api_key(key)
    time.sleep(1)

pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM