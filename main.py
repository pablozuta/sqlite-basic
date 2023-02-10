import sqlite3
from employee import Employee # aca importamos la clase 'Employee'


conn = sqlite3.connect('employee.db') # esto crea el archivo de sqlite

c = conn.cursor()

# aca creamos una tabla usando SQL 
# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer)""")  

# this are regular python objects
emp_1 = Employee('Erwin', 'Panofsky', 1953)
emp_2 = Employee('Sydney', 'Freedberg', 1948)
print(emp_1.first) # we use dot notation to access the values
print(emp_1.last)
print(emp_1.pay)
print(emp_1)
print(emp_2.first)
print(emp_2.last)
print(emp_2.pay)
print(emp_2)

# bad practice to add python objects to database
# proclive to attacks/injections
# c.execute("INSERT INTO employees VALUES ('{}', {}', {})".format(emp_1.first, emp_1.last, emp_1.pay)) 

# first good way to do it (using ? as placeholder and passing a tuple)
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()

# second proper way (using dictionary)
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
#     {'first': emp_2.first,'last': emp_2.last,'pay': emp_2.pay})
# conn.commit()     


# esto agrega data a nuestra table
# c.execute("INSERT INTO employees VALUES ('Bomarzo', 'Gardens', 1899)") 
# c.execute("INSERT INTO employees VALUES ('Paul', 'Cezanne', 1981)") 

# c.execute("SELECT * FROM employees WHERE last = 'Gardens'")
# c.execute("SELECT * FROM employees WHERE first = 'Paul'")
c.execute("SELECT * FROM employees")

# print(c.fetchone()) # muestra solo un resultado
print(c.fetchall()) # muestra todos los resultados


conn.commit()

conn.close()
