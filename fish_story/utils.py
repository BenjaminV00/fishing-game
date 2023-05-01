from pygame.image import load

from pathlib import Path
from entities import Entity


class Singleton(object):
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass


class State(Singleton):
    def __init__(self, state="world", substate=""):
        self.state = state
        self.substate = substate


def load_sprite(name, alpha=True):
    filename = Path(__file__).parent / Path("assets/sprites/" + name)
    sprite = load(filename.resolve())

    if alpha:
        return sprite.convert_alpha()

    return sprite.convert()
