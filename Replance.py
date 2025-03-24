from collections import Counter
import json

def analyze_frequency(ciphertext):
    """Phân tích tần suất xuất hiện của các ký hiệu trong văn bản mã hóa."""
    symbols = Counter(ciphertext)
    sorted_symbols = symbols.most_common()
    return sorted_symbols

def decrypt_substitution(ciphertext, mapping):
    """Giải mã văn bản dựa trên bảng thay thế ký tự."""
    decrypted_text = ciphertext
    for key, value in mapping.items():
        decrypted_text = decrypted_text.replace(key, value)  # Thay thế tất cả các ký hiệu
    return decrypted_text

# Nhập văn bản mã hóa
ciphertext = input("Nhập văn bản mã hóa: ")

# Bước 1: Phân tích tần suất xuất hiện
freq_analysis = analyze_frequency(ciphertext)
print("\nTần suất ký hiệu:")
for symbol, count in freq_analysis:
    print(f"{symbol}: {count}")

# Bước 2: Nhập bảng thay thế thủ công
mapping = {}
print("\nNhập bảng thay thế (gõ 'exit' để dừng):")
while True:
    symbol = input("Nhập ký hiệu cần thay thế: ")
    if symbol.lower() == 'exit':
        break
    replacement = input(f"Thay thế '{symbol}' bằng: ")
    mapping[symbol] = replacement

# Bước 3: Giải mã văn bản
plaintext = decrypt_substitution(ciphertext, mapping)
print("\nVăn bản giải mã:")
print(plaintext)

# Bước 4: Ghi kết quả ra file
output_filename = "decrypted_output.txt"
with open(output_filename, "w", encoding="utf-8") as file:
    file.write(plaintext)

print(f"\nVăn bản đã được lưu vào {output_filename}")
