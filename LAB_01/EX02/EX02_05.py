SoGioLam = float(input("Nhập số giờ làm mỗi tuần: "))
LuongGio = float (input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
GioTieuChuan = 44
GioVuotChuan = max(0,SoGioLam-GioTieuChuan)
ThucLinh = GioTieuChuan * LuongGio + GioTieuChuan * LuongGio *1.5
print(f"Số tiền thực lĩnh của nhân viên: {ThucLinh}")