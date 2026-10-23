#学生信息管理系统
import os
lazy import time
import manager
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_choose(choice):
    if choice == '1':
        manager.list_all_student()
    elif choice == '2':
        clear()
        name, sex, age, stu_id = input("分别输入姓名、性别、年龄、学生ID，中间用空格隔开").split()
        manager.add_student(name, int(sex), int(age), int(stu_id))
    elif choice == '3':
        manager.find_student()
    elif choice == '4':
        ...
    elif choice == '5': ...
    elif choice == '6': ...
    elif choice == 'Q':
        while 1:
            q = input("确定要退出本系统吗？[Y/N]")
            if q == 'Y' or q == 'y':
                exit()
            else:
                break

def main():
    clear()
    while 1:
        print("""
        -----------------学生信息管理系统-----------------------------
        |   1.列出所有学生信息       2.录入学生信息                     |
        |   3.查找学生信息          4.删除学生信息                     |
        |   5.更新所有信息          6.调整默认设置和帮助                |
        |   Q.退出系统                                              |
        |                                                         |
        |版本 BETA 1.0                                             |
        |                                                         |
        |                                                         |
        |-----------------------------------------------------------
        """)
        choice = input("选择选项：")
        menu_choose(choice)

if __name__ == '__main__':
    main()


