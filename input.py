import api
import output

def get_weather() -> str:
    while True:
        city_id = input('Input city id (q to quit): ')
        if city_id == 'q':
            break
        units = input('Input units (metric or imperial, default Kelvin): ')
        try:
            data = api.get_result(api.build_url(city_id, units))
            if units == 'metric':
                output.get_output(data, 'C')
            elif units == 'imperial':
                output.get_output(data, 'F')
            else:
                output.get_output(data, 'K')
        except:
            print('Error')
    
if __name__ == '__main__':
    get_weather()
