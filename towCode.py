sun=[{
    'name':'小红',
    'age':15
},{
    'name':'小黄',
    'age':22
}]
for n in sun:
    print(n['name']+'：'+str(n['age']))
def sun1(x,y):
    return x+y
print(sun1(1,2))

temp = [x for x in range(1, 10)]
print(temp)


print(temp[1:2:3])
print(temp[:2:3])
# QQ=input("请输入QQ：")
# print("你的QQ号是："+QQ)
temp = "welcome to my web https://www.itprojects.my cn"
QQ=temp.rfind("o")
print(QQ)
print(",".join(["Q","W","Obj"]))
teacher = ["王老师", "山东省青岛市", 18, 176.5]  # 18为年龄，176.5为身高
i=0
while(i< len(teacher)):
    print(teacher[i])
    i+=1
mark=input("请输入你的成绩：")
mark=int(mark)
if(mark>=90):
    print("A")
elif(mark>=80):
    print("B")
elif(mark>=70):
    print("C")
else:
    print("D")