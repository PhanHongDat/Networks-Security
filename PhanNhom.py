import string
from collections import Counter
def shift_text(text):
    size = len(text)
    matrix = []
    for i in range(size):
        row = [(text[(j + i) % size]) for j in range(size)]
        matrix.append(row)
    return matrix

def print_shifted_matrix(text):
    text = text.replace(" ", "")[:25]  # Loại bỏ dấu cách và giới hạn 25 ký tự
    matrix = shift_text(text)
    
    print("   " + " ".join(text))
    print("  " + "-" * (2 * len(text)))
    
    for i, row in enumerate(matrix):
        colored_row = []
        for j, char in enumerate(row):
            if char == text[j]:  # Nếu ký tự sau khi dịch trùng với ký tự gốc
                colored_row.append(f'\033[91m{char}\033[0m')  # ANSI escape code for red
            else:
                colored_row.append(char)
        print(f"{i+1:2} | " + " ".join(colored_row))

# Nhập chuỗi từ người dùng
user_input = input("Nhập vào tối đa 25 ký tự (không tính dấu cách): ")
print_shifted_matrix(user_input)



# phân nhóm ký tự


def group_characters(text, group_size):
    text = "".join(filter(str.isalpha, text.upper()))  # Loại bỏ dấu cách, dấu câu
    grouped = [text[i::group_size] for i in range(group_size)]
    
    result = {}
    for i, group in enumerate(grouped):
        counter = Counter(group)
        result[f"Nhóm {i+1}"] = counter
    
    return result

def print_grouped_characters(text, group_size):
    grouped_data = group_characters(text, group_size)
    for group, counter in grouped_data.items():
        print(group + ":")
        for char, count in counter.items():
            print(f"  {char}: {count} lần")
        print()

# Nhập dữ liệu từ người dùng
user_input = input("Nhập vào một đoạn văn bản: ")
group_size = int(input("Nhập số nhóm muốn phân loại: "))
print_grouped_characters(user_input, group_size)