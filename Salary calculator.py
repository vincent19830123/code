#coding=gbk
Basic_salary = 6000
car_fare = 0
Delivery_times = 0
installation_cost = 0
food_subsidy = 440
telephone_bill = 100
print("��Ļ��������ǣ�",Basic_salary)
print("��ķ����ǣ�",food_subsidy)
print("��ĵ绰�Ѳ����ǣ�",telephone_bill)
car_fare = int(input("������Ҫ������·�ѣ�"))
Delivery_times = int(input("�������ͻ�������"))
installation_cost = int(input("�����밲װ���ã�"))
salary = Basic_salary + car_fare + Delivery_times * 20 + installation_cost + food_subsidy + telephone_bill
print("����ܹ����ǣ�",salary)
input()