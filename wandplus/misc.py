#!/usr/bin/env python

from wand.api import libmagick
from wand.compat import string_type
import ctypes
import collections

libmagick.SetLogEventMask.restype = ctypes.c_int
libmagick.SetLogEventMask.argtypes = [
    ctypes.c_char_p
]
libmagick.SetLogFormat.restype = ctypes.c_char_p
libmagick.SetLogFormat.argtypes = [
    ctypes.c_char_p
]
libmagick.SetLogMethod.argtypes = [
    ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)
]
libmagick.SetLogName.restype = ctypes.c_char_p
libmagick.SetLogName.argtypes = [
    ctypes.c_char_p
]
libmagick.GetLogName.restype = ctypes.c_char_p
libmagick.GetLogName.argtypes = []


LOG_EVENT_TYPES = dict(undefined=0, no=0, trace=0x1, annotate=0x2,
                       blob=0x4, cache=0x8, coder=0x10, configure=0x20,
                       deprecate=0x40, draw=0x80, exception=0x100,
                       image=0x200, locale=0x400, module=0x800,
                       policy=0x1000, resource=0x2000, transform=0x4000,
                       user=0x9000, wand=0x10000, X11=0x20000,
                       accelerate=0x40000, all=0x7fffffff)

# callback function called from 'logcallback'
_logfunction = None


def setlogeventmask(eventtypes):
    """accepts a list that determines which events to log.  All
    other events are ignored.  By default, no debug is enabled.  This method
    returns the previous log event mask.

    :param eventtypes: string or list of strings(LOG_EVENT_TYPES).
                       e.g. 'all', 'wand', ['image', 'resource']
    """
    if isinstance(eventtypes, string_type):
        if eventtypes not in LOG_EVENT_TYPES:
            raise ValueError('expected string from LOG_EVENT_TYPES, not ' +
                             repr(eventtypes))
        types = eventtypes
    elif isinstance(eventtypes, collections.Sequence):
        for eventtype in eventtypes:
            if eventtype not in LOG_EVENT_TYPES:
                raise ValueError('expected string from LOG_EVENT_TYPES, not ' +
                                 repr(eventtype))
        types = '|'.join(eventtypes)
    else:
        raise TypeError('eventtypes must be string or string-list, not',
                        type(eventtypes))
    text_buffer = ctypes.create_string_buffer(types.encode())
    return libmagick.SetLogEventMask(text_buffer)


def setlogformat(format, encoding=None):
    r"""Set the format of the log

    The format is defined by embedding special format characters:
    %c   client name
    %d   domain
    %e   event
    %f   function
    %g   generation
    %l   line
    %m   module
    %n   log name
    %p   process id
    %r   real CPU time
    %t   wall clock time
    %u   user CPU time
    %v   version
    %%   percent sign
    \n   newline
    \r   carriage return

    default is '%t %r %u %v %d %c[%p]: %m/%f/%l/%d\n  %e'
    """
    if not isinstance(format, string_type):
        raise TypeError('eventtypes must be string, not', repr(format))
    if encoding:
        bformat = format.encode(encoding=encoding)
    else:
        bformat = format.encode()
    buffer = ctypes.create_string_buffer(bformat)
    libmagick.SetLogFormat(buffer)


def setlogmethod(callback):
    """sets the method that will be called when an event is logged.

    :param callback: f(eventtype: int, message: string)
    """
    global _logfunction
    _logfunction = callback
    libmagick.SetLogMethod(_logcallback)


@ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)
def _logcallback(eventtype, message):
    if _logfunction:
        _logfunction(eventtype, message)


def setlogname(name, encoding=None):
    if not isinstance(name, string_type):
        raise TypeError('eventtypes must be string, not', repr(name))
    if encoding:
        bname = name.encode(encoding=encoding)
    else:
        bname = name.encode()
    buffer = ctypes.create_string_buffer(bname)
    prev = libmagick.SetLogName(buffer)
    if encoding:
        return prev.decode(encoding=encoding)
    else:
        return prev.decode()


def getlogname(encoding=None):
    name = libmagick.GetLogName()
    if encoding:
        return name.decode(encoding=encoding)
    else:
        return name.decode()


if __name__ == '__main__':
    pass
