import math
class Triangles:   
    def __init__(self,side1,side2,side3,high=None): # attributler
        self.side1=side1  
        self.side2=side2
        self.side3=side3      
        self.high=high   
                      #ucgenin alan ve cevre hesaplarinin goruntulenmesi icin
    def __str__(self):
        return f'Alan:{self.area()} <<<<<>>>>>> Circumradius:{self.circum()}'        
        
    def area(self):       #ucgen alan hesaplama islemleri 
        if self.high!=None: #eger yukselik bilgisi girilmez ise sadece cevre sonucunu verir ve elseye gecer
            return (self.side1*self.high/2)
        else:
            return "Enter height for area calculation "
    
    def circum(self):
        if self.side1>0 and self.side2>0 and self.side3>0: #ucgen cevre hesabi icin kenar uzunluklari eksik girilirse elseye gecer
            return (self.side1+self.side2+self.side3)
        else:
            return ("Enter the side lengths for circumference calculation")
    
class Rectangle():          #dikdortgen sinifi
    def __init__(self,side1,side2): 
        self.side1=side1
        self.side2=side2    
    @property
    def area_rect(self): #butun hesaplamalarda kullanildi.
        if self.side2 is not None:
            return (self.side1*self.side2) 
        else:
            return self.side1             
    @property
    def Circumference(self):
        return ((self.side1+self.side2)*2)
    
    def __str__(self):
        return f'Rectangle Area:{self.area_rect} <<<<<>>>>>> Rectangle Circumference:{self.Circumference}'        
       
        
class Square(Rectangle): #kare sinifi dikdortgen sinifindan inherit 
    def __init__(self,side1,side2):
        super().__init__(side1,side2) #super metodu ile iki kenar inherit ediliyor.
        
    def __str__(self):
        return (f'Square Are:{self.area_rect} <<<<<>>>>>> Square Circumference:{self.Circumference}')  #kare sinifinin area rect mehthodu ve  circumferencee metdou kullanilarak hesap yapiliyo      


class Cube(Square): #kup sinifi
    def __init__(self,side1,side2=None):
        super().__init__(side1,side2)
        
    def __str__(self):        
        if self.side2==None and type(self.side1) is int:
            self.side2=1
            return (f'Cube Area:{pow(self.area_rect,2)*6} Cube Volume:{pow(self.area_rect,3)}')#area_rect func. kullanilarak alan ve hacim hesabi yapiliyor
        else:
            return 'Please enter one side length'     
 
class Pyramid(Triangles,Square): #pyramid sinifi iki farkli siniftan inherit 
   
    def __init__(self,side1,side2=None,side3=None,high=None):
        super().__init__(side1,side2,side3,high)
    def __str__(self):                                  #area_rect methodu kullanilarak kare piramit icin alan ve hacim hesabi yapiliyor
        return (f'Pyramid Area{self.side1*(self.side1+(math.sqrt(pow(self.area_rect,2) + 4*pow(self.high,2))))}\nPyramid volume:{pow(self.area_rect,2)*self.high/3}')
  


tria_1=Triangles(5,5,5,5)
print(tria_1)

rect_1=Rectangle(5,8)
print(rect_1)

sgr_1=Square(5,5)
print(sgr_1)

cube_1=Cube(int(input('One Side Length:'))) #kup icin tek bir kenar uzunlugu input ediliyor
print(cube_1)

pyr_1=Pyramid(side1=int(input('side: ')),high=int(input('high: '))) #taban kenar uzunlugu ve yukseklik input ediliyor.
print(pyr_1)


