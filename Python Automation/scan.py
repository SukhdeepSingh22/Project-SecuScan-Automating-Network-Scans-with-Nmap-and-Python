# Author: Sukhdeep Singh
# Date: November 15, 2024
# Purpose: Automate terminal commands for Nmap using a Python script.

import subprocess  # Safer alternative to os.system

def run_nmap_scan():
    """
    Prompts the user for a target IP/hostname and runs an Nmap scan with the -A and -T5 options.
    """
    # Input validation: Ensure target is not empty
    target = input("Enter target IP or hostname: ").strip()
    if not target:
        print("Error: Target cannot be empty. Please enter a valid IP or hostname.")
        return

    # Construct the Nmap command
    command = f"sudo nmap -A -T5 {target}"

    try:
        # Run the Nmap command using subprocess
        print("\nRunning Nmap scan...\n")
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

        # Print the output of the command
        print("Nmap Scan Results:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # Handle errors in subprocess
        print(f"An error occurred while running the Nmap scan: {e}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("# Script: Nmap Automation")
    print("# Written by Sukhdeep Singh, Fall 2024\n")
    run_nmap_scan()
