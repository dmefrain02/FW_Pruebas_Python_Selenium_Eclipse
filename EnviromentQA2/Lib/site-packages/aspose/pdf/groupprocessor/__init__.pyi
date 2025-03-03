from aspose.pdf.groupprocessor import creators
import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class ExtractorFactory:
    '''Represents factory for creating IPdfTypeExtractor objects.'''
    
    pdf: aspose.pdf.groupprocessor.creators.PdfTypeObjectCreator
    
    ...

class IDocumentPageTextExtractor:
    '''Interface for document page text extractor.'''
    
    def extract_page_text(self, page_number: int) -> str:
        '''Extracted page text.
        
        :param page_number: Page number.
        :returns: Extracted page text.'''
        ...
    
    @property
    def page_count(self) -> int:
        '''Returns page count.'''
        ...
    
    ...

class IDocumentTextExtractor:
    '''Interface for document text extractor.'''
    
    def extract_all_text(self) -> list[str]:
        '''Returns collection of extracted text values.
        
        :returns: Extracted text values.'''
        ...
    
    ...

class IPdfTypeExtractor:
    '''Represents interface to interacting with extractor.'''
    
    def extract_all_text(self) -> list[str]:
        '''Returns collection of extracted text values.
        
        :returns: Collection of extracted text values.'''
        ...
    
    def extract_page_text(self, page_number: int) -> str:
        '''Returns page text.
        
        :param page_number: Page number.
        :returns: Page text.'''
        ...
    
    def dispose(self) -> None:
        '''Dispose.'''
        ...
    
    @property
    def page_count(self) -> int:
        '''Returns page count.'''
        ...
    
    @property
    def version(self) -> str:
        '''Returns version.'''
        ...
    
    @property
    def is_fast_extraction_used(self) -> bool:
        '''Returns if fast extraction mechanism used.'''
        ...
    
    ...

