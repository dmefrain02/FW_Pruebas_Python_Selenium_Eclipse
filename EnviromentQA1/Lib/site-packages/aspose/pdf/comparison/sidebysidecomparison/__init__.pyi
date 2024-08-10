import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class SideBySideComparisonOptions:
    '''Represents an options class for comparing documents with side-by-side output.'''
    
    def __init__(self):
        ...
    
    @property
    def comparison_mode(self) -> aspose.pdf.comparison.sidebysidecomparison.ComparisonMode:
        '''Gets and sets a comparison mode.
        The default value is :attr:`ComparisonMode.IGNORE_SPACES`.'''
        ...
    
    @comparison_mode.setter
    def comparison_mode(self, value: aspose.pdf.comparison.sidebysidecomparison.ComparisonMode):
        ...
    
    @property
    def additional_change_marks(self) -> bool:
        '''Get and set the property that determines whether additional change markers are displayed.
        If set, displays change marks that are not on the current page but are present on another page.
        If the change lacates between words, the mark may not be positioned exactly relative to the whitespace character.
        The default value is false.'''
        ...
    
    @additional_change_marks.setter
    def additional_change_marks(self, value: bool):
        ...
    
    @property
    def exclude_tables(self) -> bool:
        '''Get and set the option that determines whether tables are excluded from comparison.
        This option cannot be set together with :attr:`SideBySideComparisonOptions.comparison_area1` and :attr:`SideBySideComparisonOptions.comparison_area2`.
        The default value is false.'''
        ...
    
    @exclude_tables.setter
    def exclude_tables(self, value: bool):
        ...
    
    @property
    def comparison_area1(self) -> aspose.pdf.Rectangle:
        '''Get and set the comparison area. Used for the first page or document in the comparison method.
        This option can't be setted along with :attr:`SideBySideComparisonOptions.exclude_tables`, :attr:`SideBySideComparisonOptions.exclude_areas1` and :attr:`SideBySideComparisonOptions.exclude_areas2` options.'''
        ...
    
    @comparison_area1.setter
    def comparison_area1(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def comparison_area2(self) -> aspose.pdf.Rectangle:
        '''Get and set the comparison area. Used for the second page or document in the comparison method.
        This option can't be setted along with :attr:`SideBySideComparisonOptions.exclude_tables`, :attr:`SideBySideComparisonOptions.exclude_areas1` and :attr:`SideBySideComparisonOptions.exclude_areas2` options.'''
        ...
    
    @comparison_area2.setter
    def comparison_area2(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def exclude_areas1(self) -> list[aspose.pdf.Rectangle]:
        '''Get and set the exclude areas. Used for the first page or document in the comparison method.
        This option can be setted along with :attr:`SideBySideComparisonOptions.exclude_tables`. This option can't be setted along with :attr:`SideBySideComparisonOptions.comparison_area1` option.'''
        ...
    
    @exclude_areas1.setter
    def exclude_areas1(self, value: list[aspose.pdf.Rectangle]):
        ...
    
    @property
    def exclude_areas2(self) -> list[aspose.pdf.Rectangle]:
        '''Get and set the exclude areas. Used for the second page or document in the comparison method.
        This option can be setted along with :attr:`SideBySideComparisonOptions.exclude_tables`. This option can't be setted along with :attr:`SideBySideComparisonOptions.comparison_area2` option.'''
        ...
    
    @exclude_areas2.setter
    def exclude_areas2(self, value: list[aspose.pdf.Rectangle]):
        ...
    
    ...

class SideBySidePdfComparer:
    
    @overload
    @staticmethod
    def compare(self, page1: aspose.pdf.Page, page2: aspose.pdf.Page, target_pdf_path: str, options: aspose.pdf.comparison.sidebysidecomparison.SideBySideComparisonOptions) -> None:
        '''Compares two pages. The result is saved in a PDF document in which the first page is written first, and then the second.
        You can open it in Adobe Acrobat in Two-page view to see the changes side by side.
        Deletions are noted on the page on the left, and insertions are noted on the page on the right.
        
        :param page1: The first page to compare.
        :param page2: The first page to compare.
        :param target_pdf_path: The path to PDF-file to save a comparison result.
        :param options: The comparison options.'''
        ...
    
    @overload
    @staticmethod
    def compare(self, document1: aspose.pdf.Document, document2: aspose.pdf.Document, target_pdf_path: str, options: aspose.pdf.comparison.sidebysidecomparison.SideBySideComparisonOptions) -> None:
        '''Compares two documents. The pages are compared one by one. The pages of the compared documents are copied one after another into the resulting document.
        First the first page from the first document, then the first page from the second document. Next is the second one from the first document and then the second one from the second document, etc.
        You can open it in Adobe Acrobat in Two-page view to see the changes side by side.
        Deletions are noted on the page on the left, and insertions are noted on the page on the right.
        
        :param document1: The first document to compare.
        :param document2: The second document to compare.
        :param target_pdf_path: The path to PDF-file to save a comparison result.
        :param options: The comparison options.'''
        ...
    
    ...

class ComparisonMode:
    '''The comparison mode enumeration.'''
    
    NORMAL: ComparisonMode
    IGNORE_SPACES: ComparisonMode
    PARSE_SPACES: ComparisonMode

