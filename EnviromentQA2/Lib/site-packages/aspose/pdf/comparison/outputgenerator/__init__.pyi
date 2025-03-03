import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class HtmlDiffOutputGenerator:
    '''Represents a class for generating html representation of texts differences.
    Deleted line breaks are indicated by - ¶.'''
    
    def __init__(self):
        ...
    
    @overload
    def __init__(self, text_style: aspose.pdf.comparison.outputgenerator.OutputTextStyle):
        ...

    @property
    def equal_style(self) -> str:
        '''Gets and sets the CSS-style string for Equal operation.
        Example:
        color: #003300; background-color: #ccff66;'''
        ...
    
    @equal_style.setter
    def equal_style(self, value: str):
        ...

    @property
    def insert_style(self) -> str:
        '''Gets and sets the СSS-style string for Insert operation.'''
        ...
    
    @insert_style.setter
    def insert_style(self, value: str):
        ...
    
    @property
    def delete_style(self) -> str:
        '''Gets and sets the СSS-style string for Delete operation.'''
        ...
    
    @delete_style.setter
    def delete_style(self, value: str):
        ...
    
    @property
    def strikethrough_deleted(self) -> bool:
        '''Get or set text-decoration: line-through style for the delete operation.
        Default value is ``False``.'''
        ...
    
    @strikethrough_deleted.setter
    def strikethrough_deleted(self, value: bool):
        ...
    
    ...

class IFileOutputGenerator:
    '''Represents an interface for generating output to a file of differences between texts.'''
    
    @overload
    def generate_output(self, diffrences, target_file_path: str) -> None:
        ...
    
    @overload
    def generate_output(self, diffrences, target_file_path: str) -> None:
        ...
    
    ...

class IStringOutputGenerator:
    '''Represents an interface for generating output to a string of differences between texts.'''
    
    @overload
    def generate_output(self, diffrences) -> str:
        ...
    
    @overload
    def generate_output(self, diffrences) -> str:
        ...
    
    ...

class JsonDiffOutputGenerator:
    '''Represents a class for displaying the results of comparing PDF documents or pages in JSON format.'''
    
    def __init__(self):
        ...
    
    ...

class MarkdownDiffOutputGenerator:
    '''Represents a class for generating markdown representation of texts differences.
    Because of the markdown syntax, it is not possible to show changes to whitespace characters.
    Selection of changes makes adding whitespace characters around formatting,
    otherwise markdown viewer will not correctly display the text.
    Deleted line breaks are indicated by - ¶.'''
    
    def __init__(self):
        ...
    
    ...

class OutputTextStyle:
    '''Represents a style set class for marking text changes.'''
    
    def __init__(self):
        ...
    
    @property
    def inserted_style(self) -> None:
        '''Get and set a text style for inserted text.'''
        ...
    
    @inserted_style.setter
    def inserted_style(self, value: None):
        ...
    
    @property
    def deleted_style(self) -> None:
        '''Get and set a text style for deleted text.'''
        ...
    
    @deleted_style.setter
    def deleted_style(self, value: None):
        ...
    
    @property
    def equal_style(self) -> None:
        '''Get and set a text style for non changed text.'''
        ...
    
    @equal_style.setter
    def equal_style(self, value: None):
        ...
    
    @property
    def strikethrough_deleted(self) -> bool:
        '''Get or set text-decoration: line-through style for the delete operation.
        Default value is ``False``.'''
        ...
    
    @strikethrough_deleted.setter
    def strikethrough_deleted(self, value: bool):
        ...
    
    ...

class PdfOutputGenerator:
    '''Represents a class for generating PDF representation of texts differences.'''
    
    @overload
    def __init__(self):
        '''Cteates an instance of :class:`PdfOutputGenerator` class.'''
        ...
    
    @overload
    def __init__(self, page_info: aspose.pdf.PageInfo):
        '''Cteates an instance of :class:`PdfOutputGenerator` class.
        
        :param page_info: The page size and margins settings.'''
        ...
    
    @overload
    def __init__(self, text_style: aspose.pdf.comparison.outputgenerator.OutputTextStyle):
        '''Cteates an instance of :class:`PdfOutputGenerator` class.
        
        :param text_style: The styles for the changed text.'''
        ...
    
    @overload
    def __init__(self, text_style: aspose.pdf.comparison.outputgenerator.OutputTextStyle, page_info: aspose.pdf.PageInfo):
        '''Cteates an instance of :class:`PdfOutputGenerator` class.
        
        :param text_style: The styles for the changed text.
        :param page_info: The page size and margins settings.'''
        ...
    
    ...

class TextStyle:
    '''Represents a text style class.'''
    
    def __init__(self):
        ...
    
    @property
    def color(self) -> aspose.pdf.Color:
        '''Gets and sets the text color.'''
        ...
    
    @color.setter
    def color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def background_color(self) -> aspose.pdf.Color:
        '''Gets and sets the background color.'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.pdf.Color):
        ...
    
    ...


