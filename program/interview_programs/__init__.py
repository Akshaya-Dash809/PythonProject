light = input('Enter your light: ').upper()

if light == 'RED':
    print('Vehicle will stop')
elif light == 'GREEN':
    print('Vehicle will run')
elif light == 'ORANGE':
    print('Vehicle will ready to run')
else:
    print('Enter a valid light')