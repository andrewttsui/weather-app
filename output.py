import api

def get_output(data: dict, unit: str) -> str:
    '''
    Prints out the results.
    '''
    print('Weather data for %s, %s:\n' % (data['name'], data['sys']['country']))
    print('\tWeather description: %s\n' % (data['weather'][0]['description']))
    print('\tCurrent Temperature: %d%s\n' % (data['main']['temp'], unit))
    print('\tLow: %d%s / High %d%s\n' %(data['main']['temp_min'], unit, data['main']['temp_max'], unit))
    
                                                

