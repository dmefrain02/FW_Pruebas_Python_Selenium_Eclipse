import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class BarcodeField(aspose.pdf.forms.TextBoxField):
    '''Class represents barcode field.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Initializes new instance of the :class:`BarcodeField` class.
        
        :param page: The page where to place new barcode.
        :param rect: Barcode sizes given in rectangle.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, rect: aspose.pdf.Rectangle):
        '''Initializes new instance of the :class:`BarcodeField` class.
        
        :param doc: Document where field will be created.
        :param rect: Rectangle where field will be placed on the page.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @property
    def resolution(self) -> int:
        '''Gets the resolution, in dots-per-inch (dpi), at which the barcode object is rendered.'''
        ...
    
    @property
    def caption(self) -> str:
        '''Gets the caption of the barcode object.'''
        ...
    
    @property
    def symbology(self) -> aspose.pdf.forms.Symbology:
        '''Specifies which barcode or glyph technology is to be used on this annotation,
        see :attr:`BarcodeField.symbology` for details.'''
        ...
    
    @property
    def x_sym_width(self) -> int:
        '''Gets The horizontal distance, in pixels, between two barcode modules.'''
        ...
    
    @property
    def x_sym_height(self) -> int:
        '''Gets the the vertical distance between two barcode modules, measured in pixels.
        The ratio XSymHeight/XSymWidth shall be an integer value.
        For PDF417, the acceptable ratio range is from 1 to 4. For QRCode and DataMatrix,
        this ratio shall always be 1'''
        ...
    
    @property
    def ecc(self) -> int:
        '''Gets an integer value representing the error correction coefficient.
        For PDF417, shall be from 0 to 8. For QRCode, shall be from 0 to 3
        (0 for �L�, 1 for �M�, 2 for �Q�, and 3 for �H�).'''
        ...
    
    ...

class ButtonField(aspose.pdf.forms.Field):
    '''Class represnets push button field.'''
    
    @overload
    def __init__(self):
        '''Button field constructor for Generator.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''ButtonField constructor.
        
        :param page: Page where button will be placed.
        :param rect: Rectangle where button is placed on the page.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, rect: aspose.pdf.Rectangle):
        '''ButtonField constructore.
        
        :param doc: Docuemtn where new field will be created.
        :param rect: Rectangle hwere button is placed on the page.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    def add_image(self, image: aspose.pydrawing.Image) -> None:
        '''Adds image into the field resources and draws it.
        
        :param image: Image ot add into text field.'''
        ...
    
    @property
    def normal_caption(self) -> str:
        '''Gets or sets normal caption.'''
        ...
    
    @normal_caption.setter
    def normal_caption(self, value: str):
        ...
    
    @property
    def rollover_caption(self) -> str:
        '''Gets or sets rollover caption of button which shall be displayed when the user rolls the cursor
        into its active area without pressing the mouse button.'''
        ...
    
    @rollover_caption.setter
    def rollover_caption(self, value: str):
        ...
    
    @property
    def alternate_caption(self) -> str:
        '''Gets or sets alternate caption of the button which shall be displayed
        when the mouse button is pressed within its active area.'''
        ...
    
    @alternate_caption.setter
    def alternate_caption(self, value: str):
        ...
    
    @property
    def normal_icon(self) -> aspose.pdf.XForm:
        '''Gets or sets normal icon of the button which shall be displayed when it is not interacting with the user.'''
        ...
    
    @normal_icon.setter
    def normal_icon(self, value: aspose.pdf.XForm):
        ...
    
    @property
    def rollover_icon(self) -> aspose.pdf.XForm:
        '''Gets or sets rollover icon of the button which shall be displayed when the user
        rolls the cursor into its active area without pressing the mouse button.'''
        ...
    
    @rollover_icon.setter
    def rollover_icon(self, value: aspose.pdf.XForm):
        ...
    
    @property
    def alternate_icon(self) -> aspose.pdf.XForm:
        '''Gets or sets alternate icon which shall be displayed when the mouse button is pressed within its active area.'''
        ...
    
    @alternate_icon.setter
    def alternate_icon(self, value: aspose.pdf.XForm):
        ...
    
    @property
    def icon_fit(self) -> aspose.pdf.forms.IconFit:
        '''Gets icon fit object specifying how the widget annotation's icon shall be displayed within its annotation rectangle.'''
        ...
    
    @property
    def ic_position(self) -> aspose.pdf.forms.IconCaptionPosition:
        '''Gets or sets icon caption position.'''
        ...
    
    @ic_position.setter
    def ic_position(self, value: aspose.pdf.forms.IconCaptionPosition):
        ...
    
    ...

class CheckboxField(aspose.pdf.forms.Field):
    '''Class representing checkbox field'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Constructor for CheckboxField class.
        
        :param page: Page where check box will be placed.
        :param rect: Position and size of the check box.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, rect: aspose.pdf.Rectangle):
        '''Constructor for CheckboxField class.
        
        :param doc: Document where will be new field created.
        :param rect: Rectangle where new field will be created.'''
        ...
    
    @overload
    def __init__(self):
        '''Create instance of CheckboxField.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document):
        '''Constructor to use with Generator.
        
        :param doc: Document where field will be created.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @overload
    def add_option(self, option_name: str) -> None:
        '''Adds new checkbox into a checkbox group, in which at most one of the checkboxes may be checked at any time.
        The new checkbox is added to the bottom of the group.
        
        :param option_name: Value of the option represented by added checkbox.'''
        ...
    
    @overload
    def add_option(self, option_name: str, rect: aspose.pdf.Rectangle) -> None:
        '''Adds new checkbox into a checkbox group, in which at most one of the checkboxes may be checked at any time.
        
        :param option_name: Value of the option represented by added checkbox.
        :param rect: Rectangle of the added checkbox.'''
        ...

    @overload
    def add_option(self, option_name: str, page: int, rect: aspose.pdf.Rectangle) -> None:
        '''Adds new checkbox into a checkbox group, in which at most one of the checkboxes may be checked at any time.
        
        :param option_name: Value of the option represented by added checkbox.
        :param page: Number of the page where the added checkbox should be placed.
        :param rect: Rectangle of the added checkbox on the page.'''
        ...

    def clone(self) -> object:
        '''Clone the checkbox.
        
        :returns: The cloned object'''
        ...
    
    @property
    def active_state(self) -> str:
        '''Gets or sets current annotation appearance state.'''
        ...
    
    @active_state.setter
    def active_state(self, value: str):
        ...
    
    @property
    def value(self) -> str:
        '''Gets or sets value of check box field.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    @property
    def allowed_states(self) -> None:
        '''Returns list of allowed states.
        
        :returns:'''
        ...
    
    @property
    def style(self) -> aspose.pdf.forms.BoxStyle:
        '''Gets or sets style of check box.'''
        ...
    
    @style.setter
    def style(self, value: aspose.pdf.forms.BoxStyle):
        ...
    
    @property
    def checked(self) -> bool:
        '''Gets or sets state of check box.'''
        ...
    
    @checked.setter
    def checked(self, value: bool):
        ...
    
    @property
    def export_value(self) -> str:
        '''Gets or sets export value of CheckBox field.'''
        ...
    
    @export_value.setter
    def export_value(self, value: str):
        ...
    
    ...

class ChoiceField(aspose.pdf.forms.Field):
    '''Represents base class for choice fields.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @overload
    def add_option(self, option_name: str) -> None:
        '''Adds new option with specified name.
        
        :param option_name: Name of the new option.'''
        ...
    
    @overload
    def add_option(self, export: str, name: str) -> None:
        '''Adds new option with specified export value and name.
        
        :param export: Export value.
        :param name: Name of the new option.'''
        ...
    
    def delete_option(self, option_name: str) -> None:
        '''Deletes option by its name.
        
        :param option_name: Name of the option which must be deleted.'''
        ...
    
    @property
    def value(self) -> str:
        '''Gets or sets value of the field.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    @property
    def commit_immediately(self) -> bool:
        '''Gets or sets commit on selection change flag.'''
        ...
    
    @commit_immediately.setter
    def commit_immediately(self, value: bool):
        ...
    
    @property
    def multi_select(self) -> bool:
        '''Gets or sets multiselection flag.'''
        ...
    
    @multi_select.setter
    def multi_select(self, value: bool):
        ...
    
    @property
    def selected(self) -> int:
        '''Gets or sets index of selected option. This property allows to change selection.'''
        ...
    
    @selected.setter
    def selected(self, value: int):
        ...
    
    @property
    def selected_items(self) -> list[int]:
        '''Gets or sets array of selected items. For multiselect list array contains more then one item. For single selection list it contains single item.'''
        ...
    
    @selected_items.setter
    def selected_items(self, value: list[int]):
        ...
    
    @property
    def options(self) -> aspose.pdf.forms.OptionCollection:
        '''Gets collection of choice options.'''
        ...
    
    ...

class ComboBoxField(aspose.pdf.forms.ChoiceField):
    '''Class representing Combobox field of the form.'''
    
    @overload
    def __init__(self):
        '''Constructor for ComboBoxField to be used in Generator.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document):
        '''Creates CombBox field to work with Generator.
        
        :param doc: Document where field will be created.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Constructor for Combobox Field.
        
        :param page: Page where field will be placed.
        :param rect: Rectangle which defines size and position of the field on the page.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, rect: aspose.pdf.Rectangle):
        '''Constructor for Combobox field.
        
        :param doc: Document where field should be created.
        :param rect: Rectangle which defines size and position of the field.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @property
    def editable(self) -> bool:
        '''Gets or sets editable status of the field.'''
        ...
    
    @editable.setter
    def editable(self, value: bool):
        ...
    
    @property
    def spell_check(self) -> bool:
        '''Gets or sets spellchaeck activiity status.'''
        ...
    
    @spell_check.setter
    def spell_check(self, value: bool):
        ...
    
    ...

class DateField(aspose.pdf.forms.TextBoxField):
    '''Date field with calendar view.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`DateField`'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document):
        '''Constructor which should be used with Generator.
        
        :param doc: Document where field will be created.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Initializes a new instance of the :class:`DateField`
        
        :param page: Page needed for create.
        :param rect: Rectangle where the text field will be placed on the page.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, rect: aspose.pdf.Rectangle):
        '''Initializes a new instance of the :class:`DateField`
        
        :param doc: Document where field will be created.
        :param rect: Rectangle of the field.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @overload
    def add_image(self, image: aspose.pdf.Image) -> None:
        '''Image adding denied for this field.
        
        :param image: The image.
        :raises System.InvalidOperationException:'''
        ...
    
    def init(self, page: aspose.pdf.Page) -> None:
        '''Initializes the JS Action.
        
        :param page: The page.'''
        ...
    
    @property
    def value(self) -> datetime.datetime:
        '''Gets or sets Date.'''
        ...
    
    @value.setter
    def value(self, value: datetime.datetime):
        ...
    
    @property
    def date_format(self) -> str:
        '''Gets or sets the date format.'''
        ...
    
    @date_format.setter
    def date_format(self, value: str):
        ...
    
    ...

class DocMDPSignature:
    '''Represents the class of document MDP (modification detection and prevention) signature type.'''
    
    def __init__(self, signature: aspose.pdf.forms.Signature, access_permissions: aspose.pdf.forms.DocMDPAccessPermissions):
        '''Initializes a new instance of the :class:`DocMDPSignature` class.
        
        :param signature: The signature object that used during signing.
        :param access_permissions: The access permissions granted for this document.'''
        ...
    
    @property
    def access_permissions(self) -> aspose.pdf.forms.DocMDPAccessPermissions:
        '''Returns the access permissions granted for this document.'''
        ...
    
    ...

class ExternalSignature(aspose.pdf.forms.Signature):
    '''Creates a detached PKCS#7Detached signature using a X509Certificate2. It supports usb smartcards, tokens without exportable private keys.'''
    
    @overload
    def __init__(self, certificate):
        '''Creates a detached PKCS#7Detached signature using a X509Certificate2. It supports usb smartcards, tokens without exportable private keys.
        
        :param certificate: The certificate with the private key'''
        ...
    
    @overload
    def __init__(self, base64: str, detached: bool):
        '''Creates a PKCS#7 (detached) signature using a X509Certificate2 as base64 string.
        
        :param base64: X509Certificate2 as base64 string.
        :param detached: Is detached.'''
        ...
    
    @property
    def certificate(self) -> None:
        '''The certificate with the private key.'''
        ...
    
    ...

class Field(aspose.pdf.annotations.WidgetAnnotation):
    '''Base class for acro form fields.'''
    
    def __init__(self, doc: aspose.pdf.Document):
        '''Creates field for use in Generator.
        
        :param doc: Document where field will be created.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        '''Gets subfield contained in this field by index.
        
        :param index: Index of the reuqested subfield.
        :returns: Field instance.'''
        ...
    
    @overload
    def import_value_from_json(self, input_json_stream: Any) -> bool:
        '''Imports data into the specified fields from a JSON stream, based on an exact match of the fields' full names.
        
        :param input_json_stream: The input JSON stream containing the field data to be imported into the field.
        :returns: True if the field was found in JSON stream; otherwise - false'''
        ...
    
    @overload
    def import_value_from_json(self, input_json_stream: Any, field_full_name_in_json: str) -> bool:
        '''Imports data into the specified field from a JSON stream, using the full name specified in the 'fieldFullNameInJSON' variable for matching.
        
        :param input_json_stream: The input JSON stream containing the field data to be imported into the field.
        :param field_full_name_in_json: The name of the data within the JSON stream for matching. If the data within the JSON stream has a nested structure, the full name should be specified with all parent and child items separated by '.'
        :returns: True if the field was found in json file; otherwise - false'''
        ...

    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        ...
    
    def flatten(self) -> None:
        '''Removes this field and place its value directly on the page.'''
        ...
    
    def recalculate(self) -> bool:
        '''Recaculates all calculated fields on the form.
        
        :returns: true if field value was changed during recalculation.'''
        ...
    
    def copy_to(self, array: list[aspose.pdf.forms.Field], index: int) -> None:
        '''Copies subfields of this field into array starting from specified index.
        
        :param array: Array where field must be copied.
        :param index: Starting index where fields will be copied.'''
        ...
    
    def set_position(self, point: aspose.pdf.Point) -> None:
        '''Set position of the field.
        
        :param point: Point where field should be positioned.'''
        ...

    def execute_field_java_script(self, java_script_action: aspose.pdf.annotations.JavascriptAction) -> None:
        '''Executes a specified JavaScript action for the field.
        
        :param java_script_action: The JavaScript action to execute.'''
        ...
    
    def export_value_to_json(self, output_json_stream: Any, indented: bool) -> None:
        '''Exports the content of the specified field into a JSON stream. Button field value are not exported.
        
        :param output_json_stream: The output JSON stream where the field data will be written.
        :param indented: Optional. Specifies whether the JSON output should be indented for better readability. The default value is true.'''
        ...

    @property
    def rect(self) -> aspose.pdf.Rectangle:
        '''Gets or sets the field rectangle.'''
        ...
    
    @rect.setter
    def rect(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def page_index(self) -> int:
        '''Gets index of page which contains this field.'''
        ...
    
    @property
    def partial_name(self) -> str:
        '''Gets or sets partial name of the field.'''
        ...
    
    @partial_name.setter
    def partial_name(self, value: str):
        ...
    
    @property
    def alternate_name(self) -> str:
        '''Gets or sets alternate name of the field (An alternate field
        name that shall be used in place of the actual field name
        wherever the field shall be identified in the user interface).
        Alternate name is used as field tooltip in Adobe Acrobat.'''
        ...
    
    @alternate_name.setter
    def alternate_name(self, value: str):
        ...
    
    @property
    def mapping_name(self) -> str:
        '''Gets or sets mapping name  of the field that shall be used when exporting interactive form field data from the document.'''
        ...
    
    @mapping_name.setter
    def mapping_name(self, value: str):
        ...
    
    @property
    def value(self) -> str:
        '''Gets or sets value of the field.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Returns true if dictionary is synchronized.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Synchronization object.'''
        ...
    
    @property
    def is_group(self) -> bool:
        '''Gets or sets boolean value which indicates is this field non-terminal field i.e. group of fields.'''
        ...
    
    @property
    def annotation_index(self) -> int:
        '''Gets or sets index of this anotation on the page.'''
        ...
    
    @annotation_index.setter
    def annotation_index(self, value: int):
        ...
    
    @property
    def is_shared_field(self) -> bool:
        '''Property for Generator support. Used when field is added to header or footer. If true, this field will created once and it's appearance will be visible on all pages of the document. If false, separated field will be created for every document page.'''
        ...
    
    @is_shared_field.setter
    def is_shared_field(self, value: bool):
        ...
    
    fit_into_rectangle: bool
    
    max_font_size: float
    
    min_font_size: float
    
    @property
    def tab_order(self) -> int:
        '''Gets or sets tab order of the field.'''
        ...
    
    @tab_order.setter
    def tab_order(self, value: int):
        ...
    
    ...

class FileSelectBoxField(aspose.pdf.forms.TextBoxField):
    '''Field for file select box element.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    ...

class Form:
    '''Class representing form object.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        '''Gets field of the form by field index.
        
        :param index: Index of the field.
        :returns: Retreived field.'''
        ...
    
    @overload
    def delete(self, field: aspose.pdf.forms.Field) -> None:
        '''Delete field from the form.
        
        :param field: Field which must be deleted.'''
        ...
    
    @overload
    def delete(self, field_name: str) -> None:
        '''Deletes field from the form by its name.
        
        :param field_name: Name of the filed which must be deleted.'''
        ...
    
    @overload
    def add(self, field: aspose.pdf.forms.Field, page_number: int) -> None:
        '''Adds field on the form.
        
        :param field: Field which must be added.
        :param page_number: Page index where added field will be placed.'''
        ...
    
    @overload
    def add(self, field: aspose.pdf.forms.Field) -> None:
        '''Adds field on the form.
        
        :param field: Field which must be added.'''
        ...
    
    @overload
    def add(self, field: aspose.pdf.forms.Field, partial_name: str, page_number: int) -> aspose.pdf.forms.Field:
        '''Adds new field to the form; If this field is already placed on other or this form, the copy of field is created.
        
        :param field: Field name.
        :param partial_name: Name of field on the form.
        :param page_number: Page number where field will be added.
        :returns: Added field returned. If copy of the field was created it will be returned.'''
        ...
    
    @overload
    def has_field(self, field: aspose.pdf.forms.Field) -> bool:
        '''Check if the form already has specified field.
        
        :param field: Field to check.
        :returns: ``True`` if the specified field name added to Form; otherwise, ``False``.'''
        ...
    
    @overload
    def has_field(self, field_name: str) -> bool:
        '''Determines if the field with specified name already added to the Form.
        
        :param field_name: PartialName of the field.
        :returns: ``True`` if the specified field name added to Form; otherwise, ``False``.'''
        ...
    
    @overload
    def has_field(self, field_name: str, search_children: bool) -> bool:
        '''Determines if the field with specified name already added to the Form, with ability to look into children hierarchy of fields.
        
        :param field_name: :attr:`Field.partial_name` or :attr:`aspose.pdf.annotations.Annotation.full_name` of the field.
        :param search_children: When set to true the whole hierarchy of form fields would be searched for the requested
                                (note that in this case the:attr:`aspose.pdf.annotations.Annotation.full_name` of the required field should be passed as ).
        :returns: True if the specified field name added to Form; otherwise, false.'''
        ...

    @overload
    def export_to_json(self, stream: Any, options: aspose.pdf.engine.io.convertstrategies.converthelpers.ExportFieldsToJsonOptions) -> Iterable[aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult]:
        '''Exports the PDF form fields to JSON format and writes the result to the provided stream.
        
        :param stream: The stream to write the JSON output to.
        :param options: Optional settings for exporting the form fields to JSON.
        :returns: A collection of :class:`aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult` indicating the result of the export operation for each form field.'''
        ...
    
    @overload
    def export_to_json(self, file_name: str, options: aspose.pdf.engine.io.convertstrategies.converthelpers.ExportFieldsToJsonOptions) -> Iterable[aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult]:
        '''Exports the PDF form fields to JSON format and writes the result to the specified file.
        
        :param file_name: The name of the file to write the JSON output to.
        :param options: Optional settings for exporting the form fields to JSON.
        :returns: A collection of :class:`aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult` indicating the result of the export operation for each form field.'''
        ...
    
    @overload
    def import_from_json(self, stream: Any) -> Iterable[aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult]:
        '''Imports the PDF form fields from JSON format provided in the stream.
        
        :param stream: The stream to read the JSON input from.
        :returns: A collection of :class:`aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult` indicating the result of the import operation for each form field.'''
        ...
    
    @overload
    def import_from_json(self, file_name: str) -> Iterable[aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult]:
        '''Imports the PDF form fields from JSON format provided in the specified file.
        
        :param file_name: The name of the file to read the JSON input from.
        :returns: A collection of :class:`aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult` indicating the result of the import operation for each form field.'''
        ...

    def copy_to(self, array: list[aspose.pdf.forms.Field], index: int) -> None:
        '''Copies fields placed on the form into array.
        
        :param array: Array where fields must be placed.
        :param index: Starting index.'''
        ...
    
    def flatten(self) -> None:
        '''Removes all form fields and place their values directly on the page.'''
        ...
    
    def add_field_appearance(self, field: aspose.pdf.forms.Field, page_number: int, rect: aspose.pdf.Rectangle) -> None:
        '''Adds additional appearance of the field to specified page of the document in the specified location.
        
        :param field: Field which appearance should be added on form.
        :param page_number: Number of the page where field must be placed.
        :param rect: Rectangle where field will be placed.'''
        ...
    
    def remove_field_appearance(self, field: aspose.pdf.forms.Field, appearance_index: int) -> None:
        '''Removes appearance of the field at specified index.
        If only one child appearance left, method embeds it into the field.
        
        :param field: Field with appearances.
        :param appearance_index: Appearances index.'''
        ...

    def get_fields_in_rect(self, rect: aspose.pdf.Rectangle) -> list[aspose.pdf.forms.Field]:
        '''Returns fields inside of specified rectangle.
        
        :param rect: Rectangle where fields should be found.
        :returns: Array with found fields.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Returns true if object is thread-safe.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Returns synchronization object.'''
        ...
    
    @property
    def auto_recalculate(self) -> bool:
        '''If set, all form fields will be recalculated when any field is changed. Default value is true. Set to false in order to increase performance when filling form with large amount of calculated fields.'''
        ...
    
    @auto_recalculate.setter
    def auto_recalculate(self, value: bool):
        ...
    
    @property
    def auto_restore_form(self) -> bool:
        '''If set, absent form fields will be automatically created if they present in annotations.'''
        ...
    
    @auto_restore_form.setter
    def auto_restore_form(self, value: bool):
        ...
    
    @property
    def default_resources(self) -> aspose.pdf.Resources:
        '''Gets default resources placed on this form.'''
        ...
    
    @property
    def default_appearance(self) -> aspose.pdf.annotations.DefaultAppearance:
        '''Gets or sets default appearance of the form (object which describes default font, text size and color for fields on the form).'''
        ...
    
    @default_appearance.setter
    def default_appearance(self, value: aspose.pdf.annotations.DefaultAppearance):
        ...
    
    @property
    def xfa(self) -> aspose.pdf.forms.XFA:
        '''Gets XFA data of the form (if presents).'''
        ...
    
    @property
    def ignore_needs_rendering(self) -> bool:
        '''If this property is true the value of NeedsRendering key will be ignored during conversion
        XFA form to Standard form. It is false by default.'''
        ...
    
    @ignore_needs_rendering.setter
    def ignore_needs_rendering(self, value: bool):
        ...
    
    @property
    def remove_permission(self) -> bool:
        '''If this property is true the "Perms" dictionary will be removed from the pdf document after conversion
        dynamic documents to standard. The "Perms" dictionary can contain a rules that disturb displaying selection of
        mandatory fields in Adobe Acrobat reader.
        It is false by default.'''
        ...
    
    @remove_permission.setter
    def remove_permission(self, value: bool):
        ...
    
    @property
    def emulate_requierd_groups(self) -> bool:
        '''If this property is true then additional red boundary rectangles will be drawn for required Xfa exclGroup elements containers
        This property was introduced because absences of analogues for the exclGroup during conversion Xfa representation of forms
        to standard.
        It is false by default.'''
        ...
    
    @emulate_requierd_groups.setter
    def emulate_requierd_groups(self, value: bool):
        ...
    
    @property
    def type(self) -> aspose.pdf.forms.FormType:
        '''Gets type of the form. Possible values are: Standard, Static, Dynamic.'''
        ...
    
    @type.setter
    def type(self, value: aspose.pdf.forms.FormType):
        ...
    
    @property
    def fields(self) -> list[aspose.pdf.forms.Field]:
        '''Gets list of all fields in lowest level of hierarhical form.'''
        ...
    
    @property
    def signatures_exist(self) -> bool:
        '''If set, the document contains at least one signature field.'''
        ...
    
    @signatures_exist.setter
    def signatures_exist(self, value: bool):
        ...
    
    @property
    def signatures_append_only(self) -> bool:
        '''If set, the document contains signatures that may be invalidated if the file is saved (written) in a way that alters its previous contents,
        as opposed to an incremental update.'''
        ...
    
    @signatures_append_only.setter
    def signatures_append_only(self, value: bool):
        ...
    
    @property
    def sign_dependent_elements_rendering_mode_when_converted(self) -> None:
        '''Forms can contain signing information, i.e. can be signed or unsigned.
        And form's view sometimes must depend on whether form is signed or not.
        This property tells to form's converter (f.e. during conversion XFA form to Standard form)
        whether result form must be rendered as signed or as unsigned.'''
        ...
    
    @sign_dependent_elements_rendering_mode_when_converted.setter
    def sign_dependent_elements_rendering_mode_when_converted(self, value: None):
        ...

    class FlattenSettings:
          '''Class which describes settings for Form flattening procedure.'''

          @property
          def update_appearances(self) -> bool:
              '''If set, all field appearances will be regenerated before flattening. This option may help if field is incorrectly flattened.
                 This option may decrease performance. By default set to false.''' 
              ...
    
          @update_appearances.setter
          def update_appearances(self, value: bool):
              ...

          @property
          def call_events(self) -> bool:
              '''If set, formatting and other JavaScript events will be called. True by default.''' 
              ...
    
          @call_events.setter
          def call_events(self, value: bool):
              ...
          
          @property
          def hide_buttons(self) -> bool:
              '''If set, buttons will be removed from flattened document. False by default.''' 
              ...
    
          @hide_buttons.setter
          def hide_buttons(self, value: bool):
              ...

          @property
          def apply_redactions(self) -> bool:
              '''If true, redaction specified Redaction annotation will be applied.''' 
              ...
    
          @apply_redactions.setter
          def apply_redactions(self, value: bool):
              ...
          
    class SignDependentElementsRenderingModes:
          '''Forms can contain signing information and can be signed or unsigned.
          Sometimes view of forms in viewer must depend on whether form is signed or not.
          This enum enumerates possible rendering modes during convertion of form type in regard to sign. '''

          RENDER_FORM_AS_UNSIGNED: SignDependentElementsRenderingModes
          RENDER_FORM_AS_SIGNED: SignDependentElementsRenderingModes

    ...

class IconFit:
    '''Describes how the widget annotation's icon shall be displayed within its annotation rectangle.'''
    
    @staticmethod
    def name_to_scaling_reason(self, reason: str) -> aspose.pdf.forms.ScalingReason:
        '''Converts name of scaling reason into ScalingReason object.
        
        :param reason: Name of scaling reason.
        :returns: Scaling reason object.'''
        ...
    
    @staticmethod
    def scaling_reason_to_name(self, reason: aspose.pdf.forms.ScalingReason) -> str:
        '''Converts scaling reason obejct to name.
        
        :param reason: Scaling reason object to be converted.
        :returns: Name of scaling reasong.'''
        ...
    
    @staticmethod
    def name_to_scaling_mode(self, mode: str) -> aspose.pdf.forms.ScalingMode:
        '''Converts scaling mode name into ScalingMode object.
        
        :param mode: Scaling mode name.
        :returns: Scaling mode object.'''
        ...
    
    @staticmethod
    def scaling_mode_to_name(self, mode: aspose.pdf.forms.ScalingMode) -> str:
        '''Converts scaling mode object into name.
        
        :param mode: Scaling mode object.
        :returns: Scaling mode name.'''
        ...
    
    @property
    def scaling_reason(self) -> aspose.pdf.forms.ScalingReason:
        '''Gets or sets scaling reason.'''
        ...
    
    @scaling_reason.setter
    def scaling_reason(self, value: aspose.pdf.forms.ScalingReason):
        ...
    
    @property
    def scaling_mode(self) -> aspose.pdf.forms.ScalingMode:
        '''The type of scaling that shall be used.        ///'''
        ...
    
    @scaling_mode.setter
    def scaling_mode(self, value: aspose.pdf.forms.ScalingMode):
        ...
    
    @property
    def leftover_left(self) -> float:
        '''Gets or sets space to allocate at the left of the icon.'''
        ...
    
    @leftover_left.setter
    def leftover_left(self, value: float):
        ...
    
    @property
    def leftover_bottom(self) -> float:
        '''Gets or sets space to allocate at the bottom of the icon.'''
        ...
    
    @leftover_bottom.setter
    def leftover_bottom(self, value: float):
        ...
    
    @property
    def spread_on_border(self) -> bool:
        '''If true, indicates that the button appearance shall be scaled to fit fully within the bounds of the annotation without taking into consideration the line width of the border.'''
        ...
    
    @spread_on_border.setter
    def spread_on_border(self, value: bool):
        ...
    
    ...

class ListBoxField(aspose.pdf.forms.ChoiceField):
    '''Class represents ListBox field.'''
    
    @overload
    def __init__(self):
        '''Constructor for ListBoxField to be used in Generator.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new ListBox field.
        
        :param page: Page where list box will be placed.
        :param rect: Rectangle where list box will be placed on the page.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, rect: aspose.pdf.Rectangle):
        '''Constructor for ListBox field.
        
        :param doc: Document to which this field will belong.
        :param rect: Rectangle where list box will be placed.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @property
    def selected(self) -> int:
        '''Gets or sets index of the selected item. Items are numbered from 1.'''
        ...
    
    @selected.setter
    def selected(self, value: int):
        ...
    
    @property
    def selected_items(self) -> list[int]:
        '''Gets or sets array of the selected items in the multiselect list. For single-select list returns array with single item.'''
        ...
    
    @selected_items.setter
    def selected_items(self, value: list[int]):
        ...
    
    @property
    def top_index(self) -> int:
        '''Gets or sets index of the top visible element of the list.'''
        ...
    
    @top_index.setter
    def top_index(self, value: int):
        ...
    
    ...

class NumberField(aspose.pdf.forms.TextBoxField):
    '''Text Field with specified valid chars'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`NumberField` class.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Initializes a new instance of the :class:`NumberField` class.
        
        :param page: Page where text field is placed.
        :param rect: Rectangle where the field will be placed on the page.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, rect: aspose.pdf.Rectangle):
        '''Initializes a new instance of the :class:`NumberField` class.
        
        :param doc: Document where field will be created.
        :param rect: Rectangle of the field.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @property
    def allowed_chars(self) -> str:
        '''Gets or sets the allowed chars.'''
        ...
    
    @allowed_chars.setter
    def allowed_chars(self, value: str):
        ...
    
    ...

class Option:
    '''Class represents option of choice field.'''
    
    @property
    def value(self) -> str:
        '''Gets or sets option export value.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets name of option.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def selected(self) -> bool:
        '''Gets or sets selected status of option. Returns true if option is selected.'''
        ...
    
    @selected.setter
    def selected(self, value: bool):
        ...
    
    @property
    def index(self) -> int:
        '''Gets index of the option.'''
        ...
    
    ...

class OptionCollection:
    '''Class representing collection of options of the choice field.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.forms.Option:
        '''Gets option by index.
        
        :param index: Index of the option.
        :returns: Option on the specified index.'''
        ...
    
    @overload
    def get(self, index: int) -> aspose.pdf.forms.Option:
        '''Gets option by index.
        
        :param index: Option index. Index should be in range [1..n] where n is options count.
        :returns: Retreived option.'''
        ...
    
    @overload
    def get(self, name: str) -> aspose.pdf.forms.Option:
        '''Gets option from colleciton by option name.
        
        :param name: Option name.
        :returns: Retreived option.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Returns true of object is synchronized.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Synchronization object of the collection.'''
        ...
    
    ...

class PKCS1(aspose.pdf.forms.Signature):
    '''Represents signature object regarding PKCS#1 standard.
    RSA encryption algorithm and SHA-1 digest method are used for signing.'''
    
    @overload
    def __init__(self, image: Any):
        '''Initializes new instance of the :class:`PKCS1` class.
        
        :param image: This image will define signature appearance on the page.'''
        ...
    
    @overload
    def __init__(self):
        '''Inititalizes new instance of the :class:`PKCS1` class.'''
        ...
    
    @overload
    def __init__(self, pfx: str, password: str):
        '''Inititalizes new instance of the :class:`PKCS1` class.
        
        :param pfx: Pfx file which contains certificate for signing.
        :param password: Password for certificate. Password to get access to the private key in the certificate.'''
        ...
    
    @overload
    def __init__(self, pfx: Any, password: str):
        '''Inititalizes new instance of the :class:`PKCS1` class.
        
        :param pfx: Stream with certificate data organized as pfx.
        :param password: Password to get access to the private key in the certificate.'''
        ...
    
    ...

class PKCS7(aspose.pdf.forms.Signature):
    '''Represents the PKCS#7 object that conform to the PKCS#7 specification in Internet RFC 2315,
    PKCS #7: Cryptographic Message Syntax, Version 1.5.
    The SHA1 digest of the document's byte range is encapsulated in the PKCS#7 SignedData field.'''
    
    @overload
    def __init__(self):
        '''Inititalizes new instance of the :class:`PKCS7` class.'''
        ...
    
    @overload
    def __init__(self, pfx: str, password: str):
        '''Inititalizes new instance of the :class:`PKCS7` class.
        
        :param pfx: Pfx file which contains certificate for signing.
        :param password: Password for certificate. Password to get access to the private key in the certificate.'''
        ...
    
    @overload
    def __init__(self, pfx: Any, password: str):
        '''Inititalizes new instance of the :class:`PKCS7` class.
        
        :param pfx: Stream with certificate data organized as pfx.
        :param password: Password to get access to the private key in the certificate.'''
        ...
    
    ...

class PKCS7Detached(aspose.pdf.forms.Signature):
    '''Represents the PKCS#7 object that conform to the PKCS#7 specification in Internet RFC 2315,
    PKCS #7: Cryptographic Message Syntax, Version 1.5.
    The original signed message digest over the document's byte range is incorporated as the normal PKCS#7 SignedData field.
    No data shall is encapsulated in the PKCS#7 SignedData field.'''
    
    @overload
    def __init__(self, image: Any):
        '''Initializes new instance of the :class:`PKCS7Detached` class.
        
        :param image: This image will define signature appearance on the page.'''
        ...
    
    @overload
    def __init__(self):
        '''Inititalizes new instance of the :class:`PKCS7Detached` class.'''
        ...
    
    @overload
    def __init__(self, pfx: str, password: str):
        '''Inititalizes new instance of the :class:`PKCS7Detached` class.
        
        :param pfx: Pfx file which contains certificate for signing.
        :param password: Password to get access to the private key in the certificate.'''
        ...
    
    @overload
    def __init__(self, pfx: Any, password: str):
        '''Inititalizes new instance of the :class:`PKCS7Detached` class.
        
        :param pfx: Stream with certificate data organized as pfx.
        :param password: Password to get access to the private key in the certificate.'''
        ...
    
    ...

class PasswordBoxField(aspose.pdf.forms.TextBoxField):
    '''Class descibes text field for entering password.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    ...

class RadioButtonField(aspose.pdf.forms.ChoiceField):
    '''Class representing radio button field.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page):
        '''Constructor for RadiouttonField
        
        :param page: Page where radio button will be placed.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document):
        '''Constructor for RadioButtonField.
        
        :param doc: Document where radio button will be created.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @overload
    def add_option(self, option_name: str, rect: aspose.pdf.Rectangle) -> None:
        '''Add  to radio button option with specifed rectangle.
        
        :param option_name: Name of new option.
        :param rect: New item rectangle.'''
        ...
    
    @overload
    def add_option(self, option_name: str) -> None:
        '''Add option to radion button.
        
        :param option_name: Name of the option which will be added.'''
        ...
    
    def set_position(self, point: aspose.pdf.Point) -> None:
        '''Move all subitems of radio button to specified positins on the page.
        
        :param point: Sets position of RadioButton field annotations.'''
        ...
    
    def add(self, new_item: aspose.pdf.forms.RadioButtonOptionField) -> None:
        '''Adds new option field to RadioButton field
        
        :param new_item: Item which should be added.'''
        ...
    
    @property
    def page_index(self) -> int:
        '''Gets index of page which contains this RadioButton field.'''
        ...
    
    @property
    def value(self) -> str:
        '''Gets or sets value of field.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    @property
    def selected(self) -> int:
        '''Gets or sets index of selected item. Numbering of items is started from 1.'''
        ...
    
    @selected.setter
    def selected(self, value: int):
        ...
    
    @property
    def options(self) -> aspose.pdf.forms.OptionCollection:
        '''Gets collection of options of the radio button.'''
        ...
    
    @property
    def style(self) -> aspose.pdf.forms.BoxStyle:
        '''Style of field box.'''
        ...
    
    @style.setter
    def style(self, value: aspose.pdf.forms.BoxStyle):
        ...
    
    @property
    def no_toggle_to_off(self) -> bool:
        '''Get or sets the flag that allows the radiobutton to have no selected value. If true, exactly one
        radio button shall be selected at all times; selecting the currently selected button has no effect. If false,
        clicking the selected button deselects it, leaving no button selected.
        
        Some PDF readers (including Adobe Acrobat) may ignore the false state of the flag.'''
        ...
    
    @no_toggle_to_off.setter
    def no_toggle_to_off(self, value: bool):
        ...

    ...

class RadioButtonOptionField(aspose.pdf.forms.Field):
    '''Class represents item of RadioButton field.'''
    
    @overload
    def __init__(self):
        '''Create new RadioButtonOptionField instance.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates radiobutton in the specified recangle on specified page.
        
        :param page: Page where RadioButton will be placed;
        :param rect: Recangle of RadioButton.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @property
    def option_name(self) -> str:
        '''Gets or sets name of the option.'''
        ...
    
    @option_name.setter
    def option_name(self, value: str):
        ...
    
    @property
    def caption(self) -> aspose.pdf.text.TextFragment:
        '''Gets or sets caption.'''
        ...
    
    @caption.setter
    def caption(self, value: aspose.pdf.text.TextFragment):
        ...
    
    @property
    def style(self) -> aspose.pdf.forms.BoxStyle:
        '''Gets or sets style of check box.'''
        ...
    
    @style.setter
    def style(self, value: aspose.pdf.forms.BoxStyle):
        ...
    
    ...

class RichTextBoxField(aspose.pdf.forms.TextBoxField):
    '''Class describes rich text editor component.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Constructor for Rich Text Box  field.
        
        :param page: Page where field will be placed.
        :param rect: Position of the field on the page.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @property
    def value(self) -> str:
        '''Value of RichTextField.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    @property
    def style(self) -> str:
        '''Gets or sets default style string of the rich text field.'''
        ...
    
    @style.setter
    def style(self, value: str):
        ...
    
    @property
    def rich_text_value(self) -> str:
        '''Gets or sets rich text value.'''
        ...
    
    @rich_text_value.setter
    def rich_text_value(self, value: str):
        ...
    
    @property
    def formatted_value(self) -> str:
        '''Gets or sets formatted rich text value with markup.'''
        ...
    
    @formatted_value.setter
    def formatted_value(self, value: str):
        ...
    
    @property
    def justify(self) -> aspose.pdf.annotations.Justification:
        '''Gets or sets justification of the rich text box.'''
        ...
    
    @justify.setter
    def justify(self, value: aspose.pdf.annotations.Justification):
        ...
    
    ...

class Signature:
    '''An abstract class which represents signature object in the pdf document.
    Signatures are fields with values of signature objects, the last contain data which is used to
    verify the document validity.'''
    
    def verify(self) -> bool:
        '''Verify the document regarding this signature and return true if document is valid
        or otherwise false.
        
        :returns: true if document is valid.'''
        ...
    
    @property
    def custom_appearance(self) -> aspose.pdf.forms.SignatureCustomAppearance:
        '''Gets/sets the custom appearance.'''
        ...
    
    @custom_appearance.setter
    def custom_appearance(self, value: aspose.pdf.forms.SignatureCustomAppearance):
        ...
    
    @property
    def authority(self) -> str:
        '''The name of the person or authority signing the document.'''
        ...
    
    @authority.setter
    def authority(self, value: str):
        ...
    
    @property
    def date(self) -> datetime.datetime:
        '''The time of signing.'''
        ...
    
    @date.setter
    def date(self, value: datetime.datetime):
        ...
    
    @property
    def location(self) -> str:
        '''The CPU host name or physical location of the signing.'''
        ...
    
    @location.setter
    def location(self, value: str):
        ...
    
    @property
    def reason(self) -> str:
        '''The reason for the signing, such as (I agreeРІР‚В¦).'''
        ...
    
    @reason.setter
    def reason(self, value: str):
        ...
    
    @property
    def contact_info(self) -> str:
        '''Information provided by the signer to enable a recipient to contact the signer
        to verify the signature, e.g. a phone number.'''
        ...
    
    @contact_info.setter
    def contact_info(self, value: str):
        ...
    
    @property
    def byte_range(self) -> list[int]:
        '''An array of pairs of integers (starting byte offset, length in bytes)
        that shall describe the exact byte range for the digest calculation.'''
        ...
    
    @property
    def timestamp_settings(self) -> aspose.pdf.TimestampSettings:
        '''Gets/sets timestamp settings.'''
        ...
    
    @timestamp_settings.setter
    def timestamp_settings(self, value: aspose.pdf.TimestampSettings):
        ...
    
    @property
    def ocsp_settings(self) -> aspose.pdf.OcspSettings:
        '''Gets/sets ocsp settings.'''
        ...
    
    @ocsp_settings.setter
    def ocsp_settings(self, value: aspose.pdf.OcspSettings):
        ...
    
    @property
    def use_ltv(self) -> bool:
        '''Gets/sets ltv validation flag.'''
        ...
    
    @use_ltv.setter
    def use_ltv(self, value: bool):
        ...
    
    @property
    def show_properties(self) -> bool:
        '''Force to show/hide signature properties.
        In case ShowProperties is true signature field has predefined format of appearance (strings to represent):
        -------------------------------------------
        Digitally signed by {certificate subject}
        Date: {signature.Date}
        Reason: {signature.Reason}
        Location: {signature.Location}
        -------------------------------------------
        where {X} is placeholder for X value. Also signature can have image, in this case listed strings are placed over image.
        ShowProperties is true by default.'''
        ...
    
    @show_properties.setter
    def show_properties(self, value: bool):
        ...
    
    ...

class SignatureCustomAppearance:
    '''An abstract class which represents signature custon appearance object.'''
    
    def __init__(self):
        ...
    
    @property
    def font_family_name(self) -> str:
        '''Gets/sets font family name. It should be existed in the document. Default value: Arial.'''
        ...
    
    @font_family_name.setter
    def font_family_name(self, value: str):
        ...
    
    @property
    def font_size(self) -> float:
        '''Gets/sets font size. Default value: 10.'''
        ...
    
    @font_size.setter
    def font_size(self, value: float):
        ...
    
    @property
    def foreground_color(self) -> aspose.pdf.Color:
        '''Gets/sets foreground color (color of text). Default value: Blue.'''
        ...
    
    @foreground_color.setter
    def foreground_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def background_color(self) -> aspose.pdf.Color:
        '''Gets/sets background color. Default value: Transparent.'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def show_contact_info(self) -> bool:
        '''Gets/sets contact info visibility. Default value: true.'''
        ...
    
    @show_contact_info.setter
    def show_contact_info(self, value: bool):
        ...
    
    @property
    def show_reason(self) -> bool:
        '''Gets/sets reason visibility. Default value: true.'''
        ...
    
    @show_reason.setter
    def show_reason(self, value: bool):
        ...
    
    @property
    def show_location(self) -> bool:
        '''Gets/sets location visibility. Default value: true.'''
        ...
    
    @show_location.setter
    def show_location(self, value: bool):
        ...
    
    @property
    def contact_info_label(self) -> str:
        '''Gets/sets contact info label. Default value: "Contact".'''
        ...
    
    @contact_info_label.setter
    def contact_info_label(self, value: str):
        ...
    
    @property
    def reason_label(self) -> str:
        '''Gets/sets reason label. Default value: "Reason".'''
        ...
    
    @reason_label.setter
    def reason_label(self, value: str):
        ...
    
    @property
    def location_label(self) -> str:
        '''Gets/sets location label. Default value: "Location".'''
        ...
    
    @location_label.setter
    def location_label(self, value: str):
        ...
    
    @property
    def digital_signed_label(self) -> str:
        '''Gets/sets digital signed label. Default value: "Digitally signed by".'''
        ...
    
    @digital_signed_label.setter
    def digital_signed_label(self, value: str):
        ...
    
    @property
    def use_digital_subject_format(self) -> bool:
        '''Gets/sets the usage state of the :attr:`SignatureCustomAppearance.digital_subject_format`.'''
        ...
    
    @use_digital_subject_format.setter
    def use_digital_subject_format(self, value: bool):
        ...
    
    @property
    def digital_subject_format(self) -> list[aspose.pdf.forms.SubjectNameElements]:
        '''Gets/sets format for order of elements in Subject string.
        Result examples:
        C=UK, CN=Org, O=Organization
        or
        CN=Org, C=UK, O=Organization
        or
        O=Organization'''
        ...
    
    @digital_subject_format.setter
    def digital_subject_format(self, value: list[aspose.pdf.forms.SubjectNameElements]):
        ...
    
    @property
    def date_signed_at_label(self) -> str:
        '''Gets/sets date signed label. Default value: "Date".'''
        ...
    
    @date_signed_at_label.setter
    def date_signed_at_label(self, value: str):
        ...
    
    @property
    def date_time_local_format(self) -> str:
        '''Gets/sets datetime local format. Default value: "yyyy.MM.dd HH:mm:ss zzz".'''
        ...
    
    @date_time_local_format.setter
    def date_time_local_format(self, value: str):
        ...
    
    @property
    def date_time_format(self) -> str:
        '''Gets/sets datetime format. Default value: "yyyy.MM.dd HH:mm:ss".'''
        ...
    
    @date_time_format.setter
    def date_time_format(self, value: str):
        ...
    
    @property
    def rotation(self) -> aspose.pdf.Rotation:
        '''Gets or sets signature rotation.'''
        ...
    
    @rotation.setter
    def rotation(self, value: aspose.pdf.Rotation):
        ...
    
    ...

class SignatureField(aspose.pdf.forms.Field):
    '''Represents signature form field.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Initializes new instance of the :class:`SignatureField` class.
        
        :param page: Page where signature field should be placed.
        :param rect: Position and size of signature field.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, rect: aspose.pdf.Rectangle):
        '''Initializes new instance of the :class:`SignatureField` class.
        
        :param doc: Page where signature field should be placed.
        :param rect: Position and size of signature field.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    @overload
    def sign(self, signature: aspose.pdf.forms.Signature, pfx: Any, password: str) -> None:
        '''Signs the document using this signature field.
        
        :param signature: Signature object, see :class:`PKCS1`, :class:`PKCS7`, :class:`PKCS7Detached`.
        :param pfx: Stream with certificate.
        :param password: Password to access private in the pfx.'''
        ...
    
    @overload
    def sign(self, signature: aspose.pdf.forms.Signature) -> None:
        '''Sign the document using this signature field.
        
        :param signature: Signature object, see :class:`PKCS1`, :class:`PKCS7` and :class:`PKCS7Detached`.'''
        ...
    
    @overload
    def extract_image(self) -> Any:
        '''Extracts signature's image as jpeg encoded stream.
        
        :returns: If image was successfully found than returns jpeg encoded stream object; otherwise, null.'''
        ...
    
    @overload
    def extract_image(self, format: aspose.pydrawing.Imaging.ImageFormat) -> Any:
        '''Extracts signature's image as encoded stream.
        
        :param format: Image format for encoding.
        :returns: If image was successfully found than returns encodedstream object; otherwise, null.'''
        ...
    
    def extract_certificate(self) -> Any:
        '''Extracts the single X.509 certificate in DER format as a stream.
        
        :returns: If certificate was found returns X.509 single certificate; otherwise, null.'''
        ...
    
    @property
    def signature(self) -> aspose.pdf.forms.Signature:
        '''Gets signature object.
        This object contains signature data regarding public-key cryptographic standards.
        Classes :class:`PKCS1`, :class:`PKCS7` and :class:`PKCS7Detached`
        represent all supported types of signature objects.'''
        ...
    
    ...

class TextBoxField(aspose.pdf.forms.Field):
    '''Class representing text box field.'''
    
    @overload
    def __init__(self, doc: aspose.pdf.Document):
        '''Constructor which should be used with Generator.
        
        :param doc: Document where field will be created.'''
        ...
    
    @overload
    def __init__(self):
        '''Create instance of TextBoxField.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Constructor of TextBox field.
        
        :param page: Page where text field is placed.
        :param rect: Rectangle where the text field will be placed on the page.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, rect: aspose.pdf.Rectangle):
        '''Constructor of TextBox field.
        
        :param doc: Document where field will be created.
        :param rect: Rectangle of the field.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.WidgetAnnotation:
        ...
    
    def add_image(self, image: aspose.pydrawing.Image) -> None:
        '''Adds image into the field resources and draws it.
        
        :param image: Image to add into text field.'''
        ...
    
    def add_barcode(self, code: str) -> None:
        '''Adds barcode 128 into the field.
        Field value will be changed onto the code and field become read only.
        
        :param code: The text to generate barcode 128.'''
        ...
    
    @property
    def value(self) -> str:
        '''Gets or sets value of the field.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    @property
    def multiline(self) -> bool:
        '''Gets or sets multiline flag of the field. If Multiline is true field can contain multiple lines of text.'''
        ...
    
    @multiline.setter
    def multiline(self, value: bool):
        ...
    
    @property
    def spell_check(self) -> bool:
        '''Gets or sets spellcheck flag for field. If true field shall be spell checked.'''
        ...
    
    @spell_check.setter
    def spell_check(self, value: bool):
        ...
    
    @property
    def scrollable(self) -> bool:
        '''Gets or sets scrollable flag of field. If true field can be scrolled.'''
        ...
    
    @scrollable.setter
    def scrollable(self, value: bool):
        ...
    
    @property
    def force_combs(self) -> bool:
        '''Gets or sets flag which indicates is field divided into spaced positions.'''
        ...
    
    @force_combs.setter
    def force_combs(self, value: bool):
        ...
    
    @property
    def max_len(self) -> int:
        '''Gets or sets maximum length of text in the field.'''
        ...
    
    @max_len.setter
    def max_len(self, value: int):
        ...
    
    @property
    def text_vertical_alignment(self) -> aspose.pdf.VerticalAlignment:
        '''Gets or sets text vertical alignment for annotation.'''
        ...
    
    @text_vertical_alignment.setter
    def text_vertical_alignment(self, value: aspose.pdf.VerticalAlignment):
        ...
    
    ...

class XFA:
    '''Represents XML form regarding XML Forms Architecture (XFA).'''
    
    def set_field_image(self, field_name: str, image: Any) -> None:
        '''Sets image for XFA field.
        
        :param field_name: Name of the field.
        :param image: Stream which contains image.'''
        ...
    
    @property
    def field_names(self) -> list[str]:
        '''List of field names in the form template.'''
        ...
    
    ...

class BoxStyle:
    '''Represents styles of check box.'''
    
    CIRCLE: BoxStyle
    CHECK: BoxStyle
    CROSS: BoxStyle
    DIAMOND: BoxStyle
    SQUARE: BoxStyle
    STAR: BoxStyle

class DocMDPAccessPermissions:
    '''The access permissions granted for this document.
    Valid values are:
    1 - No changes to the document are permitted; any change to the document invalidates the signature.
    2 - Permitted changes are filling in forms, instantiating page templates, and signing; other changes invalidate the signature.
    3 - Permitted changes are the same as for 2, as well as annotation creation, deletion, and modification; other changes invalidate the signature.'''
    
    NO_CHANGES: DocMDPAccessPermissions
    FILLING_IN_FORMS: DocMDPAccessPermissions
    ANNOTATION_MODIFICATION: DocMDPAccessPermissions

class FormType:
    '''Enumeration of posible types of Acro Form.'''
    
    STANDARD: FormType
    STATIC: FormType
    DYNAMIC: FormType

class IconCaptionPosition:
    '''Describes position of icon.'''
    
    NO_ICON: IconCaptionPosition
    NO_CAPTION: IconCaptionPosition
    CAPTION_BELOW_ICON: IconCaptionPosition
    CAPTION_ABOVE_ICON: IconCaptionPosition
    CAPTION_TO_THE_RIGHT: IconCaptionPosition
    CAPTION_TO_THE_LEFT: IconCaptionPosition
    CAPTION_OVERLAID: IconCaptionPosition

class ScalingMode:
    '''The type of scaling that shall be used.'''
    
    PROPORTIONAL: ScalingMode
    ANAMORPHIC: ScalingMode

class ScalingReason:
    '''The circumstances under which the icon shall be scaled inside the annotation rectangle.'''
    
    ALWAYS: ScalingReason
    ICON_IS_BIGGER: ScalingReason
    ICON_IS_SMALLER: ScalingReason
    NEVER: ScalingReason

class SubjectNameElements:
    '''Enumeration describes elements in signature subject string.'''
    
    CN: SubjectNameElements
    O: SubjectNameElements
    L: SubjectNameElements
    OU: SubjectNameElements
    S: SubjectNameElements
    C: SubjectNameElements
    E: SubjectNameElements

class Symbology:
    '''A (Barcode) Symbology defines the technical details of a particular type of barcode:
    the width of the bars, character set, method of encoding, checksum specifications, etc.'''
    
    PDF417: Symbology
    QR_CODE: Symbology
    DATA_MATRIX: Symbology

