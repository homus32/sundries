# Как пользоватся этим модулем?
Скажу сразу, идею взял с gmod lua, lib hook. Реализовал все команды, кроме Call(...).
Пример кода(сохраните как example.py):
```python
import hook

def without(): # Функция без аргументов
    print("hello, im function which without args. Im return None")

def dynamic(*args,**kwargs): # сюды можно что угодно пихать
    print("hello, im dynamic function i.e мне похуй что ты в меня суешь. Возвращаю все, что ты в меня сунул")
    return args, kwargs

def strict(a,b): # Можно засунуть только а и б
    print("Hello, Im Strict Function! Im return a, b args! Here: ",a,b)
    return a,b

def simple(a,b,c): # та же самая функция как и статик, только буим по другому её юзать
    print("hello, im simple function")
    return a,b,c

hook.Event("TEST") # Создаем иветн. В гарике тама все ивенты созданы, а мы сами будем их creat

event = hook.GetEvent("TEST") #Тута мы присваиваем це ивент к переменной, чтобы её можно было удобно вызывать.

hook.Add("TEST","without",without) # Тута уже как у луа добавляем хук. Хук без аргументов. В конце можно либо WITHOUT_ARGS или оставить пустоту
hook.Add("TEST","dynamic",dynamic,hook.DYNAMIC_ARGS) #На конце DYNAMIC_ARGS, значит це фигня будет копировать аргументы с event(...)
hook.Add("TEST","strict",strict,hook.STRICT_ARGS) #Опа, тут уже STRICT_ARGS. Значит тут строгие аргументы. Будет ошибка - ничего не будет
hook.Add("TEST","simple",simple,hook.FIX_ARGS("one","two","three!")) #Тут мы фиксируем аргрументы. удобно. можно просто ((...),{...})

print(hook.GetTable()) # Получить таблицу хуков и ивентов. Изучите, и тогда вы поймете как робит це модуль без чтения кода.

print(event(123,123)) # Призыв ивента ебать

hook.Remove("TEST","without") # УДАЛЕНИЕ ХУЯ! Извините, хука

print(hook.Run("TEST",123,123)) # Есть Run. Очевидно же
print(hook.Run("TEST",228,1337,666)) # Чуть другие аргументы

hook.Event("TEST") # Хм, а что будет ещё раз определить ивент ТЕСТ?
print(hook.GetTable()) # Ответ на вопрос

oldprint = print # Это другой пример использование модуля. сохраняем принт

def log(*args, sep=' ', end="\n", file=None): # Функция, копирущие функцию принт. Представьте, что это какой то логгер, который пишет в файл
    oldprint("Типа Сохранил в main.log:", *args,sep=sep,end=end,file=file)

print = hook.Event("logging",oldprint,hook.DYNAMIC_ARGS) #В ивенте можно создать дефолтную функцию, чтобы зря не писать hook.Add
hook.Add("logging","log",log,hook.STRICT_ARGS) # Подключаем логгер

print(123,123,123,opa="error") # Вызвваем логгер. Опа, ашибка
```

Думаю, кому-то пригодится 
	
