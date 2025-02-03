
# 🌐 **Project SecuScan - Exploring Nmap and Shodan.io**  

---

## 📖 **Introduction**  
**🔍 Purpose:**  
- Mask our IP address to a target destination using Nmap's **Decoy (-D)** option and verify it with Wireshark.  
- Automate Nmap commands with Python to test the **T3** and **T5 timing templates**, analyze time differences, and observe outputs of the **-A (Aggressive Scan)** option.  

---

## ⚙️ **Pre-requisites**  
- **Ubuntu Server 20.04 LTS** (or later)  

  **📌 IPv4 Addresses (in our environment):**  
  - 🖥️ **Kali Linux IP:** `10.0.18.4`  
  - 🖥️ **Ubuntu Server IP:** `10.0.18.7`  

- **VirtualBox** (with Guest Additions installed)  
- **Tools Used:**  
  - 🐍 **Python3**  
  - 🌐 **Nmap**  
  - 📊 **Wireshark**  

---

### 🎯 **Target**:  
`testphp.vulnweb.com`

---

## 🛠️ **Steps for the Lab**  

### 1️⃣ **Masking Our IP Address**  
🔑 **Commands:**  
```bash
1. Execute the following command to initiate an Nmap scan with decoys:  
   sudo nmap -D RND:10 testphp.vulnweb.com  
   ⚠️ **Important: Do not run this command yet.**  

2. Open a new terminal, type `wireshark`, and press Enter.  
   - Select the network interface **"eth0"**, right-click on it, and choose **"Start Capture"** to begin monitoring.  

3. Once Wireshark is capturing packets, execute the command from Step 1 in the first terminal.  

4. Observe the Wireshark capture.  
   - You will notice **10 decoy IP addresses**, along with your real IP address, attempting to connect to the target.  

5. Use the filter below in Wireshark to observe these 10 decoys and your real IP:  
   ip.addr == <target>
```

---

### 2️⃣ **Testing Timing Templates (-T3 and -T5) with Automation**  
#### **Steps:**  
1. Open the terminal and type:  
   ```bash
   mousepad scan.py
   ```  
   - This opens the `scan.py` file in a text editor.  

2. Write the following Python script:  
   ```python
   import os
   target = input("Enter target IP or hostname: ")
   os.system(f"nmap -A -T5 {target}")
   ```  
   Save and close the file.  

3. Run the script:  
   ```bash
   python scan.py
   ```  
   - Enter your target's IP or hostname and your system password if prompted.  

4. Record the time taken for the **T5** scan.  

5. Modify the Python script for the **T3** timing template:  
   ```python
   import os
   target = input("Enter target IP or hostname: ")
   os.system(f"nmap -A -T3 {target}")
   ```  
   Save and execute the updated script.  

6. **Compare** the time taken for both scans (**T3** and **T5**) and note differences.  

---

## 💭 **Reflection**  

### ✅ **Questions:**  
1. **What was the easiest part of this lab?**  
2. **What was the most challenging part of this lab?**  
3. **Why did changing the time template (T3, T5) affect the result of the scan?**  
4. **What is the purpose of using Decoy (-D), and what are the benefits?**  
5. **What is Shodan, and how does it differ from regular search engines like Google?**  

---
### 📝 **Contributors**  
- **Sukhdeep Singh** - ID: 10044****  
- **Dilraj Kaur** - ID: 10044****

---

## 📚 **References**  
1. 🌐 [Shodan Help Center](https://help.shodan.io)  
2. 🌐 [Nmap: The Network Mapper](https://nmap.org)  

---

### 🙏 **Acknowledgements**  
A heartfelt thank you to **Professor Kwan Benjamin** for designing this amazing experience. Your guidance made this learning journey insightful and rewarding.  

---
