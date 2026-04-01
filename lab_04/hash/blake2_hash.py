import hashlib

if __name__ == "__main__":
    text = input("Nhap chuoi can bam Blake2: ")
    result = hashlib.blake2b(text.encode("utf-8")).hexdigest()
    print("Blake2b:", result)