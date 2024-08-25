import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class HeadingLevels:
    '''Represents a class to work with header levels based on font size.'''
    
    @overload
    def __init__(self):
        '''Creates a new instance of the HeadingLevels class.'''
        ...
    
    @overload
    def __init__(self, threshold: float):
        '''Creates a new instance of the HeadingLevels class.
        
        :param threshold: The threshold value to compare font sizes.
                          Within the threshold, the header levels are the same.
                          The threshold default value is 0.01.'''
        ...
    
    def add_levels(self, font_sizes) -> None:
        ...
    
    @property
    def all_levels(self) -> list[float]:
        '''Gets all heading levels.'''
        ...
    
    ...

class MarkdownSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Represents the document save option class in the markdown format.'''
    
    def __init__(self):
        ...
    
    @property
    def extract_vector_graphics(self) -> bool:
        '''Gets and sets a property indicating whether vector graphics should be extracted.'''
        ...
    
    @extract_vector_graphics.setter
    def extract_vector_graphics(self, value: bool):
        ...

    @property
    def area_to_extract(self) -> aspose.pdf.Rectangle:
        '''Get or set an rectangle area to extract content to markdown.'''
        ...
    
    @area_to_extract.setter
    def area_to_extract(self, value: aspose.pdf.Rectangle):
        ...

    @property
    def subscript_and_superscript_conversion(self) -> bool:
        '''Gets ans sets allowance to convert subscript and superscript.
        This value is true by default.'''
        ...
    
    @subscript_and_superscript_conversion.setter
    def subscript_and_superscript_conversion(self, value: bool):
        ...

    @property
    def resources_directory_name(self) -> str:
        '''Gets and sets the directory name to save document resources such as images.
        If the value is not specified, then the images will be written to the same directory as the markdown file itself.
        This is not path, it is only name!
        This directory will be automatically created in the directory with the saved markdown file.'''
        ...
    
    @resources_directory_name.setter
    def resources_directory_name(self, value: str):
        ...
    
    @property
    def use_image_html_tag(self) -> bool:
        '''Gets and sets allowance to use of an img tag to insert images to the left and right of the text.
        In this case, in the markdown viewer, the text will wrap around the image.'''
        ...
    
    @use_image_html_tag.setter
    def use_image_html_tag(self, value: bool):
        ...
    
    @property
    def line_break_style(self) -> aspose.pdf.pdftomarkdown.LineBreakStyle:
        '''Gets or sets the line break style for generated document.'''
        ...
    
    @line_break_style.setter
    def line_break_style(self, value: aspose.pdf.pdftomarkdown.LineBreakStyle):
        ...
    
    @property
    def emphasis_style(self) -> aspose.pdf.pdftomarkdown.EmphasisStyle:
        '''Gets or sets the style of emphasis for generated document.'''
        ...
    
    @emphasis_style.setter
    def emphasis_style(self, value: aspose.pdf.pdftomarkdown.EmphasisStyle):
        ...
    
    @property
    def heading_style(self) -> aspose.pdf.pdftomarkdown.HeadingStyle:
        '''Gets or sets the heading style for generated document.'''
        ...
    
    @heading_style.setter
    def heading_style(self, value: aspose.pdf.pdftomarkdown.HeadingStyle):
        ...
    
    @property
    def heading_levels(self) -> aspose.pdf.pdftomarkdown.HeadingLevels:
        '''Defines expected heading levels to use in FontSize recognition headers strategy.
        If this property value is set, then header recognition :attr:`HeadingRecognitionStrategy.HEURISTIC` strategy will be selected when set :attr:`HeadingRecognitionStrategy.AUTO` strategies even if the document contains bookmarks.'''
        ...
    
    @heading_levels.setter
    def heading_levels(self, value: aspose.pdf.pdftomarkdown.HeadingLevels):
        ...
    
    @property
    def heading_recognition_strategy(self) -> aspose.pdf.pdftomarkdown.HeadingRecognitionStrategy:
        '''Gets or sets the heading recognition strategy.'''
        ...
    
    @heading_recognition_strategy.setter
    def heading_recognition_strategy(self, value: aspose.pdf.pdftomarkdown.HeadingRecognitionStrategy):
        ...
    
    ...

class EmphasisStyle:
    '''Defines the available serialization styles for emphasis and strong emphasis.
    For specification see CommonMark - Emphasis and strong emphasis.'''
    
    ASTERISK: EmphasisStyle
    UNDERSCORE: EmphasisStyle

class HeadingRecognitionStrategy:
    '''Represents types of header recognition strategies.'''
    
    OUTLINES: HeadingRecognitionStrategy
    HEURISTIC: HeadingRecognitionStrategy
    AUTO: HeadingRecognitionStrategy
    NONE: HeadingRecognitionStrategy

class HeadingStyle:
    '''Defines the available serialization styles for headings.
    For specification see CommonMark - ATX headings,
    respectively CommonMark - Setext headings.'''
    
    ATX: HeadingStyle
    SETEXT: HeadingStyle

class LineBreakStyle:
    '''Represents the possible line break styles for a file.'''
    
    WINDOWS: LineBreakStyle
    UNIX: LineBreakStyle
    AUTO: LineBreakStyle

