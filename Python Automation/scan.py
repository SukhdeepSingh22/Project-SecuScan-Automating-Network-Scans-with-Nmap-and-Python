import os
target = input("Enter target IP or hostname: ")
os.system(f"sudo nmap -A -T5 {target}")

