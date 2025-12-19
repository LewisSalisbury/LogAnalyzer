import re
from collections import defaultdict

THRESHOLD = 5
LOG_FILE = "sample2.log"



def extract_ip(line):
    pattern = re.compile(r"ip=(\d+\.\d+\.\d+\.\d+)")
    match = pattern.search(line)
    if match:
        return match.group(1)
    return None


def process_line(line, failed_login):
    #process log line, increment failed login count if ip failed login
    if "FAILED_LOGIN" in line:
        ip = extract_ip(line)
        if ip:
            failed_login[ip] += 1


def flag_suspicious_ips(failed_login, threshold=THRESHOLD):
    #return list of tuples of failed ips and attempt count
    return [(ip, count) for ip, count in failed_login.items() if count > threshold]


def print_report(suspicious_ips):
    if suspicious_ips:
        print("Suspicious IPs Detected")
        for ip, count in suspicious_ips:
            print(f"{ip} - {count} failed attempts")
    else:
        print("No suspicious activity detected.")


def main():
    failed_login = defaultdict(int)
    #read log line by line
    with open(LOG_FILE) as log_file:
        for line in log_file:
            process_line(line, failed_login)

    suspicious_ips = flag_suspicious_ips(failed_login)
    print_report(suspicious_ips)


if __name__ == "__main__":
    main()
