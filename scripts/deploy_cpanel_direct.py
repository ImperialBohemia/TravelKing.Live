import os
import sys
import time

# Add core to path
sys.path.append("/home/q/TravelKing.Live")

from core.connectors.cpanel import CPanelConnector

def deploy():
    print("--- STARTING DIRECT CPANEL DEPLOYMENT ---")
    cp = CPanelConnector()
    
    local_root = "/home/q/TravelKing.Live/TravelKing"
    remote_root = "TravelKing"
    
    print(f"Local Source: {local_root}")
    print(f"Remote Target: {remote_root}")
    
    # Check connection
    print("Checking connection...")
    res = cp.test_connection()
    print(f"Connection Status: {res}")
    if res.get("status") != "OK":
        print("Aborting.")
        return

    # 1. Create root dir if missing
    print(f"Ensuring remote directory {remote_root} exists...")
    try:
        cp.mkdir("", remote_root)
    except:
        pass
    
    count = 0
    errors = 0
    skipped = 0
    
    for root, dirs, files in os.walk(local_root):
        rel_path = os.path.relpath(root, local_root)
        
        if rel_path == ".":
            remote_subdir = remote_root
        else:
            remote_subdir = f"{remote_root}/{rel_path}"
            
        # Create directories
        for d in dirs:
            # print(f"MKDIR: {remote_subdir}/{d}")
            try:
                cp.mkdir(remote_subdir, d)
            except:
                pass
            
        # Upload files
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in ['.html', '.txt', '.js', '.css', '.json', '.xml']:
                local_f = os.path.join(root, f)
                print(f"UPLOAD: {remote_subdir}/{f}")
                try:
                    with open(local_f, 'r', encoding='utf-8') as fh:
                        content = fh.read()
                    cp.save_file(remote_subdir, f, content)
                    count += 1
                    # time.sleep(0.1) 
                except Exception as e:
                    print(f"FAILED {f}: {e}")
                    errors += 1
            else:
                skipped += 1
                    
    print(f"--- DEPLOYMENT FINISHED: {count} uploaded, {errors} errors, {skipped} skipped (binary) ---")

if __name__ == "__main__":
    deploy()
