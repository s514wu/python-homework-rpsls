#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����
���ڣ�2021/11/26
"""
import random #����randomģ��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=='ʯͷ':
        name=0
    elif name=='ʷ����':
        name=1
    elif name=='ֽ':
        name=2
    elif name=='����':
        name=3
    else:
        name=4
    return name##

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        number='ʯͷ'
    elif number==1:
        number='ʷ����'
    elif number==2:
        number='ֽ'
    elif number==3:
        number='����'
    else:
        number='����'
    return number

def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    comp_number=random.randrange(0,5) #����randrange��������0-4֮����������
    player_choice_number=name_to_number(player_choice)
    comp_name=number_to_name(comp_number)
    print('����ѡ��Ϊ��%s'%player_choice)
    print('�������ѡ��Ϊ��%s'%comp_name)
    if comp_number==0:
        if player_choice_number==3 or player_choice_number==4:
            print('�����Ӯ��')
        elif player_choice_number==0:
            print('���ͼ��������һ����')
        else:
            print('��Ӯ��')#
    elif comp_number==1:
        if player_choice_number==0 or player_choice_number==4:
            print('�����Ӯ��')
        elif player_choice_number==1:
            print('���ͼ��������һ����')
        else:
            print('��Ӯ��')
    elif comp_number==2:
        if player_choice_number==0 or player_choice_number==1:
            print('�����Ӯ��')
        elif player_choice_number==2:
            print('���ͼ��������һ����')
        else:
            print('��Ӯ��')
    elif comp_number==3:
        if player_choice_number==1 or player_choice_number==2:
            print('�����Ӯ��')
        elif player_choice_number==3:
            print('���ͼ��������һ����')
        else:
            print('��Ӯ��')
    else:
        if player_choice_number==3 or player_choice_number==2:
            print('�����Ӯ��')
        elif player_choice_number==4:
            print('���ͼ��������һ����')
        else:
            print('��Ӯ��')
    """
    ͨ��if,elif,else�����ж���Ӯ�������Ӧ���
    """
    return 0

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
print("----------------")
if choice_name != 'ʯͷ' and choice_name != 'ʷ����' and choice_name != 'ֽ' and choice_name != '����' and choice_name != '����':
    print('Error: No Correct Name')
    """
    ��������������ж�
    """
else:
    rpsls(choice_name)
