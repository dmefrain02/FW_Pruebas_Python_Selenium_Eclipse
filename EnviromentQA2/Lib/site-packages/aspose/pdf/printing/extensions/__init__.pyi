import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class PageSettingsExtensions:
    '''Represents extensions methods for :class:`aspose.pdf.printing.PageSettings`.'''
    
    @staticmethod
    def to_native_page_settings(self, page_settings: aspose.pdf.printing.PageSettings) -> aspose.pydrawing.Printing.PageSettings:
        '''Converts :class:`aspose.pdf.printing.PageSettings` to Windows-specific System.Drawing.Printing.PageSettings.
        
        :param page_settings: Page settings to convert.
        :returns: Windows page settings.'''
        ...
    
    @staticmethod
    def to_aspose_page_settings(self, native_settings: aspose.pydrawing.Printing.PageSettings) -> aspose.pdf.printing.PageSettings:
        '''Converts Windows-specific System.Drawing.Printing.PageSettings to :class:`aspose.pdf.printing.PageSettings`.
        
        :param native_settings: Windows page settings to convert.
        :returns: Converted page settings.'''
        ...
    
    ...

class PaperSizeExtensions:
    '''Represents extensions methods for :class:`aspose.pdf.printing.PaperSize`.'''
    
    @staticmethod
    def to_native_paper_size(self, paper_size: aspose.pdf.printing.PaperSize) -> aspose.pydrawing.Printing.PaperSize:
        '''Converts :class:`aspose.pdf.printing.PaperSize` to Windows-specific System.Drawing.Printing.PaperSize.
        
        :param paper_size: Paper size to convert.
        :returns: Windows paper size.'''
        ...
    
    @staticmethod
    def to_aspose_paper_size(self, native_size: aspose.pydrawing.Printing.PaperSize) -> aspose.pdf.printing.PaperSize:
        '''Converts Windows-specific System.Drawing.Printing.PaperSize to :class:`aspose.pdf.printing.PaperSize`.
        
        :param native_size: Windows paper size to convert.
        :returns: Converted paper size.'''
        ...
    
    ...

class PaperSourceExtensions:
    '''Represents extensions methods for :class:`aspose.pdf.printing.PaperSource`.'''
    
    @staticmethod
    def to_native_paper_source(self, paper_source: aspose.pdf.printing.PaperSource) -> aspose.pydrawing.Printing.PaperSource:
        '''Converts :class:`aspose.pdf.printing.PaperSource` to Windows-specific System.Drawing.Printing.PaperSource.
        
        :param paper_source: Paper source to convert.
        :returns: Windows paper source.'''
        ...
    
    @staticmethod
    def to_aspose_paper_source(self, native_source: aspose.pydrawing.Printing.PaperSource) -> aspose.pdf.printing.PaperSource:
        '''Converts Windows-specific System.Drawing.Printing.PaperSource to :class:`aspose.pdf.printing.PaperSource`.
        
        :param native_source: Windows paper source to convert.
        :returns: Converted paper source.'''
        ...
    
    ...

class PrinterResolutionExtensions:
    '''Represents extensions methods for :class:`aspose.pdf.printing.PrinterResolution`.'''
    
    @staticmethod
    def to_native_printer_resolution(self, printer_resolution: aspose.pdf.printing.PrinterResolution) -> aspose.pydrawing.Printing.PrinterResolution:
        '''Converts :class:`aspose.pdf.printing.PrinterResolution` to Windows-specific System.Drawing.Printing.PrinterResolution.
        
        :param printer_resolution: Printer resolution to convert.
        :returns: Windows printer resolution.'''
        ...
    
    @staticmethod
    def to_aspose_printer_resolution(self, native_resolution: aspose.pydrawing.Printing.PrinterResolution) -> aspose.pdf.printing.PrinterResolution:
        '''Converts Windows-specific System.Drawing.Printing.PrinterResolution :class:`aspose.pdf.printing.PrinterResolution`.
        
        :param native_resolution: Windows printer resolution to convert.
        :returns: Converted printer resolution.'''
        ...
    
    ...

class PrinterSettingsExtensions:
    '''Represents extension methods for :class:`aspose.pdf.printing.PrinterSettings`.'''
    
    @staticmethod
    def to_native_printer_settings(self, printer_settings: aspose.pdf.printing.PrinterSettings) -> aspose.pydrawing.Printing.PrinterSettings:
        '''Converts :class:`aspose.pdf.printing.PrinterSettings` to Windows-specific System.Drawing.Printing.PrinterSettings.
        
        :param printer_settings: Printer settings to convert.
        :returns: Windows printer settings.'''
        ...
    
    @staticmethod
    def to_aspose_printer_settings(self, native_settings: aspose.pydrawing.Printing.PrinterSettings) -> aspose.pdf.printing.PrinterSettings:
        '''Converts Windows-specific System.Drawing.Printing.PrinterSettings to :class:`aspose.pdf.printing.PrinterSettings`.
        
        :param native_settings: Windows printer settings to convert.
        :returns: Converted printer settings.'''
        ...
    
    ...

