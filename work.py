#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    HOMME = True
    FEMME = False

    def __init__(self):
        self.sex = Paysan.HOMME

class Paysan(Person):
    def __init__(self):
        self.pv = 100

    def aie(self):
        print("aie")
        print("Mes pvs"+str(self.pv))

class Warrior(Person):
    def __init__(self):
        self.pv = 300
        self.attackLevel = 10

    def attack(self, paysan):
        print("aie")
        paysan.pv -= self.attackLevel


paysan = Paysan()
warrior = Warrior()

warrior.attack(paysan)
paysan.aie()




