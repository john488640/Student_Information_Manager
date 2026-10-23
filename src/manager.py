lazy import main
lazy import json

stu_info = []
operate_successful = False
lazy from pathlib import Path

def add_student(name:str, sex:int, age:int,stu_id:int) -> bool:
    global operate_successful
    global stu_info
    temp = {'name':name,'age':age,'stu_id':stu_id}
    if sex % 2 == 0:
        temp['sex'] = '女'
    else:
        temp['sex'] = '男'
    if input(f"学生姓名：{temp['name']}，学生年龄：{temp['age']}，学生ID号码{temp['stu_id']}，学生性别{temp['sex']}，确定添加吗？") == 'Y' or 'y':
        stu_info.append(temp)
        operate_successful = True
        return operate_successful
    else:
        return operate_successful
def find_student(name:str):
    pass
def list_all_student():
    global operate_successful
    main.clear()
    print(stu_info)
    operate_successful = True
    return operate_successful

    #这里要做json读取
def delete_student(name:str):
    pass

def update_all_student(name:str):
    pass

def save_information():
    global operate_successful
    main.clear()
    print(f"即将保存的信息：\n-----------------------------\n{stu_info}\n--------------------------")
    path = Path("students.json")
    contents = json.dumps(stu_info)
    path.write_text(contents)
