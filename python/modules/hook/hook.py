#ver: 1. Пожалуйста, не трогайте переменные с __. Мне лень переделывать в ооп.

__events = {}
__event_act = {}

WITHOUT_ARGS, DYNAMIC_ARGS, STRICT_ARGS = lambda: None, lambda: None, lambda: None
FIX_ARGS = lambda *args, **kwargs: (args, kwargs)

def Event(eventName, defaultFunc=None, mode=WITHOUT_ARGS):
    __events[eventName] = {}
    act = lambda *args, **kwargs: _call(__events[eventName], *args, **kwargs)
    __event_act[eventName] = act

    if callable(defaultFunc):
        Add(eventName,"defFunc",defaultFunc,mode)

    return act

def GetEvent(eventName):
    return __event_act[eventName]

def Add(eventName, hookName, func, mode=WITHOUT_ARGS):

    if mode in (WITHOUT_ARGS,DYNAMIC_ARGS,STRICT_ARGS):
        __events[eventName][hookName] = (func, mode)
    else:
        __events[eventName][hookName] = (func, mode[0], mode[1])

def GetTable():
    return __events

def Remove(eventName, hookName):
    del __events[eventName][hookName]

def Run(eventName, *args, **kwargs):
    return _call(__events[eventName], *args, **kwargs)

def _call(dictionary,*args,**kwargs):
    returnable = {}
    for key in dictionary:
        hook = dictionary[key]
        function = hook[0]
        params = hook[1:]

        if params[0] is WITHOUT_ARGS:
            returnable[key] = function()
        elif params[0] is DYNAMIC_ARGS:
            returnable[key] = function(*args,**kwargs)
        elif params[0] is STRICT_ARGS:
            try:
                returnable[key] = function(*args, **kwargs)
            except TypeError:
                continue
        else:
            returnable[key] = function(*params[0],**params[1])

    return returnable
