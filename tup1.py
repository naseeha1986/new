emp_1=('john',30,'sales','$50000')
emp_2=('Alice',28,'Marketing','$48000')
print("employee details\n", emp_1+emp_2)
print("Department of john is :", emp_1[2])
average= (int(emp_1[1]) +int(emp_2[1]))/2
print ("Average age of employees:", average)
emp_list=list(emp_1+emp_2)
print("Employee data as list:", emp_list)
