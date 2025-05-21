from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhvien = []

    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = self.listSinhvien[0]._id
            for sv in self.listSinhvien:  # sửa đúng tên thuộc tính
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId
    
    def soLuongSinhVien(self):
        return len(self.listSinhvien)  # sửa đúng tên

    def nhapSinhvien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhập giới tính sinh vien: ")
        major = input("Nhap chuyen nganh của sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhvien.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if sv is not None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh của sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh vien có ID = {ID} khong ton tai")

    def sortByID(self):
        self.listSinhvien.sort(key=lambda x: x._id)

    def sortByName(self):
        self.listSinhvien.sort(key=lambda x: x._name)

    def sortByDiemTB(self):
        self.listSinhvien.sort(key=lambda x: x._diemTB)

    def findByID(self, ID):
        for sv in self.listSinhvien:
            if sv._id == ID:
                return sv
        return None
    
    def findByName(self, keyword):
        return [sv for sv in self.listSinhvien if keyword.upper() in sv._name.upper()]
    
    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhvien.remove(sv)
            return True
        return False
    
    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showListSinhVien(self, listSV):  # đổi tên cho khớp với Main.py
        print("{:<8} {:<18} {:<8} {:<12} {:<8} {:<10}"
              .format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<12} {:<8} {:<10}"
                  .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print()

    def getListSinhVien(self):
        return self.listSinhvien
