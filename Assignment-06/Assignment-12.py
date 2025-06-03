

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius):

        fahrenheit = (celsius * 9/5) + 32

        return fahrenheit
    
print(TemperatureConverter.celsius_to_fahrenheit(25))
