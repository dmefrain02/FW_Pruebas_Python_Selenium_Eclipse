import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class FontEmbeddingOptions:
    '''PDF/A standard requires, that all fonts must be embedded into document.
    This class includes flags for cases when it's not possible to embed some font cause this font is absent
    on destination PC.'''
    
    def __init__(self):
        ...
    
    @property
    def use_default_substitution(self) -> bool:
        '''Declares to substitute non-embedded font using default font substitution strategy. By default false;'''
        ...
    
    @use_default_substitution.setter
    def use_default_substitution(self, value: bool):
        ...
    
    ...

class ToUnicodeProcessingRules:
    '''This class describes rules which can be used to solve Adobe Preflight error
    "Text cannot be mapped to Unicode".'''
    
    @overload
    def __init__(self):
        '''Constructor'''
        ...
    
    @overload
    def __init__(self, remove_spaces: bool):
        '''Constructor
        
        :param remove_spaces: sets :attr:`ToUnicodeProcessingRules.remove_spaces_from_c_map_names` flag'''
        ...
    
    @overload
    def __init__(self, remove_spaces: bool, map_non_linked_unicodes_on_space: bool):
        '''Constructor
        
        :param remove_spaces: sets :attr:`ToUnicodeProcessingRules.remove_spaces_from_c_map_names` flag
        :param map_non_linked_unicodes_on_space: sets :attr:`ToUnicodeProcessingRules.map_non_linked_symbols_on_space` flag'''
        ...
    
    @property
    def remove_spaces_from_c_map_names(self) -> bool:
        '''Some fonts have ToUnicode character code maps with spaces in names. These spaces could call errors
        with unicode text mapping. This flag commands to remove spaces from names of ToUnicode character code maps.
        By default false.'''
        ...
    
    @remove_spaces_from_c_map_names.setter
    def remove_spaces_from_c_map_names(self, value: bool):
        ...
    
    @property
    def map_non_linked_symbols_on_space(self) -> bool:
        '''Some fonts doesn't provide information about unicodes for some text symbols.
        This lack of information calls an error "Text cannot be mapped to Unicode".
        Use this flag to map non-linked symbols on unicode "space"(code 32).'''
        ...
    
    @map_non_linked_symbols_on_space.setter
    def map_non_linked_symbols_on_space(self, value: bool):
        ...
    
    ...

