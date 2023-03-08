"""
The Listener Pattern

This is one that I have run into myself in the wild but not
found any documentation on (haven't looked too hard either).

The basic concept is that there is a thing which has events
that it emits. These emitted events then trigger zero or more
listeners that have been registered with the event.
"""


from enum import Enum
from typing import Callable


class ChatBotEvents(Enum):
    Login = 0
    Logout = 1
    Message = 2


class ChatBot:
    def __init__(self):

        # We'll initialize our events with an empty list of functions
        # for each of the event types.
        self.events: dict[str, list[Callable[[], None]]] = {
            e: [] for e in [i.name for i in ChatBotEvents]
        }

    def register(self, event: ChatBotEvents, f: Callable) -> None:
        """Registers a given function with a callback."""

        if not self.isRegistered(event, f):
            self.events[event.name].append(f)
        else:
            print("Function already registered!")

    def isRegistered(self, event: ChatBotEvents, f: Callable) -> bool:
        """Returns whether function f is already registered with an event."""
        return f in self.events[event.name]

    def emit(self, event: ChatBotEvents):
        """Emits an event of a given type."""
        for func in self.events[event.name]:
            func()


if __name__ == "__main__":
    cb = ChatBot()

    cb.register(ChatBotEvents.Login, lambda: print("Hello, Login!"))

    cb.emit(ChatBotEvents.Login)
