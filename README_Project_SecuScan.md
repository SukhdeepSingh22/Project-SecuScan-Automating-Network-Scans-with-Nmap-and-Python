Sukhdeep Singh and Dilraj Kaur 
ID: 100447918  and 100447804

# Project SecuScan - Exploring Nmap and Shodan.io  

---

## **Introduction**  
**Purpose:**  
Mask our IP address to a target destination using Nmap's Decoy (-D) option and verify it with Wireshark. Next, automate Nmap commands with Python to test the T3 and T5 timing templates, analyze the time differences, and observe the outputs of the -A (Aggressive Scan) option.  

---

## **Pre-requisites**  
- **Ubuntu Server 20.04 LTS** (or later)  

  **IPv4 Addresses (in my system environment):**  
  - **Kali Linux IP:** `10.0.18.4`  
  - **Ubuntu Server IP:** `10.0.18.7`  

- **VirtualBox with Guest Additions Installed**  
- **Tools Used:**  
  - Python3  
  - Nmap  
  - Wireshark  

---

- **Our Target:** `testphp.vulnweb.com`  

---

## **Steps for the Lab**  

### **1. Masking Our IP Address**  
- **Commands:**  
  ```
1. Execute the following command to initiate an Nmap scan with decoys:  
   `sudo nmap -D RND:10 testphp.vulnweb.com`. **Important: Do not run this command yet.**  

2. Open a new terminal, type `wireshark`, and press Enter. Select the network interface **"eth0"**, right-click on it, and choose **"Start Capture"** to begin monitoring.  

3. Once Wireshark is configured and capturing packets, execute the command from Step 1 in the first terminal.  

4. Observe the Wireshark capture. You will notice 10 decoy IP addresses, along with your real IP address, attempting to connect to the target.  

5. You can observe these 10 decoys and your real IP using the filter:  
   `ip.addr == <target>`.  
  ```

---

### **2. Testing Timing Templates (-T3 and -T5) with Automation and Saving -A Scan Outputs to Text Files**  

#### **Steps to Follow:**  
1. Open the terminal and type `mousepad scan.py`. This command will open the `scan.py` file in the text editor, which will be saved in the current directory shown in the terminal prompt.  

2. Write the following Python code into the `scan.py` file:  
   ```python
   import os
   target = input("Enter target IP or hostname: ")
   os.system(f"nmap -A -T5 {target}")
   ```
   Save and close the file after writing the code.  

3. Run the script by typing `python scan.py` in the terminal. When prompted, enter your target's IP address or hostname, and if required, your system password.  

4. Observe the output of the `-A` scan for the `-T5` timing template. Record the time taken for this scan.  

5. Modify the Python script or manually repeat the process by changing `-T5` to `-T3` in the `scan.py` file:  
   ```python
   import os
   target = input("Enter target IP or hostname: ")
   os.system(f"nmap -A -T3 {target}")
   ```
   Save and execute the updated script.  

6. Compare the time taken for both scans (`-T3` and `-T5`) and note the differences in performance.  

---

## **Reflection**  
1. **What was the easiest part of this lab?**  

2. **What was the most challenging part of this lab?**  

3. **Why did changing the time template (T3, T5) affect the result of the scan?**  

4. **What is the purpose of using Decoy (-D) and what are the benefits of using it?**  

5. **What is Shodan, and how does it differ from regular search engines like Google?**  

---

## **References**  
1. Shodan Help Center. *Shodan Help Center*.  
2. Nmap: The Network Mapper - *Free Security Scanner*.  
