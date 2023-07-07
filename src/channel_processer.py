from functions_eq import Processing_equations as pe

class Channel_Processor:


    def find_b(X, para_dic):

    # Empty dictionary to save all the I/O data 
        data = {
            "Input" : {},
            "Output" : {},
            "Output_metrics" : {}
            }



        # Insert "X" into data dictionary
        data["Input"]["X"] = X
        

        # Insert "m","c" into data dictionary
        data["Input"]["m"] = para_dic["m"]
        data["Input"]["c"] = para_dic["c"]


        #  Function 1 =>  𝑌 = 𝑚𝑋 + 𝑐
        # using for loop to access individual "X" values in the array 
        Y = []
        for x in X:    
            a = pe.functin_1(para_dic,x)
            Y.append(a)
        # Insert temp output "Y" into data dictionary
        data["Output"]["Y"] = Y


        # Function 3 => 𝐴 = 1/X
        A = []
        for x in X:
            x = pe.function_3(x)
            A.append(x)
        # Insert temp output "A" into data dictionary
        data["Output"]["A"] = A
    


        # Function 2: 𝐵 = 𝐴 + 𝑌
        b = pe.function_2(A,Y)
        # Insert output metrics "b" into data dictionary
        data["Output_metrics"]["b"] = b
        


        # Function 4: 𝐶 = 𝑋 + 𝑏  <- not in use
        C = []
        for x in X:
            a = pe.function_4(x,b)
            C.append(a)
        # Insert output "C" into data dictionary <- in use but not required 
        data["Output"]["C"] = C

    # return data dictionary
        return data

    # New function can be added in "functions_eq" and can be called here to extend the channel