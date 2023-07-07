import pytest
from functions_eq import Processing_equations
from read_data import Read_data
from channel_processer import Channel_Processor


# Test class for Channel_Processor
class TestChannelProcessor:

    # Test find_b method
    def test_find_b(self):
        path = "raw_data"
        channel_processor = Channel_Processor()
        expected_result = {
            "Input": {
                "X": [0.814723686393179, 0.905791937075619, 0.126986816293506,
                      0.913375856139019, 0.63235924622541, 0.0975404049994095],
                "m": 2.0,
                "c": 3.0
            },
            "Output": {
                "Y": [4.444448756179455, 4.821379874371856, 3.253973632587012,
                      4.826751568278038, 3.26471849245082, 3.195080809998819],
                "A": [1.2274370839818595, 1.1031471299017904, 7.87412583182346,
                      1.0945208999632784, 1.5793050628948534, 10.247963467949723],
                "C": [4.444448756179455, 4.826751568278038, 3.253973632587012,
                      4.826751568278038, 3.26471849245082, 3.195080809998819]
            },
            "Output_metrics": {
                "b": 3.890892160530963
            }
        }
        op = {
            "m": 2.0,
            "c": 3.0
            }
        x = [0.814723686393179, 0.905791937075619, 0.126986816293506,
                      0.913375856139019, 0.63235924622541, 0.0975404049994095]
        result = Channel_Processor.find_b(x,op)
        assert type(result) == type(expected_result)

# Test class for Read_data
class TestReadData:

        # Test read_channels method
    def test_read_channels(self):
        path = "raw_data"
        read_data = Read_data(path)
        expected_result = [0.814723686393179,0.905791937075619,0.126986816293506,0.913375856139019,0.63235924622541,0.0975404049994095,]
        result = read_data.read_channels()
        assert type(result) == type(expected_result)

    # Test read_parameters method
    def test_read_parameters(self):
        path = "raw_data"
        read_data = Read_data(path)
        expected_result = {
            "m": 2.0,
            "c": 0.5,
        }
        result = read_data.read_parameters()
        assert result == expected_result


class TestProcessingEquations:

    # Test functin_1 method
    def test_functin_1(self):
        Pr = {"m": 2, "c": 3}
        I = 5
        result = Processing_equations.functin_1(Pr, I)
        assert result == 13.0

    # Test function_2 method
    def test_function_2(self):
        A = [1, 2, 3]
        Y = [4, 5, 6]
        result = Processing_equations.function_2(A, Y)
        assert result == 7.0

    # Test function_3 method
    def test_function_3(self):
        X = 2
        result = Processing_equations.function_3(X)
        assert result == 0.5

    # Test function_4 method
    def test_function_4(self):
        X = 2
        b = 3
        result = Processing_equations.function_4(X, b)
        assert result == 5.0






# Run the tests
if __name__ == "__main__":
    pytest.main()
