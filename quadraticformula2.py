def f(lst):      

    for a,b,c in lst :
        x1 = (-b+((b**2-4*a*c)**0.5))/(2*a)
        x2 = (-b-((b**2-4*a*c)**0.5))/(2*a)
    
        print (x1,x2)


