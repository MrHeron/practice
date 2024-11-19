from abc import ABC, abstractmethod

class DeliveryPartner(ABC):
    _FEE_PER_ROUND = 32

    def __init__(self, callSign, name):
        self.__callSign = callSign
        self.__name = name

    @property
    def callSign(self):
        return self.__callSign

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def computePay():
        pass

    def __str__(self):
        return 'Name: {} CallSign: {}'.format(self.__name, self.__callSign)
        

class FullTimeDeliveryPartner(DeliveryPartner):
    def __init__(self, callSign, name, basicSalary):
        super().__init__(self,callSign,name)
        self.__basicSalary = basicSalary
    
    def computePay(self, rounds):
        pay = self.__basicSalary + (rounds * _FEE_PER_ROUND)
        return super().__str__() + f' Pay: {pay}'

class PartTimeDeliveryPartner(DeliveryPartner):
    _BONUS_ROUNDS = 30
    _BONUS_RATE = 1.85
    
    def computePay(self,rounds):
        if rounds <= 30:
            pay = rounds * _FEE_PER_ROUND
            return super().__str__() + f' Pay: {pay}'
        else:
            pay = (_BONUS_ROUNDS * _FEE_PER_ROUND) + ((rounds - _BONUS_ROUNDS) * (_FEE_PER_ROUND * _BONUS_RATE))
            return super().__str__() + f' Pay: {pay}'

    
def main():
    part_time_partner = PartTimeDeliveryPartner("DP-007", "Lim Lim Kee")
    full_time_partner = FullTimeDeliveryPartner("Maverick", "Tom Yam Kong", 1200)
    
    part_time_partner.computePay(50)
    full_time_partner.computePay(40)
main()
