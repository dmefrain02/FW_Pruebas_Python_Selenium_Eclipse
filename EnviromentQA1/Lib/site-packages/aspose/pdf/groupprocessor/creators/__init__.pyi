import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class PdfTypeObjectCreator:
    '''Represents an creator of IPdfTypeExtractor object.'''
    
    def __init__(self):
        ...
    
    @overload
    def create_extractor(self, pdf_document_path: str, buffer_size: int, allow_async_initialization: bool) -> aspose.pdf.groupprocessor.IPdfTypeExtractor:
        '''Creates IPdfTypeExtractor object.
        
        :param pdf_document_path: Path to a pdf document.
        :param buffer_size: Maximum size of content in bytes that can be kept in memory.
        :param allow_async_initialization: Allows async initialization of resources.
        :returns: object of IPdfTypeExtractor'''
        ...
    
    @overload
    def create_extractor(self, pdf_document_stream: Any, buffer_size: int, allow_async_initialization: bool) -> aspose.pdf.groupprocessor.IPdfTypeExtractor:
        '''Creates IPdfTypeExtractor object.
        
        :param pdf_document_stream: Stream containing pdf document.
        :param buffer_size: Maximum size of content in bytes that can be kept in memory.
        :param allow_async_initialization: Allows async initialization of resources.
        :returns: object of IPdfTypeExtractor'''
        ...
    
    @overload
    def create_extractor(self, pdf_document_path: str, password: str, buffer_size: int, allow_async_initialization: bool) -> aspose.pdf.groupprocessor.IPdfTypeExtractor:
        '''Creates IPdfTypeExtractor object.
        
        :param pdf_document_path: Path to a pdf document.
        :param password: Document password.
        :param buffer_size: Maximum size of content in bytes that can be kept in memory.
        :param allow_async_initialization: Allows async initialization of resources.
        :returns: object of IPdfTypeExtractor'''
        ...
    
    @overload
    def create_extractor(self, pdf_document_stream: Any, password: str, buffer_size: int, allow_async_initialization: bool) -> aspose.pdf.groupprocessor.IPdfTypeExtractor:
        '''Creates IPdfTypeExtractor object.
        
        :param pdf_document_stream: Stream containing pdf document.
        :param password: Document password.
        :param buffer_size: Maximum size of content in bytes that can be kept in memory.
        :param allow_async_initialization: Allows async initialization of resources.
        :returns: object of IPdfTypeExtractor'''
        ...
    
    ...

