import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class Element:
    '''Class representing base element of logical structure.'''
    
    def remove(self) -> None:
        '''Remove element.'''
        ...

    @property
    def children(self) -> None:
        '''Gets child elements collection.'''
        ...
    
    @property
    def lang(self) -> str:
        '''(Optional; PDF 1.4) A language specifying the natural language for all text
        in the structure element except where overridden by language specifications for nested structure
        elements or marked content.'''
        ...
    
    @lang.setter
    def lang(self, value: str):
        ...
    
    @property
    def actual_text(self) -> str:
        '''(Optional; PDF 1.4) Text that is an exact replacement for the structure element and its children.
        This replacement text (which should apply to as small a piece of content as possible)
        is useful when extracting the document’s contents in support of accessibility to users
        with disabilities or for other purposes.'''
        ...
    
    @actual_text.setter
    def actual_text(self, value: str):
        ...
    
    @property
    def alt(self) -> str:
        '''(Optional) An alternate description of the structure element and its children in
        human-readableform, which is useful when extracting the document’s contents in support
        of accessibility to users with disabilities or for other purposes.'''
        ...
    
    @alt.setter
    def alt(self, value: str):
        ...
    
    @property
    def e(self) -> str:
        '''(Optional; PDF 1.5) The expanded form of an abbreviation.'''
        ...
    
    @e.setter
    def e(self, value: str):
        ...
    
    ...


class ElementCollection:
    '''Collection of base logical structure elements.'''
    
    def remove(self, item: aspose.pdf.structure.Element) -> bool:
        '''Remove element.'''
        ...

    @property
    def count(self) -> int:
        '''Count of elements.'''
        ...

class FigureElement(aspose.pdf.structure.Element):
    '''Class representing logical structure figure.'''
    
    @property
    def image(self) -> aspose.pydrawing.Image:
        '''Gets the value of figure structure element.'''
        ...
    
    ...

class RootElement(aspose.pdf.structure.Element):
    '''Root structure element.'''
 
    ...

class StructElement(aspose.pdf.structure.Element):
    '''General structure element.'''
    
    ...

class TextElement(aspose.pdf.structure.Element):
    '''General text element of document logical structure.'''
    
    @property
    def text(self) -> str:
        '''Gets the value of text structure element.'''
        ...
    
    ...

