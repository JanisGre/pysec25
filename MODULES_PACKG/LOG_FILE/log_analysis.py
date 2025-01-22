# import libraries
import re

# log file location
log_file_path = '/Users/janis/Desktop/ViA/PYTHON_DROSIBAS_TESTETAJIEM/GIT/usb_log_sample.log'

# check usb log file for "usb" keyword
def get_unique_usb_logs(file_path):
    try:
        # read all lines
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # check if there is a content in file
            if not lines:
                print("Empty file")
                return

            # store unique USB logs
            usb_logs = set()

            # loop through code and look for 'usb' keyword
            for line in lines:
                if 'usb' in line.lower(): 
                    usb_logs.add(line.strip()) 

            # check if USB logs were found
            if usb_logs:
                print("Unique USB logs:")
                for log in usb_logs:
                    
                    device_info = {
                        'idVendor': re.search(r'idVendor=([0-9A-Fa-f]+)', log),
                        'idProduct': re.search(r'idProduct=([0-9A-Fa-f]+)', log),
                        'Product': re.search(r'Product:\s*([^,]+)', log),
                        'Manufacturer': re.search(r'Manufacturer:\s*([^,]+)', log),
                        'SerialNumber': re.search(r'SerialNumber:\s*([^,]+)', log)
                    }

                    # only print log details if at least one field is found
                    log_details = [f"{key}: {match.group(1)}" for key, match in device_info.items() if match]
                    if log_details:
                        print("Log details:")
                        print("\n".join(log_details))
                        print("-" * 40)
            else:
                print("No unique USB logs found in the file.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' not found.")
    except Exception as e:
        print(f"error : {e}")

# check for unique USB logs
get_unique_usb_logs(log_file_path)