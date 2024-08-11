import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class ExportFieldsOptions:
    '''Represents base class of options for exporting form fields.'''
    
    @property
    def export_password_value(self) -> bool:
        '''Gets or sets a value indicating whether the password value should be exported.'''
        ...
    
    @export_password_value.setter
    def export_password_value(self, value: bool):
        ...
    
    ...

class ExportFieldsToJsonOptions(aspose.pdf.engine.io.convertstrategies.converthelpers.ExportFieldsOptions):
    '''Represents options for exporting form fields to Json format.
    
    Inherits from :class:`ExportFieldsOptions` and adds specific options for Json export.'''
    
    def __init__(self):
        ...
    
    @property
    def write_indented(self) -> bool:
        '''Gets or sets a value indicating whether the Json output should be indented.'''
        ...
    
    @write_indented.setter
    def write_indented(self, value: bool):
        ...
    
    ...

class FieldSerializationResult:
    '''Represents the result of a form field serialization process.'''
    
    @property
    def field_serialization_status(self) -> aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationStatus:
        '''Gets the status of the form field serialization.'''
        ...
    
    @property
    def field_full_name(self) -> str:
        '''Gets the full name of the field.'''
        ...
    
    ...

class FieldSerializationStatus:
    '''Represents the status of the form field serialization.'''
    
    SUCCESS: FieldSerializationStatus
    WARNING: FieldSerializationStatus
    ERROR: FieldSerializationStatus

