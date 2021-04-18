#---- code:utf-8 ----

'''
verification part 1
'''

def verification1():
    print("part 1")
    print("main idea is test")
    print("wellcome to test server")
    none = True
    while none:

        part1 = input(str("please type your invention code:"))
        if part1 == "0":
            print("successful")
            none = False
        else:
            print("unknow code")

verification1()
