from collections import OrderedDict


class Bill:

    def __init__(self, amount):
        self.__amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.__amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.__amount

    def __eq__(self, obj):
        return self.__amount == obj.__amount

    def __hash__(self):
        return hash(self.__amount)


class BillBatch:

    def __init__(self, bills):
        self.__bills = bills

    def __repr__(self):
        return str(self.__bills)

    def __len__(self):
        return len(self.__bills)

    def __getitem__(self, index):
        return self.__bills[index]

    def total(self):
        total_sum = 0
        for i in self.__bills:
            total_sum += int(i)
        return total_sum


class CashDesk:

    def __init__(self):
        self.__batch = []

    def take_money(self, money):
        try:
            for m in money:
                self.__batch.append(m)
        except:
            self.__batch.append(money)

    def total(self):
        total = 0
        for i in self.__batch:
            total += int(i)
        return total

    def inspect(self):
        dic = {}
        for el in self.__batch:
            if el not in dic:
                dic[el] = 1
            else:
                dic[el] += 1
        return self.__sort_dic_keys(dic)

    def __get_key(self, item):
        return item[0]

    def __sort_dic_keys(self, dic):
        l = []
        for i in dic:
            l.append([int(i), int(dic[i])])
        l = sorted(l, key=self.__get_key)
        # return self.__to_bills(l)
        print(self.__to_bills(l))

    def __to_bills(self, l):
        for i in l:
            i[0] = Bill(i[0])
        return l
