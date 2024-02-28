class Trapec():
    
    #поля
    def __init__(self, a, b, c, d):
        #self.storoni = storoni
        
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
        self.perimetr = self.perimeter(self.a, self.b, self.c, self.d)
        self.area = self.area(self.a, self.b, self.c, self.d)
    
    #периметр трапеции
    def perimeter(self, a, b, c, d):
        P = a+b+c+d
        print("Периметр:", P)  
    
    #площдь трапеции    
    def area(self, a, b, c, d):
        S = ((a+b)/2)*(math.sqrt((c**2)-((((b-a)**2)+(c**2)-(d**2))/(2*(b-a)))))
        print("Площадь:", S, "\n")
    
    #вывод   
    def printing(self):
        print(f'Трапеция имеет периметр {self.perimetr} и площадь{self.area} и заслуживает стипендию!')
        
Trapec1 = Trapec([10], [5],[8],[9])        
Trapec1.printing()