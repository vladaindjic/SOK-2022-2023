"""
===================================
Strategy Pattern
"""

# TODO: Make this class abstract
class Sort:
    def sort(students_list):
        pass

class BubbleSort(Sort):
    def sort(students_list):
        print("BubbleSort")

# TODO: Implement QuickSort class

class StudenstaSluzba():
    def __init__(self):
        self.sorter = BubbleSort()

    # TODO: use @property instead
    def set_sorter(new_sorter):
        self.sorter = new_sorter

    def showStudents():
        self.sorter.sort(self.students)
        

def client():
    sorter = QuickSort()
    ss = StudentskaSluzba()
    ss.set_sorter(sorter)
    ss.showStudents()
    # TODO: change sorting strategy and show students again


# TODO: call the client function

"""
===================================
Observer Pattern
"""
# TODO: abstract class
class Observable():
    def __init__(self):
        self.observers = []

    def add_observer(new_obs):
        self.observers.append(new_obs)
        # TODO: store the reference to observable in observer class

    def delete_observer(old_obs):
        # TODO: remove old_obs from the list
        pass

    def notify():
        for obs in self.observers:
            obs.update()

# TODO: make this abstract class
class Observer:
    def initialize(observable):
        self.observable = observable

    # TODO: make this abstract
    def update():
        pass

class PritisakPrikaz(Observer):
    def __init__():
        # TODO: observer needs reference to observable
        self.merac_pritiska = ...

    def update():
        print(self.merac_pritiska.uzmi_pritisak())

class SigurnosniVentil(Observer):
    def __init__():
        self.opened = False
        # TODO: observer needs reference to observable
        self.merac_pritiska = ...

    def update():
        # TODO: check whether it is opened. If so, do nothing.
        # Otherwise, execute the if-block.
        if self.merac_pritiska.uzmi_vrednost() > limit:
            self.opened = True
            print("Ventil otvoren")

class MeracPritiska(Observable):
    def __init__():
        self.pritisak = 0

    def uzmi_pritisak():
        return self.pritisak

    def podesi_pritisak(novi_pritisak):
        self.pritisak = novi_pritisak
        # notify observers about the change
        self.notify()

def client():
    # observable
    merac = MeracPritiska()
    # observer 1
    ventil = SigurnosniVentil()
    # observer 2
    prikaz = PritisakPrikaz()
    merac.add_observer(ventil)
    merac.add_observer(prikaz)
    # TODO: finish the simulation
    merac.podesi_pritisak(1)
    merac.podesi_pritisak(2)
    merac.podesi_pritisak(100)
    

# TODO: start the client



"""
===================================
Strategy again.
"""

class Student():
    # TODO: implement constructor and other methods
    pass

class StudentSelectionSort():
    def sort(students_list):
        # TODO: implement selection sort algorithm
        # When comparing two students, use "compare" method
        pass

    def compare(student1, student2):
        # TODO: make this an abstract method
        # Use it to compare two students
        pass

class StudentSortIndeks(StudentSelectionSort):
    def compare(student1, student2):
        if student1.indeks < student2.indeks:
            return -1
        elif student1.indeks > student2.indeks:
            return 1
        else:
            return 0

# TODO: implement StudentSortIme and StudentSortPrezime

def client():
    # TODO: generate list of studnets
    students_list = []
    # TODO: sort students by indeks
    # TODO: sort students by ime
    # TODO: sort students by prezime

# TODO: call client method


"""
======================================
Selection sort by using strategy pattern
"""

# TODO: make this abstract
# strategy for comparing two students while sorting them
class Comparator():
    # TODO: abstract method
    def compare(student1, student2):
        pass

class ComparatorIndeks(Comparator):
    def compare(student1, student2):
        if student1.indeks < student2.indeks:
            return -1
        elif student1.indeks > student2.indeks:
            return 1
        else:
            return 0

# TODO: implement ComparatorIme and ComparatorPrezime

class StudentSelectionSort():
    def __init__(self, comparator):
        self.comparator = comparator

    def sort(students_list):
        # TODO: implement selection sort algorithm
        # When comparing two students, use "compare" method of "comparator"
        pass

    # TODO: use @property.setter instead
    def set_comparator(comparator):
        self.comparator = comparator


def client():
    # TODO: fill the list
    students_list = []
    comparator = ComparatorIndeks()
    sss = StudentSelectionSort(None)
    # compare students by indeks
    sss.set_comparator(comparator)
    sss.sort(students_list)
    # TODO: sort students by ime
    # TODO: sort students by prezime
