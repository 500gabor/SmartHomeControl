import requests
import sys
import random
from urllib.parse import urlparse


def extract_ip(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Get the netloc (host:port) or path for cases without "http"
    ip = parsed_url.netloc or parsed_url.path

    return ip

def set_temp():
    # Define the Node-RED HTTP In node endpoint
    try:
        ip = sys.argv[1]
        ip = extract_ip(ip)
    except:
        print("No URL given, using default")
        ip = "127.0.0.1:1880"
    url = f"http://{ip}//temperature_in"

    # Add the temperature as a query parameter
    temperature = random.randint(-20, 60)
    params = {
        "payload": str(temperature)
    }

    # Make the GET request
    response = requests.get(url, params=params, timeout=5)

    # Print the response from Node-RED
    print("Response status code:", response.status_code)
    print("Response content:", response.text)

if __name__ == "__main__":
    set_temp()
