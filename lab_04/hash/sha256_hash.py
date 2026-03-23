import hashlib

if __name__ == "__main__":
    text = input("Nhap chuoi can bam SHA-256: ")
    result = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print("SHA-256:", result)