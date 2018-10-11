list=[1,2,3]
print(sum(list))
import random
point1=random.randrange(1,7)
point2=random.randrange(1,7)
point3=random.randrange(1,7)
print(point1,point2,point3)
def game():
    list=[]
    number1=random.randrange(1,7)
    number2=random.randrange(1,7)
    number3=random.randrange(1,7)
    list.append(number1)
    list.append(number2)
    list.append(number3)
    output=input('Big or Small:')
    output_1=output=='Big'
    output_2=output=='Small'
    if output_1:
        if sum(list)>=11 and sum(list)<=18:
            print('The points are '+str(list)+' You are win!')
        elif sum(list)>=3 and sum(list)<=10:
            print('The points are '+str(list)+' You are lose!')
    elif output_2:
        if sum(list)>=11 and sum(list)<=18:
            print('The points are '+str(list)+' You are lose!')
        elif sum(list)>=3 and sum(list)<=10:
            print('The points are '+str(list)+' You are win')
import random
def roll_dice(number=3,points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points=[]
    while number>0:
        point=random.randrange(1,7)#randrange是指调用范围内任意一个值，必须在使用random模块的时候才能够使用
        points.append(point)
        number=number-1
    return points
def start_result(total):
    isBig= 11<=total<=18
    isSmall= 3<=total<=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'
def start_game():#赌大小的函数
    money=1000
    while money>0:
        print('<<<<< Game Start! >>>>>')
        choice=['Big','Small']
        your_choice=input('Big or Small:')
        if your_choice in choice:
            your_money=int(input('How much you wanna bet? -'))
            points=roll_dice()
            total=sum(points)
            you_win=your_choice==start_result(total)
            if you_win:
                print('you points are ',points,'you win')
                print('you gained {},your have {} now'.format(your_money,your_money+money))
                money=money+your_money
            else:
                print('you points are ',points,'you lose')
                print('you lost {},your have {} now'.format(your_money,money-your_money))
                money=money-your_money
        else:
            print('Invalid Words!')
    else:
        print('Game Over')
def number_locate():#查询电话归属的函数
    CN_mobile=[134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,1705]
    CN_union=[130,131,132,155,156,185,186,145,176,1709]
    CN_telecom=[133,153,180,181,189,177,1700]
    number=input('Enter your phone number:')
    your_number_1=int(number[:3])
    your_number_2=int(number[:4])
    if len(number)==11:
        message='We\'re sending verification code via text to your phone: '+str(number)
        if your_number_1 in CN_mobile or your_number_2 in CN_mobile:
            print('Operator: China Mobile')
            print(message)
        elif your_number_1 in CN_union or your_number_2 in CN_union:
            print('Operator: China Union')
            print(message)
        elif your_number_1 in CN_telecom or your_number_2 in CN_telecom:
            print('Operator: China Telecom')
            print(message)
        else:
            print('No such a operator')
    else:
        print('Invalid length,your number should be in 11 digits')
    number_locate()
periodic_table=['H','He','Li','Be','B','C','N','O','F','Ne']
print(periodic_table[-10:-7])
print(periodic_table[:9])
print(periodic_table[0:3])
a={'key':123,'keys':123}
print(a)
NASDAQ_code={'BIDU':'Baidu','SINA':'Sina'}
NASDAQ_code['YOKU']='Youku'#字典添加
print(NASDAQ_code)
NASDAQ_code.update({'FB':"Facebook",'TSLA':'Tesla'})
del NASDAQ_code['FB']
print(NASDAQ_code)
print(NASDAQ_code['TSLA'])
a_set={'apple','cherry','orange'}
a_set.add('banana')
print(a_set)
a_set.discard('orange')
print(a_set)
a=[i**2 for i in range(-5,5)]
c=[j+1 for j in range(-10,0)]
k=[n for n in range(1,10) if n%2==0]
z=[letter.lower() for letter in 'ABCDEFGHILKLMN']
print(a)
print(c)
print(k)
print(z)
d={i:i+1 for i in range(4)}
print(d)
g={i:j for i,j in zip(range(1,6),range(4,9))}
print(g)
g={i:f.upper() for i,f in zip(range(1,6),'abcde')}#字典简易的表达
print(g)
letter=['a','b','c','d','e']
for num,letter in enumerate(letter):#循环列表时获取元素的索引（enumerate)
    print(letter,'is',num)
letter_1=['apple','orange','cherry']
for num,letter_1 in enumerate(letter_1):
    print(letter_1,'is',num)
lyric='The night begin to shine,the night begin to shine'#split方法将字符串的每个单词分开，得到独立的单词
word=lyric.split()
print(word)
michael={'hair':'black','sex':'boy','hobby':'singing'}
for key,value in michael.items():#遍历所有的键-值
    print('key is '+key)
    print('value is '+value)
for feature in michael:
    print(feature)
liuyang={'hair':'yellow','sex':'man','hobby':'internet','health':'internet'}
favorite_feature=['hair']
for feature in liuyang:#遍历所有的键
    print(feature)
    print(sorted(feature))#把每个键的顺序排列
    if feature in favorite_feature:
        print('good')
for feature_1 in sorted(liuyang):#把字典里的键进行排列
    print(feature_1)
for feature3 in sorted(liuyang.values()):#把字典里的值进行排列
    print(feature3)
for feature4 in set(liuyang.values()):#set函数表示集合，避免重复的值
    print(feature4)
apple={'color':'red'}
banana={'color':'yellow'}
watermelon={'color':'green'}
fruit_color=[apple,banana,watermelon]#几个列表储存到一起的方法
print(fruit_color)
for fruit_color1 in fruit_color:
    print(fruit_color1)
fruit=[]
for fruit_number in range(3):
    new_fruit={'color':'red'}
    fruit.append(new_fruit)
for fruits in fruit:
    print(fruits)
print('total number of fruits: '+str(len(fruit)))
fruits=[]
for fruit_number in range(4):
    new_fruits={'color':'yellow','price':'2'}
    fruits.append(new_fruits)
for fruit in fruits[0:2]:
    color1=fruit['color']=='yellow'
    color2=fruit['price']=='2'
    if color1:
        fruit['color']='red'
    if color2:
        fruit['price']='3'
for fruit in fruits:
    print(fruit)
favorite_language={'jen':['python','ruby'],'sarah':['c','c++'],'edward':['ruby','go'],'phil':['python','haskell']}#字典里一个键有多个值
for name,languages in favorite_language.items():
    print('\n{}\'s favorite language are:'.format(name.title()))
    for language in languages:
        print(language)
users={'haha':{'first_name':'xiao','last_name':'ming','sex':'boy'},'hehe':{'first_name':'xiao','last_name':'hong','sex':'girl'},'dada':{'first_name':'xiao','last_name':'li','sex':'girl'}}
for user,information in users.items():
    sex=information['sex']=='boy'
    if sex:
        print('users name is {},fullname is {}'.format(user,information['first_name']+information['last_name']))
    else:
        print('users are girl.their names are {}. '.format(information['first_name']+information['last_name']))
number=0
while number<10:
    number+=1
    if number%2==0:
        continue
    else:
        print(number)
def pokemons(xiaoming_pokemons,xiaozhi_pokemon):
    while xiaoming_pokemons:
        pokemon=xiaoming_pokemons.pop()
        xiaozhi_pokemon.append(pokemon)
        print('这是小明的{}'.format(pokemon))
def show_pokemon(xiaozhi_pokemon):
    print('\n这是小智的:')
    for pokemon1 in xiaozhi_pokemon:
        print(pokemon1)
xiaoming_pokemons=['pikaqiu','xiaohonglong','miaohuazhongzi','huobaohou']
xiaozhi_pokemon=[]
pokemons(xiaoming_pokemons[:],xiaozhi_pokemon)
show_pokemon(xiaozhi_pokemon)