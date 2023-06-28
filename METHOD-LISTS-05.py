danhSach = [1, 4, 12, -2, 100, 37]
danhSach.sort() #sắp xếp danh sách
print(danhSach)

danhSach2 = [1, 4, 12, -2, 100, 37]
danhSach2.sort(reverse=True) #đảo ngược vị trí sắp xếp
print(danhSach2)

danhSach3 = ['A', 'Z', 'a', 'z']
danhSach3.sort(key=str.lower) #key=str.lower để sắp xếp theo Alphabet chứ không phải ASCII
print(danhSach3)