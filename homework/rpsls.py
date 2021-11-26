#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：杨杰
日期：2021/11/26
"""
import random #导入random模块

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=='石头':
        name=0
    elif name=='史波克':
        name=1
    elif name=='纸':
        name=2
    elif name=='蜥蜴':
        name=3
    else:
        name=4
    return name##

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        number='石头'
    elif number==1:
        number='史波克'
    elif number==2:
        number='纸'
    elif number==3:
        number='蜥蜴'
    else:
        number='剪刀'
    return number

def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    comp_number=random.randrange(0,5) #利用randrange方法产生0-4之间的随机整数
    player_choice_number=name_to_number(player_choice)
    comp_name=number_to_name(comp_number)
    print('您的选择为：%s'%player_choice)
    print('计算机的选择为：%s'%comp_name)
    if comp_number==0:
        if player_choice_number==3 or player_choice_number==4:
            print('计算机赢了')
        elif player_choice_number==0:
            print('您和计算机出的一样呢')
        else:
            print('您赢了')#
    elif comp_number==1:
        if player_choice_number==0 or player_choice_number==4:
            print('计算机赢了')
        elif player_choice_number==1:
            print('您和计算机出的一样呢')
        else:
            print('您赢了')
    elif comp_number==2:
        if player_choice_number==0 or player_choice_number==1:
            print('计算机赢了')
        elif player_choice_number==2:
            print('您和计算机出的一样呢')
        else:
            print('您赢了')
    elif comp_number==3:
        if player_choice_number==1 or player_choice_number==2:
            print('计算机赢了')
        elif player_choice_number==3:
            print('您和计算机出的一样呢')
        else:
            print('您赢了')
    else:
        if player_choice_number==3 or player_choice_number==2:
            print('计算机赢了')
        elif player_choice_number==4:
            print('您和计算机出的一样呢')
        else:
            print('您赢了')
    """
    通过if,elif,else函数判断输赢并输出相应结果
    """
    return 0

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
print("----------------")
if choice_name != '石头' and choice_name != '史波克' and choice_name != '纸' and choice_name != '蜥蜴' and choice_name != '剪刀':
    print('Error: No Correct Name')
    """
    对输错的情况进行判断
    """
else:
    rpsls(choice_name)
