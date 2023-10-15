import time
import threading

# Tukang cukur
def barber(customers):
    while True:
        # Tukang cukur tidur
        while not any(customer.is_waiting for customer in customers):
            sleep()

        # Tukang cukur memotong rambut pelanggan pertama yang masuk
        for customer in customers:
            if customer.is_waiting:
                customer.is_waiting = False
                customer.cut_hair()  # Memanggil metode cut_hair dari objek customer
                break

# Pelanggan
class Customer:
    def __init__(self, name):
        self.name = name
        self.is_waiting = False

    # Pelanggan masuk ke toko
    def enter_shop(self, customers):
        self.is_waiting = True
        customers.append(self)

    # Pelanggan dipotong rambutnya
    def cut_hair(self):
        print("Tukang cukur sedang memotong rambut {}.".format(self.name))
        time.sleep(1)
        print("Tukang cukur selesai memotong rambut {}.".format(self.name))

    # Pelanggan keluar dari toko
    def exit_shop(self, customers):
        customers.remove(self)

def sleep():
    time.sleep(1)

# Variabel global
customers = []

# Main program
if __name__ == "__main__":
    john = Customer("John")
    jane = Customer("Jane")
    peter = Customer("Peter")

    john.enter_shop(customers)
    jane.enter_shop(customers)
    peter.enter_shop(customers)
    barber(customers)
