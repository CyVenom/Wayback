import requests
import sys
import json
import time

def waybackurls(host, with_subs):
    """Fetch URLs from the Wayback Machine for the given host."""
    # Construct the appropriate URL based on subdomain inclusion
    if with_subs:
        url = f'http://web.archive.org/cdx/search/cdx?url=*.{host}/*&output=json&fl=original&collapse=urlkey'
    else:
        url = f'http://web.archive.org/cdx/search/cdx?url={host}/*&output=json&fl=original&collapse=urlkey'
    
    try:
        # Fetch data from the Wayback Machine
        print(f"[*] Fetching data from Wayback Machine for {host} (include_subdomains={with_subs})...")
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # Raise an error for HTTP issues

        # Parse the JSON response
        results = r.json()
        if len(results) <= 1:
            print("[-] No URLs found in the Wayback Machine.")
            return []

        return results[1:]  # Exclude the header row from the results
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
        return []

def normalize_url(url):
    """Normalize the URL by removing the protocol and trailing slashes."""
    url = url.strip().rstrip('/')
    if url.startswith('http://'):
        return url[7:]
    elif url.startswith('https://'):
        return url[8:]
    return url

def print_results(urls):
    """Print the retrieved URLs to the console."""
    if urls:
        print(f"[*] Found {len(urls)} URLs:")
        for url in urls:
            print(url[0])  # Print the original URL (first column of the result)
    else:
        print('[-] No URLs found.')

def main():
    argc = len(sys.argv)
    if argc < 2:
        print('Usage:\n\tpython waybackurls.py <url> [include_subdomains]')
        sys.exit(1)

    # Normalize the provided host URL
    host = normalize_url(sys.argv[1])
    with_subs = argc == 3  # Check if the optional subdomains argument is given

    start_time = time.time()  # Measure script execution time
    urls = waybackurls(host, with_subs)
    print_results(urls)  # Print the results instead of saving them

    elapsed_time = time.time() - start_time
    print(f"[*] Completed in {elapsed_time:.2f} seconds.")

if __name__ == '__main__':
    main()
