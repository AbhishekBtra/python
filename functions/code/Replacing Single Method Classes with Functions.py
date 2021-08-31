class Button:
    def __init__(self,state):
        self.state = state
        pass

    def switch(self):
        if self.state == 'ON' : self.state = 'OFF' 
        else: self.state = 'ON'
        return self.state

b = Button('OFF')
switch_on  = b.switch()
print(switch_on) #ON

# The Button class can be replaced by a clousre

def  button(state):
    def switch():
        if state=='ON':return 'OFF'
        else: return 'ON'
    return switch

switch_on = button('OFF')
print(switch_on()) #ON