import os
import shutil

def copy_dir(source_dir, destination_dir):
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    
    os.mkdir(destination_dir)
    
    items = os.listdir(source_dir)
    
    for item in items:
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(destination_dir, item)
        
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} -> {dest_path}")
        else:
            print(f"Processing directory: {source_path}")
            copy_dir(source_path, dest_path)
    
    return True