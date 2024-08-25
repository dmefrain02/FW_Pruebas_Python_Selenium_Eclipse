import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class XfaParserOptions:
    '''class to handle related data incapsulation'''
    
    def __init__(self, page_size: aspose.pydrawing.SizeF):
        '''Initializes a new instance of the :class:`XfaParserOptions` class.
        
        :param page_size: Size of the page.'''
        ...
    
    @property
    def page_size(self) -> aspose.pydrawing.SizeF:
        '''Gets or sets the size of the page.'''
        ...
    
    @page_size.setter
    def page_size(self, value: aspose.pydrawing.SizeF):
        ...
    
    @property
    def signed(self) -> bool:
        '''If this property is true then document will be converted with using of xfa form stream (if it exists).
        If it is false then xfa form stream will be ignored.
        This property was inrtoduced because it's not clear how to calculate check sum that used for checking sygnature.'''
        ...
    
    @signed.setter
    def signed(self, value: bool):
        ...
    
    @property
    def emulate_requierd_groups(self) -> bool:
        '''If this property is true then additional red rectangles will be drawn for required Xfa "excluded groups"
        This property was introduced because absences of analogues of excluded groups during conversion Xfa representation of forms
        to standard.
        It is false by default.'''
        ...
    
    @emulate_requierd_groups.setter
    def emulate_requierd_groups(self, value: bool):
        ...
    
    @property
    def base_path(self) -> None:
        '''Gets or sets the base path.'''
        ...
    
    @base_path.setter
    def base_path(self, value: None):
        ...
    
    ...

