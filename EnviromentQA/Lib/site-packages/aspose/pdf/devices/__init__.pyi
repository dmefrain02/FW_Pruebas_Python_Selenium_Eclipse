import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class BmpDevice(aspose.pdf.devices.ImageDevice):
    '''Represents image device that helps to save pdf document pages into bmp.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`BmpDevice` class with default resolution.'''
        ...
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`BmpDevice` class.
        
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`BmpDevice` class with provided image dimensions and
        resolution.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`BmpDevice` class with provided page size and
        resolution.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int):
        '''Initializes a new instance of the :class:`BmpDevice` class with provided image dimensions,
        default resolution (=150).
        
        :param width: Image output width.
        :param height: Image output height.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize):
        '''Initializes a new instance of the :class:`BmpDevice` class with provided page size,
        default resolution (=150).
        
        :param page_size: Page size of the output image.'''
        ...
    
    @overload
    def process(self, page: aspose.pdf.Page, output: Any) -> None:
        '''Converts the page into bmp and saves it in the output stream.
        
        :param page: The page to convert.
        :param output: Output stream with bmp image.'''
        ...
    
    ...

class Device:
    '''Abstract class for all types of devices. Device is used to represent pdf document in some format.
    For example, document page can be represented as image or text.'''
    
    ...

class DicomDevice(aspose.pdf.devices.ImageDevice):
    '''Represents image device that helps to save pdf document pages into Dicom format.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`DicomDevice` class with default resolution.'''
        ...
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`DicomDevice` class.
        
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize):
        '''Initializes a new instance of the :class:`DicomDevice` class with provided page size,
        with default resolution (=150).
        
        :param page_size: Page size of the output image.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int):
        '''Initializes a new instance of the :class:`DicomDevice` class with provided image dimensions,
        with default resolution (=150).
        
        :param width: Image output width.
        :param height: Image output height.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`DicomDevice` class with provided page size and
        resolution.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`DicomDevice` class with provided image dimensions and
        resolution.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def process(self, page: aspose.pdf.Page, output: Any) -> None:
        '''Converts the page into Dicom and saves it in the output stream.
        
        :param page: The page to convert.
        :param output: Output stream with image.'''
        ...
    
    ...

class DocumentDevice(aspose.pdf.devices.Device):
    '''Abstract class for all devices which is used to process the whole pdf document.'''
    
    @overload
    def process(self, document: aspose.pdf.Document, from_page: int, to_page: int, output: Any) -> None:
        '''Each device represents some operation on the document, e.g. we can convert pdf document into another format.
        
        :param document: The document to process.
        :param from_page: Defines the page from which to start processing.
        :param to_page: Defines the last page to process.
        :param output: Defines stream where the results of processing are stored.'''
        ...
    
    @overload
    def process(self, document: aspose.pdf.Document, output: Any) -> None:
        '''Processes the whole document and saves results into stream.
        
        :param document: The document to process.
        :param output: Defines stream where the results of processing are stored.'''
        ...
    
    @overload
    def process(self, document: aspose.pdf.Document, output_file_name: str) -> None:
        '''Processes the whole document and saves results into file.
        
        :param document: The document to process.
        :param output_file_name: Defines file where the results of processing are stored.'''
        ...
    
    @overload
    def process(self, document: aspose.pdf.Document, from_page: int, to_page: int, output_file_name: str) -> None:
        '''Processes certain pages of the document and saves results into file.
        
        :param document: The document to process.
        :param from_page: The first page to start processing.
        :param to_page: The last page of processing.
        :param output_file_name: Defines file where the results of processing are stored.'''
        ...
    
    ...

class EmfDevice(aspose.pdf.devices.ImageDevice):
    '''Represents image device that helps to save pdf document pages into emf.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`EmfDevice` class with default resolution of raster image written to emf.'''
        ...
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`EmfDevice` class.
        
        :param resolution: Resolution for the raster image written to emf, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int):
        '''Initializes a new instance of the :class:`EmfDevice` class with provided image dimensions,
        and default resolution for the raster image written to emf (=150)
        
        :param width: Image output width.
        :param height: Image output height.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize):
        '''Initializes a new instance of the :class:`EmfDevice` class with provided page size,
        and default resolution for the raster image written to emf (=150)
        
        :param page_size: Page size of the output image.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`JpegDevice` class with provided image dimensions,
        and resolution for the raster image written to emf.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the for the raster image written to emf, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`JpegDevice` class with provided page size,
        and resolution for the raster image written to emf.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the for the raster image written to emf, see :class:`Resolution` class.'''
        ...
    
    @overload
    def process(self, page: aspose.pdf.Page, output: Any) -> None:
        '''Converts the page into emf and saves it in the output stream.
        
        :param page: The page to convert.
        :param output: Output stream with emf image.'''
        ...
    
    ...

class GifDevice(aspose.pdf.devices.ImageDevice):
    '''Represents image device that helps to save pdf document pages into gif.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`GifDevice` class with default resolution.'''
        ...
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`GifDevice` class.
        
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`GifDevice` class with provided image dimensions and
        resolution.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`GifDevice` class with provided page size and
        resolution.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int):
        '''Initializes a new instance of the :class:`GifDevice` class with provided image dimensions,
        default resolution (=150).
        
        :param width: Image output width.
        :param height: Image output height.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize):
        '''Initializes a new instance of the :class:`GifDevice` class with provided page size,
        default resolution (=150).
        
        :param page_size: Page size of the output image.'''
        ...
    
    @overload
    def process(self, page: aspose.pdf.Page, output: Any) -> None:
        '''Converts the page into gif and saves it in the output stream.
        
        :param page: The page to convert.
        :param output: Output stream with gif image.'''
        ...
    
    ...

class ImageDevice(aspose.pdf.devices.PageDevice):
    '''An abstract class for image devices.'''
    
    @property
    def coordinate_type(self) -> aspose.pdf.PageCoordinateType:
        '''Gets or sets the page coordinate type (Media/Crop boxes). CropBox value is used by default.'''
        ...
    
    @coordinate_type.setter
    def coordinate_type(self, value: aspose.pdf.PageCoordinateType):
        ...
    
    @property
    def rendering_options(self) -> aspose.pdf.RenderingOptions:
        '''Gets or sets rendering options.'''
        ...
    
    @rendering_options.setter
    def rendering_options(self, value: aspose.pdf.RenderingOptions):
        ...
    
    @property
    def form_presentation_mode(self) -> aspose.pdf.devices.FormPresentationMode:
        '''Gets or sets form presentation mode.'''
        ...
    
    @form_presentation_mode.setter
    def form_presentation_mode(self, value: aspose.pdf.devices.FormPresentationMode):
        ...
    
    @property
    def resolution(self) -> aspose.pdf.devices.Resolution:
        '''Gets image resolution.'''
        ...
    
    @property
    def width(self) -> int:
        '''Gets image output width.'''
        ...
    
    @property
    def height(self) -> int:
        '''Gets image output height.'''
        ...
    
    ...

class JpegDevice(aspose.pdf.devices.ImageDevice):
    '''Represents image device that helps to save pdf document pages into jpeg.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`JpegDevice` class with default resolution and maximum quality.'''
        ...
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`JpegDevice` class.
        
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, quality: int):
        '''Initializes a new instance of the :class:`JpegDevice` class.
        
        :param quality: Specifies the level of compression for an image.
                        The range of useful values for the quality is from 0 to 100.
                        The lower the number specified, the higher the compression and therefore the lower the quality of the image.
                        Zero would give you the lowest quality image and 100 the highest.'''
        ...
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution, quality: int):
        '''Initializes a new instance of the :class:`JpegDevice` class.
        
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.
        :param quality: Specifies the level of compression for an image.
                        The range of useful values for the quality is from 0 to 100.
                        The lower the number specified, the higher the compression and therefore the lower the quality of the image.
                        Zero would give you the lowest quality image and 100 the highest.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int):
        '''Initializes a new instance of the :class:`JpegDevice` class with provided image dimensions,
        default resolution (=150) and maximum quality.
        
        :param width: Image output width.
        :param height: Image output height.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize):
        '''Initializes a new instance of the :class:`JpegDevice` class with provided page size,
        default resolution (=150) and maximum quality.
        
        :param page_size: Page size of the output image.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`JpegDevice` class with provided image dimensions,
        resolution and maximum quality.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`JpegDevice` class with provided page size,
        resolution and maximum quality.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution, quality: int):
        '''Initializes a new instance of the :class:`JpegDevice` class with provided image dimensions,
        resolution and quality.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.
        :param quality: Specifies the level of compression for an image.
                        The range of useful values for the quality is from 0 to 100.
                        The lower the number specified, the higher the compression and therefore the lower the quality of the image.
                        Zero would give you the lowest quality image and 100 the highest.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution, quality: int):
        '''Initializes a new instance of the :class:`JpegDevice` class with provided page size,
        resolution and quality.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.
        :param quality: Specifies the level of compression for an image.
                        The range of useful values for the quality is from 0 to 100.
                        The lower the number specified, the higher the compression and therefore the lower the quality of the image.
                        Zero would give you the lowest quality image and 100 the highest.'''
        ...
    
    @overload
    def process(self, page: aspose.pdf.Page, output: Any) -> None:
        '''Converts the page into jpeg and saves it in the output stream.
        
        :param page: The page to convert.
        :param output: Output stream with jpeg image.'''
        ...
    
    ...

class Margins:
    '''This class represents margins of an image.'''
    
    @overload
    def __init__(self, left: int, right: int, top: int, bottom: int):
        '''Initializes a new instance of the :class:`Margins` class.
        
        :param left: The left coordinate.
        :param right: The right coordinate.
        :param top: The top coordinate.
        :param bottom: The bottom coordinate.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`Margins` class.'''
        ...
    
    @property
    def left(self) -> int:
        '''Gets or sets the left.'''
        ...
    
    @left.setter
    def left(self, value: int):
        ...
    
    @property
    def right(self) -> int:
        '''Gets or sets the right.'''
        ...
    
    @right.setter
    def right(self, value: int):
        ...
    
    @property
    def top(self) -> int:
        '''Gets or sets the top.'''
        ...
    
    @top.setter
    def top(self, value: int):
        ...
    
    @property
    def bottom(self) -> int:
        '''Gets or sets the bottom.'''
        ...
    
    @bottom.setter
    def bottom(self, value: int):
        ...
    
    ...

class PageDevice(aspose.pdf.devices.Device):
    '''Abstract class for all devices which is used to process certain page the pdf document.'''
    
    @overload
    def process(self, page: aspose.pdf.Page, output: Any) -> None:
        '''Perfoms some operation on the given page, e.g. converts page into graphic image.
        
        :param page: The page to process.
        :param output: This stream contains the results of processing.'''
        ...
    
    @overload
    def process(self, page: aspose.pdf.Page, output_file_name: str) -> None:
        '''Perfoms some operation on the given page and saves results into the file.
        
        :param page: The page to process.
        :param output_file_name: This file contains the results of processing.'''
        ...
    
    ...

class PngDevice(aspose.pdf.devices.ImageDevice):
    '''Represents image device that helps to save pdf document pages into png.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PngDevice` class with default resolution.'''
        ...
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`PngDevice` class.
        
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`PngDevice` class with provided image dimensions and
        resolution.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`PngDevice` class with provided page size and
        resolution.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the result image file, see :class:`Resolution` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int):
        '''Initializes a new instance of the :class:`PngDevice` class with provided image dimensions,
        default resolution (=150).
        
        :param width: Image output width.
        :param height: Image output height.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize):
        '''Initializes a new instance of the :class:`PngDevice` class with provided page size,
        default resolution (=150).
        
        :param page_size: Page size of the output image.'''
        ...
    
    @overload
    def process(self, page: aspose.pdf.Page, output: Any) -> None:
        '''Converts the page into png and saves it in the output stream.
        
        :param page: The page to convert.
        :param output: Output stream with png image.'''
        ...
    
    @property
    def transparent_background(self) -> bool:
        '''Gets or sets if image has transparent background.'''
        ...
    
    @transparent_background.setter
    def transparent_background(self, value: bool):
        ...
    
    ...

class Resolution:
    '''Represents class for holding image resolution.'''
    
    @overload
    def __init__(self, value: int):
        '''Initializes a new instance of the :class:`Resolution` class.
        
        :param value: Value which represents the horizontal and vertical resolution.'''
        ...
    
    @overload
    def __init__(self, value_x: int, value_y: int):
        '''Initializes a new instance of the :class:`Resolution` class.
        
        :param value_x: Horizontal resolution.
        :param value_y: Vertical resolution.'''
        ...
    
    @property
    def x(self) -> int:
        '''Gets or sets horizontal image resolution.'''
        ...
    
    @x.setter
    def x(self, value: int):
        ...
    
    @property
    def y(self) -> int:
        '''Gets or sets vertical image resolution.'''
        ...
    
    @y.setter
    def y(self, value: int):
        ...
    
    ...

class TextDevice(aspose.pdf.devices.PageDevice):
    '''Represents class for converting pdf document pages into text.
    
    The :class:`TextDevice` object is basically used to extract text from pdf page.'''
    
    @overload
    def __init__(self, extraction_options: aspose.pdf.text.TextExtractionOptions):
        '''Initializes a new instance of the :class:`TextDevice` with text extraction options.
        
        :param extraction_options: Text extraction options.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`TextDevice` with the Raw text formatting mode and Unicode text encoding.'''
        ...
    
    @overload
    def __init__(self, encoding: str):
        '''Initializes a new instance of the :class:`TextDevice` for the specified encoding.
        
        :param encoding: Encoding of extracted text'''
        ...
    
    @overload
    def __init__(self, extraction_options: aspose.pdf.text.TextExtractionOptions, encoding: str):
        '''Initializes a new instance of the :class:`TextDevice` for the specified encoding with text extraction options.
        
        :param extraction_options: Text extraction options.
        :param encoding: Encoding of extracted text.'''
        ...
    
    @overload
    def process(self, page: aspose.pdf.Page, output: Any) -> None:
        '''Convert page and save it as text stream.
        
        :param page: The page to convert.
        :param output: Result stream.'''
        ...
    
    @property
    def extraction_options(self) -> aspose.pdf.text.TextExtractionOptions:
        '''Gets or sets text extraction options.'''
        ...
    
    @extraction_options.setter
    def extraction_options(self, value: aspose.pdf.text.TextExtractionOptions):
        ...
    
    @property
    def encoding(self) -> str:
        '''Gets or sets encoding of extracted text.'''
        ...
    
    @encoding.setter
    def encoding(self, value: str):
        ...
    
    ...

class ThumbnailDevice(aspose.pdf.devices.ImageDevice):
    '''Represents image device that save pdf document pages into Thumbnail image.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`ThumbnailDevice` class
        with default size of thumbnail image (200x200 pixels).'''
        ...
    
    @overload
    def __init__(self, width: int, height: int):
        '''Initializes a new instance of the :class:`ThumbnailDevice` class.
        
        :param width: Thumbnail image output width.
        :param height: Thumbnail image output height.'''
        ...
    
    @overload
    def process(self, page: aspose.pdf.Page, output: Any) -> None:
        '''Converts the page into thumbnail image png and saves it in the output stream.
        
        :param page: The page to convert.
        :param output: Output stream with png image.'''
        ...
    
    ...

class TiffDevice(aspose.pdf.devices.DocumentDevice):
    '''This class helps to save pdf document page by page into the one tiff image.'''
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param resolution: Resolution for the result image file.'''
        ...
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution, settings: aspose.pdf.devices.TiffSettings):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param resolution: Resolution for the output image.
        :param settings: Tiff settings, see :class:`TiffSettings` class.'''
        ...
    
    @overload
    def __init__(self, resolution: aspose.pdf.devices.Resolution, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param resolution: Resolution for the output image.
        :param settings: Tiff settings, see :class:`TiffSettings` class.
        :param converter: External converter'''
        ...
    
    @overload
    def __init__(self, settings: aspose.pdf.devices.TiffSettings):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param settings: Tiff settings, see :class:`TiffSettings` class.'''
        ...
    
    @overload
    def __init__(self, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param settings: Tiff settings, see :class:`TiffSettings` class.
        :param converter: External converter'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`TiffDevice` class with default settings.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution, settings: aspose.pdf.devices.TiffSettings):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the output image.
        :param settings: Tiff settings, see :class:`TiffSettings` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the output image.
        :param settings: Tiff settings, see :class:`TiffSettings` class.
        :param converter: External converter'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution, settings: aspose.pdf.devices.TiffSettings):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the output image.
        :param settings: Tiff settings, see :class:`TiffSettings` class.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the output image.
        :param settings: Tiff settings, see :class:`TiffSettings` class.
        :param converter: External converter'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param width: Image output width.
        :param height: Image output height.
        :param resolution: Resolution for the output image.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, resolution: aspose.pdf.devices.Resolution):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param page_size: Page size of the output image.
        :param resolution: Resolution for the output image.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, settings: aspose.pdf.devices.TiffSettings):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param width: Image output width.
        :param height: Image output height.
        :param settings: Tiff settings, see :class:`TiffSettings` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param width: Image output width.
        :param height: Image output height.
        :param settings: Tiff settings, see :class:`TiffSettings` class.
        :param converter: External converter'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param page_size: Page size of the output image.
        :param settings: Tiff settings, see :class:`TiffSettings` class.
        :param converter: External converter'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize, settings: aspose.pdf.devices.TiffSettings):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param page_size: Page size of the output image.
        :param settings: Tiff settings, see :class:`TiffSettings` class.'''
        ...
    
    @overload
    def __init__(self, width: int, height: int):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param width: Image output width.
        :param height: Image output height.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pdf.PageSize):
        '''Initializes a new instance of the :class:`TiffDevice` class.
        
        :param page_size: Page size of the output image.'''
        ...
    
    @overload
    def process(self, document: aspose.pdf.Document, from_page: int, to_page: int, output: Any) -> None:
        '''Converts certain document pages into tiff and save it in the output stream.
        
        :param document: The document to convert.
        :param from_page: Defines page number from which converting will start.
        :param to_page: Defines page number which will end the converting.
        :param output: Output stream with tiff image.'''
        ...
    
    def binarize_bradley(self, input_image_stream: Any, output_image_stream: Any, threshold: float) -> None:
        '''Do Bradley binarization for input stream.
        
        :param input_image_stream: The input image stream.
        :param output_image_stream: The output image stream.
        :param threshold: The threshold value between 0.0 and 1.0.'''
        ...

    @property
    def rendering_options(self) -> aspose.pdf.RenderingOptions:
        '''Gets or sets rendering options.'''
        ...
    
    @rendering_options.setter
    def rendering_options(self, value: aspose.pdf.RenderingOptions):
        ...
    
    @property
    def form_presentation_mode(self) -> aspose.pdf.devices.FormPresentationMode:
        '''Gets or sets form presentation mode.'''
        ...
    
    @form_presentation_mode.setter
    def form_presentation_mode(self, value: aspose.pdf.devices.FormPresentationMode):
        ...
    
    @property
    def settings(self) -> aspose.pdf.devices.TiffSettings:
        '''Gets settings for mapping pdf into tiff image.'''
        ...
    
    @property
    def resolution(self) -> aspose.pdf.devices.Resolution:
        '''Gets image resolution.'''
        ...
    
    @property
    def width(self) -> int:
        '''Gets image output width.'''
        ...
    
    @property
    def height(self) -> int:
        '''Gets image output height.'''
        ...
    
    ...

class TiffSettings:
    '''This class represents settings for importing pdf to Tiff.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`TiffSettings` class.'''
        ...
    
    @overload
    def __init__(self, shape_type: aspose.pdf.devices.ShapeType):
        '''Initializes a new instance of the :class:`TiffSettings` class.
        
        :param shape_type: Type of the shape.'''
        ...
    
    @overload
    def __init__(self, compression_type: aspose.pdf.devices.CompressionType):
        '''Initializes a new instance of the :class:`TiffSettings` class.
        
        :param compression_type: Type of the compression.'''
        ...
    
    @overload
    def __init__(self, color_depth: aspose.pdf.devices.ColorDepth):
        '''Initializes a new instance of the :class:`TiffSettings` class.
        
        :param color_depth: The color depth.'''
        ...
    
    @overload
    def __init__(self, margins: aspose.pdf.devices.Margins):
        '''Initializes a new instance of the :class:`TiffSettings` class.
        
        :param margins: The margins.'''
        ...
    
    @overload
    def __init__(self, compression_type: aspose.pdf.devices.CompressionType, color_depth: aspose.pdf.devices.ColorDepth, margins: aspose.pdf.devices.Margins):
        '''Initializes a new instance of the :class:`TiffSettings` class.
        
        :param compression_type: Type of the compression.
        :param color_depth: The color depth.
        :param margins: The margins.'''
        ...
    
    @overload
    def __init__(self, compression_type: aspose.pdf.devices.CompressionType, color_depth: aspose.pdf.devices.ColorDepth, margins: aspose.pdf.devices.Margins, skip_blank_pages: bool):
        '''Initializes a new instance of the :class:`TiffSettings` class.
        
        :param compression_type: Type of the compression.
        :param color_depth: The color depth.
        :param margins: The margins.
        :param skip_blank_pages: if set to ``True`` need to skip blank pages.'''
        ...
    
    @overload
    def __init__(self, compression_type: aspose.pdf.devices.CompressionType, color_depth: aspose.pdf.devices.ColorDepth, margins: aspose.pdf.devices.Margins, skip_blank_pages: bool, shape_type: aspose.pdf.devices.ShapeType):
        '''Initializes a new instance of the :class:`TiffSettings` class.
        
        :param compression_type: Type of the compression.
        :param color_depth: The color depth.
        :param margins: The margins.
        :param skip_blank_pages: if set to ``True`` need to skip blank pages.
        :param shape_type: Type of the shape.'''
        ...
    
    @overload
    def __init__(self, skip_blank_pages: bool):
        '''Initializes a new instance of the :class:`TiffSettings` class.
        
        :param skip_blank_pages: if set to ``True`` [skip blank pages].'''
        ...
    
    @property
    def margins(self) -> aspose.pdf.devices.Margins:
        '''Gets the margins.'''
        ...
    
    @property
    def skip_blank_pages(self) -> bool:
        '''Gets or sets a value indicating whether to skip blank pages.
        
        Default value is false'''
        ...
    
    @skip_blank_pages.setter
    def skip_blank_pages(self, value: bool):
        ...
    
    @property
    def compression(self) -> aspose.pdf.devices.CompressionType:
        '''Gets or sets the type of the compression.
        
        Default value is CompressionType.LZW'''
        ...
    
    @compression.setter
    def compression(self, value: aspose.pdf.devices.CompressionType):
        ...
    
    @property
    def depth(self) -> aspose.pdf.devices.ColorDepth:
        '''Gets or sets the color depth.
        
        Default value is ColorDepth.Default'''
        ...
    
    @depth.setter
    def depth(self, value: aspose.pdf.devices.ColorDepth):
        ...
    
    @property
    def shape(self) -> aspose.pdf.devices.ShapeType:
        '''Gets or sets the type of the shape.
        
        Default value is ShapeType.None'''
        ...
    
    @shape.setter
    def shape(self, value: aspose.pdf.devices.ShapeType):
        ...
    
    @property
    def brightness(self) -> float:
        '''Get or sets a value boundary of the transformation of colors in white and black.
        This parameter can be applied with EncoderValue.CompressionCCITT4, EncoderValue.CompressionCCITT3, EncoderValue.CompressionRle or ColorDepth.Format1bpp == 1'''
        ...
    
    @brightness.setter
    def brightness(self, value: float):
        ...
    
    @property
    def coordinate_type(self) -> aspose.pdf.PageCoordinateType:
        '''Get or sets the page coordinate type (Media/Crop boxes). CropBox value is used by default.'''
        ...
    
    @coordinate_type.setter
    def coordinate_type(self, value: aspose.pdf.PageCoordinateType):
        ...
    
    ...

class ColorDepth:
    '''Used to specify the parameter value passed to a Tiff image device.'''
    
    DEFAULT: ColorDepth
    FORMAT_24BPP: ColorDepth
    FORMAT_8BPP: ColorDepth
    FORMAT_4BPP: ColorDepth
    FORMAT_1BPP: ColorDepth

class CompressionType:
    '''Used to specify the parameter value passed to a Tiff image device.'''
    
    LZW: CompressionType
    CCITT4: CompressionType
    CCITT3: CompressionType
    RLE: CompressionType
    NONE: CompressionType

class FormPresentationMode:
    '''Used to specify the form presentation mode when printing or converting to image pdf documents.'''
    
    PRODUCTION: FormPresentationMode
    EDITOR: FormPresentationMode

class ShapeType:
    '''This enum represents shape type for the extracted images.'''
    
    NONE: ShapeType
    LANDSCAPE: ShapeType
    PORTRAIT: ShapeType

