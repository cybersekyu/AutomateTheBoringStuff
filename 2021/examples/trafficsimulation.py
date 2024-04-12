market_2nd = {'ns':'green', 'ew':'red'}
mission_16th = {'ns':'red', 'ew':'green'}

def switchlights(stopLight):
    for key in stopLight.keys():
        if stopLight[key] == 'green':
            stopLight[key] = 'yellow'
        elif stopLight[key] == 'yellow':
            stopLight[key] = 'red'
        elif stopLight[key] == 'red':
            stopLight[key] = 'green'
    assert 'red' in stopLight.values(), 'Neither light is red! ' + str(stopLight)

switchlights(market_2nd) 