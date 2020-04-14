import os
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片

filePath = '..\\images'
names = os.listdir(filePath)
line = int(input("Which line last time?"))
assert line >= 2, "Line begins at 2"
plt.ion()  # 这是为了能自动close（虽然写的时候还要点一下cmd，不然它不在第一层。很烦。）
filler = open('../filler_objectlist_classification.txt')
fList = filler.readlines()
filler.close()
for i in range(line - 2, len(names) - 1):
    imgPath = "..\\images\\" + names[i]
    img = mpimg.imread(imgPath)

    plt.imshow(img)
    plt.axis('off')
    plt.show()  # 这一段是打开图片（包括前面要地址那些）
    ipt = int(input("Which type? (00~04)"))
    if 0 <= ipt <= 4:
        fList[line - 1] = f"{fList[line - 1][:22]}0{ipt}{fList[line - 1][24:]}"  # 这一串if都是写入。else是不想做了用来break的
        ipt = input("Any comment?(y/n)")
        if ipt == "y":
            ipt = input("Comment: ")
            fList[line - 1] = f"{fList[line - 1][:37]}{ipt}\n"
    elif ipt == 99:
        fList[line - 1] = f"{fList[line - 1][:22]}{ipt}{fList[line - 1][24:]}"
        ipt = input("Any comment?(y/n)")
        if ipt == "y":
            ipt = input("Comment: ")
            fList[line - 1] = f"{fList[line - 1][:37]}{ipt}\n"
    else:
        break
    plt.close()
    line = line + 1
filler = open('../filler_objectlist_classification.txt', 'w')
filler.writelines(fList)