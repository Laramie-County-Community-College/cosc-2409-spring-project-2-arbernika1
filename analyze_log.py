import re
import os

def process_log_file(filename="access.log"):
    try:
        with open(filename, "r") as file:
            log_entries = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    url_frequencies = {}
    ip_addresses = set()
    error_total = 0

    for entry in log_entries:
        _, ip, url, status = extract_log_data(entry)
        if ip and url and status:
            ip_addresses.add(ip)
            url_frequencies[url] = url_frequencies.get(url, 0) + 1
            if int(status) >= 400:
                error_total += 1

    print(f"Number of Error Responses (4xx/5xx): {error_total}")
    print(f"Count of Unique IPs: {len(ip_addresses)}")
    print("Frequency of URL Requests:")
    [print(f"    {url}: {count}") for url, count in url_frequencies.items()]

def extract_log_data(line):
    # No changes needed here — this function works as intended.
    match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \"GET (.+) HTTP/1.1\" (\d+)", line)
    if match:
        timestamp, ip, url, status_code = match.groups()
        return timestamp, ip, url, status_code
    else:
        return None, None, None, None

# Run the log analyzer
process_log_file()
