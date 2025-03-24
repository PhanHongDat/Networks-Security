import string

def mark_character_positions(text):
    original_text = text  # Lưu lại chuỗi gốc để hiển thị đúng định dạng
    text = "".join(filter(str.isalpha, text.upper()))  # Loại bỏ dấu cách, dấu câu
    length = len(text)
    markers = "".join(str((i % 6) + 1) for i in range(length))  # Đánh số theo chu kỳ 1-6
    
    marked_text = []
    marker_line = []
    index = 0
    
    for char in original_text:
        if char.isalpha():
            marked_text.append(char)
            marker_line.append(markers[index])
            index += 1
        else:
            marked_text.append(char)
            marker_line.append(" ")
    
    print("Chuỗi đã nhập: ")
    print("".join(marked_text))
    print("".join(marker_line))

# Nhập dữ liệu từ người dùng
user_input = input("Nhập vào một đoạn văn bản: ")
mark_character_positions(user_input)