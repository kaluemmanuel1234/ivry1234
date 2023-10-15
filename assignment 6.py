#Assignment 1
def convert_to_uppercase(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.upper(), end='')
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    convert_to_uppercase(file_name)

#Assignment 2
def extract_host_from_email(email):
    _, host = email.split("@", 1)
    return host

def process_mbox_file(filename):
    email_hosts = set()
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("From:"):
                    parts = line.split()
                    if len(parts) >= 2:
                        email = parts[1]
                        host = extract_host_from_email(email)
                        if host:
                            email_hosts.add(host)

        print("Unique email hosts:")
        for host in email_hosts:
            print(host)

        print("Number of unique email hosts:", len(email_hosts))
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)

if __name__ == "__main__":
    file_name = "mbox.txt"  
    process_mbox_file(file_name)




#Assignment 3
def process_file(filename):
    total_confidence = 0.0
    count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    try:
                        confidence = float(line.split(":")[1].strip())
                        total_confidence += confidence
                        count += 1
                    except ValueError:
                        print(f"Skipping line with invalid confidence value: {line}")

        print("Extracted confidence values:", total_confidence)

        if count > 0:
            average_confidence = total_confidence / count
            print("Average confidence:", average_confidence)
        else:
            print("No valid confidence values found in the file.")
    except FileNotFoundError:
        print("Error: File not found.")
        exit(1)

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    process_file(file_name)
