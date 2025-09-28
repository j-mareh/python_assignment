import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url, content):
    """
    Extract filename from URL. If missing, generate one using a hash of the content.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # If URL has no filename, generate one using hash of content
    if not filename or '.' not in filename:
        hash_name = hashlib.sha1(content).hexdigest()[:10]
        filename = f"image_{hash_name}.jpg"

    return filename

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    url = input("Please enter the image URL: ").strip()

    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Check content type before saving
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type.lower():
            print("✗ The provided URL does not appear to be an image.")
            return

        # Extract filename or generate one
        filename = get_filename_from_url(url, response.content)

        # Build full file path
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicate downloads
        if os.path.exists(filepath):
            print(f"✓ Image already exists: {filename}")
            print(f"✓ Located at {filepath}")
            return

        # Save the image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()
