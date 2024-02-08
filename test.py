# lst = []
#
# a = input()
# while a != '1':
#     lst.append(a)
#     a = input()
#
# for i in lst:
#     a, b = i.split('=')
#     print(f"{a} = self.variables.{a},")


# self.da_np = mywindow.is_float(self.main_window.ui.doubleSpinBox_31)

def f1(s):
    lst1 = []
    lst2 = []
    lst4 = []

    lst = s.split(', ')

    for i in lst:
        lst1.append(f"{i}=self.variables.{i},")
        lst2.append(f"self.{i} = mywindow.is_float(self.main_window.ui.doubleSpinBox)")
        lst4.append(f"self.{i}=None")

    print()
    for i in lst4:
        print(i)
    print()
    for i in lst2:
        print(i)
    print()
    for i in lst1:
        print(i)


s = 'n0, i, s1, n1, s2, n2'
f1(s)
#
lst = '''self.n0 = mywindow.is_float(self.main_window.ui.doubleSpinBox_31)
        self.i = mywindow.is_float(self.main_window.ui.doubleSpinBox_32)
        self.s1 = mywindow.is_float(self.main_window.ui.doubleSpinBox_35)
        self.n1 = mywindow.is_float(self.main_window.ui.doubleSpinBox_37)
        self.s2 = mywindow.is_float(self.main_window.ui.doubleSpinBox_36)
        self.n2 = mywindow.is_float(self.main_window.ui.doubleSpinBox_38)'''\
    .replace('        ', '').replace('(', ')').split('\n')

for i in lst:
    a = i.split(')')
    print(f"self.ui.{a[1].split('.')[3]}.setValue()  # {a[0].split('=')[0].split('.')[1]}")
