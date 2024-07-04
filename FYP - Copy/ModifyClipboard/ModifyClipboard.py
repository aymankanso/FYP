import win32clipboard
import re
import argparse
from time import sleep

# Regular expressions for various types of sensitive information
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_regex = r'\b(?:\d{3}[-.]?|\(\d{3}\) )?\d{3}[-.]?\d{4}\b'
url_regex = r'\bhttps?://\S+\b'
date_regex = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
credit_card_regex = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
ssn_regex = r'\b\d{3}-\d{2}-\d{4}\b'

# Description for each type of sensitive information
email_regex_description = "Email addresses"
phone_regex_description = "Phone numbers"
url_regex_description = "URLs"
date_regex_description = "Dates"
ip_regex_description = "IP addresses"
credit_card_regex_description = "Credit card numbers"
ssn_regex_description = "Social security numbers"

def replace_sensitive_info(data, pattern, replacement):
    """Replace sensitive information in clipboard data."""
    modified_data = re.sub(pattern, replacement, data)
    return modified_data

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Replace sensitive information in clipboard data.")
    parser.add_argument("--type", choices=['email', 'phone', 'url', 'date', 'ip', 'credit_card', 'ssn'], required=True, help="Type of sensitive information to replace")
    parser.add_argument("--replacement", required=True, help="Replacement value for sensitive information")
    return parser.parse_args()

def main():
    """Main function."""
    args = parse_arguments()
    choices = {
        'email': (email_regex, email_regex_description),
        'phone': (phone_regex, phone_regex_description),
        'url': (url_regex, url_regex_description),
        'date': (date_regex, date_regex_description),
        'ip': (ip_regex, ip_regex_description),
        'credit_card': (credit_card_regex, credit_card_regex_description),
        'ssn': (ssn_regex, ssn_regex_description)
    }

    pattern, pattern_description = choices[args.type]
    replacement = args.replacement

    try:
        while True:
            win32clipboard.OpenClipboard()
            data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            modified_data = replace_sensitive_info(data, pattern, replacement)

            if modified_data != data:
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.SetClipboardText(modified_data)
                win32clipboard.CloseClipboard()
                print(f"Replaced {pattern_description} in clipboard with custom value")
                break

            sleep(1)

    except KeyboardInterrupt:
        print("Script terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
