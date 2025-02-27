import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class GraphicElement:
    '''Represents base class for graphics object on the page.'''
    
    @overload
    def save_to_svg(self, page: aspose.pdf.Page) -> str:
        '''Converts the element into a single SVG image.
        
        :param page: The page of element.
        :returns: The SVG-string.'''
        ...
    
    @overload
    def save_to_svg(self, page: aspose.pdf.Page, svg_file_path: str) -> None:
        '''Converts the element into a single SVG image file.
        
        :param page: The page of element.
        :param svg_file_path: The file path to save svg-image.'''
        ...

    def remove(self) -> None:
        '''Removes current element from the page.
        If there are many elements to remove better use :meth:`aspose.pdf.Page.delete_graphics`.'''
        ...
    
    def add_on_page(self, destination: aspose.pdf.Page) -> None:
        '''Adds current element on the page.
        If there are many elements to add better use :meth:`aspose.pdf.Page.add_graphics`.
        
        :param destination: Destination page'''
        ...
    
    @property
    def source_page(self) -> aspose.pdf.Page:
        '''Gets the page from which the graphic element is extracted.'''
        ...

    @property
    def matrix(self) -> aspose.pdf.Matrix:
        '''Gets graphic element matrix. The matrix sets when element is created.
        It changes when SetPosition() is called.'''
        ...

    @property
    def rectangle(self) -> aspose.pdf.Rectangle:
        '''Gets the bounding rectangle of the :class:`GraphicElement`.'''
        ...
    
    @property
    def position(self) -> aspose.pdf.Point:
        '''Gets or sets the position in the current coordinate space.
        If :attr:`GraphicElement.parent` is not null then the element have xForm coordinate space.'''
        ...
    
    @position.setter
    def position(self, value: aspose.pdf.Point):
        ...
    
    @property
    def parent(self) -> aspose.pdf.vector.XFormPlacement:
        '''Gets the current :class:`XFormPlacement` in which the element is located.'''
        ...
    
    @property
    def operators(self) -> None:
        '''Gets a collection of operators representing the element.'''
        ...
    
    ...

class GraphicElementCollection:
    '''Represents :class:`GraphicElement` collection.'''
    
    def __init__(self):
        '''Initializes the new collection.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.vector.GraphicElement:
        '''Gets the :class:`GraphicElement` element at the specified index.
        
        :param index: Index within the collection.
        :returns: :class:`GraphicElement`.'''
        ...
    
    ...

class GraphicState:
    '''Represents graphic state of the current :class:`GraphicElement`.'''
    
    @property
    def matrix(self) -> aspose.pdf.Matrix:
        '''Gets the current transformation matrix.'''
        ...
    
    @matrix.setter
    def matrix(self, value: aspose.pdf.Matrix):
        ...
    
    @property
    def clips_and_matrices(self) -> None:
        '''Gets the operators representing clips and concatenation matrices.'''
        ...
    
    ...

class GraphicsAbsorber:
    '''Represents an absorber object of graphics elements.
    Performs graphics search and provides access to search results via :attr:`GraphicsAbsorber.elements` collection.'''
    
    def __init__(self):
        ...
    
    def visit(self, page: aspose.pdf.Page) -> None:
        '''Performs search on the specified page.
        
        :param page: PDF document page object.'''
        ...
    
    def suppress_update(self) -> None:
        '''Suppresses update for :attr:`aspose.pdf.Page.contents` and all :attr:`aspose.pdf.XForm.contents`
        Was made for performance increase, see also .'''
        ...
    
    def resume_update(self) -> None:
        '''Resume update for :attr:`aspose.pdf.Page.contents` and all :attr:`aspose.pdf.XForm.contents`
        Was made for performance increase, see also .'''
        ...
    
    @property
    def elements(self) -> aspose.pdf.vector.GraphicElementCollection:
        '''Gets collection of search occurrences that are presented with :class:`GraphicElement` objects.'''
        ...
    
    ...

class SubPath(aspose.pdf.vector.GraphicElement):
    '''Represents vector graphics object on the page.
    Basically, vector graphics objects are represented by two groups of SubPaths.
    One of them is represented by a set of lines and curves.
    Others are presented as rectangles and can sometimes be confused.
    Usually it is a rectangular area that has a color, but very often this rectangle
    is placed at the beginning of the page and defines the entire space of the page in white.
    So you get the SubPath, but visually you only see the text on the page.'''
    
    ...

class XFormPlacement(aspose.pdf.vector.GraphicElement):
    '''Represents XForm placement.
    If the XForm is displayed on the page more than 1 time,
    all XformPlacements associated with this XForm will have common graphical elements, but different graphical states.'''
    
    def add_on_page(self, destination: aspose.pdf.Page) -> None:
        '''Adds current element on the page.
        If there are many elements to add better use :meth:`aspose.pdf.Page.add_graphics`.
        
        :param destination: Destination page'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets name of the XForm.'''
        ...
    
    @property
    def x_form(self) -> aspose.pdf.XForm:
        '''Gets XForm associated with this XFormPlacement.'''
        ...
    
    @property
    def elements(self) -> aspose.pdf.vector.GraphicElementCollection:
        '''Gets graphic elements inside this XForm.'''
        ...
    
    ...

