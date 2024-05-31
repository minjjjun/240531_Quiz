class Beverage:
    def __init__(self):
     self.menu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}

    def calculate(self, drink, quantity):
        if drink in self.menu:
            price = self.menu[drink] * quantity
            return price
def main():
    kiosk = Beverage()
    drink = input("주문하실 음료를 선택해주세요.(커피, 녹차, 아이스티):")
    quantity = int(input("수량을 입력해주세요.:"))
    total_price = kiosk.calculate(drink, quantity)
    print("총 가격은",total_price,"원 입니다.")

if __name__ == "__main__":
    main()

