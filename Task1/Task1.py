import os
import hashlib
import json
import time

# Directory to monitor
MONITOR_DIR = "E:\Internship(Cyber security)\\"
HASH_FILE = "file_hashes.json"
CHECK_INTERVAL = 10  # Time interval in seconds


def calculate_hash(file_path):
    #Calculate the SHA256 hash of a file.
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None


def load_hashes():
    #Load stored file hashes from JSON.
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}


def save_hashes(hashes):
    #Save file hashes to JSON.
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)


def scan_files():
    #Scan files in the directory and return their hashes.
    file_hashes = {}
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path)
    return file_hashes


def monitor_changes():
    #Monitor file changes.
    print(f"Monitoring directory: {MONITOR_DIR}")
    old_hashes = load_hashes()

    while True:
        new_hashes = scan_files()

        added_files = new_hashes.keys() - old_hashes.keys()
        deleted_files = old_hashes.keys() - new_hashes.keys()
        modified_files = {f for f in new_hashes if f in old_hashes and new_hashes[f] != old_hashes[f]}

        if added_files:
            print(f"Added files: {', '.join(added_files)}")
        if deleted_files:
            print(f"Deleted files: {', '.join(deleted_files)}")
        if modified_files:
            print(f"Modified files: {', '.join(modified_files)}")

        save_hashes(new_hashes)
        old_hashes = new_hashes

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    monitor_changes()
