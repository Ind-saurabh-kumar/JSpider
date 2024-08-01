
class Fibonacci:
    
    def fibonacciSeries(self):
        
        num = int(input("Enter the number:\n"))
        
        first = 0
        second = 1
        print(first,end=" ")
        print(second, end=" ")
        sum = 0
        
       
        for _ in range(2, num):
            f_series = first+second
            first = second
            second = f_series
            
            sum = sum+f_series
            if sum <= num:
                print(f_series, end=" ")
            


feb=Fibonacci()
feb.fibonacciSeries()