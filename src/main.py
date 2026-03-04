import wmi
import psutil
import tkinter as tk
from tkinter import messagebox
import sys

def get_parent_info(pid):
    
    try:
        proc = psutil.Process(pid)
        parent = proc.parent()
        return parent.name() if parent else "Unknown"
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return "N/A"

def alert_user(proc_name, cmd_line, pid):
    """Creates a high-priority popup to intercept the process."""
    parent_name = get_parent_info(pid)
    
    
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True) # Ensure popup is on top

    message = (
        f" TERMINAL INTERCEPTED \n\n"
        f"Process: {proc_name}\n"
        f"PID: {pid}\n"
        f"Parent: {parent_name}\n"
        f"Command: {cmd_line}\n\n"
        f"Do you want to KILL this process?"
    )
    
    response = messagebox.askyesno("TermiWatch Alert", message)
    root.destroy()
    return response

def main():
    print(" TermiWatch is active. Monitoring for CMD/PowerShell...")
    
    try:
        
        c = wmi.WMI()
        watcher = c.watch_for(notification_type="Creation", wmi_class="Win32_Process")
        
        while True:
            new_proc = watcher()
            name = new_proc.Name.lower()
            cmd_line = new_proc.CommandLine or "None"
            pid = new_proc.ProcessId

        
            if any(term in name for term in ["cmd.exe", "powershell.exe"]):
                print(f"[!] Caught: {name} (PID: {pid})")
                
                if alert_user(name, cmd_line, pid):
                    try:
                        p = psutil.Process(pid)
                        p.terminate()
                        print(f"[+] Process {pid} terminated successfully.")
                    except Exception as e:
                        print(f"[-] Error killing process: {e}")
                else:
                    print("[*] Process allowed by user.")

    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        print("Note: Ensure you are running this script as Administrator.")

if __name__ == "__main__":
    main()