class Data:

    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def formatada(self):
        print(self.dd, self.mm, self.yyyy, sep="/")
