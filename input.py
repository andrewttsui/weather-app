import api
import output

def get_weather() -> str:
    while True:
        city_id = input('Input city id (q to quit): ')
        if city_id == 'q':
            break
        
        data = api.get_result(api.build_url(city_id))
        output.get_output(data)
    
if __name__ == '__main__':
    get_weather()
