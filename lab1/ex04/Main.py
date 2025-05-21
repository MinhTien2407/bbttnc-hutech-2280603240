from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("Chao mung ban den voi chuong trinh quan ly sinh vien")
    print("Lua chon chuc nang:")
    print("1. Them sinh vien")
    print("2. Cap nhat sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tim kiem sinh vien")
    print("5. Sap xep danh sach sinh vien theo diem TB")
    print("6. Sap xep danh sach sinh vien theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat chuong trinh")
    print("========================================")
    
    key = int(input("Nhap lua chon: "))
    if (key == 1):
        print("Them sinh vien")
        qlsv.nhapSinhvien()
        print("Them sinh vien thanh cong")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("Cap nhat sinh vien")
            print("Nhap ID sinh vien can cap nhat: ")
            ID = int(input("ID: "))
            qlsv.updateSinhVien(ID)
        else:
            print("Khong co sinh vien nao de cap nhat")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("Xoa sinh vien")
            print("Nhap ID sinh vien can xoa: ")
            ID = int(input("ID: "))
            if (qlsv.deleteByID(ID)):
                print("Sinh vien co ID = {} da bi xoa".format(ID))
            else:
                print("Khong tim thay sinh vien co ID = {}".format(ID))
        else:
            print("Khong co sinh vien nao de xoa")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("Tim kiem sinh vien")
            print("Nhap ten sinh vien can tim: ")
            name = input("Ten: ")
            searchResult = qlsv.findByName(name)
            qlsv.showListSinhVien(searchResult)
        else:
            print("Khong co sinh vien nao de tim kiem")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("Sap xep sinh vien theo diem TB")
            qlsv.sortByDiemTB()
            qlsv.showListSinhVien(qlsv.listSinhvien)
        else:
            print("Khong co sinh vien nao de sap xep")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("Sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.showListSinhVien(qlsv.listSinhvien)
        else:
            print("Khong co sinh vien nao de sap xep")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("Hien thi danh sach sinh vien")
            qlsv.showListSinhVien(qlsv.listSinhvien)
        else:
            print("Khong co sinh vien nao de hien thi")
    elif (key == 0):
        print("Ban da thoat chuong trinh")
        break
    else:
        print("Lua chon khong hop le")
    print("========================================")
    print("Ban co muon tiep tuc khong? (Y/N)")
    cont = input("Nhap Y de tiep tuc, N de thoat: ")
    if (cont.upper() == "N"):
        print("Ban da thoat chuong trinh")
        break
    elif (cont.upper() != "Y"):
        print("Lua chon khong hop le")