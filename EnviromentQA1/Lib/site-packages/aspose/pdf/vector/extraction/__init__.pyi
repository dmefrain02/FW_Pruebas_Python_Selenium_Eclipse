import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class SubPathGroup:
    '''Represents a class for a group of graphic element containers.
    Class objects have a bounding box to account for group size.'''
    
    ...

class SvgExtractionOptions:
    '''Represents an options class for extracting vector graphics from the pdf document page.'''
    
    def __init__(self):
        ...
    
    @property
    def unpack_page_content_x_form(self) -> bool:
        '''Gets and sets a flag that determines whether XFrom found on pages should be unpacked or not.
        XFrom elements can end up in different SVG files.
        Only XForms that are rendered by Do statements from the page content are unpacked. Nested XForms are not unpacked.'''
        ...
    
    @unpack_page_content_x_form.setter
    def unpack_page_content_x_form(self, value: bool):
        ...
    
    @property
    def extract_every_sub_path_to_svg(self) -> bool:
        '''Gets and sets opttion to extracts every subpath from a PDF document to separate SVG images.'''
        ...
    
    @extract_every_sub_path_to_svg.setter
    def extract_every_sub_path_to_svg(self, value: bool):
        ...
    
    @property
    def extraction_area_bound(self) -> aspose.pdf.Rectangle:
        '''Gets and sets the bounding rectangle that defines the extraction area for SVG extraction.'''
        ...
    
    @extraction_area_bound.setter
    def extraction_area_bound(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def strict_extraction_area_bound_check(self) -> bool:
        '''Gets and sets an option to define strictly checks whether subpaths are within the specified rectangle in :attr:`SvgExtractionOptions.extraction_area_bound`.
        If set to false, then subpaths that are not completely included in :attr:`SvgExtractionOptions.extraction_area_bound` will be extracted.
        The default value is True.'''
        ...
    
    @strict_extraction_area_bound_check.setter
    def strict_extraction_area_bound_check(self, value: bool):
        ...
    
    @property
    def group_strength(self) -> float:
        '''Gets and sets an option The strength of grouping subpaths into images. Allows you to configure the degree of grouping of subpaths.
        The value ranges is from 0 to 1. A value of 0 corresponds to the :attr:`SvgExtractionOptions.extract_every_sub_path_to_svg` option being enabled.
        A value of 1 will create single image for all vector paths on the page.
        The option has an effect when :attr:`SvgExtractionOptions.auto_grouping` is false.
        The default value is 0.8.'''
        ...
    
    @group_strength.setter
    def group_strength(self, value: float):
        ...
    
    @property
    def auto_grouping(self) -> bool:
        '''Gets and sets the option to automatically group subpaths into images.
        This option excludes the :attr:`SvgExtractionOptions.group_strength` option.'''
        ...
    
    @auto_grouping.setter
    def auto_grouping(self, value: bool):
        ...
    
    @property
    def min_stroke_width(self) -> float:
        '''Gets or sets the minimum stroke width that will be used in the resulting SVG.
        If the PDF use a thinner stroke width, it will be replaced with this width.
        The default value is 0.5.
        
        The value is expressed in transformed user space units of the converted PDF page. By default 1 user
        space unit is 1/72 inch (0.35 mm), but this can be overridden by the PDF document. Transforms can affect
        the actual minimum width in the generated SVG.'''
        ...
    
    @min_stroke_width.setter
    def min_stroke_width(self, value: float):
        ...
    
    ...

class SvgExtractor:
    '''Represents a class to SVG-images extraction from page.'''
    
    @overload
    def __init__(self):
        '''Represents a class to extract SVG images from a page.'''
        ...
    
    @overload
    def __init__(self, options: aspose.pdf.vector.extraction.SvgExtractionOptions):
        '''Represents a class to extract SVG images from a page.
        
        :param options: The extraction options.'''
        ...
    
    @overload
    def extract(self, elements: Iterable[aspose.pdf.vector.GraphicElement], page: aspose.pdf.Page) -> str:
        ...
    
    @overload
    def extract(self, elements: Iterable[aspose.pdf.vector.GraphicElement], page: aspose.pdf.Page, svg_file_path: str) -> None:
        ...
    
    @overload
    def extract(self, page: aspose.pdf.Page) -> None:
        '''Extracts Svg images from a page to strings.
        
        :param page: The page to extract.
        :returns: The list of SVG content strings.'''
        ...
    
    @overload
    def extract(self, page: aspose.pdf.Page, directory: str) -> None:
        '''Extracts Svg images from a page to files.
        
        :param page: The page to extract.
        :param directory: The target directory to place SVG images.'''
        ...
    
    ...

