import os
import shutil

# --- CẤU HÌNH ---
# Thư mục gốc chứa các folder nhân vật (Ví dụ: Alice, Amiya, Neko...)
SOURCE_DIR = r"C:\Users\thanhbinh\Desktop\AssetBundles"
# Thư mục tạm để huynh sửa file
TEMP_WORK_DIR = r"C:\Users\thanhbinh\Desktop\Packs"

def collect_files():
    if not os.path.exists(TEMP_WORK_DIR):
        os.makedirs(TEMP_WORK_DIR)
    
    mapping = {}
    print(">>> Đang gom file .ab về thư mục làm việc...")
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        # Bỏ qua thư mục tạm nếu nó nằm bên trong thư mục gốc
        if TEMP_WORK_DIR in root: continue
        
        for file in files:
            if file.endswith(".ab"):
                src_path = os.path.join(root, file)
                dst_path = os.path.join(TEMP_WORK_DIR, file)
                
                # Lưu lại đường dẫn gốc
                mapping[file] = root
                shutil.copy2(src_path, dst_path)
                print(f"  [+] Đã copy ra: {file}")
    
    print(f"\n>>> Xong! Sư huynh hãy mod file trong: {TEMP_WORK_DIR}")
    return mapping

def copy_back_files(mapping):
    print("\n>>> Đang copy file đã sửa đè về vị trí cũ (Vẫn giữ bản mod tại Packs)...")
    count = 0
    for file, original_dir in mapping.items():
        processed_file = os.path.join(TEMP_WORK_DIR, file)
        
        if os.path.exists(processed_file):
         
            shutil.copy2(processed_file, os.path.join(original_dir, file))
            print(f"  [<-] Đã ghi đè: {file} -> {original_dir}")
            count += 1
            
    print(f"\n>>> HOÀN TẤT! Đã cập nhật {count} file thành công.")
    print(">>> Bản mod vẫn còn nguyên trong Packs để huynh dự phòng.")

if __name__ == "__main__":

    file_map = collect_files()
    
    print("-" * 60)
    print("SAU KHI HUYNH XỬ LÝ XONG TRONG THƯ MỤC Packs:")
    user_input = input("Ấn phím '1' rồi Enter để COPY file về lại các folder gốc: ")
    
    if user_input == "1":
        copy_back_files(file_map)
    else:
        print("Huynh không nhấn phím '1', script kết thúc. Không có file nào bị ghi đè.")