# Look for unencrypted communications, especially those involving sensitive information. (For example, unencrypted HTTP communication could lead to data leakage.)
# For each TCP packet, the payload (Payload) is extracted and converted to string form for easy analysis.
# Call the is_unencrypted_http_request function to check if the payload represents an unencrypted HTTP request,
# And whether it contains sensitive information (assuming sensitive information is transmitted in clear text).

import csv
# import openpyxl
import pandas as pd
import os
from scapy.all import rdpcap, TCP, UDP


# keywords
keywords = ["username", "ip address", "iotlab", "password","passwd",
            "pass","pwd","user","userid","ucliotlab@gmail.com", 
            "login","logon","account","admin","root",
            "guest"," email","mail","address","postal",
            "zip","postcode","credit card","card number","card num",
            "cvv","cvv2","ccv","expiry","expiration",
            "expdate","social security","ssn","dob","date of birth",
            "birth date","phone number","phone","mobile","cell",
            "name","first name","last name","middle name","full name",
            "session","ucl","iot","lab","university of london",
            "cookie","session id","token","swift",
            "auth","authorization","authenticate","authentication","otp",
            "one time password","two factor","2 factor","backup code","recovery code",
            "reset password","change password","pin","bank","banking",
            "routing","sort code","account number","security question","security answer",
            "iban","bic","secret question","secret answer","mothersmaiden name",
            "pet name","license","passport","student",
            "ssn","mac address","port","gateway","dns",
            "ntp","sensor","command","control","ctrl",
            "setting","response","request","value","connect",
            "disconnect","location","gps","log","time stamp",
            "restart","encryption","permission","role","subscription",
            "protocol","patch","upgrade","debug","warning",
            "message","send","receive","transfer","vendor"]


def contains_keywords(payload_str):
    for keyword in keywords:
        if keyword in payload_str:
            return True
    return False

def is_unencrypted_communication(packet):
    try:
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload_str = str(packet.payload)
            return contains_keywords(payload_str)
        return False
    except:
        return False

def analyze_pcap_file(file_path):
    packets = rdpcap(file_path)
    total_tcp_udp_packets = 0
    unencrypted_packets = 0

    for packet in packets:
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            total_tcp_udp_packets += 1
            if is_unencrypted_communication(packet):
                unencrypted_packets += 1

    return total_tcp_udp_packets, unencrypted_packets

def main():
    directory = "/Users/liujia/Desktop/data/wyze_cam_pan_v2"  # pcap file folder path
    total_tcp_udp = 0
    total_unencrypted = 0

    for file_name in os.listdir(directory):
        if file_name.endswith(".pcap"):
            file_path = os.path.join(directory, file_name)
            tcp_udp, unencrypted = analyze_pcap_file(file_path)
            total_tcp_udp += tcp_udp
            total_unencrypted += unencrypted

    print(f"Total TCP/UDP packets: {total_tcp_udp}")
    print(f"Total unencrypted packets: {total_unencrypted}")
    if total_tcp_udp != 0:
        percentage = (total_unencrypted / total_tcp_udp) * 100
        print(f"Percentage of unencrypted TCP/UDP messages: {percentage:.2f}%")

if __name__ == "__main__":
    main()