class MyMixin(object):
    mixin_prop = ''
    
#метод приводит строку к верхнему регистру
    def get_prop(self):
        return self.mixin_prop.upper()

#метод приводит строку к верхнему регистру
    def get_upper(self, s):
        if isinstance(s, str):#прроверяем является ли переданный аргумент s строкой
            return s.upper()# если да вызываем строковый метод upper()
        else:
            return s.title.upper()#если это обьект берём у него атрибут title, которыйстрока, и приводим его к верхнему регистру
