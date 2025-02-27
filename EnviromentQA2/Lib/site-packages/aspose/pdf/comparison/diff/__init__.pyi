import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class DiffOperation:
    '''Represents a class of diff operation.'''
    
    def equals(self, op: aspose.pdf.comparison.diff.DiffOperation) -> bool:
        ...
    
    @property
    def operation(self) -> aspose.pdf.comparison.diff.Operation:
        '''Gets and sets operation type.'''
        ...
    
    @property
    def text(self) -> str:
        '''Get and set operation text.'''
        ...
    
    ...

class Operation:
    '''Represents a difference operation type.'''
    
    EQUAL: Operation
    DELETE: Operation
    INSERT: Operation

