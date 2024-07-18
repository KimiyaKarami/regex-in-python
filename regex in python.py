import re

def validate_email(email):
    if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return True
    else:
        return False

email1 = "kimiya@gmail.com"
email2 = "invalidemail@"
print(validate_email(email1))
print(validate_email(email2)) 

import jdatetime 
from datetime import datetime 
date_pattern = r'(\d{1,2})[-/](\d{1,2}|\w+)[-/](\d{2,4})' 

text = "Some dates: 11-07-2024, 9-7-2024, 9/7/2024, 9/7/24" 
matches = re.findall(date_pattern, text) 
for match in matches: 
    day, month, year = match
    if month.isdigit(): 
        m = int(month) 
        y = int(year) 
        d=int(day)
        gregorian_date = datetime(y, m,d ) 
        jalali_date =jdatetime.date.fromgregorian(day=d,month=m,year=y).strftime("%Y/%m/%d")
        print(f"Gregorian date: {gregorian_date.strftime('%Y-%m-%d')}, Jalali date: {jalali_date}")

def parse_log(log_str):
    pattern = r'(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}).*error\] (\d+)#(\d+): \*(\d+) (.+), client: ([\d.]+), server: ([\w.]+), request: "(.+)", upstream: "(.+)", host: "([\w.]+)", referrer: "(.+)"'
    result = re.match(pattern, log_str)
    if result:
        return result.groups()

log1 = '2024/07/11 15:30:45 [error] 1234#1234: *56789 connect() failed (111: Connection refused) while connecting to upstream, client: 192.168.1.100, server: example.com, request: "GET /api/data HTTP/1.1", upstream: "http://127.0.0.1:8000/api/data", host: "example.com", referrer: "https://example.com/"'
log2 = '2024/07/11 16:15:20 [error] 1234#1234: *67890 open() "/usr/share/nginx/html/not_found.html" failed (2: No such file or directory), client: 192.168.1.101, server: example.com, request: "GET /nonexistent-page HTTP/1.1", host: "example.com", referrer: "https://example.com/"'

print(parse_log(log1))
print(parse_log(log2))
