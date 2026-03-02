class Outer:
    def __init__(self):
        self.name="outer class" 

    class Inner:
        def __init__(self,outer):
            self.name="inner class"
            self.outer=outer
        
        def display(self):
            print("This is the inner class")
        def displayOuter(self):
            print(f"Outer class name: {self.outer.name}")


outer = Outer()
inner=outer.Inner(outer)
# print(outer.name)
inner.display()
inner.displayOuter()