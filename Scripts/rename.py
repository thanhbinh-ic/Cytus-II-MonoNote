import os

# --- CẤU HÌNH ---
# Đường dẫn tới thư mục 'mods' chứa các file .ab-mod của sư huynh
TARGET_DIR = r"C:\Users\thanhbinh\Desktop\mods"

def rename_files():
    count = 0
    # Duyệt qua tất cả các file trong thư mục
    for filename in os.listdir(TARGET_DIR):
        # Kiểm tra nếu file có đuôi là .ab-mod
        if filename.endswith(".ab-mod"):
            # Tạo tên mới bằng cách thay thế .ab-mod thành .ab
            new_name = filename.replace(".ab-mod", ".ab")
            
            old_path = os.path.join(TARGET_DIR, filename)
            new_path = os.path.join(TARGET_DIR, new_name)
            
            try:
                # Thực hiện đổi tên
                os.rename(old_path, new_path)
                print(f"Đã đổi: {filename} -> {new_name}")
                count += 1
            except Exception as e:
                print(f"Lỗi khi đổi tên file {filename}: {e}")

    print(f"\n--- Hoàn tất! Đã xử lý xong {count} file cho sư huynh. ---")

if __name__ == "__main__":
    rename_files()