# Python3 program to calculate the CGPA# python3 program to calculate the cgpa
# and cgpa percentage of a student
def cgpacalc(marks, n):

  # variable to store the grades in
  # every subject
  grade = [0] * n

  # variables to store cgpa and the
  # sum of all the grades
  sum = 0

  # computing the grades
  for i in range(n):
    grade[i] = (marks[i] / 10)

  # computing the sum of grades
  for i in range(n):
    sum += grade[i]

  # computing the cgpa
  cgpa = sum / n

  return cgpa


# driver code
n = 5
marks = [90, 80, 70, 80, 90]

cgpa = cgpacalc(marks, n)

print("cgpa = ", '%.1f' % cgpa)
print("cgpa percentage = ", '%.2f' % (cgpa * 9.5))

# this code is contributed by divyeshrabadiya07￼not