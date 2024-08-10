import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class Arc(aspose.pdf.drawing.Shape):
    '''Represents arc.'''
    
    def __init__(self, pos_x: float, pos_y: float, radius: float, alpha: float, beta: float):
        '''Initializes a new instance of the :class:`Arc` class.
        
        :param pos_x: The x-coordinate of the center point of the arc.
        :param pos_y: The y-coordinate of the center point of the arc.
        :param radius: The radius value of the arc.
        :param alpha: The beginning angle value of the arc.
        :param beta: The end angle value of the arc.'''
        ...
    
    @property
    def pos_x(self) -> float:
        '''Gets or sets a float value that indicates the x-coordinate of the center of the arc.'''
        ...
    
    @pos_x.setter
    def pos_x(self, value: float):
        ...
    
    @property
    def pos_y(self) -> float:
        '''Gets or sets a float value that indicates the y-coordinate of the center of the arc.'''
        ...
    
    @pos_y.setter
    def pos_y(self, value: float):
        ...
    
    @property
    def radius(self) -> float:
        '''Gets or sets a float value that indicates the radius of the arc.'''
        ...
    
    @radius.setter
    def radius(self, value: float):
        ...
    
    @property
    def alpha(self) -> float:
        '''Gets or sets a float value that indicates the beginning angle degree of the arc.'''
        ...
    
    @alpha.setter
    def alpha(self, value: float):
        ...
    
    @property
    def beta(self) -> float:
        '''Gets or sets a float value that indicates the ending angle degree of the arc.'''
        ...
    
    @beta.setter
    def beta(self, value: float):
        ...
    
    ...

class Circle(aspose.pdf.drawing.Shape):
    '''Represents circle.'''
    
    def __init__(self, pos_x: float, pos_y: float, radius: float):
        '''Initializes a new instance of the :class:`Circle` class.
        
        :param pos_x: The x-coordinate of the center of the circle.
        :param pos_y: The y-coordinate of the center of the circle.
        :param radius: The radius of the circle.'''
        ...
    
    @property
    def pos_x(self) -> float:
        '''Gets or sets a float value that indicates the x-coordinate of the center of the circle.'''
        ...
    
    @pos_x.setter
    def pos_x(self, value: float):
        ...
    
    @property
    def pos_y(self) -> float:
        '''Gets or sets a float value that indicates the y-coordinate of the center of the circle.'''
        ...
    
    @pos_y.setter
    def pos_y(self, value: float):
        ...
    
    @property
    def radius(self) -> float:
        '''Gets or sets a float value that indicates the radius of the circle.'''
        ...
    
    @radius.setter
    def radius(self, value: float):
        ...
    
    ...

class Curve(aspose.pdf.drawing.Shape):
    '''Represents bezier curve.'''
    
    def __init__(self, position_array: list[float]):
        '''Initializes a new instance of the :class:`Curve` class.
        
        :param position_array: The position array of the control points of the curve.There should be four
                               control points,so the length of the array should be eight.'''
        ...
    
    @property
    def position_array(self) -> list[float]:
        '''Gets or sets a float position array.'''
        ...
    
    @position_array.setter
    def position_array(self, value: list[float]):
        ...
    
    ...

class Ellipse(aspose.pdf.drawing.Shape):
    '''Represents ellipse.'''
    
    def __init__(self, left: float, bottom: float, width: float, height: float):
        '''Initializes a new instance of the :class:`Ellipse` class.
        
        :param left: The left position of the ellipse.
        :param bottom: The bottom position of the ellipse.
        :param width: The width of the ellipse.
        :param height: The height of the ellipse.'''
        ...
    
    @property
    def left(self) -> float:
        '''Gets or sets a float value that indicates the left position of the ellipse.'''
        ...
    
    @left.setter
    def left(self, value: float):
        ...
    
    @property
    def bottom(self) -> float:
        '''Gets or sets a float value that indicates the bottom position of the ellipse.'''
        ...
    
    @bottom.setter
    def bottom(self, value: float):
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets a float value that indicates the width of the ellipse.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets a float value that indicates the height of the ellipse.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    ...

class GradientAxialShading(aspose.pdf.drawing.PatternColorSpace):
    '''Represents gradient axial shading class.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`GradientAxialShading` class.'''
        ...
    
    @overload
    def __init__(self, start_color: aspose.pdf.Color, end_color: aspose.pdf.Color):
        '''Initializes a new instance of the :class:`GradientAxialShading` class.
        
        :param start_color: The start point.
        :param end_color: The end point.'''
        ...
    
    @property
    def start(self) -> aspose.pdf.Point:
        '''Gets or sets start point.'''
        ...
    
    @start.setter
    def start(self, value: aspose.pdf.Point):
        ...
    
    @property
    def end(self) -> aspose.pdf.Point:
        '''Gets or sets end point.'''
        ...
    
    @end.setter
    def end(self, value: aspose.pdf.Point):
        ...
    
    @property
    def start_color(self) -> aspose.pdf.Color:
        '''Gets or sets start color.'''
        ...
    
    @start_color.setter
    def start_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def end_color(self) -> aspose.pdf.Color:
        '''Gets or sets end color.'''
        ...
    
    @end_color.setter
    def end_color(self, value: aspose.pdf.Color):
        ...
    
    ...

class GradientRadialShading(aspose.pdf.drawing.PatternColorSpace):
    '''Represents gradient radial shading type.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`GradientRadialShading` class.'''
        ...
    
    @overload
    def __init__(self, start_color: aspose.pdf.Color, end_color: aspose.pdf.Color):
        '''Initializes a new instance of the :class:`GradientRadialShading` class.
        
        :param start_color: The starting circle color.
        :param end_color: The ending circle color.'''
        ...
    
    @property
    def start(self) -> aspose.pdf.Point:
        '''Gets or sets starting circle center point.'''
        ...
    
    @start.setter
    def start(self, value: aspose.pdf.Point):
        ...
    
    @property
    def end(self) -> aspose.pdf.Point:
        '''Gets or sets ending circle center point.'''
        ...
    
    @end.setter
    def end(self, value: aspose.pdf.Point):
        ...
    
    @property
    def starting_radius(self) -> float:
        '''Gets or sets starting circle radius.'''
        ...
    
    @starting_radius.setter
    def starting_radius(self, value: float):
        ...
    
    @property
    def ending_radius(self) -> float:
        '''Gets or sets ending circle radius.'''
        ...
    
    @ending_radius.setter
    def ending_radius(self, value: float):
        ...
    
    @property
    def start_color(self) -> aspose.pdf.Color:
        '''Gets or sets start color.'''
        ...
    
    @start_color.setter
    def start_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def end_color(self) -> aspose.pdf.Color:
        '''Gets or sets end color.'''
        ...
    
    @end_color.setter
    def end_color(self, value: aspose.pdf.Color):
        ...
    
    ...

class Graph(aspose.pdf.BaseParagraph):
    '''Represents graph - graphics generator paragraph.'''
    
    def __init__(self, width: float, height: float):
        '''Initializes a new instance of the :class:`Graph` class.
        
        :param width: The width of the graph.
        :param height: The height of the graph.'''
        ...
    
    def clone(self) -> object:
        '''Clone the graph.
        
        :returns: The cloned object'''
        ...
    
    @property
    def graph_info(self) -> aspose.pdf.GraphInfo:
        '''Gets or sets a :attr:`Graph.graph_info` object that indicates the graph info,such as color,
        line width,etc.'''
        ...
    
    @graph_info.setter
    def graph_info(self, value: aspose.pdf.GraphInfo):
        ...
    
    @property
    def border(self) -> aspose.pdf.BorderInfo:
        '''Gets or sets the border.'''
        ...
    
    @border.setter
    def border(self, value: aspose.pdf.BorderInfo):
        ...
    
    @property
    def is_change_position(self) -> bool:
        '''Gets or sets change curret position after process paragraph.(default true)'''
        ...
    
    @is_change_position.setter
    def is_change_position(self, value: bool):
        ...
    
    @property
    def left(self) -> float:
        '''Gets or sets the table left coordinate.'''
        ...
    
    @left.setter
    def left(self, value: float):
        ...
    
    @property
    def top(self) -> float:
        '''Gets or sets the table top coordinate.'''
        ...
    
    @top.setter
    def top(self, value: float):
        ...
    
    @property
    def shapes(self) -> None:
        '''Gets or sets a :attr:`Graph.shapes` collection that indicates all shapes in the graph.'''
        ...
    
    @shapes.setter
    def shapes(self, value: None):
        ...
    
    @property
    def title(self) -> aspose.pdf.text.TextFragment:
        '''Gets or sets a string value that indicates the title of the graph.'''
        ...
    
    @title.setter
    def title(self, value: aspose.pdf.text.TextFragment):
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets a float value that indicates the graph width.
        The unit is point.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets a float value that indicates the graph height.
        The unit is point.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    ...

class Line(aspose.pdf.drawing.Shape):
    '''Represents line.'''
    
    def __init__(self, position_array: list[float]):
        '''Initializes a new instance of the :class:`Line` class.
        
        :param position_array: The line position array.'''
        ...
    
    @property
    def position_array(self) -> list[float]:
        '''Gets or sets a :attr:`Line.position_array` object that indicates the position array.The array is
        composed by coordinates of each control point of the line.
        directly.'''
        ...
    
    @position_array.setter
    def position_array(self, value: list[float]):
        ...
    
    ...

class Path(aspose.pdf.drawing.Shape):
    '''Represents arc.'''
    
    @overload
    def __init__(self, shapes: list[aspose.pdf.drawing.Shape]):
        '''Initializes a new instance of the :class:`Path` class.
        
        :param shapes: The shape array contains path segments set.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`Path` class.'''
        ...
    
    @property
    def shapes(self) -> None:
        '''Gets or sets shapes collection.'''
        ...
    
    ...

class PatternColorSpace:
    '''Represents base pattern class.'''
    
    ...

class Rectangle(aspose.pdf.drawing.Shape):
    '''Represents rectangle.'''
    
    def __init__(self, left: float, bottom: float, width: float, height: float):
        '''Initializes a new instance of the :class:`Rectangle` class.
        
        :param left: The left position of the rectangle.
        :param bottom: The bottom position of the rectangle.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.'''
        ...
    
    @property
    def rounded_corner_radius(self) -> float:
        '''Gets or sets a float value that indicates the radius of rectangle corners.'''
        ...
    
    @rounded_corner_radius.setter
    def rounded_corner_radius(self, value: float):
        ...
    
    @property
    def left(self) -> float:
        '''Gets or sets a float value that indicates the left position of the rectangle.'''
        ...
    
    @left.setter
    def left(self, value: float):
        ...
    
    @property
    def bottom(self) -> float:
        '''Gets or sets a float value that indicates the bottom position of the rectangle.'''
        ...
    
    @bottom.setter
    def bottom(self, value: float):
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets a float value that indicates the width of the rectangle.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets a float value that indicates the height of the rectangle.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    ...

class Shape:
    '''Represents shape - the base graphics object.'''
    
    @property
    def graph_info(self) -> aspose.pdf.GraphInfo:
        '''Gets or sets a :attr:`Shape.graph_info` object that indicates the graph info,such as color,
        line width,etc.'''
        ...
    
    @graph_info.setter
    def graph_info(self, value: aspose.pdf.GraphInfo):
        ...
    
    @property
    def text(self) -> aspose.pdf.text.TextFragment:
        '''Gets or sets a text for shape'''
        ...
    
    @text.setter
    def text(self, value: aspose.pdf.text.TextFragment):
        ...
    
    ...

class ImageFormat:
    '''This enum represents image formats.'''
    
    BMP: ImageFormat
    JPEG: ImageFormat
    GIF: ImageFormat
    PNG: ImageFormat
    TIFF: ImageFormat
    EMF: ImageFormat
    DICOM: ImageFormat
    MEMORY_BMP: ImageFormat
    WMF: ImageFormat
    EXIF: ImageFormat

