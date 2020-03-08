events = {}
event_act = {}

def Event(eventName, defaultFunc=None,*func_args,**func_kwargs):
    events[eventName] = {}

    def act(*args, **kwargs):
        return _call(events[eventName],*args,**kwargs)

    event_act[eventName] = act

    if callable(defaultFunc):
        Add(eventName,"defFunc",defaultFunc,*func_args,**func_kwargs)

    return act

        
def GetEvent(eventName):
    return event_act[eventName]

def Add(eventName, hookName, func, *args, **kwargs):
    if get_index(args, 0) is None and len(kwargs) == 0 and len(args) == 1:
        events[eventName][hookName] = (func, None)
    elif len(args) != 0 or len(kwargs) != 0:
        events[eventName][hookName] = (func, args, kwargs)
    elif len(args) == 0 and len(kwargs) == 0:
        events[eventName][hookName] = (func, True)

def GetTable():
    return events

def Remove(eventName, hookName):
    del events[eventName][hookName]

def Run(eventName, *args, **kwargs):
    return _call(events[eventName],*args,**kwargs)

def _call(dictionary,*args,**kwargs):
    returnable = {}
    for key in dictionary:
        hook = dictionary[key]
        function = hook[0]
        params = hook[1:]

        if params[0] is None:
            returnable[key] = function()
        elif params[0] is True:
            returnable[key] = function(*args,**kwargs)
        else:
            returnable[key] = function(*params[0],**params[1])

    return returnable

def get_index(arr,index):
    try: return arr[index]
    except: return None

