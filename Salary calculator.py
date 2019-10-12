#coding=gbk
Basic_salary = 6000
car_fare = 0
Delivery_times = 0
installation_cost = 0
food_subsidy = 440
telephone_bill = 100
print("你的基本工资是：",Basic_salary)
print("你的饭补是：",food_subsidy)
print("你的电话费补助是：",telephone_bill)
car_fare = int(input("请输入要报销的路费："))
Delivery_times = int(input("请输入送货次数："))
installation_cost = int(input("请输入安装费用："))
salary = Basic_salary + car_fare + Delivery_times * 20 + installation_cost + food_subsidy + telephone_bill
print("你的总工资是：",salary)
input()