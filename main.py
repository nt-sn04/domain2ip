import socket
import json


def get_ip_by_domain(domain: str) -> str:
    return socket.gethostbyname(domain)


def main() -> None:
    with open('domains.json') as jsonfile:
        data = json.loads(jsonfile.read())

    for domain in data['domains']:
        data['ips'].append({
            'domain': domain,
            'ip': get_ip_by_domain(domain)
        })

    with open('domains.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))

main()
