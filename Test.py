# Задание 1

def isEven(value):
    return value % 2 == 0


''' Алгоритм (функция) isEven проста для понимания. Если остаток от деления на 2 целого числа (value)
    равно 0 значит число четное , иначе нечетное.'''


def isEven_2(value):
    p = '02468'
    return str(value)[-1] in p


''' Алгоритм (функция) isEven_2 создает локальную переменную (р), меняет тип (value) на строку и проверяет 
    последний элемент по индексу у (value) на вхождение в переменную (р), если она там есть значит число 
    четное, иначе нечетное '''


# ------------------------------------------------------------------------------------------------------------------
# Задание 2

class Queue:
    def __init__(self):
        self.res = []  # Создается список для очереди

    def isEmpty(self):
        return self.res == []  # Возврашает True если список очереди пуст

    def in_Q(self, obj):
        self.res.insert(0, obj)  # Вставляет обьект в начало списка очереди

    def out_Q(self):
        return self.res.pop()  # Удаляет и возврашает последний обьект списка очереди

    def size_Q(self):
        return len(self.res)  # Возврашает количество обьектов в очереди

    def print_Q(self):
        for i in self.res:
            print(i, end=' ')  # Показывает все обьекты в списке очереди
        print()


a = Queue()  # Создается обьект класса
a.in_Q(4)  # В начало очериди встает обьект [4]
a.in_Q(66)  # [66, 4]
a.in_Q('stop')  # ['stop', 66, 4]
a = a.out_Q()  # Первый в очереди удаляется из очереди 4
a.print_Q()  # stop 66

'''Класс Queue создает список , и при добавлении нового обьекта ставит его в начало списка , при удалении
   выходит первый вошедший элемент'''


class StackObj:
    def __init__(self, data):
        self.data = data  # Обьект для записи
        self.next = None  # Ссылка на следуюший обьект


class Stack:
    def __init__(self):
        self.top = None  # Первый обьект в связанном списке

    def push(self, obj):
        # Добавление нового обьекта, и создание ссылки для нынешнего обьекта на новый обьект
        if self.top is None:
            self.top = obj
            return
        n = self.top
        while True:
            if n.next is None:
                n.next = obj
                break
            n = n.next

    def pop(self):
        # Удаление первого обьекта, ссылка первого обьекта становится первым обьектом
        if self.top.next is None:
            n = self.top.data
            self.top.data = None
            return n.data
        n = self.top
        self.top = self.top.next
        return n.data  # Возврашает удаленный обьект

    def get_data(self):
        if self.top.data is None:
            self.top = None
            return []
        n = self.top
        res = []
        while True:
            res.append(n.data)
            if n.next is None:
                break
            n = n.next
        return res  # Возврашает список всех обьектов в связанном списке


st = Stack()  # Создание обьекта класса
st.push(StackObj("obj1"))  # Запись первого обьекта в связаннный список ["obj1"]
st.push(StackObj("obj2"))  # ["obj1", "obj2"]
st.push(StackObj("obj3"))  # ["obj1", "obj2", "obj3"]
w = st.pop()  # obj1
res = st.get_data()  # ['obj2', 'obj3']

'''Класс Stack записывает обьек класса StackObj который хранит данные и ссылку на следубший обьект класса StackObj.
   При удалении данных ссылка на следуюший обьект становится в начало в обьекте класса Stack'''


# --------------------------------------------------------------------------------------------------------------------
# Задание 3

def quicksort(array):
    if len(array) < 2:  # Если длинна массива меньше двух, то рекурсия завершается
        return array
    else:
        pivot = array[0]  # Опорный элемент
        less = [i for i in array[1:] if i <= pivot]  # Список элементов меньше или равны опорному элементу
        greater = [i for i in array[1:] if i > pivot]  # Список элементов больше опорного элемента
        return quicksort(less) + [pivot] + quicksort(greater)  # Вызывается рекурсия со списком less и greater


'''Количество произведенных операций в алгоритме(функции) quicksort зависит от выбора опорного элемента. Если список 
   отсартирован то функция при выборе опорного элемента будет перебирать весь оставшийся массив данных на каждом
   уровне стэка вызова рекурсии О(n**2)
   Если список не отсартирован то в среднем количество операций сокрашается О(n log n) . Количество рекурсий
   сократится'''
