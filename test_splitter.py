
from utils.document_loader import extract_text
from utils.text_splitter import split_text


# Your uploaded PDF
file_path = "documents/runtime.txt"


# Extract PDF text
text = extract_text(file_path)


# Split text into chunks
chunks = split_text(
    text,
    chunk_size=500,
    chunk_overlap=50
)


print("\n==============================")
print("TEXT SPLITTING SUCCESSFUL")
print("==============================")

print("\nTotal chunks:", len(chunks))


for i, chunk in enumerate(chunks[:5]):

    print(
        f"\n--- CHUNK {i + 1} ---\n"
    )

    print(chunk)

