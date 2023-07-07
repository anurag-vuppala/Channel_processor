import uvicorn
from fastapi import FastAPI
from channel_processer import Channel_Processor
from read_data import Read_data

app = FastAPI()

@app.get("/")
def calculate_function():
    data_path = 'raw_data'
    # Using Read_data class to read .txt file 
    read = Read_data(data_path)
    X = read.read_channels()
    para_dic = read.read_parameters()
    output = Channel_Processor.find_b(X,para_dic)
    return output

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")