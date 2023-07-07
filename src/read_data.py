

class Read_data():


    def __init__(self, path):
        self.path = path


    
# This function reads channel data and return it as a list.
    def read_channels(self):
        with open(f'{self.path}/channels.txt') as f:
            raw_x = f.read()
        raw_x = raw_x.split(',')
        X = raw_x[1:]
        # Converting string to float data type and inserting into a list while cleaning whitespaces
        channel = [float(i.strip()) for i in X]
        return channel

    
# This function reads parameters data and return it as a dictionary.
    def read_parameters(self):
        #open the text file  
        with open( f'{self.path}/parameters.txt', 'r') as f: 
        #read the text file into a list of lines 
            lines = f.readlines() 
        
        #create an empty dictionary 
        para_dict = {} 
        
        #loop through the lines in the text file  
        for line in lines: 
        #split the line on ',' 
            key, value = line.split(',') 
            #strip the whitespace 
            key = key.strip() 
            value = value.strip() 
            #add the key, value pair to the dictionary 
            para_dict[key] = float(value) 

        return para_dict
    
    