# currently only works for question 2 and 3

import re
from collections import defaultdict

def analyze_access_log(file_path):
    total_requests = 0
    root_requests = 0
    status_405_count = 0
    ip_requests = defaultdict(int)
    total_bytes_transferred = 0

    # Define a regex pattern to parse the log entries
    log_pattern = re.compile(
        r'(?P<ip>\S+) - - \[(?P<date>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) HTTP/\d\.\d" (?P<status>\d{3}) (?P<size>\d+|-)'
    )

    with open(file_path, 'r') as log_file:
        for line in log_file:
            match = log_pattern.search(line)
            if match:
                total_requests += 1
                ip = match.group('ip')
                path = match.group('path')
                status = match.group('status')
                size = match.group('size')

                # Count requests for the root path
                if path == '/':
                    root_requests += 1
                
                # Count requests with a 405 status code
                if status == '405':
                    status_405_count += 1

                # Count requests by IP address
                ip_requests[ip] += 1

                # Add to total bytes transferred (skip if size is '-')
                if size != '-':
                    total_bytes_transferred += int(size)

    # Determine the IP address with the most requests
    most_requests_ip = max(ip_requests, key=ip_requests.get)
    most_requests_count = ip_requests[most_requests_ip]

    print(f"Total requests for '/': {root_requests}")
    print(f"Total requests with a 405 status code: {status_405_count}")
    print(f"IP address with the most requests: {most_requests_ip} ({most_requests_count} requests)")
    print(f"Total bytes transferred: {total_bytes_transferred}")

if __name__ == "__main__":
    log_file_path = 'access.log'
    analyze_access_log(log_file_path)

