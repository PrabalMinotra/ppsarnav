
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

#"""Firstly simple"emp1" would search for '__str__' THEN '__repr__'  """

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
emp2 =Employee("Rohan", 55, "Cleaner")
print(str(emp1))
print(repr(emp1))



"""Addition          a + b           add(a, b)

Concatenation
seq1 + seq2
concat(seq1, seq2)

Containment Test
obj in seq
contains(seq, obj)

Division
a / b
truediv(a, b)

Division
a // b
floordiv(a, b)

Bitwise And
a & b
and_(a, b)

Bitwise Exclusive Or
a ^ b
xor(a, b)

Bitwise Inversion
~ a
invert(a)

Bitwise Or
a | b
or_(a, b)

Exponentiation
a ** b
pow(a, b)

Identity
a is b
is_(a, b)

Identity
a is not b
is_not(a, b)

Indexed Assignment
obj[k] = v
setitem(obj, k, v)

Indexed Deletion
del obj[k]
delitem(obj, k)

Indexing
obj[k]
getitem(obj, k)

Left Shift
a << b
lshift(a, b)

Modulo
a % b
mod(a, b)

Multiplication
a * b
mul(a, b)

Matrix Multiplication
a @ b
matmul(a, b)

Negation (Arithmetic)
- a
neg(a)

Negation (Logical)
not a
not_(a)

Positive
+ a
pos(a)

Right Shift
a >> b
rshift(a, b)

Slice Assignment
seq[i:j] = values
setitem(seq, slice(i, j), values)

Slice Deletion
del seq[i:j]
delitem(seq, slice(i, j))

Slicing
seq[i:j]
getitem(seq, slice(i, j))

String Formatting
s % obj
mod(s, obj)

Subtraction
a - b
sub(a, b)

Truth Test
obj
truth(obj)

Ordering
a < b
lt(a, b)

Ordering
a <= b
le(a, b)

Equality
a == b
eq(a, b)

Difference
a != b
ne(a, b)

Ordering
a >= b
ge(a, b)

Ordering
a > b
gt(a, b)

"""