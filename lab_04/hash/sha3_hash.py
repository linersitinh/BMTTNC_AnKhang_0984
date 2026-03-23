import hashlib

if __name__ == "__main__":
    text = input("Nhap chuoi can bam SHA-3: ")
    result = hashlib.sha3_256(text.encode("utf-8")).hexdigest()
    print("SHA-3-256:", result)