ini_dict = {'nikhil': 1, 'vashu': 5,
            'manjeet': 10, 'akshat': 15}
print("initial 1st dictionary", ini_dict)
ini_dict['akash'] = ini_dict['akshat']
del ini_dict['akshat']
print("final dictionary", str(ini_dict))
