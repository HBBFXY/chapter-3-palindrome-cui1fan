num = input("请输入一个 5 位数：")
if len(num) != 5 or not num.isdigit():
    print("输入不是 5 位自然数！")
else:
    if num == num[::-1]:
        print("{} 是回文数".format(num))
    else:
        print("{} 不是回文数".format(num))# 这里编写你的代码
