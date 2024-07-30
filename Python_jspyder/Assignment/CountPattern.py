# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:21:30 2024

@author: saura
"""



class CountPatt:
    
    def pattCount(self):
         
        
        n=5 
        
        for i in range(n):
            
            for j in range(n-i):
                print(' ', end=' ')
                
            for k in range(2*i+1):
                
                if i==0:
                    print(i+1, end=' ')
                
                else:
                    print((i*i)+k+1 , end=' ')
            
            
            print()



cp=CountPatt()
cp.pattCount()