import requests
import json

API_URL = 'https://jsonplaceholder.typicode.com/posts'

def fetch_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(data)
            return data

        else:
            print(f'Error fetching data. Status code: {response.status_code}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    fetch_data()
