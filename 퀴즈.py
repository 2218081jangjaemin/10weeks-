class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        return self.price * quantity

Coffee = Beverage("커피", 3000)
GreenTea = Beverage("녹차", 2500)
IceTea = Beverage("아이스티", 3000)

while True:
    selected_beverage = input("주문하실 음료를 선택해주세요(커피, 녹차, 아이스티): ")
    if selected_beverage == "커피":
        quantity = int(input("수량을 입력해주세요: "))
        print("총 가격은", Coffee.calculate(quantity), "원입니다.")
    elif selected_beverage == "녹차":
        quantity = int(input("수량을 입력해주세요: "))
        print("총 가격은", GreenTea.calculate(quantity), "원입니다.")
    elif selected_beverage == "아이스티":
        quantity = int(input("수량을 입력해주세요: "))
        print("총 가격은", IceTea.calculate(quantity), "원입니다.")
    else:
        print("다시 입력해주세요.")
