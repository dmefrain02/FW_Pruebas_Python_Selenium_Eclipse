import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class CosPdfBoolean(aspose.pdf.utils.publicdata.CosPdfPrimitive):
    '''This class represents boolean type.'''
    
    def __init__(self, value: bool):
        '''Initializes a new instance of the Aspose.Pdf.Engine.Data.PdfBoolean class.
        
        :param value: if set to ``True`` [value].'''
        ...
    
    def to_cos_pdf_boolean(self) -> aspose.pdf.utils.publicdata.CosPdfBoolean:
        '''Tries cast this instance to :class:`CosPdfBoolean`.
        
        :returns: null if instance is not :class:`CosPdfBoolean` else :class:`CosPdfBoolean`.'''
        ...
    
    @property
    def value(self) -> bool:
        '''Gets the value.'''
        ...
    
    ...

class CosPdfName(aspose.pdf.utils.publicdata.CosPdfPrimitive):
    '''This class represents Pdf Name object.'''
    
    def __init__(self, value: str):
        '''Initializes a new instance of the :class:`CosPdfName` class.
        
        :param value: The name.'''
        ...
    
    def to_cos_pdf_name(self) -> aspose.pdf.utils.publicdata.CosPdfName:
        '''Tries cast this instance to :class:`CosPdfName`.
        
        :returns: null if instance is not :class:`CosPdfName` else :class:`CosPdfName`.'''
        ...
    
    @property
    def value(self) -> str:
        '''Gets the value.'''
        ...
    
    ...

class CosPdfNumber(aspose.pdf.utils.publicdata.CosPdfPrimitive):
    '''This class represents Pdf Number type.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`CosPdfNumber` class.'''
        ...
    
    @overload
    def __init__(self, value: float):
        '''Initializes a new instance of the :class:`CosPdfNumber` class.
        
        :param value: The number.'''
        ...
    
    def to_cos_pdf_number(self) -> aspose.pdf.utils.publicdata.CosPdfNumber:
        '''Tries cast this instance to :class:`CosPdfNumber`.
        
        :returns: null if instance is not :class:`CosPdfNumber` else :class:`CosPdfNumber`.'''
        ...
    
    @property
    def value(self) -> float:
        '''Gets the value.'''
        ...
    
    ...

class CosPdfPrimitive:
    '''This class represents base public type :class:`CosPdfPrimitive`.'''
    
    def to_cos_pdf_number(self) -> aspose.pdf.utils.publicdata.CosPdfNumber:
        '''Tries cast this instance to :class:`CosPdfNumber`.
        
        :returns: null if instance is not :class:`CosPdfNumber` else :class:`CosPdfNumber`.'''
        ...
    
    def to_cos_pdf_name(self) -> aspose.pdf.utils.publicdata.CosPdfName:
        '''Tries cast this instance to :class:`CosPdfName`.
        
        :returns: null if instance is not :class:`CosPdfName` else :class:`CosPdfName`.'''
        ...
    
    def to_cos_pdf_string(self) -> aspose.pdf.utils.publicdata.CosPdfString:
        '''Tries cast this instance to :class:`CosPdfString`.
        
        :returns: null if instance is not :class:`CosPdfString` else :class:`CosPdfString`.'''
        ...
    
    def to_cos_pdf_boolean(self) -> aspose.pdf.utils.publicdata.CosPdfBoolean:
        '''Tries cast this instance to :class:`CosPdfBoolean`.
        
        :returns: null if instance is not :class:`CosPdfBoolean` else :class:`CosPdfBoolean`.'''
        ...
    
    ...

class CosPdfString(aspose.pdf.utils.publicdata.CosPdfPrimitive):
    '''This class represents Pdf String object.'''
    
    @overload
    def __init__(self, value: str):
        '''Initializes a new instance of the :class:`CosPdfString` class.
        
        :param value: The value.'''
        ...
    
    @overload
    def __init__(self, value: str, is_hexadecimal: bool):
        '''Initializes a new instance of the :class:`CosPdfString` class.
        
        :param value: The string.
        :param is_hexadecimal: if set to ``True`` [is hexadecimal].'''
        ...
    
    def to_cos_pdf_string(self) -> aspose.pdf.utils.publicdata.CosPdfString:
        '''Tries cast this instance to :class:`CosPdfString`.
        
        :returns: null if instance is not :class:`CosPdfString` else :class:`CosPdfString`.'''
        ...
    
    @property
    def is_hexadecimal(self) -> bool:
        '''Gets a value indicating whether this instance is hexadecimal.'''
        ...
    
    @property
    def value(self) -> str:
        '''Gets the string (ANSII).'''
        ...
    
    ...

class ICosPdfPrimitive:
    '''Interface for work with PDF data entity'''
    
    def to_cos_pdf_name(self) -> aspose.pdf.utils.publicdata.CosPdfName:
        '''Tries cast this instance to :class:`CosPdfName`.
        
        :returns: null if instance is not :class:`CosPdfName` else :class:`CosPdfName`.'''
        ...
    
    def to_cos_pdf_string(self) -> aspose.pdf.utils.publicdata.CosPdfString:
        '''Tries cast this instance to :class:`CosPdfString`.
        
        :returns: null if instance is not :class:`CosPdfString` else :class:`CosPdfString`.'''
        ...
    
    def to_cos_pdf_boolean(self) -> aspose.pdf.utils.publicdata.CosPdfBoolean:
        '''Tries cast this instance to :class:`CosPdfBoolean`.
        
        :returns: null if instance is not :class:`CosPdfBoolean` else :class:`CosPdfBoolean`.'''
        ...
    
    def to_cos_pdf_number(self) -> aspose.pdf.utils.publicdata.CosPdfNumber:
        '''Tries cast this instance to :class:`CosPdfNumber`.
        
        :returns: null if instance is not :class:`CosPdfNumber` else :class:`CosPdfNumber`.'''
        ...
    
    def to_string(self) -> str:
        '''System.String representation of instance :class:`ICosPdfPrimitive`.
        
        :returns: Value of System.String representation of instance :class:`ICosPdfPrimitive`.'''
        ...
    
    ...

