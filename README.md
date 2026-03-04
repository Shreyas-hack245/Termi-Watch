# 🛡️ TermiWatch

**TermiWatch** is a real-time endpoint security tool designed to intercept, inspect, and terminate "ghost" terminal processes. Built for Windows environments, it uses WMI event-driven hooks to catch CMD and PowerShell instances the millisecond they are created.

## 🔍 The Problem
Many Windows systems experience "ghosting"—where a terminal window flashes briefly and disappears. This can be a benign scheduled task or a sign of malicious script execution. TermiWatch pauses these processes, allowing for forensic analysis before they can execute fully.

## ✨ Features
* **Real-Time Interception**: Uses WMI `Win32_Process` creation events for zero-lag detection.
* **Forensic Insights**: Displays the full command-line arguments and the Parent Process ID (PPID).
* **Manual Override**: Interactive GUI (Tkinter) allows the user to manually "Kill" or "Allow" the process.
* **Security Focused**: Designed for blue-teamers and researchers investigating persistent system behaviors.



## 🛠️ Technical Stack
* **Language**: Python
* **Libraries**: `wmi`, `psutil`, `pywin32`, `tkinter`
* **OS**: Windows (Requires Administrator Privileges)

## 🚀 Getting Started

### Prerequisites
Ensure you have Python installed. You must run your terminal as **Administrator**.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shreyas-hack245/Termi-Watch.git
   ```
2. Install dependencies:
      ``` bash
      python -m pip install -r requirements.txt
      ```
3. Run the main script:
      ``` bash
    python src/main.py
    ```
