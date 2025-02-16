'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''

with open('student_grades.csv', 'r') as f:
    # collect all lines from the file
    lines = f.readlines()

    # validate file has data
    if len(lines) > 0:
        grades = []

        # iterate through each line and collect the grade
        # skipping the first 'header' line
        for line in lines[1:]:
            # split the line into a list (i.e. columns)
            row = line.split(',')

            # convert the grade to a float and add it to the list
            grades.append(float(row[3].replace('\n','')))

        avg = sum(grades) / len(grades)

        # open output file and write differences
        with open('student_grade_differences.csv', 'w') as out_f:
            # write header line
            out_f.write('name, grade, difference\n')
            
            # calculate differences for each student
            for line in lines[1:]:
                row = line.split(',')
                name = row[1]
                grade = float(row[3].replace('\n',''))
                diff = grade - avg
                out_f.write(f'{name}, {grade}, {diff}\n')
