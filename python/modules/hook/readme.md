# Как пользоватся этим модулем?
Скажу сразу, идею взял с gmod lua, lib hook. Реализовал все команды, кроме ```hook.Call(...)```.
В модуль входят команды:
```python
hook.Event(eventName, defaultFunc=None,*func_args,**func_kwargs)
hook.GetEvent(eventName)
hook.GetTable()
hook.Remove(eventName, hookName)
hook.Run(eventName, *args, **kwargs)
```
Пример кода:
```python
import hook

old_print = print

hook.Event("log",old_print) # Создаю иветн лог с дефолтной функцией old_print, которая принимает любое значение
print = hook.GetEvent("log") # Возвращает ивент. Мы его будем использовать дальше.
hook.Add("log","logger",old_print,"хоба") # Добавляю функцию к ивенту.
print(hook.GetTable()) # Вызываю таблицу со всеми хуками и ивентами.
```
Думаю, кому-то пригодится 
