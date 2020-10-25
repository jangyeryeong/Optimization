# #for a in range(10):
#     print('Welcome python world!', end = "")

# print("Welcome, %s %(myname,)")
# myname = "A"
# print("Hi, myname is %s. %d years old." %(myname, 16))

# A = 3+1
# B = 3-1
# C = 3*1
# D = 3/1
# E = 3**10
# F = 17//3 #몫이 나옴
#
# print(A,B,C,D,E,F)

# a = 2**32
# b = 10**1024
# print(a,b)

# a = 3.14
# b = 100000000
# print(type(a),type(a+b))

# sum = 0.0
# for i in range(10):
#     sum+=0.1

# print(sum) #2진수로 저장하기때문에 오차가 발생, 소수는 조심스럽게 계산하자 ㅎㅎ

#print("""sa
# dj  al
# dkjlk""") #여러 줄의 문자열을 사용할 때
#
# a = 'sdadad'
# b = 'asda asd'
#
# print(a + '' +b)
# print("="*30)
#
# a = 'apple from the sky'
#
# print(a[0],a[1],a[-1])
# print(a[0:5],a[6:],a[:5],a[:])

# print("apple".count("p"))
# print("pithon".replace("i", "y"))

# a = []
# b = [1,2,3]
# t = ["car", ["BMW",1,2,3,4,5,6,7],["Audi",3,4,5,6]]
# print(t)

# a = [1,2,3,['a','b','c',["inner","most","list"]],4,5,6]
# print(a[0])
# print(a[3])
# print(a[3][1])
# print(a[3][3][2])

# print(a[0:2])
# print(a[4:])
# print(a[3][2:])

# a = [1,2,3]
# b = [4,5,6]
#
# print(a + [])
# print(a+b) 순서를 보장
# print(a*3)

# a = [1,2,3]
# b = [4,5,6]
#
# a[0] = 2
# a[1] = 3
# a[2] = b
#
# print(a)

# a = [1,2,3]
# a[0:1] = []
#
# print(a)
#
# del a[1]
# print(a)

# a = [1,2,3]
# print(a.pop(1)) #삭제하고 리턴!
# print(a)
#
# a = [4,2,3,1,5]
# a.sort()
# print(a)

#값을 바꿔도 안바뀜 튜플이기 때문
# a = ('a','b','c')
# b = (1,2,3)
# c = (1,) 콤마를 안 찍어주면 숫자로 인식하기 때문
# d = ('a','b',('ab','cd'))
# b[0] = 10
# del b[0]
# print(d)

# grade = {'kevin':95,'bill':93,'mark':55,'larry':30}
# print(grade['mark'])
#
# grade['paul'] = 100
# grade['paul']
# del grade['larry']
#
# print(grade)

# d = {'name': "kevin","final": 84, "report":90}
# print(d.get('name'))
# d.clear()
# d = {}
# print(d.get('hello')) #키가 없는 경우 get을 써야지 에러가 안남

# a = 1<2
# print(bool(bool(None) == False)) #데이터가 없으면 false 1은 true

# a = 11
# b = 13
# if a > 10 and b > 10:
#     print(" 두 숫자는 10보다 큽니다")
# elif a > 10 or b > 10:
#     print(" a또는 b는 10보다 큽니다")
# else:
#     print(" a,b, 둘다 10보다 작습니다")

# while True:
#     name = input("Enter YOur Name: ")
#     title = input("your Title (Mr.,Miss, Prof.): ")
#     print("환영, %s %s." %(title,name))

# for item in ["apple", "banana", "orange"]:
#     print(item)
#
# for fib in (1,1,2,3,5,8,13,21,34,55,89):
#     print(fib)
#
# menu = {"Coffee": 3800, "Latte": 4500} #순서가 보장 X
# for item in list(menu.items()):
#     print("%s\t\t\t%d WON" %item)

# for number in range(1,10):
#     print("%d of 9" %(number,))

avleadtime = 1
mxleadtime = 2
stock = []
purchase = []
sale = []
purchase_average = []
stock_cycle = []
while True:
    if len(stock) == 0:
        print("=" * 100)
        a = int(input("구매량 : "))
        b = int(input("판매량 : "))
        c = int(a) - int(b)
        purchase.append(int(a))
        sale.append(int(b))
        stock.append(c)
        print("구매량 리스트 : %s \n판매량 리스트 : %s \n재고량 리스트 : %s" % (purchase, sale, stock))
        print("최대 판매량 : %s" %(max(sale)))
        print("평균 판매량 : %s" %(sum(sale) / len(sale)))
        print("안전 재고량 : %s" %((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime)))

    elif len(stock) < 3:
        print("=" * 100)
        a = int(input("구매량 : "))
        b = int(input("판매량 : "))
        c = int(a) - int(b) + stock[-1]
        stock.append(c)
        purchase.append(int(a))
        sale.append(int(b))
        print("구매량 리스트 : %s \n판매량 리스트 : %s \n재고량 리스트 : %s" %(purchase, sale, stock))
        print("최대 판매량 : %s" % (max(sale)))
        print("평균 판매량 : %s" %(sum(sale) / len(sale)))
        print("안전 재고량 : %s" %((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime)))

    else :
        print("=" * 100)
        a = int(input("구매량 : "))
        b = int(input("판매량 : "))
        c = int(a) - int(b) + stock[-1]
        stock.append(c)
        purchase.append(int(a))
        sale.append(int(b))
        print("구매량 리스트 : %s \n판매량 리스트 : %s \n재고량 리스트 : %s" %(purchase, sale, stock))
        #판매량 평균
        d = (sale[-1] + sale[-2] + sale[-3] + sale[-4])/4
        purchase_average.append(d)
        print("판매량 평균 : %s" %purchase_average)

        #재고 주기
        e = stock[-1]/purchase_average[-1]
        stock_cycle.append(round(e,2))
        print("재고주기 : %s" %stock_cycle)
        print("최대 판매량 : %s" % (max(sale)))
        print("평균 판매량 : %s" %(sum(sale) / len(sale)))
        print("안전 재고량 : %s" %((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime)))
        print("안전 재고 주기: %s" %(((max(sale) * mxleadtime) - (sum(sale) / len(sale) * avleadtime))/d))

