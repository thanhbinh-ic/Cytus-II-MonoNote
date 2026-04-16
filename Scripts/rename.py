import os

# --- CONFIGURATION ---
# The path to the 'mods' folder contains the .ab-mod files
TARGET_DIR = r"C:\Users\thanhbinh\Desktop\mods"

def rename_files():
    count = 0

    for filename in os.listdir(TARGET_DIR):

        if filename.endswith(".ab-mod"):
      
            new_name = filename.replace(".ab-mod", ".ab")
            
            old_path = os.path.join(TARGET_DIR, filename)
            new_path = os.path.join(TARGET_DIR, new_name)
            
            try:
               
                os.rename(old_path, new_path)
                print(f"Đã đổi: {filename} -> {new_name}")
                count += 1
            except Exception as e:
                print(f"Lỗi khi đổi tên file {filename}: {e}")

    print(f"\n--- Hoàn tất! Đã xử lý xong {count} file cho sư huynh. ---")

if __name__ == "__main__":
    rename_files()