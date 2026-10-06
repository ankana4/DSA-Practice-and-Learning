'''
Given the temperature and humidity for the day, determine which category the day's weather falls into.

Temperature (°C)	Humidity (%)	Weather
>=30	>=90	Hot and Humid
>=30	<90	Hot
<30	>=90	Cool and Humid
<30	<90	Cool

'''
t = int(input())
for _ in range(t):
    temp, hum = map(int, input().split())

    if(temp >= 30 and hum >= 90):
        print("Hot and Humidty")
    elif(temp >= 30 and hum <90):
        print("Hot") 
    elif(temp < 30 and hum >= 90):
        print("Cool and Humid")
    else:
        print("Cool")           