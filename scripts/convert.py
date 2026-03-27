#!/usr/bin/env python3
"""
Trackers List Converter
Convert trackers from ngosang/trackerslist to OpenClash rules format
"""

import os
import requests
import yaml
from datetime import datetime
from urllib.parse import urlparse

# Configuration
TRACKERS_URL = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"
OUTPUT_FILE = "rule/Custom_Direct.yaml"
GITHUB_REPO = "https://github.com/ngosang/trackerslist"


def extract_domain(url):
    """Extract domain from URL"""
    try:
        parsed = urlparse(url.strip())
        return parsed.netloc.lower()
    except Exception:
        return None


def fetch_trackers():
    """Fetch trackers list from source"""
    print(f"Fetching trackers from {TRACKERS_URL}...")
    response = requests.get(TRACKERS_URL, timeout=30)
    response.raise_for_status()
    
    trackers = []
    for line in response.text.strip().split('\n'):
        line = line.strip()
        if line and not line.startswith('#'):
            domain = extract_domain(line)
            if domain:
                trackers.append(domain)
    
    print(f"Found {len(trackers)} trackers")
    return sorted(set(trackers))


def generate_yaml(trackers):
    """Generate YAML content with OpenClash rules format"""
    # Header
    total = len(trackers)
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    
    header_lines = [
        "# Generated from rule/Custom_Direct.yaml",
        f"# REPO: {GITHUB_REPO}",
        f"# SOURCE: {TRACKERS_URL}",
        f"# TOTAL: {total}",
        f"# UPDATED: {timestamp}",
        "",
        "payload:",
    ]
    
    # Generate rules
    payload_lines = [f"  - DOMAIN-SUFFIX:{domain}" for domain in trackers]
    
    return '\n'.join(header_lines + payload_lines)


def main():
    """Main function"""
    # Create output directory if not exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    # Fetch trackers
    trackers = fetch_trackers()
    
    # Generate YAML
    yaml_content = generate_yaml(trackers)
    
    # Write to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(yaml_content)
    
    print(f"Written {len(trackers)} rules to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()