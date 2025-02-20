import os
import sys
import shutil
import email
import email.policy
from email.utils import parsedate_to_datetime
from dateutil import tz

def print_email_datetime(eml_path):
    with open(eml_path, 'r', encoding='utf-8') as file:
        msg = email.message_from_file(file, policy=email.policy.default)

    date_header = msg['Date']
    if date_header:
        try:
            mail_datetime = parsedate_to_datetime(date_header)
            if mail_datetime.tzinfo is None:
                mail_datetime = mail_datetime.replace(tzinfo=tz.UTC)
            local_datetime = mail_datetime.astimezone(tz.tzlocal())
            return local_datetime.strftime('%Y-%m-%dT%H-%M-%S')
        except Exception as e:
            print(f"Error parsing date: {e}")
            return None
    else:
        print("No Date header found in the email.")
        return None

def copy_eml_files_with_timestamp(input_dir, output_dir):
    total_emails = 0
    successfully_renamed = 0
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.eml'):
                total_emails += 1
                eml_path = os.path.join(root, file)
                timestamp = print_email_datetime(eml_path)
                if timestamp:
                    relative_path = os.path.relpath(root, input_dir)
                    dest_dir = os.path.join(output_dir, relative_path)
                    os.makedirs(dest_dir, exist_ok=True)
                    new_filename = f"{timestamp} {file}"
                    shutil.copy2(eml_path, os.path.join(dest_dir, new_filename))
                    successfully_renamed += 1
    print(f"Successfully renamed {successfully_renamed} of {total_emails} emails.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_directory> <output_directory>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    copy_eml_files_with_timestamp(input_directory, output_directory)
