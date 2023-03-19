class dsl(object):
    def __init__(self,name):
        self.name=name
    def whois(self):
        if self.name == "HyunBeen":
            print(f'{self.name} is a 석박통합')
        elif self.name == 'Serin':
            print(f'{self.name}is a 석사과정')
        elif self.name == 'Sunmin':
            print(f'{self.name}is a 인턴중')
        else:
            print(f'{self.name}가 자유다')