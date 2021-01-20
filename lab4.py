#!/usr/bin/env python3
class energy:
 
    def __init__(self, name, price, energytype, objectof, mdiffrnce):
        self.name = name
        self.price = price  
        self.energytype = energytype  
        self.objectof = objectof
        self.mdiffrnce = mdiffrnce   

    def __repr__(self):
        return '\nНазвание энергосберегающего мероприятия = {} \nСтоимость проведения мероприятия = {} \nТип затрагиваемого энергетического ресурса = {} \nОбъект, на котором будет проводится мероприятие = {} \nЭкономия на ресурсе в месяц после приминения мероприятия = {}\n'.format(self.name, self.price, self.energytype, self.objectof, self.mdiffrnce)

    def display_info(self):
        print("\nНазвание энергосберегающего мероприятия - ",self.name)
        print("Стоимость проведения мероприятия - ",self.price)
        print("Тип затрагиваемого энергетического ресурса - ",self.energytype)
        print("Объект, на котором будет проводится мероприятие - ",self.objectof)
        print("Экономия на ресурсе в месяц после приминения мероприятия - ",self.mdiffrnce,"\n")
 
    def ocup(self):
        self.oc = self.price // self.mdiffrnce
        return "\nСрок окупаемости мероприятия с названием %s %s месяц(ев)" % (self.name, self.oc) 
    
    def percentof(self):
        self.prc = self.mdiffrnce / self.price * 100
        return "\nЭкономия на ресурс в месяц состовляет %s процента от стоимости мероприятия %s" % (self.prc, self.name)

exmpl1 = energy("замена толпивоподающие системы", 545999,"мазут","Топливоподающая система",17300)
exmpl2 = energy("установка топливных фильтров", 124700,"мазут","Топливоподающая система",6800)
exmpl3 = energy("Установка новых топливных ёмкостей", 221000,"мазут","Топливные резервуары",13400)

import sqlite3
conn = sqlite3.connect('lab3.db')
c = conn.cursor()

c.execute('SELECT * FROM table1')
print(c.fetchone())
