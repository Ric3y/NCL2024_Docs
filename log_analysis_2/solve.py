#this only solves problem 2 and 3
from collections import Counter

def process_log(log_file):
    ip_addresses = []
    
    with open(log_file, 'r') as file:
        for line in file:
            if "[client" in line:
                # Extract IP address between "[client " and the closing "]"
                start_index = line.find("[client ") + len("[client ")
                end_index = line.find("]", start_index)
                ip_address = line[start_index:end_index]
                ip_addresses.append(ip_address)
    
    # Find the number of unique IP addresses
    unique_ips = set(ip_addresses)
    unique_ip_count = len(unique_ips)
    
    # Find the IP address that generated the most errors
    ip_counter = Counter(ip_addresses)
    most_common_ip, most_common_count = ip_counter.most_common(1)[0]

    return unique_ip_count, most_common_ip, most_common_count

log_file = 'error.log'

unique_ip_count, most_common_ip, most_common_count = process_log(log_file)

print(f"Number of unique IP addresses: {unique_ip_count}")
print(f"IP address that generated the most errors: {most_common_ip} with {most_common_count} errors")

