import os
import sys
import time

# Add core to path
sys.path.append("/home/q/TravelKing.Live")

from core.connectors.cpanel import CPanelConnector

def deploy_to(remote_root):
    print(f"--- STARTING DIRECT CPANEL DEPLOYMENT TO {remote_root} ---")
    cp = CPanelConnector()
    
    local_root = "/home/q/TravelKing.Live/web-latest/out"
    
    print(f"Local Source: {local_root}")
    print(f"Remote Target: {remote_root}")
    
    # Check connection
    res = cp.test_connection()
    if res.get("status") != "OK":
        print("Connection failed. Aborting.")
        return

    # 1. Ensure remote root exists
    print(f"Ensuring remote directory {remote_root} exists...")
    try:
        cp.mkdir("", remote_root)
    except:
        pass
    
    count = 0
    errors = 0
    
    for root, dirs, files in os.walk(local_root):
        rel_path = os.path.relpath(root, local_root)
        
        if rel_path == ".":
            remote_subdir = remote_root
        else:
            remote_subdir = f"{remote_root}/{rel_path}"
            
        # Create directories
        for d in dirs:
            # Recursive directory creation
            parts = rel_path.split("/") if rel_path != "." else []
            current_path = remote_root
            for part in parts + [d]:
                try:
                    cp.mkdir(current_path, part)
                except:
                    pass
                current_path = f"{current_path}/{part}"
            
        # Upload files
        for f in files:
            local_f = os.path.join(root, f)
            print(f"UPLOAD: {remote_subdir}/{f}")
            try:
                cp.upload_file(remote_subdir, f, local_f)
                count += 1
            except Exception as e:
                print(f"FAILED {f}: {e}")
                errors += 1
                    
    print(f"--- DEPLOYMENT TO {remote_root} FINISHED: {count} uploaded, {errors} errors ---")

if __name__ == "__main__":
    # Deploy to both for maximum safety
    deploy_to("public_html")
    deploy_to("TravelKing")
