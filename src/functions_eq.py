import pandas as pd
import statistics as sta


class Processing_equations():

    
    #  Function 1 =>  𝑌 = 𝑚𝑋 + 𝑐
    #   
    def functin_1(Pr,I):
        return float(float((Pr["m"]) * float(I)) + float(Pr["c"]))




     # Function 2: 𝐵 = 𝐴 + 𝑌
    def function_2(A,Y):
        B = []
        for a in range(len(A)):
            temp = A[a] + Y[a]
            B.append(temp)
        return float(sta.mean(B))




    # Function 3 => 𝐴 = 1/X
    def function_3(X):
        return float((1/X))
    


    # Function 4: 𝐶 = 𝑋 + 𝑏
    def function_4(X,b):
        return float(X + b)