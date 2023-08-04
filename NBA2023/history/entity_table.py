class EntityTable:
    def __init__(self,name):
        self.name = name
        self.head = []
        self.body = []

    def add_head(self, element):
        self.head.append(element)    

    def add_body(self, element):
        self.body.append(element)    

    def print(self):
        print(self.name)
        print('head')
        for element in self.head:
            print(element.print_array())
        print('body')
        for element in self.body:
            print(element.print_array())
        return 0
    def to_csv(self):
        dataCsv = []
        for element in self.body:
            dataCsv.append(element.array)
        return dataCsv