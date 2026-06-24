#!/usr/bin/env python3
import os
import sys
import platform
import urllib.request
import zipfile

def download_and_extract_accesskit():
    version = "v0.21.2"
    repo = "AccessKit/accesskit-c"
    
    # Programmatically detect the runner OS
    os_type = platform.system().lower()
    
    # Map the runner OS to the exact release asset names hosted on AccessKit/accesskit-c
    if os_type == "linux":
        asset_name = "accesskit-c-linux-x86_64.zip"
    elif os_type == "darwin":
        asset_name = "accesskit-c-macos.zip"
    elif os_type == "windows":
        asset_name = "accesskit-c-windows-x86_64.zip"
    else:
        print(f"Error: Unsupported OS detected ({os_type})")
        return False

    url = f"https://github.com/{repo}/releases/download/{version}/{asset_name}"
    target_dir = "accesskit-c-0.21.2"
    zip_path = os.path.join(target_dir, "accesskit_c.zip")

    try:
        # Create target directory matching the SCONSFLAGS layout
        os.makedirs(target_dir, exist_ok=True)
        
        print(f"Fetching AccessKit {version} asset: {asset_name}")
        print(f"Source URL: {url}")
        
        # Safe cross-platform file download
        _ = urllib.request.urlretrieve(url, zip_path)
        
        print(f"Extracting package directly into: {target_dir}")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
            
        print("AccessKit SDK successfully configured.")
        return True
    except Exception as e:
        print(f"Failed to handle AccessKit installation natively: {e}")
        return False

if __name__ == "__main__":
    if download_and_extract_accesskit():
        sys.exit(0)
    else:
        sys.exit(1)