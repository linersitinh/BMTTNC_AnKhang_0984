import hashlib

if __name__ == "__main__":
    text = input("Nhap chuoi can bam MD5: ")
    result = hashlib.md5(text.encode("utf-8")).hexdigest()
    print("MD5 (library):", result)