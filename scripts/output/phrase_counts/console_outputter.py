def output_dict(phrase_dict):
    # Header
    print(f'{'Video':<60} {'SOALAS Count':<20} {'LAS Count':<20} {'Applewood Count':<20}')

    for k, v in phrase_dict.items():
        print(f'{v["Title"]:<60} {v["SOALAS Count"]:<20} {v["LAS Count"]:<20} {v["Applewood Count"]:<20}')
