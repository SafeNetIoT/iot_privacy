# Extract dns traffic and all DNS information
# Detect if there is a third-party DNS connection
# All DNS requests are deduplicated and classified. Finally, save these classification results to an Excel file.

import os
from scapy.all import *
from openpyxl import Workbook

def classify_domain(domain):
    # Classify DNS by related names...

    if "wyze" in domain:
        return "First/Support Party DNS"
    else:
        return "Other DNS need to be manually classified"

def analyze_pcap_files(folder_path):
    all_dns = []
    
    # loop through all pcap files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".pcap"):
            packets = rdpcap(os.path.join(folder_path, filename))
            for packet in packets:
                if packet.haslayer(DNS) and packet.getlayer(DNS).qd:  # check DNS
                    domain = packet.getlayer(DNS).qd.qname.decode('utf-8').rstrip('.')
                    all_dns.append(domain)
    
    # Unique
    unique_dns = list(set(all_dns))
    
    # Categorize
    categorized_dns = {domain: classify_domain(domain) for domain in unique_dns}
    return categorized_dns

folder_path = "/Users/liujia/Desktop/data/wyze_cam_pan_v2"

dns_data = analyze_pcap_files(folder_path)

# Save all DNS in Excel
workbook = Workbook()
sheet = workbook.active
sheet.title = "DNS Analysis"
sheet.append(["Domain", "Classification"])

for domain, classification in dns_data.items():
    sheet.append([domain, classification])
    if classification == "Other DNS need to be manually classified":
        print(domain)

workbook.save("/Users/liujia/Desktop/data/wyze_cam_pan_v2/dns_analysis.xlsx")

# Calculate the proportion of third-party DNS

# third_party_count = sum(1 for classification in dns_data.values() if classification == "Other DNS need to be manually classified")
# total_dns = len(dns_data)
# third_party_percentage = (third_party_count / total_dns) * 100

# print(f"Other DNS need to be manually classified: {third_party_count} out of {total_dns} ({third_party_percentage:.2f}%)")