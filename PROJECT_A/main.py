# This script creates a va-test.txt file on a given server

import paramiko

def create_va_test_file(hostname, username, password):
    try:
        # Create an SSH client instance
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add host keys
        
        # Connect to the server
        ssh_client.connect(hostname=hostname, username=username, password=password)
        
        # Command to create a va-test.txt file in the C: drive
        command = 'echo "This is a va-test file created by Paramiko for VA project" > C:\\va-test.txt'
        
        # Execute the command
        stdin, stdout, stderr = ssh_client.exec_command(command)
        
        # Optionally: Print the output and any error messages
        print(stdout.read().decode())
        print(stderr.read().decode())

        # Close the SSH connection
        ssh_client.close()
        
        print(f"va-test.txt created successfully on {hostname}.")
        
    except Exception as e:
        print(f"Failed to create va-test.txt on {hostname}: {e}")

if __name__ == '__main__':
    # Predefined server details
    servers = [
        {'hostname': '192.168.88.88', 'username': 'Janis Grencions', 'password': 'moon4$'},
        {'hostname': '192.168.88.99', 'username': 'Sesoma', 'password': ''}
    ]
    
    # Iterate over the server list and create the va-test file
    for server in servers:
        create_va_test_file(server['hostname'], server['username'], server['password'])