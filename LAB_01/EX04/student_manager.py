from student import Student


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Nhap ten sinh vien: ").strip()
        gender = input("Nhap gioi tinh: ").strip()
        major = input("Nhap chuyen nganh: ").strip()

        while True:
            try:
                gpa = float(input("Nhap diem trung binh: "))
                if 0 <= gpa <= 10:
                    break
                print("Diem phai nam trong khoang 0 -> 10.")
            except ValueError:
                print("Vui long nhap dung dinh dang so.")

        student = Student(name, gender, major, gpa)
        self.students.append(student)
        print("Da them sinh vien thanh cong.")

    def display_students(self):
        if not self.students:
            print("Danh sach rong.")
            return

        print("-" * 80)
        print(f"{'ID':<5}{'Ten':<20}{'Gioi tinh':<10}{'Chuyen nganh':<20}{'GPA':<10}{'Hoc luc':<15}")
        print("-" * 80)
        for student in self.students:
            print(student)
        print("-" * 80)

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def update_student_by_id(self):
        try:
            student_id = int(input("Nhap ID sinh vien can cap nhat: "))
        except ValueError:
            print("ID khong hop le.")
            return

        student = self.find_student_by_id(student_id)
        if not student:
            print("Khong tim thay sinh vien.")
            return

        new_name = input(f"Nhap ten moi ({student.name}): ").strip()
        new_gender = input(f"Nhap gioi tinh moi ({student.gender}): ").strip()
        new_major = input(f"Nhap chuyen nganh moi ({student.major}): ").strip()

        while True:
            try:
                new_gpa_input = input(f"Nhap GPA moi ({student.gpa}): ").strip()
                if new_gpa_input == "":
                    new_gpa = student.gpa
                    break
                new_gpa = float(new_gpa_input)
                if 0 <= new_gpa <= 10:
                    break
                print("Diem phai nam trong khoang 0 -> 10.")
            except ValueError:
                print("Vui long nhap dung dinh dang so.")

        if new_name:
            student.name = new_name
        if new_gender:
            student.gender = new_gender
        if new_major:
            student.major = new_major
        student.gpa = new_gpa

        print("Cap nhat sinh vien thanh cong.")

    def delete_student_by_id(self):
        try:
            student_id = int(input("Nhap ID sinh vien can xoa: "))
        except ValueError:
            print("ID khong hop le.")
            return

        student = self.find_student_by_id(student_id)
        if not student:
            print("Khong tim thay sinh vien.")
            return

        self.students.remove(student)
        print("Da xoa sinh vien thanh cong.")

    def search_student_by_name(self):
        keyword = input("Nhap ten can tim: ").strip().lower()
        results = [s for s in self.students if keyword in s.name.lower()]

        if not results:
            print("Khong tim thay sinh vien.")
            return

        print("-" * 80)
        print(f"{'ID':<5}{'Ten':<20}{'Gioi tinh':<10}{'Chuyen nganh':<20}{'GPA':<10}{'Hoc luc':<15}")
        print("-" * 80)
        for student in results:
            print(student)
        print("-" * 80)

    def sort_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa, reverse=True)
        print("Da sap xep theo diem trung binh giam dan.")

    def sort_by_major(self):
        self.students.sort(key=lambda s: s.major.lower())
        print("Da sap xep theo ten chuyen nganh.")