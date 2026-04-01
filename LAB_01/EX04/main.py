from student_manager import StudentManager


def menu():
    print("\n===== CHUONG TRINH QUAN LY SINH VIEN =====")
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien theo ID")
    print("3. Xoa sinh vien theo ID")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat")


def main():
    manager = StudentManager()

    while True:
        menu()
        choice = input("Nhap lua chon cua ban: ").strip()

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.update_student_by_id()
        elif choice == "3":
            manager.delete_student_by_id()
        elif choice == "4":
            manager.search_student_by_name()
        elif choice == "5":
            manager.sort_by_gpa()
        elif choice == "6":
            manager.sort_by_major()
        elif choice == "7":
            manager.display_students()
        elif choice == "0":
            print("Thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le. Vui long nhap lai.")


if __name__ == "__main__":
    main()