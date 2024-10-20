[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FCyVenom%2FWayback&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# Wayback URLs Fetcher

A simple Python script to fetch archived URLs from the Wayback Machine for a given domain. This tool allows you to gather historical URLs and subdomains for web applications, aiding in research, security assessments, and web scraping.

## Features

- **Fetch URLs**: Retrieve archived URLs for a specified domain.
- **Subdomain Support**: Optionally include subdomains in your search.
- **User-Friendly Output**: Display results directly in the terminal for easy access.
- **Error Handling**: Gracefully handles network and JSON decoding errors.

## Prerequisites

- Python 3.x
- `requests` library

### Installation

You can install the required library using pip:

```bash
pip install requests
```

## Usage

-python waybackurls.py <url> [include_subdomains]

## Example 1

-python waybackurls.py https://example.com

[*] Found 3 URLs:
http://example.com/page1
http://example.com/page2
http://example.com/about

## Example 2

-python waybackurls.py https://example.com include_subdomains

[*] Found 5 URLs:
http://example.com/page1
http://blog.example.com/article1
http://shop.example.com/item1
http://example.com/page2
http://example.com/about
