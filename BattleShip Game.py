import random, os, Greeting

nameList = []
typeList = []


def Intro(index):
    ShipList = ("Destroyer", "Cruiser", "Armored", "Submarine")
    if index == 1:
        print("Welcome to World of Warships")
        print(ShipList)
        i = 0
        while (i == 0):
            Info = str(input(
                "Do you want to learn more about BattleShips\nAdvice: Take time and read them carefully [yes/no]"))
            if Info.strip().lower() == "yes":
                f = open("BattleShips.txt", "r")
                print(f.read())
                i += 1
            elif Info.strip().lower() == "no":
                i += 1
            else:
                print("Please write yes or no")

    name = str(input(f"Can I have your name captain the {index}."))
    j = 0
    while (j == 0):
        print(ShipList)
        type = str(input("Now you can choose your ship from list"))
        if type.strip().capitalize() in ShipList:
            j += 1
            return (type.strip().capitalize(), name.capitalize().strip())
        else:
            print("Please choose appropriate ship type")
    pass


for i in range(1, 3):
    type, name = Intro(i)
    nameList.append(name)
    typeList.append(type)
print("Now Let's Start The Battle")
print("------------------------------------------------------------------------------------")


class AirStrike():
    def __init__(self):
        self.numberOfArk = 6


class BattleShips(AirStrike):
    def __init__(self, type, name):
        self.type = type
        self.name = name
        if self.type == "Destroyer":
            self.hp = 1200
            self.armor = 100
            self.numberOfCanons = 4
            self.numberOfTorpedoes = 6
            self.selfDefense = 1
        elif self.type == "Cruiser":
            self.hp = 1400
            self.armor = 200
            self.numberOfCanons = 6
            self.selfDefense = 1
        elif self.type == "Armored":
            self.hp = 1600
            self.armor = 400
            self.numberOfCanons = 8
            self.selfDefense = 2
            self.Round = 0
        elif self.type == "Submarine":
            self.hp = 500
            self.armor = 800
            self.numberOfNuces = 1
            self.numberOfJericho = 3
            self.numberOfTorpedoes = 8
            self.criticHit = 1
            self.Round = 0
        pass

    def ShipFire(self, round):
        if self.type == "Destroyer":
            i = 0
            while (i == 0):
                if self.numberOfTorpedoes <= 0:
                    # CANON BREAK
                    canon = self.numberOfCanons
                    Chance = random.randrange(0, 21)
                    if Chance == 10:
                        canon -= 2
                        print("Shit! Captain we lost 2 canons")
                    elif Chance == 5 or Chance == 20:
                        canon -= 1
                        print("Oh! Captain we lost 1 canon")

                    hp = 200 * (canon / self.numberOfCanons)
                    i += 1
                    print(
                        f"We are out of Torpedoes sir!!\nFiring HP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), 0, "TP")

                else:
                    bulletType = str(input(f"Select the bullet type {self.name}\nTP(Torpedoes) ,HP(High-Spreader)"))
                    if bulletType.upper().strip() == "HP":
                        # CANON BREAK
                        canon = self.numberOfCanons
                        Chance = random.randrange(0, 21)
                        if Chance == 10:
                            canon -= 2
                            print("Shit! Captain we lost 2 canons")
                        elif Chance == 5 or Chance == 20:
                            canon -= 1
                            print("Oh! Captain we lost 1 canon")

                        hp = 200 * (canon / self.numberOfCanons)
                        i += 1
                        print(
                            f"Firing HP shells with {canon} out of {self.numberOfCanons} canons Captain {name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                        print("------------------------------------------------------------------------------------")
                        return (int(hp), 0, "TP")

                    elif bulletType.upper().strip() == "TP":
                        self.numberOfTorpedoes -= 1
                        hit = 400
                        percent = random.randrange(0, 45) / 100
                        hp, armor = hit * percent, hit * (1 - percent)
                        i += 1
                        print(
                            f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                        print("------------------------------------------------------------------------------------")
                        return (int(hp), int(armor), "TP")

        elif self.type == "Cruiser":
            i = 0
            while (i == 0):
                bulletType = str(input(f"Select the bullet type {self.name}:\nAP(Armor-Piercing) ,HP(High-Spreader)"))
                # CANON BREAK
                canon = self.numberOfCanons
                Chance = random.randrange(0, 16)
                if Chance == 10:
                    canon -= 2
                    print("Shit! Captain we lost 2 canons")
                elif Chance == 5 or Chance == 15:
                    canon -= 1
                    print("Oh! Captain we lost 1 canon")

                if bulletType.upper() == "AP":
                    hit = 200 * (canon / self.numberOfCanons)
                    percent = random.randrange(1, 41) / 100
                    hp, armor = hit * percent, hit * (1 - percent)
                    i += 1
                    print(
                        f"Firing AP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), int(armor), "AP")

                elif bulletType.upper() == "HP":
                    hp = 200 * (canon / self.numberOfCanons)
                    i += 1
                    print(
                        f"Firing HP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), 0, "HP")

        elif self.type == "Armored":
            i = 0
            while (i == 0):
                bulletType = str(input(f"Select the bullet type {self.name}:\nAP(Armor-Piercing) ,HP(High-Spreader)"))
                # CANON BREAK
                canon = self.numberOfCanons
                Chance = random.randrange(0, 26)
                if Chance == 10:
                    canon -= self.numberOfCanons
                    print("Shit! Captain we lost all canons")
                elif Chance == 5 or Chance == 10 or Chance == 15 or Chance == 20 or Chance == 25:
                    canon -= 2
                    print("Oh! Captain we lost 2 canon")
                elif Chance == 2 or Chance == 4 or Chance == 6 or Chance == 8 or Chance == 10 or Chance == 12:
                    canon -= 1
                    print("Captain we lost 1 canon")

                if bulletType.upper() == "AP":
                    hit = 400 * (canon / self.numberOfCanons)
                    percent = random.randrange(1, 41) / 100
                    hp, armor = hit * percent, hit * (1 - percent)
                    i += 1
                    print(
                        f"Firing AP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), int(armor), "AP")

                elif bulletType.upper() == "HP":
                    hp = 400 * (canon / self.numberOfCanons)
                    i += 1
                    print(
                        f"Firing HP shells with {canon} out of {self.numberOfCanons} canons Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print("------------------------------------------------------------------------------------")
                    return (int(hp), 0, "HP")

        elif self.type == "Submarine":
            if ROUND >= 7:
                i = 0
                while (i == 0):
                    if self.numberOfNuces <= 0:
                        print(f"We are out of Nuclear Missiles sir!!")
                        print("------------------------------------------------------------------------------------")
                        i += 1
                        continue

                    else:
                        nuces = str(input("Sir do you want to fire Nuclear Missile [yes/no]....."))
                        if nuces.strip().lower() == "yes":
                            hit = 1000
                            percent = 0.5
                            hp, armor = hit * percent, hit * percent
                            print(
                                f"Firing Nuclear Missiles Captain {self.name}.\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                            print(
                                "------------------------------------------------------------------------------------")
                            self.numberOfNuces -= 1
                            chance = random.randrange(1, 16)
                            if chance == 10:
                                hp = 0
                                armor = 0
                                self.hp -= 50
                                self.armor -= 150
                                print(
                                    f"Fuck! Captain our Nuclear Missile explode unexpectedly\n{self.type}: {-50}hp {-150} armor")

                            i += 1
                            return (int(hp), int(armor), "Nuce")
                        elif nuces.strip().lower() == "no":
                            bulletType = str(
                                input(f"Select the bullet type {self.name}:\nTP(Torpedoes) ,JR(Jericho Missile)"))
                            if bulletType.strip().upper() == "TP":
                                self.numberOfTorpedoes -= 1
                                hit = 400
                                percent = random.randrange(0, 45) / 100
                                hp, armor = hit * percent, hit * (1 - percent)
                                i += 1
                                print(
                                    f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                                print(
                                    "------------------------------------------------------------------------------------")
                                return (int(hp), int(armor), "TP")
                            elif bulletType.strip().upper() == "JR":
                                self.numberOfJericho -= 1
                                hit = 500
                                hp = hit
                                i += 1
                                print(
                                    f"Firing Jericho Missiles out of {self.numberOfJericho} Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                                print(
                                    "------------------------------------------------------------------------------------")
                                return (int(hp), 0, "JR")
                            else:
                                print("Waiting for your order....")

                        if self.numberOfJericho <= 0 and self.numberOfTorpedoes > 0:
                            print("Sir we are out of Jericho Missiles")
                            self.numberOfTorpedoes -= 1
                            hit = 400
                            percent = random.randrange(0, 45) / 100
                            hp, armor = hit * percent, hit * (1 - percent)
                            i += 1
                            print(
                                f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                            print(
                                "------------------------------------------------------------------------------------")
                            return (int(hp), int(armor), "TP")
                        elif self.numberOfTorpedoes <= 0 and self.numberOfJericho > 0:
                            print("Sir we are out of Torpedoes")
                            self.numberOfJericho -= 1
                            hit = 500
                            hp = hit
                            i += 1
                            print(
                                f"Firing Jericho Missiles Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                            print(
                                "------------------------------------------------------------------------------------")
                            return (int(hp), 0, "JR")
                        elif self.numberOfNuces <= 0 and self.numberOfJericho <= 0 and self.numberOfTorpedoes <= 0:
                            print(f"It was a pleasure to serve you sir {self.name}")
                        else:
                            print("Waiting for your order....")
            else:
                if self.numberOfJericho <= 0 and self.numberOfTorpedoes > 0:
                    print("Sir we are out of Jericho Missiles")
                    self.numberOfTorpedoes -= 1
                    hit = 400
                    percent = random.randrange(0, 45) / 100
                    hp, armor = hit * percent, hit * (1 - percent)
                    print(
                        f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                    print(
                        "------------------------------------------------------------------------------------")
                    return (int(hp), int(armor), "TP")

                elif self.numberOfTorpedoes <= 0 and self.numberOfJericho > 0:
                    print("Sir we are out of Torpedoes")
                    self.numberOfJericho -= 1
                    hit = 500
                    hp = hit
                    print(
                        f"Firing Jericho Missiles out of {self.numberOfJericho} Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                    print(
                        "------------------------------------------------------------------------------------")
                    return (int(hp), 0, "JR")
                elif self.numberOfNuces <= 0 and self.numberOfJericho <= 0:
                    print(f"Sir we are out of everything but one chance in ROUND 9 {self.name}")
                    return (0, 0, "None")
                i = 0
                while (i == 0):
                    bulletType = str(input(f"Select the bullet type {self.name}:\nTP(Torpedoes) ,JR(Jericho Missile)"))
                    if bulletType.strip().upper() == "TP":
                        self.numberOfTorpedoes -= 1
                        hit = 400
                        percent = random.randrange(0, 45) / 100
                        hp, armor = hit * percent, hit * (1 - percent)
                        i += 1
                        print(
                            f"Firing 1 Torpedoes out of {self.numberOfTorpedoes} Captain {self.name}\nHopping to deal {int(hp + armor)} damage to the enemy ship!!")
                        print(
                            "------------------------------------------------------------------------------------")
                        return (int(hp), int(armor), "TP")
                    elif bulletType.strip().upper() == "JR":
                        self.numberOfJericho -= 1
                        hit = 500
                        hp = hit
                        i += 1
                        print(
                            f"Firing Jericho Missiles out of {self.numberOfJericho} Captain {self.name}.\nHopping to deal {int(hp)} damage to the enemy ship!!")
                        print("------------------------------------------------------------------------------------")
                        return (int(hp), 0, "JR")
                    else:
                        print("Waiting for your order....")

        else:
            return False

    def ShipDefense(self, hp, armor, round, bullet):
        if self.type == "Destroyer":
            if bullet == "AP" or bullet == "HP":
                chance = random.randrange(1, 11)
                if chance == 1 or chance == 2 or chance == 3 or chance == 4:
                    print("MISS SIR")
                else:
                    print("DIRECT HIT SIR")
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use Phalanx CIWS\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                self.hp -= hp
                                self.armor -= armor
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        self.hp -= hp
                        self.armor -= armor
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))

            elif bullet == "TP":
                print("DIRECT HIT SIR")
                hp = hp * (random.randrange(70, 101) / 100)
                armor = armor * (random.randrange(71, 101) / 100)
                self.hp -= hp
                self.armor -= armor
                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
            elif bullet == "Nuce":
                if hp==0:
                    print("MISS SIR")
                else:
                    print("DIRECT HIT SIR")
                    self.hp -= hp
                    self.armor = 0
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
            elif bullet == "JR":
                print("DIRECT HIT SIR")
                hp = hp * (random.randrange(50, 61) / 100)
                self.hp -= hp
                self.armor -= armor
                print((f"-{int(hp)}hp\n-{int(armor)} armor"))



        elif self.type == "Cruiser":
            if self.armor > 0:
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2 or chance == 3:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= hp
                        self.armor -= armor
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))

                elif bullet == "TP":
                    print("DIRECT HIT SIR")
                    hp = hp * (random.randrange(80, 91) / 100)
                    armor = armor * (random.randrange(80, 91) / 100)
                    self.hp -= hp
                    self.armor -= armor
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                elif bullet == "Nuce":
                    if hp==0:
                        print("MISS SIR")
                    else:
                        if self.selfDefense > 0:
                            loop = 0
                            while (loop == 0):
                                Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                                if Defense.lower().strip() == "yes":
                                    print("BOOOM Thank God!")
                                    self.selfDefense -= 1
                                    loop += 1
                                elif Defense.lower().strip() == "no":
                                    print("DIRECT HIT SIR")
                                    self.hp -= hp
                                    self.armor = 0
                                    loop += 1
                                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                                else:
                                    print("Waiting for your order....")
                        else:
                            print("DIRECT HIT SIR")
                            self.hp -= hp
                            self.armor = 0
                            print((f"-{int(hp)}hp\n-{int(armor)} armor"))

                elif bullet == "JR":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            hp = hp * (random.randrange(60, 71) / 100)
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        hp = hp * (random.randrange(60, 71) / 100)
                        self.hp -= hp
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
            else:
                self.armor = 0
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2 or chance == 3:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= (hp+armor)
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))

                elif bullet == "TP":
                    print("DIRECT HIT SIR")
                    hp = hp * (random.randrange(80, 91) / 100)
                    armor = armor * (random.randrange(80, 91) / 100)
                    self.hp -= (hp+armor)
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "Nuce":
                    if hp==0:
                        print("MISS SIR")
                    else:
                        if self.selfDefense > 0:
                            loop = 0
                            while (loop == 0):
                                Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                                if Defense.lower().strip() == "yes":
                                    print("BOOOM Thank God!")
                                    self.selfDefense -= 1
                                    loop += 1
                                elif Defense.lower().strip() == "no":
                                    print("DIRECT HIT SIR")
                                    self.hp -= hp
                                    loop += 1
                                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                                else:
                                    print("Waiting for your order....")
                        else:
                            print("DIRECT HIT SIR")
                            self.hp -= hp
                            print((f"-{int(hp)}hp\n-{int(armor)} armor"))

                elif bullet == "JR":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                hp = hp * (random.randrange(60, 71) / 100)
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        hp = hp * (random.randrange(60, 71) / 100)
                        self.hp -= hp
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))



        elif self.type == "Armored":

            if self.armor > 0:
                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= hp
                        self.armor -= armor
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "TP":
                    print("DIRECT HIT SIR")
                    hp = hp * (random.randrange(60, 61) / 100)
                    armor = armor * (random.randrange(60, 61) / 100)
                    self.hp -= hp
                    self.armor -= armor
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "Nuce":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                self.hp -= hp
                                self.armor = 0
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= hp
                        self.armor = 0
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "JR":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                hp = hp * (random.randrange(60, 71) / 100)
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        hp = hp * (random.randrange(60, 71) / 100)
                        self.hp -= hp
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))


            else:
                self.armor = 0


                if bullet == "AP" or bullet == "HP":
                    chance = random.randrange(1, 11)
                    if chance == 1 or chance == 2:
                        print("MISS SIR")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= (hp+armor)
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                elif bullet == "TP":
                    hp = hp * (random.randrange(60, 61) / 100)
                    armor = armor * (random.randrange(60, 61) / 100)
                    self.hp -= (hp+armor)
                    print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "Nuce":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        print("DIRECT HIT SIR")
                        self.hp -= hp
                        self.armor = 0
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))


                elif bullet == "JR":
                    if self.selfDefense > 0:
                        loop = 0
                        while (loop == 0):
                            Defense = str(input(f"Want to use SeaRAM\n+{hp}hp +{armor} armor\n[YES/NO]"))
                            if Defense.lower().strip() == "yes":
                                print("BOOOM Thank God!")
                                self.selfDefense -= 1
                                loop += 1
                            elif Defense.lower().strip() == "no":
                                print("DIRECT HIT SIR")
                                hp = hp * (random.randrange(60, 71) / 100)
                                self.hp -= hp
                                loop += 1
                                print((f"-{int(hp)}hp\n-{int(armor)} armor"))
                            else:
                                print("Waiting for your order....")
                    else:
                        hp = hp * (random.randrange(60, 71) / 100)
                        self.hp -= hp
                        print((f"-{int(hp)}hp\n-{int(armor)} armor"))



        elif self.type == "Submarine":
            if bullet == "AP" or bullet == "HP" or bullet == "TP":
                if self.armor <= 0:
                    self.hp -= hp
                    self.armor = 0
                else:
                    hp = hp * (random.randrange(50, 81) / 100)
                    armor = armor * (random.randrange(70, 91) / 100)
                    self.hp -= hp
                    self.armor -= armor
            print(f"-{int(hp)}hp\n-{int(armor)} armor")
        print(f"Captain {self.name} we have {int(self.hp)}hp and {int(self.armor)} armor left.")
        print("------------------------------------------------------------------------------------")

        pass


Ship1 = BattleShips(typeList[0], nameList[0])
Ship2 = BattleShips(typeList[1], nameList[1])
ROUND = 1
while not Ship1.hp <= 0 or not Ship2.hp <= 0 and not ROUND <= 0:
    print(f"~ROUND{ROUND}~")
    hp1, armor1, AMMUNATION = Ship1.ShipFire(ROUND)
    Ship2.ShipDefense(hp1, armor1, ROUND, AMMUNATION)
    if Ship1.hp <= 0:
        print(f"Captain {Ship2.name} is the ruler of the seas\nTHE END")
        ROUND = -1
        break
    elif Ship2.hp <= 0:
        print(f"Captain {Ship1.name} is the ruler of the seas\nTHE END")
        ROUND = -1
        break
    hp2, armor2, AMMUNATION2 = Ship2.ShipFire(ROUND)
    Ship1.ShipDefense(hp2, armor2, ROUND, AMMUNATION2)
    if Ship1.hp <= 0:
        print(f"Captain {Ship2.name} is the ruler of the seas\nTHE END")
        ROUND = -1
        break
    elif Ship2.hp <= 0:
        print(f"Captain {Ship1.name} is the ruler of the seas\nTHE END")
        ROUND = -1
        break
    ROUND += 1
