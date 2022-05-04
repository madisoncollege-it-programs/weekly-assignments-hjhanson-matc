import argparse
import sys
import json
import requests

parser = argparse.ArgumentParser(description="This script will get information about an IP address")

parser.add_argument('--ipaddress', dest='varIP', metavar='[An IP address]',
type=str, required=False, help='Enter a valid IP address')

args = parser.parse_args()

if len(sys.argv) == 1:
    (parser.print_help())
    exit(0)


url = f'http://ipinfo.io/{args.varIP}/json'

jsonResp = requests.get(url)

dictResp = json.loads(jsonResp.text)


for key in dictResp.keys():
    print(f"{key: <10}:{dictResp[key]: <10}")
