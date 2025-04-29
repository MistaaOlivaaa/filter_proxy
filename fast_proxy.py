import requests

def check_fast_proxy(proxy_d):
    timeout = 10
    url = "https://ifconfig.me/ip"
    socks_proxy = {
        'http': f'socks5://{proxy_d}',
        'https': f'socks5://{proxy_d}'
    }
    
    try:
        response = requests.get(url, proxies=socks_proxy, timeout=timeout)
        if response.status_code == 200:
            print(f"Working proxy: {proxy_d} (IP: {response.text.strip()})")
            return True
    except Exception as e:
        print(f"Failed proxy: {proxy_d} - Error: {str(e)}")
    return False

def read_data_from_file(filename):
    working_proxies = []
    try:
        with open(filename, 'r') as read_file:
            file_data = read_file.readlines()
        
        for line in file_data:
            line = line.strip()
            if line:  # Skip empty lines
                if check_fast_proxy(line):
                    working_proxies.append(line)
                    
        return working_proxies
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return []
    
if __name__ == "__main__":
    proxy_file = "socks5.txt" 
    working = read_data_from_file(proxy_file)
    print(f"\nFound {len(working)} working proxies:")
    for proxy in working:
        print(proxy)