import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class SanitizationException(RuntimeError):
    '''The exception that is thrown when an sanitization operation failed.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`SanitizationException` class.'''
        ...
    
    @overload
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`SanitizationException` class.
        
        :param message: The message.'''
        ...
    
    ...

