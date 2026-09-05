from utils.document_loader import extract_text

file_path = "documents/runtime.txt"

text = extract_text(file_path)

print("\n===== EXTRACTED TEXT =====\n")
print(text[:3000])