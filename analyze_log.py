import re
import os


def analyze_log_file(filename="access.log"):
    try:
        with open(filename, "r") as file:
            log_lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: Log file '{filename}' not found.")
        return

    url_counts = {}
    unique_ips = set()
    error_count = 0

    for line in log_lines:
        _, ip, url, status = extract_log_data(line)
        if ip and url and status:
            unique_ips.add(ip)
            url_counts[url] = url_counts.get(url, 0) + 1
            error_count += int(status) >= 400

    print(f"Total Errors (4xx and 5xx): {error_count}")
    print(f"Unique IP Addresses: {len(unique_ips)}")
    print("URL Access Counts:")
    [print(f"    {url}: {count}") for url, count in url_counts.items()]


def extract_log_data(line):
    #please note that you do not need to edit this function, just the analyze_log_file function above!
    #example usage: timestamp, ip, url, status_code = extract_log_data(line)
    
    match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \"GET (.+) HTTP/1.1\" (\d+)", line)
    if match:
        timestamp, ip, url, status_code = match.groups()
        return timestamp, ip, url, status_code
    else:
        return None, None, None, None


# Generate a sample log file (uncomment to create the file)
# generate_log_file()

# Analyze the log file
analyze_log_file()
