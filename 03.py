class CocaCola:
    formula=['caffeine','sugar','water','soda']#使用class来定义一个类，formula就是类的属性
coke_for_me=CocaCola()
coke_for_you=CocaCola()#创建变量就如同赋值
print(CocaCola.formula)
print(coke_for_me.formula)
print(coke_for_you.formula)
for element in coke_for_you.formula:#类是属性与正常的变量并无区别
    print(element)
coke_for_China=CocaCola()
coke_for_China.local_logo='可口可乐'#创建实例属性
print(coke_for_China.local_logo)#打印实例属性引用结果
class CocaCola:
    formula=['caffeine','sugar','water','soda']
    def drink(self,how_much):
        if how_much=='a sip':
            print('Cool')
        if how_much=='whole bottle':
            print('Headache')
ice_coke=CocaCola()
ice_coke.drink('whole bottle')
class CocaCola:
    formula=['caffeine','sugar','water','soda']
    def __init__(self):
        self.local_logo='可口可乐'
    def drink(self):
        print('Energy')
coke=CocaCola()
print(coke.local_logo)
coke.drink()
class CocaCola:
    formula=['caffeine','sugar','water','soda']
    def __init__(self):
        for element in self.formula:
            print('Coke has {}'.format(element))
    def drink(self):
        print('Energy')
coke=CocaCola()
coke.drink()
class CocaCola:
    formula=['caffeine','sugar','water','soda']
    def __init__(self,logo_game):
        self.local_logo=logo_game
    def drink(self):
        print('energy')
coke1=CocaCola('可口可乐')
print(coke1.local_logo)
class CocaCola:
    calories=140
    sodium=45
    total_carb=39
    caffeine=34
    ingredient=[
        'High fructose Corn Syrup',
        'Carbonated Water',
        'phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]
    def __init__(self,logo_game):
        self.local_logo=logo_game
    def drink(self):
        print('You got {} cal energy!'.format(self.calories))
class CaffeineFree(CocaCola):#类的传承
    calories = 0
    ingredient=[
        'High fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'caramel Color'#对于上面可口可乐的覆盖与改动
    ]
coke2=CaffeineFree('Caffeine_FREE')
coke2.drink()
class TestA:
    attr=1
obj_a=TestA()
TestA.attr=42
print(obj_a.attr)
class TestA:
    attr=1
obj_a=TestA
obj_b=TestA
obj_a.attr=42
print(obj_b.attr)
class TestA:
    attr=1
    def __init__(self):
        self.attr=42
obj_a=TestA()
print(obj_a.attr)
n=abs(-87867)#求取定义数字的绝对值
print(n)
n=round(3.4)#四舍五入的函数
print(n)
n=pow(2,5)#幂函数2的5次方
print(n)
message='xiao hong \n xiao ming'
print(message)
message1='%s ,you have some money'%'liuyang'
print(message1)
message2='I am %s ,I\'m %d years old'
print(message2%('sunbin',21))