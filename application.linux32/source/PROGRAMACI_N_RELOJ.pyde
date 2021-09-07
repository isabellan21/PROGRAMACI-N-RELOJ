s= 0
m= 0
h= 0
def setup():
    size (150, 150)
def draw():
    background(188, 252, 255)
    s = second()  # Values from 0 - 59
    m = minute()  # Values from 0 - 59
    h = hour()  # Values from 0 - 23
    rect(s, 25, s, 25)
    rect(m, 45, m, 25)
    rect(h, 65, h, 25)
