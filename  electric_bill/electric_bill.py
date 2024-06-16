#Write a program to calculate the amount of electricity to be paid in a month of households. Knowing that the electricity unit price is calculated on a progressive basis: the first 100 numbers cost 550 VND/number, the next 100 numbers cost 900 VND/number, from the 201st number onwards, and the price is 1500 VND/number. 
#Print the list in descending order of electricity bills.

class ElectricBill:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.bill = 0
    def calculate_bill(self):
        if self.number <= 100:
            self.bill = self.number * 550
        elif self.number <= 200:
            self.bill = 100 * 550 + (self.number - 100) * 900
        else:
            self.bill = 100 * 550 + 100 * 900 + (self.number - 200) * 1500
        return self.bill 
    
    def __str__(self):
        return f"{self.name}: {self.bill}"
    
def main():
    n = int(input())
    households = []
    for i in range(n):
        name, number = input().split()
        number = int(number)
        house = ElectricBill(name, number)
        house.calculate_bill()
        households.append(house)
    households.sort(key=lambda x: x.bill, reverse=True)
    for house in households:
        print(house)

if __name__ == "__main__":
    main()