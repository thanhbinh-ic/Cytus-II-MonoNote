import os
import json

# --- CONFIGURATION ---
# Path to the folder containing the JSON files that you exported dumped
JSON_DIR = r"C:\Users\thanhbinh\Desktop\TextAsset"

# Chart content: 1 note, standard JSON format, string escape
ONE_NOTE_SCRIPT = "{\"format_version\":0,\"time_base\":480,\"start_offset_time\":0,\"page_list\":[{\"start_tick\":0,\"end_tick\":1920,\"scan_line_direction\":-1},{\"start_tick\":1920,\"end_tick\":3840,\"scan_line_direction\":1},{\"start_tick\":3840,\"end_tick\":5120,\"scan_line_direction\":-1}],\"tempo_list\":[{\"tick\":0,\"value\":468750}],\"event_order_list\":[],\"note_list\":[{\"page_index\":2,\"type\":0,\"id\":0,\"tick\":4000,\"x\":0.5,\"has_sibling\":false,\"hold_tick\":0,\"next_id\":0,\"is_forward\":false}]}"

def batch_modify_json():
    count = 0
 
    for filename in os.listdir(JSON_DIR):
        if filename.endswith(".json"):
            file_path = os.path.join(JSON_DIR, filename)
            
            try:
         
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if "0 TextAsset Base" in data:
                    data["0 TextAsset Base"]["1 string m_Script"] = ONE_NOTE_SCRIPT
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                    
                    print(f"Thành công: {filename}")
                    count += 1
            except Exception as e:
                print(f"Lỗi khi xử lý file {filename}: {e}")

    print(f"\n--- Hoàn tất! Đã sửa {count} file JSON cho sư huynh. ---")

if __name__ == "__main__":
    batch_modify_json()