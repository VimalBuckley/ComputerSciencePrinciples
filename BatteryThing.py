class Battery:
    def __init__(self, name: str):
        self.name = name
        self.charge: int = None
    
    def update(self, charge: int):
        self.charge = charge

    def sumarize(self):
        print(str(self.charge))

jayden = Battery("Jayden")
jayden.update(130)

batteries = {
    jayden.name : jayden
}

def checkBatteries(names: list):
    for name in names:
        batteries.get(name).sumarize()