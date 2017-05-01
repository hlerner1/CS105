# Carrie Guan ------------- cguan@bu.edu
# Hannah Lerner ----------- hlerner@bu.edu
# Phillip Petrosian ------- philp@bu.edu
# May 1, 2017
# fix_weather.py

# Open the files
filename = 'weather-check.csv'
infile = open(filename, 'r')
outfile = open('fixed-'+filename, 'w')

# Change the numeric values to nominal values
for line in infile:
    fields = line.split(',')
    
    

    # Discretizes how people check weather
    if 'phone' in fields[1]:
        fields[1] = 'mobile'
    elif 'website' in fields[1] or 'internet' in fields[1] or 'Internet' in fields[1]:
        fields[1] = 'internet'
    elif 'TV' in fields[1] or 'Channel' in fields[1]:
        fields[1] = 'tv'
    elif 'Radio' in fields[1]:
        fields[1] = 'radio'
    elif 'paper' in fields[1]:
        fields[1] = 'paper'
    
    # Discretizes likelihood of checking smartwatch to numbers 1-4 (1 being very unlikely, 4 being very likely)
    if 'Very likely' in fields[6]:
        fields[6] = 4
    elif 'Somewhat likely' in fields[6]:
        fields[6] = 3
    elif 'Somewhat unlikely' in fields[6]:
        fields[6] = 2
    elif 'Very unlikely' in fields[6]:
        fields[6] = 1

    if fields[6] == 4 or fields[6] == 3:
        fields[7] = 'positive'
    elif fields[6] == 2 or fields[6] == 1:
        fields[7] = 'negative'
    
# Print results to a file
    for i in range(len(fields)):
        print(str(fields[i])+',',end='', file = outfile)
    #print(fields[-1],end='',file=outfile)
    print(file=outfile) 
    
# Close the files
infile.close()
outfile.close()
