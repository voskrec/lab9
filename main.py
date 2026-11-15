ips = [
    "192.168.1.3", "10.0.0.5", "192.168.1.1",
    "172.16.4.1", "10.0.0.5", "8.8.8.8"
]

# Через множество (быстро)
unique_ips = set(ips)

# Сортировка (сначала по первому октету)
sorted_ips = sorted(unique_ips, key=lambda ip: tuple(map(int, ip.split('.'))))

for ip in sorted_ips:
    print(ip)