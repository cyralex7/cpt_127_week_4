
'''

This assignment is supposed to  read in the CSV
file and calculate an average grade for the class.

Please find the error and fix it!

You will know the problem is solved when you get an output of:

The average grade for the class is: 84.75

'''


#%%

with open('student_grades.csv','w') as f:

    # collect all lines from the file
    lines = f.readlines()


    # validate file has data
    if len(lines) > 0:
        grades = []

        # iterate through each line and collect the grade
        # skipping the first 'header' line
        for line in lines[1:]:
            # split the line into a list (i.e. columns)
            row = l.split(',')

            # convert the grade to a float and add it to the list
            grades.append(row[3].replace('\n',''))

        avg = sum(grades) / len(grades)

        print(f'The average grade for the class is: {avg}')
        
# %%


