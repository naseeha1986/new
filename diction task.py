emp_sal={
    "jubaidha":40000,
    "naseeha":30000,
    "rifa":20000,
    "hasan":50000,
    "nafees":60000,
    }
print(emp_sal)
emp_sal["kaleel"]=70000
print(emp_sal)
emp_sal.update({
    "hasan":70000})
print(emp_sal)
del emp_sal["naseeha"]
print(emp_sal)
