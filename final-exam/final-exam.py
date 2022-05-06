# Hunter Hanson
import sys, argparse, requests, bs4, json, socket

parser = argparse.ArgumentParser(description="This is the final exam script")

parser.add_argument('-i', '--ipaddress', dest='varIP', metavar='[an ip address]',
type=str, required=True, help='Enter an ip address')

parser.add_argument('-f', '--function', dest='varFunction', metavar='[a function (1-5)]',
type=int, required=True, help='Enter the number for a function 1, 2, 3, 4, or 5')



if len(sys.argv) == 1:
    (parser.print_help())
    sys.exit()

args = parser.parse_args()

if not 1 <= args.varFunction <= 5:
    (parser.print_help())
    sys.exit()

URL = f'http://{args.varIP}/q{args.varFunction}'
print (f"Name: Hunter Hanson\n{URL}")

def get_response(URL):
    res = requests.get(f'{URL}')
    try:
        res.raise_for_status()
    except:
        print ('There was a problem: %s' % (exc))
    print ("ANSWER:", res.text)
def parse_string(URL):
    res = requests.get(f'{URL}')
    try:
        res.raise_for_status()
    except:
        print ('There was a problem: %s' % (exc))
    HTMLsoup = bs4.BeautifulSoup(res.text, 'html.parser')
    h3elem = HTMLsoup.select('H3')
    string = h3elem[0].getText()
    sliced = string[4:21:2]
    print (f"ANSWER: {sliced} Hunter")
def parse_header(URL):
    res = requests.get(f'{URL}')
    try:
        res.raise_for_status()
    except:
        print ('There was a problem: %s' % (exc))
    print (f"ANSWER:", res.headers['MATC-HEADER'])
def parse_json(URL):
    res = requests.get(f'{URL}')
    try:
        res.raise_for_status()
    except:
        print ('There was a problem: %s' % (exc))
    jsonfile = json.dumps(json.loads(res.text))
    for key in jsonfile:
        if key['title'] == 'The Shining':
            print (jsonfile["publisher"])

def socket_client(ip):
    out_message = b"secret"
    in_message = ""
    try:
        for port in range(5000,6001):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                sock.send(out_message)
                in_message = sock.recv(1024)
                print("ANSWER:", in_message.decode())
                sys.exit()
            sock.close()
    except KeyboardInterrupt:
        sys.exit()
    except socket.error:
        print ("Could not connect")
        sys.exit()


if args.varFunction == 1:
    get_response(URL)
elif args.varFunction == 2:
    parse_string(URL)
elif args.varFunction == 3:
    parse_header(URL)
elif args.varFunction == 4:
    parse_json(URL)
elif args.varFunction == 5:
    socket_client(args.varIP)
