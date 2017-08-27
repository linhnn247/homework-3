import sys
#--- PHẦN KHAI BÁO CÁC FUNCTION------------
def printitem():
# đoạn lệnh paste thành 2 column cách nhau 1 khoảng fixed
#print("\n".join("{0}\t{1}".format(items, price) for items, price in zip(items, price)))
    print()
    print('Danh sách hàng hiện tại là: ')
    itemno = 1
    for item in items:
        print(itemno, end=". ")
        print(item, end = '\t')
        print(price[itemno - 1])
        itemno += 1
    print()
def adminaction():
    print()
    print('Bạn muốn làm gì: ')
    print()
    print('1. Thêm quần áo')
    print('2. Xem quần áo')
    print('3. Sửa thông tin quần áo')
    print('4. Xóa thông tin quần áo')
    print('5. Thoát')
def cusaction():
    print()
    print('Bạn muốn làm gì: ')
    print('1. Xem quần áo')
    print('2. Thoát')

##-----------DỮ LIỆU HIỆN TẠI CỦA SHOP ---------
items = ['T-shirt','Sweater','Jeans']
price = ['100','200','300']
#retype1
retype2 = 1

##----------BẮT ĐẦU VÀO CHƯƠNG TRÌNH------------
print('Chào bạn, bạn là admin hay khách hàng?')
print('1: Admin')
print('2: Khách hàng')
print('3: Thoát')
choice1 = int(input('>> '))

##--------PHẦN XỬ LÝ ADMIN
if choice1 == 1:
    ## ------ PHẦN XỬ LÝ PASSWORD
    while retype2 == 1:
        pwd = input('Vui lòng nhập password của shop: ')
        ## pass đây anh nhé, anh sửa thành ngắn hơn cho dễ test =))
        if pwd != 'incubatorofchange':
            print('Password không đúng')
            print()
            print('1. Nhập lại password')
            print('2. Thoát')
            choice2 = int(input('>> '))
            if choice2 == 2:
                print("C'ya")
                sys.exit()
        else:
            retype2 = 0
    ##------PHẦN XỬ LÝ CÁC CHỨC NĂNG CỦA ADMIN
    while True:
        adminaction()
        choice3 = int(input('>> '))
        if choice3 == 1:
            printitem()
            hangmoi = input('Nhập tên mặt hàng mới: ')
            giamoi = input('Nhập tên giá của ' + hangmoi + ' (k): ')
            items.append(hangmoi)
            price.append(giamoi)
            print('Mặt hàng mới đã được thêm vào')
        elif choice3 == 2:
            printitem()
        elif choice3 == 3:
            printitem()
            print('Bạn muốn sửa tên mặt hàng hay sửa giá: ')
            print('1. Sửa tên quần áo')
            print('2. Sửa giá quần áo')
            print('3. Sửa cả 2')
            print('4. Thoát')
            choice4 = int(input('>> '))
            if choice4 == 1:
                position = int(input('Bạn muốn sửa mặt hàng ở vị trí thứ mấy: '))
                hangmoi = input('Bạn muốn sửa thành gì: ')
                items[position - 1] = hangmoi
                print('Đã cập nhật thành công')
            elif choice4 == 2:
                position = int(input('Bạn muốn sửa giá của mặt hàng ở vị trí thứ mấy: '))
                giamoi = input('Bạn muốn sửa thành bao nhiêu (k): ')
                price[position - 1] = giamoi
                print('Đã cập nhật thành công')
            elif choice4 == 3:
                position = int(input('Bạn muốn sửa mặt hàng ở vị trí thứ mấy: '))
                hangmoi = input('Bạn muốn sửa tên thành gì: ')
                giamoi = input('Bạn muốn sửa giá thành bao nhiêu (k): ')
                items[position - 1] = hangmoi
                price[position - 1] = giamoi
                print('Đã cập nhật thành công')
            else:
                print("C'ya")
                sys.exit()
        elif choice3 == 4:
            printitem()
            position = int(input('Bạn muốn xóa mặt hàng ở vị trí thứ mấy: '))
            items.pop(position - 1)
            price.pop(position - 1)
            print('Đã cập nhật thành công')
        else:
            print("C'ya")
            sys.exit()
        print()
        print('Bạn có muốn thao tác gì nữa không: ')
        print('1. Thao tác tiếp: ')
        print('2. Thoát')
        choice5 = int(input('>> '))
        if choice5 == 1:
            continue
        else:
            print("C'ya")
            sys.exit()
##------------PHÂN XỬ LÝ CÁC CHỨC NĂNG CỦA KHÁCH---------

elif choice1 == 2:
    cusaction()
    cuschoice1 = int(input('>> '))
    if cuschoice1 == 1:
        muatiep = True
        while muatiep == True:
            printitem()
            selectposition = int(input('Bạn muốn mua mặt hàng số mấy: '))
            noproduct = int(input('Bạn muốn mua bao nhiêu sản phẩm ' + items[selectposition - 1] +': '))
            giatien = int(price[selectposition-1]) * noproduct
            print()
            print('Bạn đã đặt mua {0} sản phẩm {1} thành công'.format(str(noproduct),items[selectposition-1]))
            print('Tổng số tiền phải trả là:',str(giatien) + 'k')
            print()
            print('Bạn có muốn mua hàng tiếp không: ')
            print('1. Quẩy lên')
            print('2. Không mua nữa')
            cuschoice2 = int(input('>> '))
            if cuschoice2 == 1:
                muatiep = True
            else:
                muatiep = False
    else:
        print("C'ya")
        sys.exit()
else:
    print("C'ya")
    sys.exit()







