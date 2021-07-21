class EventEmitter:
    def __init__(self):
        self.events = dict()

    def on(self, event, func):
        if event in self.events:
            event_list = self.events[event]
            event_list.append(func)
            self.events[event] = event_list
        else:
            self.events.setdefault(event, [func])

    def emit(self, event):
        if event in self.events:
            event_list = self.events[event]
            for func in event_list:
                func()


def print_one():
    print("one")


def print_two():
    print("two")


event_emitter = EventEmitter()

event_emitter.on("Come", print_one)
event_emitter.on("Come", print_two)
event_emitter.on("ComeToMe", lambda: print('two two'))

event_emitter.emit('Come')


