class device:
    def power_on(self):
        print("device switched on")
class phone(device):
    def call(self):
        print("making a phone call")
class computer(device):
    def run_program(self):
        print("running python program")
samsung=phone()
samsung.call()
samsung.power_on()
hp=computer()
hp.power_on()
hp.run_program()


class phone:
    def camera(self):
        print("taking a normal photo")
class smartphone(phone):
    def camer(self):
        print("taking a portrait photo")
samsung=smartphone()
samsung.camera()
nokia=phone()
nokia.camera()

class bank:
    __amount=200
    def printamount(self):
        return self.__amount
hdfc=bank()
print(hdfc.printamount())



from abc import ABC,abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(payment):
    def pay(self):
        print("payment done using UPI")
class phonepe(payment):
    def pay(self):
        print("payment done using phonepe")
payment=UPI()
payment.pay()
payment=phonepe
payment.pay()
