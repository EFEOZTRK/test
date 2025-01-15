import os

def main():
    api_key = os.getenv('API_KEY', 'default_key')
    print(f"API Key: {api_key}")

if __name__ == "__main__":
    main()