from aspose.pdf.utils import publicdata
import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class DictionaryEditor:
    '''A class for accessing an object's dictionary.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page):
        ''':param page: A page with a dictionary for work.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        ''':param document: A document with a dictionary for work.'''
        ...
    
    def contains_key(self, key: str) -> bool:
        '''Determines whether the :class:`DictionaryEditor` contains an element with the specified key.
        
        :param key: The key to locate in the  :class:`DictionaryEditor`.
        :returns: true if the :class:`DictionaryEditor` contains an editable element with the key; otherwise, false.'''
        ...
    
    def remove(self, key: str) -> bool:
        '''Removes the element with the specified key from the :class:`DictionaryEditor`.
        
        :param key: The key of the element to remove.
        :returns: True if the element is successfully removed; otherwise, false.
                  This method also returns false if key was not found in the original dictionary or key the key is not editable'''
        ...
    
    def try_get_value(self, key: str, value) -> bool:
        '''For access to simple data type like string, name, bool, number.
        Returns null for other types.
        
        :param key: Key value
        :param value: returns :class:`aspose.pdf.utils.publicdata.ICosPdfPrimitive` for key or null.
        :returns: Returns true if :class:`aspose.pdf.utils.publicdata.ICosPdfPrimitive` is like string, name, bool, number.
                  Returns false for all other types.'''
        ...
    
    def add(self, key: str, value: aspose.pdf.utils.publicdata.ICosPdfPrimitive) -> None:
        '''Set :class:`aspose.pdf.utils.publicdata.ICosPdfPrimitive` to dictionary.
        
        :param key: Key.
        :param value: Value.'''
        ...
    
    def clear(self) -> None:
        '''Removes all items from the :class:`DictionaryEditor`.'''
        ...
    
    @property
    def all_keys(self) -> None:
        '''Full collection of keys.
        Contains editable and not editable keys.'''
        ...
    
    @property
    def keys(self) -> None:
        '''Collection of editable keys.'''
        ...
    
    @property
    def values(self) -> None:
        '''Gets an System.Collections.ICollection containing the values in the :class:`DictionaryEditor`.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the :class:`DictionaryEditor`.'''
        ...
    
    @property
    def is_read_only(self) -> bool:
        '''Gets a value indicating whether the :class:`DictionaryEditor` is read-only.
        
        :returns: true if the :class:`DictionaryEditor` is read-only; otherwise, false.'''
        ...
    
    ...

