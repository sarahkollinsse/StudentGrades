#Sarah Kollins, JARED HOFER, Michael Supeck, Zack Leytze
#CSE 211
#Purpose: Create a new file and write to the file a student's name, final grade, and letter grade
#Date:2/11/2018
#Homework01

#Opens studentGrades file and creates a new writeable file
file = open("studentGrades.txt",'r')
newFile = open("finalGrades.txt",'w')

#loops through the file and writes it to the new file
for line in file:
    singleLine = line.split()
    name = singleLine[0]
    avgQ = ((int(singleLine[1]) + int(singleLine[2]) + int(singleLine[3]))/3)*.2
    avgHw = ((int(singleLine[4]) + int(singleLine[5]) + int(singleLine[6])+int(singleLine[7])+int(singleLine[8]))/5)*.3
    avgEx=((int(singleLine[9])+int(singleLine[10]))/2)*.5
    total = avgQ + avgHw + avgEx

    if total >=90:
        grade='A'
    elif total >=80 and total<90:
        grade='B'
    elif total >=70 and total<80:
        grade='C'
    elif total >= 60 and total < 70:
            grade = 'D'
    else:
        grade='F'
   # print('{:>25}'.format(name),'{:>5}'.format('%.1f'%total),grade)
    newFile.write('{:>20}'.format(name))
    newFile.write('{:>5}'.format('%.1f'%total)+" ")
    newFile.write(grade+"\n")


file.close()
newFile.close()