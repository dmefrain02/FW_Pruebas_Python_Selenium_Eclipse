import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class IInterruptMonitor:
    '''Represents information about interruption.'''
    
    def interrupt(self) -> None:
        '''Sends a request to interrupt operations.'''
        ...
    
    ...

class InterruptMonitor:
    '''Represents information about interruption.'''
    
    def __init__(self):
        ...
    
    def interrupt(self) -> None:
        '''Sends a request to interrupt operations.'''
        ...
    
    thread_local_instance: aspose.pdf.multithreading.IInterruptMonitor
    
    ...

