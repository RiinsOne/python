import random
import string


class BSMGenerator():

    def __init__(self):
        self.start = 'BSM'
        self.end = 'ENDBSM'

    def air_departure(self):
        self.a = input('Type departure airport: ')

        v_string = f'.V/1L{self.a}'
        return v_string

    def flight_information(self):
        self.a = input('Type airline\'s IATA code: ')
        self.b = input('Type flight four-digit flight number: ')
        self.c = input('Type flight date (example 15JUN): ')
        self.d = input('Type destination airport (example SVO): ')
        
        f_string = f'.F/{self.a}{self.b}/{self.c}/{self.d}/Y'
        return f_string

    def tag_num(self):
        self.first_part = '0777'
        self.last_part = '001'
        self.middle_part = str(random.randint(100000, 999999))
        self.full_tag = self.first_part+self.middle_part+self.last_part
        
        n_string = f'.N/{self.full_tag}'
        return n_string

    def seat_place(self):
        self.a = input('Type seat place (example 12F): ')
        self.first_num = str(random.randint(0, 2))
        self.second_num = str(random.randint(0, 9))
        self.third_num = str(random.randint(0, 9))
        self.bn_num = f'{self.first_num}{self.second_num}{self.third_num}'

        s_string = f'.S/Y/{self.a}/C/{self.bn_num}//N//A'
        return s_string
    
    def luggage_weight(self):
        self.pieces = random.randint(1, 3)
        self.weight = 0
        a = self.pieces
        b = self.weight
        
        if a == 1:
            b = str(random.randint(10, 20))
        else:
            b = str(random.randint(25, 35))
        
        w_string = f'.W/K/{a}/{b}'
        return w_string

    def passenger_info(self):
        self.name = a = input('Type passenger\'s name: ')
        self.surname = b = input('Type passenger\'s surname: ')

        p_string = f'.P/{b.upper()}/{a.upper()}'
        return p_string

    def pnr_number(self):
        self.chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        pnr = ''
        for char in range(6):
            pnr = pnr + random.choice(self.chars)
        
        l_string = f'.L/{pnr}'
        return l_string


def bsm_result():
    bsm = BSMGenerator()

    v = bsm.air_departure()
    f = bsm.flight_information()
    n = bsm.tag_num()
    s = bsm.seat_place()
    w = bsm.luggage_weight()
    p = bsm.passenger_info()
    l = bsm.pnr_number()

    bsm_string = f'{bsm.start}\n{v}\n{f}\n{n}\n{s}\n{w}\n{p}\n{l}\n{bsm.end}'
    return bsm_string


print(bsm_result())


# print(x.pnr_number())
# chars = string.ascii_letters.upper()
# b = random.choice(chars)
# print(b)
# print(chars)

# print(x.passenger_info())
# print(x.seat_place())
# print(x.tag_num())
# x1 = x.flight_information()
# print(x.end)
# print(x1)
# print(x.air_depart())


# a = [chr(i) for i in range(ord('a'), ord('z')+1)]
# print(a)


#