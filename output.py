import api

def get_output(data: dict) -> str:
    '''
    Prints out the results.
    '''
    print('Weather data for %s, %s:\n' % (data['name'], data['sys']['country']))
    print('\tWeather description: %s\n' % (data['weather'][0]['description']))
    print('\tCurrent Temperature: %d\n' % (data['main']['temp']))
    print('\tLow: %d / High %d\n' %(data['main']['temp_min'], data['main']['temp_max']))
    
                                                

