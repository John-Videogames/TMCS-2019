"""colors is a simple module for creating a color dictionary"""

color = {}  # declare a color dictionary
color['yellow'] = [1.0, 1.0, 0.0]  # fill each entry of the color dictionary with a list of three floats
color['blue'] = [0.0, 0.0, 1.0]
color['red'] = [1.0, 0.0, 0.0]
color['green'] = [0.0, 1.0, 0.0]
color['sienna'] = [0.627, 0.322, 0.176]
color['hotpink'] = [1.0, 0.412, 0.706]

def printAvailableColors():
    """This function prints all available colors within our dictionary"""
    print('\tyellow')
    print('\tblue')
    print('\tred')
    print('\tgreen')
    print('\tsienna')
    print('\thotpink')

if __name__== "__main__":
    print('executing colors.py as the main routine')
    print('we have definitions of:')
    printAvailableColors()