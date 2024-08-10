import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class AlignmentType:
    '''Class contains possibly alignment types.'''
    
    def __init__(self, name: str):
        '''Constructor of AlignmentType.
        
        :param name: Alignment type name.'''
        ...
    
    center: aspose.pdf.facades.AlignmentType
    
    left: aspose.pdf.facades.AlignmentType
    
    right: aspose.pdf.facades.AlignmentType
    
    ...

class AutoFiller:
    '''Represents a class to receive data from database or other datasource, fills them into the designed fields of the template pdf and at last generates new pdf file or stream.
    It has two template file input modes:input as a stream or a pdf file.
    It has four types of output modes:one merged stream, one merged file, many small streams, many small files.
    It can recieve literal data contained in a System.Data.DataTable.'''
    
    def __init__(self):
        ...
    
    @overload
    def save(self) -> None:
        '''Saves all the pdfs.'''
        ...
    
    @overload
    def save(self, dest_file: str) -> None:
        '''Saves all the pdfs.
        
        :param dest_file: Output file name.'''
        ...
    
    @overload
    def save(self, dest_stream: Any) -> None:
        '''Saves all the pdfs.
        
        :param dest_stream: Output stream.'''
        ...
    
    @overload
    def bind_pdf(self, src_file: str) -> None:
        '''Binds a Pdf file.
        
        :param src_file: Pdf file name.'''
        ...
    
    @overload
    def bind_pdf(self, src_stream: Any) -> None:
        '''Binds a Pdf file.
        
        :param src_stream: Pdf file stream.'''
        ...
    
    @overload
    def bind_pdf(self, src_doc: aspose.pdf.Document) -> None:
        '''Binds a Pdf document.
        
        :param src_doc: Pdf document.'''
        ...
    
    def close(self) -> None:
        '''Closes the object and output streams.'''
        ...
    
    @property
    def output_stream(self) -> Any:
        '''Gets or sets the OutputStream. One of four output modes. Its classical use case is Response.OutputStream.
        Please refer to the online demo.'''
        ...
    
    @output_stream.setter
    def output_stream(self, value: Any):
        ...
    
    @property
    def output_streams(self) -> list[Any]:
        '''Gets or sets the many Output Streams. One of four output modes.'''
        ...
    
    @output_streams.setter
    def output_streams(self, value: list[Any]):
        ...
    
    @property
    def input_stream(self) -> Any:
        '''Gets or sets the input template stream. One of two input modes.'''
        ...
    
    @input_stream.setter
    def input_stream(self, value: Any):
        ...
    
    @property
    def input_file_name(self) -> str:
        '''Gets or sets the input template file. One of two input modes.'''
        ...
    
    @input_file_name.setter
    def input_file_name(self, value: str):
        ...
    
    @property
    def output_file_name(self) -> str:
        '''Gets or sets the one big merged output file. One of the four output modes.'''
        ...
    
    @output_file_name.setter
    def output_file_name(self, value: str):
        ...
    
    @property
    def generating_path(self) -> str:
        '''Gets or sets the Generating Path of the small pdf files if many small pdf files to be generated. It works with another property :attr:`AutoFiller.basic_file_name` BasicFileName.
        One of the four output modes.'''
        ...
    
    @generating_path.setter
    def generating_path(self, value: str):
        ...
    
    @property
    def basic_file_name(self) -> str:
        '''Gets or sets the basic file name if many small files will be generated. The generated file will be like "BasicFileName0","BasicFileName1",...
        It works with another property :attr:`AutoFiller.generating_path` GeneratingPath.'''
        ...
    
    @basic_file_name.setter
    def basic_file_name(self, value: str):
        ...
    
    ...

class BDCProperties:
    '''BDC operator properties.'''
    
    @overload
    def __init__(self, mcid: int, lang: str, expansion_text: str):
        ...
    
    @overload
    def __init__(self, lang: str, expansion_text: str):
        '''Constructor for properties of BDC operator.
        
        :param lang: Lang tag.
        :param expansion_text: Expansion text.'''
        ...

    @property
    def mcid(self) -> int:
        '''Gets/sets MCID value.'''
        ...
    
    @mcid.setter
    def mcid(self, value: int):
        ...
    
    @property
    def lang(self) -> str:
        '''Gets/sets Language value.'''
        ...
    
    @lang.setter
    def lang(self, value: str):
        ...
    
    @property
    def e(self) -> str:
        '''Gets/sets Expansion text value.'''
        ...
    
    @e.setter
    def e(self, value: str):
        ...
    
    ...

class Bookmark:
    '''Represents a bookmark.'''
    
    def __init__(self):
        ...
    
    @property
    def action(self) -> str:
        '''Gets or sets the action bound with the bookmark.
        If PageNumber is presented the action can not be specified.
        The action type includes: "GoTo", "GoToR", "Launch", "Named".'''
        ...
    
    @action.setter
    def action(self, value: str):
        ...
    
    @property
    def bold_flag(self) -> bool:
        '''Gets or sets the bold flag of bookmark's title.'''
        ...
    
    @bold_flag.setter
    def bold_flag(self, value: bool):
        ...
    
    @property
    def child_item(self) -> aspose.pdf.facades.Bookmarks:
        '''Gets or sets bookmark's children.'''
        ...
    
    @child_item.setter
    def child_item(self, value: aspose.pdf.facades.Bookmarks):
        ...
    
    @property
    def child_items(self) -> aspose.pdf.facades.Bookmarks:
        '''Gets or sets bookmark's children.'''
        ...
    
    @child_items.setter
    def child_items(self, value: aspose.pdf.facades.Bookmarks):
        ...
    
    @property
    def custom_acorbat_viewer_menu_action_name(self) -> None:
        '''The action name corresponding to execute a menu item in Acrobat viewer.'''
        ...
    
    @custom_acorbat_viewer_menu_action_name.setter
    def custom_acorbat_viewer_menu_action_name(self, value: None):
        ...
    
    @property
    def destination(self) -> str:
        '''Gets or sets bookmark's destination page. Required if action is set as string.Empty.'''
        ...
    
    @destination.setter
    def destination(self, value: str):
        ...
    
    @property
    def italic_flag(self) -> bool:
        '''Gets or sets the italic flag of bookmark's title.'''
        ...
    
    @italic_flag.setter
    def italic_flag(self, value: bool):
        ...
    
    @property
    def level(self) -> int:
        '''Gets or sets bookmark's hierarchy level.'''
        ...
    
    @level.setter
    def level(self, value: int):
        ...
    
    @property
    def page_display(self) -> str:
        '''Gets or sets the type of display bookmark's destination page.'''
        ...
    
    @page_display.setter
    def page_display(self, value: str):
        ...
    
    @property
    def page_display_bottom(self) -> int:
        '''Gets or sets the bottom coordinate of page display.'''
        ...
    
    @page_display_bottom.setter
    def page_display_bottom(self, value: int):
        ...
    
    @property
    def page_display_left(self) -> int:
        '''Gets or sets the left coordinate of page display.'''
        ...
    
    @page_display_left.setter
    def page_display_left(self, value: int):
        ...
    
    @property
    def page_display_right(self) -> int:
        '''Gets or sets the right coordinate of page display.'''
        ...
    
    @page_display_right.setter
    def page_display_right(self, value: int):
        ...
    
    @property
    def page_display_top(self) -> int:
        '''Gets or sets the top coordinate of page display.'''
        ...
    
    @page_display_top.setter
    def page_display_top(self, value: int):
        ...
    
    @property
    def page_display_zoom(self) -> int:
        '''Gets or sets the zoom factor of page display.'''
        ...
    
    @page_display_zoom.setter
    def page_display_zoom(self, value: int):
        ...
    
    @property
    def page_number(self) -> int:
        '''Gets or sets the number of bookmark's destination page.'''
        ...
    
    @page_number.setter
    def page_number(self, value: int):
        ...
    
    @property
    def remote_file(self) -> str:
        '''Gets or sets the file (path) which is required for "GoToR" action of bookmark.'''
        ...
    
    @remote_file.setter
    def remote_file(self, value: str):
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets bookmark's title.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def title_color(self) -> aspose.pydrawing.Color:
        '''Gets or sets the color of bookmark's title.'''
        ...
    
    @title_color.setter
    def title_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def open(self) -> bool:
        '''Gets or sets bookmark state (open, close).'''
        ...
    
    @open.setter
    def open(self, value: bool):
        ...
    
    ...

class Bookmarks:
    '''Represents a collection of :class:`Bookmark` objects.'''
    
    def __init__(self):
        ...
    
    ...

class DocumentPrivilege:
    '''Represents the privileges for accessing Pdf file. Refer to:class:`PdfFileSecurity`.
    There are 4 ways using this class:
    1.Using predefined privilege directly.
    2.Based on a predefined privilege and change some specifical permissions.
    3.Based on a predefined privilege and change some specifical Adobe Professional permissions combination.
    4.Mixes the way2 and way3.'''
    
    def compare_to(self, obj: object) -> int:
        '''Compares two :class:`DocumentPrivilege` objects.
        
        :param obj: The object to compare with.
        :returns: A signed integer that indicates the relative values of this instance and value. Less than zero this instance is less than value.
                  Zero this instance is equal to value. Greater than zero this instance is greater than value.'''
        ...
    
    @property
    def allow_print(self) -> bool:
        '''Sets the permission which allow print or not.
        true is allow and false is forbidden.'''
        ...
    
    @allow_print.setter
    def allow_print(self, value: bool):
        ...
    
    @property
    def allow_degraded_printing(self) -> bool:
        '''Sets the permission which allow degraded printing or not.
        true is allow and false is forbidden.'''
        ...
    
    @allow_degraded_printing.setter
    def allow_degraded_printing(self, value: bool):
        ...
    
    @property
    def allow_modify_contents(self) -> bool:
        '''Sets the permission which allow modify contents or not.
        true is allow and false is forbidden.'''
        ...
    
    @allow_modify_contents.setter
    def allow_modify_contents(self, value: bool):
        ...
    
    @property
    def allow_copy(self) -> bool:
        '''Sets the permission which allow copy or not.
        true is allow and false is forbidden.'''
        ...
    
    @allow_copy.setter
    def allow_copy(self, value: bool):
        ...
    
    @property
    def allow_modify_annotations(self) -> bool:
        '''Sets the permission which allow modify annotations or not.
        true is allow and false is forbidden.'''
        ...
    
    @allow_modify_annotations.setter
    def allow_modify_annotations(self, value: bool):
        ...
    
    @property
    def allow_fill_in(self) -> bool:
        '''Sets the permission which allow fill in forms or not.
        true is allow and false is forbidden.'''
        ...
    
    @allow_fill_in.setter
    def allow_fill_in(self, value: bool):
        ...
    
    @property
    def allow_screen_readers(self) -> bool:
        '''Sets the permission which allow screen readers or not.
        true is allow and false is forbidden.'''
        ...
    
    @allow_screen_readers.setter
    def allow_screen_readers(self, value: bool):
        ...
    
    @property
    def allow_assembly(self) -> bool:
        '''Sets the permission which allow assembly or not.
        true is allow and false is forbidden.'''
        ...
    
    @allow_assembly.setter
    def allow_assembly(self, value: bool):
        ...
    
    degraded_printing: aspose.pdf.facades.DocumentPrivilege
    
    print: aspose.pdf.facades.DocumentPrivilege
    
    modify_contents: aspose.pdf.facades.DocumentPrivilege
    
    copy: aspose.pdf.facades.DocumentPrivilege
    
    modify_annotations: aspose.pdf.facades.DocumentPrivilege
    
    fill_in: aspose.pdf.facades.DocumentPrivilege
    
    screen_readers: aspose.pdf.facades.DocumentPrivilege
    
    assembly: aspose.pdf.facades.DocumentPrivilege
    
    allow_all: aspose.pdf.facades.DocumentPrivilege
    
    forbid_all: aspose.pdf.facades.DocumentPrivilege
    
    ...

class Facade:
    '''Base facade class.'''
    
    @overload
    def bind_pdf(self, src_file: str) -> None:
        '''Initializes the facade.
        
        :param src_file: The PDF file.'''
        ...
    
    @overload
    def bind_pdf(self, src_stream: Any) -> None:
        '''Initializes the facade.
        
        :param src_stream: The stream of PDF file.'''
        ...
    
    @overload
    def bind_pdf(self, src_doc: aspose.pdf.Document) -> None:
        '''Initializes the facade.
        
        :param src_doc: The Aspose.Pdf.Document object.'''
        ...
    
    def close(self) -> None:
        '''Disposes Aspose.Pdf.Document bound with a facade.'''
        ...
    
    @property
    def document(self) -> aspose.pdf.Document:
        '''Gets the document facade is working on.'''
        ...
    
    ...

class FontColor:
    '''Class representing color of the text.'''
    
    @overload
    def __init__(self, r: int, g: int, b: int):
        '''Initializes color with specified color components.
        
        :param r: Red component.
        :param g: Green component.
        :param b: Blue component.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes color.'''
        ...
    
    @property
    def green(self) -> int:
        '''Green component of color.'''
        ...
    
    @green.setter
    def green(self, value: int):
        ...
    
    @property
    def red(self) -> int:
        '''Red component of color.'''
        ...
    
    @red.setter
    def red(self, value: int):
        ...
    
    @property
    def blue(self) -> int:
        '''Blue component of color.'''
        ...
    
    @blue.setter
    def blue(self, value: int):
        ...
    
    ...

class Form(aspose.pdf.facades.SaveableFacade):
    '''Class representing Acro form object.'''
    
    @overload
    def __init__(self, src_stream: Any, dest_stream: Any):
        '''Constructor of Form with two stream parameters.
        Specify same source and destination stream for incremental update.
        
        :param src_stream: Source stream.
        :param dest_stream: Destination stream.'''
        ...
    
    @overload
    def __init__(self):
        '''Construtcor of Form without parameters.'''
        ...
    
    @overload
    def __init__(self, src_file_name: str):
        '''Constructor of Form.
        
        :param src_file_name: Source file path.'''
        ...
    
    @overload
    def __init__(self, src_stream: Any):
        '''Constructor for form.
        
        :param src_stream: source stream.'''
        ...
    
    @overload
    def __init__(self, src_file_name: str, dest_file_name: str):
        '''Constructor of Form class.
        Specify same source file name and destination file name to perform incremental update.
        
        :param src_file_name: Path of the source file.
        :param dest_file_name: Path of the destination file.'''
        ...
    
    @overload
    def __init__(self, src_file_name: str, dest_stream: Any):
        '''Constructor of Form.
        
        :param src_file_name: Source file path.
        :param dest_stream: Destination file path.'''
        ...
    
    @overload
    def __init__(self, src_stream: Any, dest_file_name: str):
        '''Constructor of Form
        
        :param src_stream: Source stream.
        :param dest_file_name: Destination file path.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`Form` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, dest_file_name: str):
        '''Initializes new :class:`Form` object on base of the document.
        
        :param document: Pdf document.
        :param dest_file_name: Path of the destination file.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, dest_stream: Any):
        '''Initializes new :class:`Form` object on base of the document.
        
        :param document: Pdf document.
        :param dest_stream: Destination stream.'''
        ...
    
    @overload
    def save(self) -> None:
        '''Saves the value of the filled fields and close the opened Pdf document.'''
        ...
    
    @overload
    def save(self, dest_file: str) -> None:
        '''Saves document into specified file.
        
        :param dest_file: File where document will be saved.'''
        ...
    
    @overload
    def save(self, dest_stream: Any) -> None:
        '''Saves document into specified stream.
        
        :param dest_stream: Stream where document will be saved.'''
        ...
    
    @overload
    def fill_field(self, field_name: str, field_value: str) -> bool:
        '''Fills the field with a valid value according to a fully qualified field name.
        Before filling the fields, every field's names and its corresponding valid values must be known.
        Both the fields' name and values are case sensitive.
        Please note that Aspose.Pdf.Facades supports only full field names and does not work with partial
        field names in contrast with Aspose.Pdf.Kit;
        For example if field has full name "Form.Subform.TextField" you should specify full name and not "TextField".
        You can use FieldNames property to explore existing field names and search required field by its partial name.
        
        :param field_name: The field's name to be filled.
        :param field_value: The field's value which must be a valid value for some fields.
        :returns: true if field is found and filled successfully.'''
        ...
    
    @overload
    def fill_field(self, field_name: str, index: int) -> bool:
        '''Fills the radio box field with a valid index value according to a fully qualified field name.
        Before filling the fields, only field's name must be known. While the value can be specified by its index.
        Notice: Only be applied to Radio Box, Combo Box and List Box fields.
        Please note that Aspose.Pdf.Facades supports only full field names and does not work with partial
        field names in contrast with Aspose.Pdf.Kit;
        For example if field has full name "Form.Subform.ListBoxField" you should specify full name and not "ListBoxField".
        You can use FieldNames property to explore existing field names and search required field by its partial name.
        
        :param field_name: Name of field to be filled.
        :param index: Index of chosen item.
        :returns: true if field was found and successfully filled.'''
        ...
    
    @overload
    def fill_field(self, field_name: str, be_checked: bool) -> bool:
        '''Fills the check box field with a boolean value.
        Notice: Only be applied to Check Box.
        Please note that Aspose.Pdf.Facades supports only full field names and does not work with partial
        field names in contrast with Aspose.Pdf.Kit;
        For example if field has full name "Form.Subform.CheckBoxField" you should specify full name and not "CheckBoxField".
        You can use FieldNames property to explore existing field names and search required field by its partial name.
        
        :param field_name: The field's name to be filled.
        :param be_checked: A boolean flag: true means to check the box, while false to uncheck it.
        :returns: true if field was found and successfully filled.'''
        ...
    
    @overload
    def fill_field(self, field_name: str, field_values: list[str]) -> None:
        '''Fill a field with multiple selections.Note: only for AcroForm List Box Field.
        
        :param field_name: The fully qualified field name.
        :param field_values: A string array which contains several items to be selected.'''
        ...
    
    @overload
    def fill_field(self, field_name: str, value: str, fit_font_size: bool) -> bool:
        '''Fills field with specified value.
        
        :param field_name: Name of field
        :param value: New value of the field
        :param fit_font_size: If true, the font size in the edit boxes will be fitted.
        :returns: true if field was found and successfully filled.'''
        ...
    
    @overload
    def import_xml(self, input_xml_stream: Any) -> None:
        '''Imports the content of the fields from the xml file and put them into the new pdf.
        
        :param input_xml_stream: Stream from which XML for import is read.'''
        ...
    
    @overload
    def import_xml(self, input_xml_stream: Any, ignore_form_template_changes: bool) -> None:
        '''Imports the content of the fields from the xml file and put them into the new pdf.
        
        :param input_xml_stream: The input xml stream.
        :param ignore_form_template_changes: If this parameter is true then all changes of the XFA form template will not be saved'''
        ...
    
    @overload
    def fill_image_field(self, field_name: str, image_file_name: str) -> None:
        '''Pastes an image onto the existing button field as its appearance according to
        its fully qualified field name.
        
        :param field_name: The fully qualified field name of the image button field.
        :param image_file_name: The path of the image file, relative and absolute are both ok.'''
        ...
    
    @overload
    def fill_image_field(self, field_name: str, image_stream: Any) -> None:
        '''Overloads function of FillImageField.
        The input is a image stream.
        
        :param field_name: The fully qualified field name.
        :param image_stream: The image's stream.'''
        ...
    
    def close(self) -> None:
        '''Closes opened files without any changes.'''
        ...
    
    def get_field_facade(self, field_name: str) -> aspose.pdf.facades.FormFieldFacade:
        '''Returns FrofmFieldFacade object containing all appearance attributes.
        
        :param field_name: Name of field to read.
        :returns: FormFieldFacade object'''
        ...
    
    def fill_fields(self, field_names: list[str], field_values: list[str], output: Any) -> bool:
        '''Fills the text box fields with a text values and save the document.
        Relevant for signed documents.
        Notice: Only be applied to Text Box.
        Both the fields' name and values are case sensitive.
        
        :param field_names: Names of fields.
        :param field_values: New values of the fields.
        :param output: Stream where document will be saved.
        :returns: true if fields was found and successfully filled.'''
        ...
    
    def get_button_option_current_value(self, field_name: str) -> str:
        '''Returns the current value for radio button option fields.
        
        :param field_name: Field Name
        :returns: String value for the current radio group optino. See also Aspose.Pdf.Facades.Form.GetButtonOptionValues(System.String)'''
        ...
    
    def get_field(self, field_name: str) -> str:
        '''Gets the field's value according to its field name.
        
        :param field_name: The fully qualified field name.
        :returns: The field's value.'''
        ...
    
    def get_full_field_name(self, field_name: str) -> str:
        '''Gets the full field name according to its short field name.
        
        :param field_name: The fully qualified field name.
        :returns: The full field name.'''
        ...
    
    def get_field_limit(self, field_name: str) -> int:
        '''Get the limitation of text field.
        
        :param field_name: The qualified field name.
        :returns: Return the limitation number of characters a text field can be filled. It not set, return 0.'''
        ...
    
    def flatten_all_fields(self) -> None:
        '''Flattens all the fields.'''
        ...
    
    def flatten_field(self, field_name: str) -> None:
        '''Flattens a specified field with the fully qualified field name.
        Any other field will remain unchangable. If the fieldName is invalid,
        all the fields will remain unchangable.
        
        :param field_name: The name of the field to be flattened.'''
        ...
    
    def fill_barcode_field(self, field_name: str, data: str) -> bool:
        '''Fill a barcode field according to its fully qualified field name.
        
        :param field_name: The fully qualified field name.
        :param data: The new barcode value.
        :returns: If filling succeed, return true; otherwise, false.'''
        ...
    
    def import_fdf(self, input_fdf_stream: Any) -> None:
        '''Imports the content of the fields from the fdf file and put them into the new pdf.
        
        :param input_fdf_stream: The input fdf stream.'''
        ...
    
    def export_fdf(self, output_fdf_stream: Any) -> None:
        '''Exports the content of the fields of the pdf into the fdf stream.
        
        :param output_fdf_stream: The output fdf stream.'''
        ...
    
    def export_xml(self, output_xml_stream: Any) -> None:
        '''Exports the content of the fields of the pdf into the xml stream.
        The button field's value will not be exported.
        
        :param output_xml_stream: Output Xml stream.'''
        ...
    
    def extract_xfa_data(self, output_xml_stream: Any) -> None:
        '''Extracts XFA data packet
        
        :param output_xml_stream: Stream where XML data will be stored.'''
        ...
    
    def set_xfa_data(self, input_xml_stream: Any) -> None:
        '''Replaces XFA data with specified data packet. Data packet may be extracted using ExtractXfaData.
        
        :param input_xml_stream: Stream where XML is stored.'''
        ...
    
    def import_xfdf(self, input_xfdf_stream: Any) -> None:
        '''Imports the content of the fields from the xfdf(xml) file and put them into the new pdf.
        
        :param input_xfdf_stream: The input xfdf(xml) stream.'''
        ...
    
    def export_xfdf(self, output_xfdf_stream: Any) -> None:
        '''Exports the content of the fields of the pdf into the xml stream.
        The button field's value will not be exported.
        
        :param output_xfdf_stream: The output xml stream.'''
        ...
    
    def export_json(self, output_json_stream: Any, indented: bool) -> None:
        '''Exports the contents of all fields in the document into a JSON stream. Button field values are not exported.
        
        :param output_json_stream: The output JSON stream where the document's fields data will be written.
        :param indented: Optional. Specifies whether the JSON output should be indented for better readability. The default value is true.'''
        ...
    
    def import_json(self, input_json_stream: Any) -> None:
        '''Imports all field data from a JSON stream into the document fields, matching the fields by their full names.
        
        :param input_json_stream: The input JSON stream containing the field data to be imported into the document fields.'''
        ...

    def rename_field(self, field_name: str, new_field_name: str) -> None:
        '''Renames a field. Either AcroForm field or XFA field is OK.
        
        :param field_name: the old field name
        :param new_field_name: the new field name'''
        ...
    
    def get_rich_text(self, field_name: str) -> str:
        '''Get a Rich Text field's value, including the formattinf information of every character.
        
        :param field_name: The fully qualified field name of the Rich Text field.
        :returns: Return a string containing formatting information of the Rich Text field.'''
        ...
    
    def get_submit_flags(self, field_name: str) -> aspose.pdf.facades.SubmitFormFlag:
        '''Returns the submit button's submission flags
        
        :param field_name: The qualified field name.
        :returns: Submission flags of the button.'''
        ...
    
    def get_field_type(self, field_name: str) -> aspose.pdf.facades.FieldType:
        '''Returns type of field.
        
        :param field_name: Field name.
        :returns: Element of FileType enumeration corresponding to field type.'''
        ...
    
    def is_required_field(self, field_name: str) -> bool:
        '''Determines whether field is required or not.
        
        :param field_name: The name of field.
        :returns: True - the field is required; otherwise, false.'''
        ...
    
    def get_field_flag(self, field_name: str) -> aspose.pdf.facades.PropertyFlag:
        '''Returns flags of the field.
        
        :param field_name: Field name
        :returns: Property flag (ReadOnly/ Required/NoExport'''
        ...
    
    @property
    def import_result(self) -> None:
        '''Result of last import operation. Array of objects which descibre result of import for each field.'''
        ...
    
    @property
    def src_file_name(self) -> str:
        '''Gets or sets source file name.'''
        ...
    
    @src_file_name.setter
    def src_file_name(self, value: str):
        ...
    
    @property
    def dest_file_name(self) -> str:
        '''Gets or sets destiination file name.'''
        ...
    
    @dest_file_name.setter
    def dest_file_name(self, value: str):
        ...
    
    @property
    def src_stream(self) -> Any:
        '''Gets or sets source stream.'''
        ...
    
    @src_stream.setter
    def src_stream(self, value: Any):
        ...
    
    @property
    def dest_stream(self) -> Any:
        '''Gets or sets destination stream.'''
        ...
    
    @dest_stream.setter
    def dest_stream(self, value: Any):
        ...
    
    @property
    def field_names(self) -> list[str]:
        '''Gets list of field names on the form.'''
        ...
    
    @property
    def form_submit_button_names(self) -> list[str]:
        '''Gets all form submit button names.'''
        ...
    
    class FormImportResult:
          '''Class which describes result if field import.'''
    
          @property
          def status(self) -> aspose.pdf.facades.Form.ImportStatus:
              '''Status of field import.'''
              ...

          @property
          def field_name(self) -> str:
              '''Full name of the field.'''
              ...

    class ImportStatus:
          '''Status of imported field.'''

          SUCCESS: ImportStatus
          FIELD_NOT_FOUND: ImportStatus
    
    ...

class FormDataConverter:
    '''Represents a class to convert data from one format to another format.
    It can convert the data in fdf/xml/pdf/xfdf to the OLEDB/OdbcDB.
    It also can convert the data in the OLEDB/OdbcDB to the data in fdf/xml/xfdf.
    It can convert the fdf to the xml with "hard-named" tag.'''
    
    def __init__(self):
        ...
    
    @staticmethod
    def convert_xml_to_fdf(self, source_xml: Any, dest_fdf: Any) -> None:
        '''Convert XML  import/export form data file into FDF format.
        
        :param source_xml: Source stream which contains XML file.
        :param dest_fdf: Destination source where resultant FDF file will be stored.'''
        ...
    
    @staticmethod
    def convert_fdf_to_xml(self, source_fdf: Any, dest_xml: Any) -> None:
        '''Convert FDF file into XML.
        
        :param source_fdf: Stream which contains FDF to convert.
        :param dest_xml: Source where reuslt XML will be placed.'''
        ...
    
    def convert_to_data_table(self, source_streams: list[Any], source_type) -> None:
        '''Convert files of strems into table.
        
        :param source_streams: Array of source streams in specified format.
        :param source_type: Format of data in streams. Valid values are: PDF, FDF, XFDF, XML.'''
        ...
    
    def import_into_data_base(self, connect_string: str, db_type) -> None:
        '''Imports data from table into database.
        
        :param connect_string: Connection string of database.
        :param db_type: Type of database connection: OLEDB or ODBC.'''
        ...
    
    def export_from_data_base(self, connect_string: str, db_type) -> None:
        '''Exports data from database into table.
        
        :param connect_string: Connection string for database.
        :param db_type: Connection type: OLEDB or ODBC.'''
        ...
    
    def convert_to_streams(self, dest_stream: list[Any], dest_type) -> None:
        '''Convert data in table into streams.
        
        :param dest_stream: Streams where data will be stored.
        :param dest_type: Type of stored data. Valid values are: XML, FDF, XFDF.'''
        ...
    
    def conver_to_streams(self, dest_stream: list[Any], dest_type) -> None:
        '''This method is obsolete. Please use ConvertToStreams() instead.
        
        :param dest_stream: Destination stream object.
        :param dest_type: Destination type value.'''
        ...
    
    @property
    def create_missing_field(self) -> bool:
        '''ConvertToDataTable will create required field if it does not exists in Table.'''
        ...
    
    @create_missing_field.setter
    def create_missing_field(self, value: bool):
        ...
    
    @property
    def replace_existing_table(self) -> bool:
        '''ImportIntoDatabase will drop existing table and create new table if this property set to true.'''
        ...
    
    @replace_existing_table.setter
    def replace_existing_table(self, value: bool):
        ...
    
    @property
    def clear_table_before_export(self) -> bool:
        '''ExportFromData will clear table before data export.'''
        ...
    
    @clear_table_before_export.setter
    def clear_table_before_export(self, value: bool):
        ...
    
    @property
    def create_missing_table(self) -> bool:
        '''ImportIntoDatabase will create table if it does not exists.'''
        ...
    
    @create_missing_table.setter
    def create_missing_table(self, value: bool):
        ...
    
    ...

class FormEditor(aspose.pdf.facades.SaveableFacade):
    '''Class for editing forms (ading/deleting field etc)'''
    
    @overload
    def __init__(self, src_stream: Any, dest_stream: Any):
        '''Constructor for FormEditor.
        
        :param src_stream: Source stream.
        :param dest_stream: Destination stream.'''
        ...
    
    @overload
    def __init__(self, src_file_name: str, dest_file_name: str):
        '''Constructor for FormEditor
        
        :param src_file_name: Name of source file.
        :param dest_file_name: Name of destination file.'''
        ...
    
    @overload
    def __init__(self):
        '''Constructor for FormEditor.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`FormEditor` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, dest_file_name: str):
        '''Initializes new :class:`FormEditor` object on base of the document.
        
        :param document: Pdf document.
        :param dest_file_name: Path of the destination file.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, dest_stream: Any):
        '''Initializes new :class:`FormEditor` object on base of the document.
        
        :param document: Pdf document.
        :param dest_stream: Destination stream.'''
        ...
    
    @overload
    def save(self) -> None:
        '''Saves changes into destination file.'''
        ...
    
    @overload
    def save(self, dest_file: str) -> None:
        '''Saves changes into destination file.'''
        ...
    
    @overload
    def save(self, dest_stream: Any) -> None:
        '''Saves changes into destination file.'''
        ...
    
    @overload
    def add_field(self, field_type: aspose.pdf.facades.FieldType, field_name: str, page_num: int, llx: float, lly: float, urx: float, ury: float) -> bool:
        '''Add field of specified type to the form.
        
        :param field_type: Type of the field which must be added.
        :param field_name: Name of the field whic must be added.
        :param page_num: Page number where new field must be placed.
        :param llx: Abscissa of the lower-left corner of the field.
        :param lly: Ordinate of the lower-left corner of the field.
        :param urx: Abscissa of the upper-right corner of the field.
        :param ury: Ordinate of the upper-right corner of the field.
        :returns: true if field was successfully added.'''
        ...
    
    @overload
    def add_field(self, field_type: aspose.pdf.facades.FieldType, field_name: str, init_value: str, page_num: int, llx: float, lly: float, urx: float, ury: float) -> bool:
        '''Add field of specified type to the form.
        
        :param field_type: Type of the field which must be added.
        :param field_name: Name of the field whic must be added.
        :param init_value: Initial value of the field.
        :param page_num: Page number where new field must be placed.
        :param llx: Abscissa of the lower-left corner of the field.
        :param lly: Ordinate of the lower-left corner of the field.
        :param urx: Abscissa of the upper-right corner of the field.
        :param ury: Ordinate of the upper-right corner of the field.
        :returns: true if field was successfully added.'''
        ...
    
    @overload
    def copy_inner_field(self, field_name: str, new_field_name: str, page_num: int) -> None:
        '''Copies an existing field to the same position in specified page number.
        A new document will be produced, which contains everything the source document has except for the newly copied field.
        
        :param field_name: The old fully qualified field name.
        :param new_field_name: The new fully qualified field name. If null, it will be set as fieldName + "~".
        :param page_num: The number of page to hold the new field. If -1, new field will be copid to the same page as old one hosted.'''
        ...
    
    @overload
    def copy_inner_field(self, field_name: str, new_field_name: str, page_num: int, abscissa: float, ordinate: float) -> None:
        '''Copies an existing field to a new position specified by both page number and ordinates.
        A new document will be produced, which contains everything the source document has except for the newly copied field.
        
        :param field_name: The old fully qualified field name.
        :param new_field_name: The new fully qualified field name. If null, it will be set as fieldName + "~".
        :param page_num: The number of page to hold the new field. If -1, new field will be copid to the same page as old one hosted.
        :param abscissa: The abscissa of the new field. If -1, the abscissa will be equaled to the original one.
        :param ordinate: The ordinate of the new field. If -1, the ordinate will be equaled to the original one.'''
        ...
    
    @overload
    def copy_outer_field(self, src_file_name: str, field_name: str) -> None:
        '''Copies an existing field from one PDF document to another document with original page number and ordinates.
        Notice: Only for AcroForm fields (excluding radio box).
        
        :param src_file_name: The name of PDF document which containes the field to be copied.
        :param field_name: The original fully qualified field name.'''
        ...
    
    @overload
    def copy_outer_field(self, src_file_name: str, field_name: str, page_num: int) -> None:
        '''Copies an existing field from one PDF document to another document with specified page number and original ordinates.
        Notice: Only for AcroForm fields (excluding radio box).
        
        :param src_file_name: The name of PDF document which containes the field to be copied.
        :param field_name: The original fully qualified field name.
        :param page_num: The number of page to hold the new field. If -1, new field will be copid to the same page as old one hosted.'''
        ...
    
    @overload
    def copy_outer_field(self, src_file_name: str, field_name: str, page_num: int, abscissa: float, ordinate: float) -> None:
        '''Copies an existing field from one PDF document to another document with specified page number and ordinates.
        Notice: Only for AcroForm fields (excluding radio box).
        
        :param src_file_name: The name of PDF document which containes the field to be copied.
        :param field_name: The original fully qualified field name.
        :param page_num: The number of page to hold the new field. If -1, new field will be copid to the same page as old one hosted.
        :param abscissa: The abscissa of the new field. If -1, the abscissa will be equaled to the original one.
        :param ordinate: The ordinate of the new field. If -1, the ordinate will be equaled to the original one.'''
        ...
    
    @overload
    def decorate_field(self, field_name: str) -> None:
        '''Changes visual attributes of the specified field.
        
        :param field_name: The fully qualified field name.'''
        ...
    
    @overload
    def decorate_field(self, field_type: aspose.pdf.facades.FieldType) -> None:
        '''Changes visual attributes of all fields with the specified field type.
        
        :param field_type: Type of fields which will be decorated.'''
        ...
    
    @overload
    def decorate_field(self) -> None:
        '''Changes visual attributes of all fields in the PDF document.'''
        ...
    
    @overload
    def add_list_item(self, field_name: str, item_name: str) -> None:
        '''Adds new item to the list box.
        
        :param field_name: Name of the field ot which new item will be added.
        :param item_name: Name if new item.'''
        ...
    
    @overload
    def add_list_item(self, field_name: str, export_name: list[str]) -> None:
        '''Add a new item with Export value to the existing list box field, only for AcroForm combo box field.
        
        :param field_name: Name of field to which items will be added.
        :param export_name: A string array denoting a new list item with Export Value, i.e. (Item Label, Export Value).'''
        ...
    
    def close(self) -> None:
        '''Closes the facade.'''
        ...
    
    def set_field_attribute(self, field_name: str, flag: aspose.pdf.facades.PropertyFlag) -> bool:
        '''Set attributes of field.
        
        :param field_name: Name of field which attributes should be set.
        :param flag: Flag (NoExport/ReadOnly/Required)
        :returns: true if attribute was set successfully.'''
        ...
    
    def set_field_appearance(self, field_name: str, flags: aspose.pdf.annotations.AnnotationFlags) -> bool:
        '''Set field flags
        
        :param field_name: Name of field whose flags should be updated.
        :param flags: Flag of the field.
        :returns: true if flags were updated successfully.'''
        ...
    
    def get_field_appearance(self, field_name: str) -> aspose.pdf.annotations.AnnotationFlags:
        '''Get field flags.
        
        :param field_name: Name of the field.
        :returns: Set of field flags'''
        ...
    
    def set_submit_flag(self, field_name: str, submit_form_flag: aspose.pdf.facades.SubmitFormFlag) -> bool:
        '''Set submit flag of submit button.
        
        :param field_name: Name of submit button.
        :param submit_form_flag: Submit flag.
        :returns: true if field was found and submit flag was successfully set.'''
        ...
    
    def set_submit_url(self, field_name: str, url: str) -> bool:
        '''Sets URL of the button.
        
        :param field_name: Submit button name.
        :param url: Fully qualified URL.
        :returns: true if URL for button was successfully set.'''
        ...
    
    def set_field_limit(self, field_name: str, field_limit: int) -> bool:
        '''Sets maximum character count of the text field.
        
        :param field_name: Name of the text field.
        :param field_limit: New value of limit for the field.
        :returns: true if field limit was successfully set.'''
        ...
    
    def set_field_comb_number(self, field_name: str, comb_number: int) -> bool:
        '''Sets number of combs for a regular single-line text field (the field is
        automatically divided into as many equally spaced positions, or combs,
        as the value of combNumber parameter).
        
        :param field_name: The qualified field name.
        :param comb_number: The number of combs to divide the field into.
        :returns: If success, return true;else false.'''
        ...
    
    def move_field(self, field_name: str, llx: float, lly: float, urx: float, ury: float) -> bool:
        '''Set new position of field.
        
        :param field_name: Name of field which must be moved.
        :param llx: Abscissa of the lower-left corner of the field.
        :param lly: Ordinate of the lower-left coerner of the field.
        :param urx: Abscissa of the upper-right corner of the field.
        :param ury: Ordinate of the upper-right corner of the field.
        :returns: true if field position was changed successfully.'''
        ...
    
    def remove_field(self, field_name: str) -> None:
        '''Remove field from the form.
        
        :param field_name: Name of the field which must be removed.'''
        ...
    
    def reset_facade(self) -> None:
        '''Reset all visual attribtues to empty value.'''
        ...
    
    def reset_inner_facade(self) -> None:
        '''Reset all visual attribtues of inner facade to empty value.'''
        ...
    
    def rename_field(self, field_name: str, new_field_name: str) -> None:
        '''Change name of the field.
        
        :param field_name: Old name of the field.
        :param new_field_name: New name of the field.'''
        ...
    
    def remove_field_action(self, field_name: str) -> None:
        '''Remove submit action of the field.
        
        :param field_name: Name of the field.'''
        ...
    
    def add_submit_btn(self, field_name: str, page: int, label: str, url: str, llx: float, lly: float, urx: float, ury: float) -> None:
        '''Add submit button on the form.
        
        :param field_name: Name of new button.
        :param page: Page where button will be placed.
        :param label: Button caption.
        :param url: URL of the submit button.
        :param llx: Abscissa of the lower-left corner.
        :param lly: Ordinate of the lower-left corner.
        :param urx: Abscissa of the upper-right corner.
        :param ury: Ordinate of the upper-right corner.'''
        ...
    
    def del_list_item(self, field_name: str, item_name: str) -> None:
        '''Delete item from the list field.
        
        :param field_name: Name of the field.
        :param item_name: Name of the item which must be deleted.'''
        ...
    
    def set_field_script(self, field_name: str, script: str) -> bool:
        '''Set JavaScript for a PushButton field. If old JavaScript existed, it will be replaced by the new one.
        
        :param field_name: The fully qualified field name.
        :param script: The Java script to be added/placed into a push button field.
        :returns: true if field scrip was successfully set.'''
        ...
    
    def add_field_script(self, field_name: str, script: str) -> bool:
        '''Add JavaScript for a PushButton field. If old event exists, new event is added after it.
        
        :param field_name: The fully qualified field name.
        :param script: The Java script to be added/placed into a push button field.
        :returns: True in case script was added successfully.'''
        ...
    
    def single_2_multiple(self, field_name: str) -> bool:
        '''Change a single-lined text field to a multiple-lined one.
        
        :param field_name: The qualified field name.
        :returns: If success, return true;else false.'''
        ...
    
    def set_field_alignment(self, field_name: str, alignment: int) -> bool:
        '''Set the alignment style of a text field.
        
        :param field_name: The qualified field name.
        :param alignment: The alignment style definition, including FormFieldFacade.AlignLeft,
                          FormFieldFacade.AlignCenter and FormFieldFacade.AlignRight.
        :returns: true if true if field was found and alignment was set.'''
        ...
    
    def set_field_alignment_v(self, field_name: str, alignment: int) -> bool:
        '''Set the vertical alignment style of a text field.
        
        :param field_name: The qualified field name.
        :param alignment: The alignment style definition, including FormFieldFacade.AlignTop,
                          FormFieldFacade.AlignMiddle and FormFieldFacade.AlignRight.
        :returns: true if field was found and alignment was successfully filled.'''
        ...
    
    @property
    def src_file_name(self) -> str:
        '''Gets or sets name of source file.'''
        ...
    
    @src_file_name.setter
    def src_file_name(self, value: str):
        ...
    
    @property
    def dest_file_name(self) -> str:
        '''Gets or sets destination file name.'''
        ...
    
    @dest_file_name.setter
    def dest_file_name(self, value: str):
        ...
    
    @property
    def src_stream(self) -> Any:
        '''Gets or sets source stream.'''
        ...
    
    @src_stream.setter
    def src_stream(self, value: Any):
        ...
    
    @property
    def dest_stream(self) -> Any:
        '''Gets or sets destination stream.'''
        ...
    
    @dest_stream.setter
    def dest_stream(self, value: Any):
        ...
    
    @property
    def items(self) -> list[str]:
        '''Sets items which will be added t onewly created list box or combo box.'''
        ...
    
    @items.setter
    def items(self, value: list[str]):
        ...
    
    @property
    def export_items(self) -> list[list[str]]:
        '''Sets options for combo box with export values.'''
        ...
    
    @export_items.setter
    def export_items(self, value: list[list[str]]):
        ...
    
    @property
    def facade(self) -> aspose.pdf.facades.FormFieldFacade:
        '''Sets visual attributes of the field.'''
        ...
    
    @facade.setter
    def facade(self, value: aspose.pdf.facades.FormFieldFacade):
        ...
    
    @property
    def radio_gap(self) -> float:
        '''The member to record the gap between two neighboring radio buttons in pixels,default is 50.'''
        ...
    
    @radio_gap.setter
    def radio_gap(self, value: float):
        ...
    
    @property
    def radio_horiz(self) -> bool:
        '''The flag to indicate whether the radios are arranged horizontally or vertically, default value is true.'''
        ...
    
    @radio_horiz.setter
    def radio_horiz(self, value: bool):
        ...
    
    @property
    def radio_button_item_size(self) -> float:
        '''Gets or sets size of radio button item size (when new radio button field is added).
        
        formEditor = new Aspose.Pdf.Facades.FormEditor("PdfForm.pdf", "FormEditor_AddField_RadioButton.pdf");
        
        formEditor.RadioGap = 4;
        
        formEditor.RadioHoriz = false;
        
        formEditor.RadioButtonItemSize = 20;
        
        formEditor.Items = new string[] { "First", "Second", "Third" };
        
        formEditor.AddField(FieldType.Radio, "AddedRadioButtonField", "Second", 1, 10, 30, 110, 130);
        
        formEditor.Save();'''
        ...
    
    @radio_button_item_size.setter
    def radio_button_item_size(self, value: float):
        ...
    
    @property
    def submit_flag(self) -> aspose.pdf.facades.SubmitFormFlag:
        '''Set the submit button's submission flags'''
        ...
    
    @submit_flag.setter
    def submit_flag(self, value: aspose.pdf.facades.SubmitFormFlag):
        ...
    
    ...

class FormFieldFacade:
    '''Class for representing field properties.'''
    
    def __init__(self):
        ...
    
    def reset(self) -> None:
        '''Reset all visual attribtues to empty value.'''
        ...
    
    @property
    def border_color(self) -> aspose.pydrawing.Color:
        '''The color of a field border.'''
        ...
    
    @border_color.setter
    def border_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def border_style(self) -> int:
        '''The style of a field border.'''
        ...
    
    @border_style.setter
    def border_style(self, value: int):
        ...
    
    @property
    def border_width(self) -> float:
        '''The width of a field border.'''
        ...
    
    @border_width.setter
    def border_width(self, value: float):
        ...
    
    @property
    def font(self) -> aspose.pdf.facades.FontStyle:
        '''The font type of a field text.'''
        ...
    
    @font.setter
    def font(self, value: aspose.pdf.facades.FontStyle):
        ...
    
    @property
    def custom_font(self) -> str:
        '''Gets or sets name of the font when this is non-standart (other then 14 standard fonts).'''
        ...
    
    @custom_font.setter
    def custom_font(self, value: str):
        ...
    
    @property
    def font_size(self) -> float:
        '''The size of a field text.'''
        ...
    
    @font_size.setter
    def font_size(self, value: float):
        ...
    
    @property
    def text_color(self) -> aspose.pydrawing.Color:
        '''The color of the field text.'''
        ...
    
    @text_color.setter
    def text_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def text_encoding(self) -> aspose.pdf.facades.EncodingType:
        '''The text encoding type of the field text.'''
        ...
    
    @text_encoding.setter
    def text_encoding(self, value: aspose.pdf.facades.EncodingType):
        ...
    
    @property
    def alignment(self) -> int:
        '''The alignment of a field text, default is left alignment.'''
        ...
    
    @alignment.setter
    def alignment(self, value: int):
        ...
    
    @property
    def rotation(self) -> int:
        '''The rotation of a field text.'''
        ...
    
    @rotation.setter
    def rotation(self, value: int):
        ...
    
    @property
    def caption(self) -> str:
        '''The normal caption of form field.'''
        ...
    
    @caption.setter
    def caption(self, value: str):
        ...
    
    @property
    def button_style(self) -> int:
        '''The style of check box or radio box field, defined by FormFieldFacade.CheckBoxStyle\*.'''
        ...
    
    @button_style.setter
    def button_style(self, value: int):
        ...
    
    @property
    def box(self) -> aspose.pydrawing.Rectangle:
        '''A rectangle object holding field's location.'''
        ...
    
    @box.setter
    def box(self, value: aspose.pydrawing.Rectangle):
        ...
    
    @property
    def position(self) -> list[float]:
        '''A rectangle object holding field's location.'''
        ...
    
    @position.setter
    def position(self, value: list[float]):
        ...
    
    @property
    def page_number(self) -> int:
        '''An integer value holding the number of page on which field locates.'''
        ...
    
    @page_number.setter
    def page_number(self, value: int):
        ...
    
    @property
    def items(self) -> list[str]:
        '''An array of string, each representing an option of a combo box/list/radio box field.'''
        ...
    
    @items.setter
    def items(self, value: list[str]):
        ...
    
    @property
    def export_items(self) -> list[list[str]]:
        '''The options for adding a list/combo/radio box'''
        ...
    
    @export_items.setter
    def export_items(self, value: list[list[str]]):
        ...
    
    @property
    def background_color(self) -> aspose.pydrawing.Color:
        '''The color of a field background, default is white.'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def backgroud_color(self) -> aspose.pydrawing.Color:
        '''Obsolete property. Use BackgroundColor.'''
        ...
    
    @backgroud_color.setter
    def backgroud_color(self, value: aspose.pydrawing.Color):
        ...
    
    BORDER_WIDTH_UNDIFIED: float
    
    BORDER_WIDTH_UNDEFINED: float
    
    BORDER_WIDTH_THIN: float
    
    BORDER_WIDTH_MEDIUM: float
    
    BORDER_WIDTH_THICK: float
    
    BORDER_STYLE_SOLID: int
    
    BORDER_STYLE_DASHED: int
    
    BORDER_STYLE_BEVELED: int
    
    BORDER_STYLE_INSET: int
    
    BORDER_STYLE_UNDERLINE: int
    
    BORDER_STYLE_UNDEFINED: int
    
    ALIGN_LEFT: int
    
    ALIGN_CENTER: int
    
    ALIGN_RIGHT: int
    
    ALIGN_UNDEFINED: int
    
    ALIGN_JUSTIFIED: int
    
    ALIGN_TOP: int
    
    ALIGN_MIDDLE: int
    
    ALIGN_BOTTOM: int
    
    CHECK_BOX_STYLE_CIRCLE: int
    
    CHECK_BOX_STYLE_CHECK: int
    
    CHECK_BOX_STYLE_CROSS: int
    
    CHECK_BOX_STYLE_DIAMOND: int
    
    CHECK_BOX_STYLE_STAR: int
    
    CHECK_BOX_STYLE_SQUARE: int
    
    CHECK_BOX_STYLE_UNDEFINED: int
    
    ...

class FormattedText:
    '''Class which represents formatted text. Contains information about text and its color, size, style.'''
    
    @overload
    def __init__(self):
        '''Initializes FormattedText.'''
        ...
    
    @overload
    def __init__(self, text: str):
        '''Initializes FormattedText.
        
        :param text: Text which contained in FormattedText.'''
        ...
    
    @overload
    def __init__(self, text: str, font_color: aspose.pdf.facades.FontColor, font_style: aspose.pdf.facades.FontStyle, encoding_type: aspose.pdf.facades.EncodingType, embedded: bool, text_size: float):
        '''Initializes FormattedText.
        
        :param text: Text content of the string.
        :param font_color: Color of the text.
        :param font_style: Style of the text.
        :param encoding_type: Encoding type (value of EncodingType enumeration).
        :param embedded: True if the font will be embedded.
        :param text_size: Size of the text.'''
        ...
    
    @overload
    def __init__(self, text: str, font_color: aspose.pdf.facades.FontColor, text_font: aspose.pdf.facades.FontStyle, text_encoding: aspose.pdf.facades.EncodingType, embedded: bool, text_size: float, line_spacing: float):
        '''Initialize FormattedText.
        
        :param text: Text content of the string.
        :param font_color: Color of the text.
        :param text_font: Font of the text.
        :param text_encoding: Encoding of the text.
        :param embedded: True if text will be embedded.
        :param text_size: Size of the text.
        :param line_spacing: Additional spacing.'''
        ...
    
    @overload
    def __init__(self, text: str, color: aspose.pydrawing.Color, text_font: aspose.pdf.facades.FontStyle, text_encoding: aspose.pdf.facades.EncodingType, embedded: bool, text_size: float):
        '''Initializes FormattedText.
        
        :param text: Text content of the string.
        :param color: Color of the text.
        :param text_font: Font of the text.
        :param text_encoding: Encoding of the text.
        :param embedded: True if text will be embedded.
        :param text_size: Size of the text.'''
        ...
    
    @overload
    def __init__(self, text: str, text_color: aspose.pydrawing.Color, text_font: aspose.pdf.facades.FontStyle, text_encoding: aspose.pdf.facades.EncodingType, embedded: bool, text_size: float, line_spacing: float):
        '''Initializes FormattedText.
        
        :param text: Text contents of the string.
        :param text_color: Color of the text.
        :param text_font: Font of the text.
        :param text_encoding: Encoding of the text.
        :param embedded: If true font will be embedded.
        :param text_size: Size of the text.
        :param line_spacing: Additional spacing.'''
        ...
    
    @overload
    def __init__(self, text: str, text_color: aspose.pdf.facades.FontColor, back_color: aspose.pdf.facades.FontColor, text_font: aspose.pdf.facades.FontStyle, text_encoding: aspose.pdf.facades.EncodingType, embedded: bool, text_size: float):
        '''Initializes FormattedText.
        
        :param text: Text content of the string.
        :param text_color: Color of the text.
        :param back_color: Color of background.
        :param text_font: Font of the text.
        :param text_encoding: Encoding of the text.
        :param embedded: If true font will be embedded.
        :param text_size: Size of the text.'''
        ...
    
    @overload
    def __init__(self, text: str, text_color: aspose.pdf.facades.FontColor, back_color: aspose.pdf.facades.FontColor, text_font: aspose.pdf.facades.FontStyle, text_encoding: aspose.pdf.facades.EncodingType, embedded: bool, text_size: float, line_spacing: float):
        '''Initializes FormattedText.
        
        :param text: Text content.
        :param text_color: Color of the text.
        :param back_color: Color of background.
        :param text_font: Font of the text.
        :param text_encoding: Encoding of the text.
        :param embedded: If true font will be embedded.
        :param text_size: Size of the text.
        :param line_spacing: Additional spacing.'''
        ...
    
    @overload
    def __init__(self, text: str, text_color: aspose.pydrawing.Color, back_color: aspose.pydrawing.Color, text_font: aspose.pdf.facades.FontStyle, encoding: aspose.pdf.facades.EncodingType, embedded: bool, text_size: float):
        '''Initializes FormattedText.
        
        :param text: Text content of the string.
        :param text_color: Color of the text.
        :param back_color: Color of background.
        :param text_font: Font of the text.
        :param encoding: Encoding of the text.
        :param embedded: True if font will be embedded.
        :param text_size: Size of the text.'''
        ...
    
    @overload
    def __init__(self, text: str, text_color: aspose.pydrawing.Color, back_color: aspose.pydrawing.Color, text_font: aspose.pdf.facades.FontStyle, text_encoding: aspose.pdf.facades.EncodingType, embedded: bool, text_size: float, line_spacing: float):
        '''Initializes FormattedText.
        
        :param text: Text contents of the string.
        :param text_color: Color of the text.
        :param back_color: Color of the background.
        :param text_font: Font of the text.
        :param text_encoding: Encoding of the text.
        :param embedded: If true font is embedded.
        :param text_size: Size of the text.
        :param line_spacing: Additional spacing.'''
        ...
    
    @overload
    def __init__(self, text: str, text_color: aspose.pydrawing.Color, back_color: aspose.pydrawing.Color, font_name: str, text_encoding: aspose.pdf.facades.EncodingType, embedded: bool, font_size: float):
        '''Initializes FormattedText.
        
        :param text: Text content.
        :param text_color: Color of the text.
        :param back_color: Color of background.
        :param font_name: Font of the text.
        :param text_encoding: Encoding of the text.
        :param embedded: If true font will be embedded.
        :param font_size: Size of the text.'''
        ...
    
    @overload
    def __init__(self, text: str, text_color: aspose.pydrawing.Color, back_color: aspose.pydrawing.Color):
        '''Initializes FormattedText.
        
        :param text: Text content.
        :param text_color: Color of the text.
        :param back_color: Color of background.'''
        ...
    
    @overload
    def __init__(self, text: str, text_color: aspose.pydrawing.Color, font_name: str, text_encoding: aspose.pdf.facades.EncodingType, embedded: bool, font_size: float):
        '''Initializes FormattedText.
        
        :param text: Text content.
        :param text_color: Color of the text.
        :param font_name: Font of the text.
        :param text_encoding: Encoding of the text.
        :param embedded: If true font will be embedded.
        :param font_size: Size of the text.'''
        ...
    
    @overload
    def add_new_line_text(self, new_line_text: str) -> None:
        '''Adds a new line to the FormattedText object and sets the newLineText to the next line's text.
        
        :param new_line_text: Text of new added line.'''
        ...
    
    @overload
    def add_new_line_text(self, new_line_text: str, line_spacing: float) -> None:
        '''Adds a new line to the FormattedText object and sets the newLineText to the next line's text.
        
        :param new_line_text: Text of new added line.
        :param line_spacing: Spacing of the line.'''
        ...
    
    def is_cjk(self) -> bool:
        '''Checks if text is CJK (Chinese, Japanese, or Korean).
        
        :returns: True if text is CJK. Otherwise false.'''
        ...
    
    def set_cjk_font_style(self) -> None:
        '''Changes FormattedText font style for CJK (Chinese, Japanese, or Korean) font.'''
        ...
    
    @property
    def text_height(self) -> float:
        '''Gets height of text.'''
        ...
    
    @property
    def text_width(self) -> float:
        '''Gets width of text.'''
        ...
    
    ...

class IFacade:
    '''General facade interface that defines common facades methods.'''
    
    @overload
    def bind_pdf(self, src_file: str) -> None:
        '''Binds PDF document for editing.
        
        :param src_file: The path of input PDF document.'''
        ...
    
    @overload
    def bind_pdf(self, src_stream: Any) -> None:
        '''Binds PDF document for editing.
        
        :param src_stream: The stream of input PDF document.'''
        ...
    
    @overload
    def bind_pdf(self, src_doc: aspose.pdf.Document) -> None:
        '''Binds PDF document for editing.
        
        :param src_doc: Input PDF document.'''
        ...
    
    def close(self) -> None:
        '''Releases any resources associates with the current facade.'''
        ...
    
    ...

class ISaveableFacade:
    '''Facade interface that defines methods common for all saveable facades.'''
    
    @overload
    def save(self, dest_file: str) -> None:
        '''Saves the result PDF document to file.
        
        :param dest_file: The path of output PDF document.'''
        ...
    
    @overload
    def save(self, dest_stream: Any) -> None:
        '''Saves the result PDF document to stream.
        
        :param dest_stream: The stream of output PDF document.'''
        ...
    
    ...

class LineInfo:
    '''Represents the information of line.'''
    
    def __init__(self):
        ...
    
    @property
    def vertice_coordinate(self) -> list[float]:
        '''Gets or sets an array of numbers representing the alternating horizontal and vertical,coordinates, respectively, of each vertex.'''
        ...
    
    @vertice_coordinate.setter
    def vertice_coordinate(self, value: list[float]):
        ...
    
    @property
    def line_color(self) -> aspose.pydrawing.Color:
        '''Gets or sets the color of a line.'''
        ...
    
    @line_color.setter
    def line_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def line_width(self) -> int:
        '''Gets or sets the width of a line.'''
        ...
    
    @line_width.setter
    def line_width(self, value: int):
        ...
    
    @property
    def visibility(self) -> bool:
        '''Gets or sets the visibility of a line.'''
        ...
    
    @visibility.setter
    def visibility(self, value: bool):
        ...
    
    @property
    def line_dash_pattern(self) -> list[int]:
        '''Gets or sets the dash pattern of a line.'''
        ...
    
    @line_dash_pattern.setter
    def line_dash_pattern(self, value: list[int]):
        ...
    
    @property
    def border_style(self) -> int:
        '''Gets or sets the border style of a line, 0 represents solid, 1 represents dashed, 2 represents beleved, 3 represents insert, 4 represents underline.'''
        ...
    
    @border_style.setter
    def border_style(self, value: int):
        ...
    
    ...

class PdfAnnotationEditor(aspose.pdf.facades.SaveableFacade):
    '''Represents a class for work with PDF document annotations (comments).'''
    
    @overload
    def __init__(self):
        '''Initializes new :class:`PdfAnnotationEditor` object.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfAnnotationEditor` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def import_annotations_from_xfdf(self, xfdf_file: str) -> None:
        '''Imports all annotations from XFDF file.
        
        :param xfdf_file: The input XFDF file.'''
        ...
    
    @overload
    def import_annotations_from_xfdf(self, xfdf_stream: Any) -> None:
        '''Imports all annotations from XFDF data stream.
        
        :param xfdf_stream: The input XFDF data stream.'''
        ...
    
    @overload
    def import_annotation_from_xfdf(self, xfdf_file: str) -> None:
        '''Imports all annotations from XFDF file.
        
        :param xfdf_file: The input XFDF file.'''
        ...
    
    @overload
    def import_annotation_from_xfdf(self, xfdf_file: str, annot_type: list[aspose.pdf.annotations.AnnotationType]) -> None:
        '''Imports the specified annotations from XFDF file.
        
        :param xfdf_file: The input XFDF file.
        :param annot_type: The annotations array to be imported.'''
        ...
    
    @overload
    def import_annotation_from_xfdf(self, xfdf_stream: Any, annot_type: list[aspose.pdf.annotations.AnnotationType]) -> None:
        '''Imports the specified annotations from XFDF data stream.
        
        :param xfdf_stream: The input XFDF data stream.
        :param annot_type: The array of annotation types to be imported.'''
        ...
    
    @overload
    def import_annotation_from_xfdf(self, xfdf_stream: Any) -> None:
        '''Imports all annotations from XFDF data stream.
        
        :param xfdf_stream: The input XFDF data stream.'''
        ...
    
    @overload
    def import_annotations(self, annot_file: list[str], annot_type: list[aspose.pdf.annotations.AnnotationType]) -> None:
        '''Imports the specified annotations into document from array of another PDF documents.
        
        :param annot_file: The array of paths of PDF documents that contain source annotations.
        :param annot_type: The array of annotation types to be imported.'''
        ...
    
    @overload
    def import_annotations(self, annot_file: list[str]) -> None:
        '''Imports annotations into document from array of another PDF documents.
        
        :param annot_file: The array of paths of PDF documents that contain source annotations.'''
        ...
    
    @overload
    def import_annotations(self, annot_file_stream: list[Any], annot_type: list[aspose.pdf.annotations.AnnotationType]) -> None:
        '''Imports the specified annotations into document from array of another PDF document streams.
        
        :param annot_file_stream: The array of streams of PDF documents that contain source annotations.
        :param annot_type: The annotation types to be imported.'''
        ...
    
    @overload
    def import_annotations(self, annot_file_stream: list[Any]) -> None:
        '''Imports annotations into document from array of another PDF document streams.
        
        :param annot_file_stream: The array of streams of PDF documents that contain source annotations.'''
        ...
    
    @overload
    def modify_annotations(self, start: int, end: int, annot_type, annotation: aspose.pdf.annotations.Annotation) -> None:
        '''Modifies the annotations of the specifed type on the specified page range.
        It supports to modify next annotation properties: Modified, Title, Contents, Color, Subject and Open.
        
        :param start: The start page number.
        :param end: The end page number.
        :param annot_type: The annotation type.
        :param annotation: The annotation object contains new properties.'''
        ...
    
    @overload
    def modify_annotations(self, start: int, end: int, annotation: aspose.pdf.annotations.Annotation) -> None:
        '''Modifies the annotations of the specifed type on the specified page range.
        It supports to modify next annotation properties: Modified, Title, Contents, Color, Subject and Open.
        
        :param start: The start page number.
        :param end: The end page number.
        :param annotation: The annotation object contains new properties.'''
        ...
    
    @overload
    def flattening_annotations(self) -> None:
        '''Flattens all annotations in the document.'''
        ...
    
    @overload
    def flattening_annotations(self, flatten_settings) -> None:
        '''Flattens all annotations in the document.
        
        :param flatten_settings: Specifies modes of flattening.'''
        ...
    
    @overload
    def flattening_annotations(self, start: int, end: int, annot_type: list[aspose.pdf.annotations.AnnotationType]) -> None:
        '''Flattens the annotations of the specified types.
        
        :param start: The start page.
        :param end: Then end page.
        :param annot_type: The annotation types should be flattened.'''
        ...
    
    @overload
    def delete_annotations(self) -> None:
        '''Deletes all annotations in the document.'''
        ...
    
    @overload
    def delete_annotations(self, annot_type: str) -> None:
        '''Deletes all annotations of the specified type in the document.
        
        :param annot_type: The type of annotation will be deleted.'''
        ...
    
    @overload
    def export_annotations_xfdf(self, xml_output_stream: Any, start: int, end: int, annot_types: list[str]) -> None:
        '''Exports the content of the specified annotation types into XFDF
        
        :param xml_output_stream: The output XFDF stream.
        :param start: Start page from which the annotations of the document will be exported.
        :param end: End page to which the annotations of the document will be exported.
        :param annot_types: The array of annotation types need be exported.'''
        ...
    
    @overload
    def export_annotations_xfdf(self, xml_output_stream: Any, start: int, end: int, annot_types: list[aspose.pdf.annotations.AnnotationType]) -> None:
        '''Exports the content of the specified annotations types into XFDF
        
        :param xml_output_stream: The output XFDF stream.
        :param start: Start page from which the annotations of the document will be exported.
        :param end: End page to which the annotations of the document will be exported.
        :param annot_types: The array of annotation types need be exported.'''
        ...
    
    @overload
    def extract_annotations(self, start: int, end: int, annot_types: list[str]) -> list[aspose.pdf.annotations.Annotation]:
        '''Gets the list of annotations of the specified types.
        
        :param start: Start page from which the annotations will be selected.
        :param end: End page to which the annotations will be selected.
        :param annot_types: The array of needed annotation types.
        :returns: Annotations list.'''
        ...
    
    @overload
    def extract_annotations(self, start: int, end: int, annot_types: list[aspose.pdf.annotations.AnnotationType]) -> list[aspose.pdf.annotations.Annotation]:
        '''Gets the list of annotations of the specified types.
        
        :param start: Start page from which the annotations will be selected.
        :param end: End page to which the annotations will be selected.
        :param annot_types: The array of needed annotation types.
        :returns: Annotations list.'''
        ...
    
    def import_annotations_from_fdf(self, fdf_file: str) -> None:
        '''Imports all annotations from FDF file.
        
        :param fdf_file: The input FDF file.'''
        ...
    
    def modify_annotations_author(self, start: int, end: int, src_author: str, des_author: str) -> None:
        '''Modifies the author of annotations on the specified page range.
        
        :param start: The start page number.
        :param end: The end page number.
        :param src_author: The author that must be modified.
        :param des_author: The new author.'''
        ...
    
    def delete_annotation(self, annot_name: str) -> None:
        '''Deletes the annotation with specified annotation name.
        
        :param annot_name: The annotation name'''
        ...
    
    def export_annotations_to_xfdf(self, xml_output_stream: Any) -> None:
        '''Exports annotations to stream.
        
        :param xml_output_stream: Output stream.'''
        ...
    
    def redact_area(self, page_index: int, rect: aspose.pdf.Rectangle, color: aspose.pydrawing.Color) -> None:
        '''Redacts area on the specified page. All contents is removed.
        
        :param page_index: Index of the page.
        :param rect: Area rectangle.
        :param color: Filling color.'''
        ...
    
    ...

class PdfBookmarkEditor(aspose.pdf.facades.SaveableFacade):
    '''Represents a class to work with PDF file's bookmarks including create, modify, export, import and delete.'''
    
    @overload
    def __init__(self):
        '''Initializes new :class:`PdfBookmarkEditor` object.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfBookmarkEditor` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def create_bookmarks(self) -> None:
        '''Creates bookmarks for all pages.'''
        ...
    
    @overload
    def create_bookmarks(self, bookmark: aspose.pdf.facades.Bookmark) -> None:
        '''Creates the specified bookmark in the document. The method can be used for forming nested bookmarks hierarchy.
        
        :param bookmark: The bookmark will be added to the document.'''
        ...
    
    @overload
    def create_bookmarks(self, color: aspose.pydrawing.Color, bold_flag: bool, italic_flag: bool) -> None:
        '''Create bookmarks for all pages with specified color and style (bold, italic).
        
        :param color: The color of title.
        :param bold_flag: The flag of bold attribution.
        :param italic_flag: The flag of italic attribution.'''
        ...
    
    @overload
    def create_bookmark_of_page(self, bookmark_name: str, page_number: int) -> None:
        '''Creates bookmark for the specified page.
        
        :param bookmark_name: The specified bookmark name.
        :param page_number: The specified desination page.'''
        ...
    
    @overload
    def create_bookmark_of_page(self, bookmark_name: list[str], page_number: list[int]) -> None:
        '''Creates bookmarks for the specified pages.
        
        :param bookmark_name: Bookmarks title array.
        :param page_number: Bookmarks desination page array.'''
        ...
    
    @overload
    def delete_bookmarks(self) -> None:
        '''Deletes all bookmarks of the PDF document.'''
        ...
    
    @overload
    def delete_bookmarks(self, title: str) -> None:
        '''Deletes the bookmark of the PDF document.
        
        :param title: The title of bookmark deleted.'''
        ...
    
    @overload
    def extract_bookmarks(self) -> aspose.pdf.facades.Bookmarks:
        '''Extracts bookmarks of all levels from the document.
        
        :returns: The bookmarks collection of all bookmarks that exist in the document.'''
        ...
    
    @overload
    def extract_bookmarks(self, upper_level: bool) -> aspose.pdf.facades.Bookmarks:
        '''Extracts bookmarks of all levels from the document.
        
        :param upper_level: If true, extracts only upper level bookmarks. Else, extracts all bookmarks recursively.
        :returns: List of extracted bookmarks.'''
        ...
    
    @overload
    def extract_bookmarks(self, title: str) -> aspose.pdf.facades.Bookmarks:
        '''Extracts the bookmarks with the specified title.
        
        :param title: Extracted item title.
        :returns: Bookmark collection has items with the same title.'''
        ...
    
    @overload
    def extract_bookmarks(self, bookmark: aspose.pdf.facades.Bookmark) -> aspose.pdf.facades.Bookmarks:
        '''Extracts the children of a bookmark with a title like in specified bookamrk.
        
        :param bookmark: The specified bookamrk.
        :returns: Bookmark collection with child bookmarks.'''
        ...
    
    @overload
    def export_bookmarks_to_xml(self, xml_file: str) -> None:
        '''Exports bookmarks to XML file.
        
        :param xml_file: The output XML file.'''
        ...
    
    @overload
    def export_bookmarks_to_xml(self, stream: Any) -> None:
        '''Exports bookmarks to XML stream.
        
        :param stream: Output stream where data will be stored.'''
        ...
    
    @overload
    def import_bookmarks_with_xml(self, xml_file: str) -> None:
        '''Imports bookmarks to the document from XML file.
        
        :param xml_file: The XML file containing bookmarks list.'''
        ...
    
    @overload
    def import_bookmarks_with_xml(self, stream: Any) -> None:
        '''Imports bookmarks to the document from XML file.
        
        :param stream: Stream with bookmarks data.'''
        ...
    
    def modify_bookmarks(self, s_title: str, d_title: str) -> None:
        '''Modifys bookmark title according to the specified bookmark title.
        
        :param s_title: Source bookmark title.
        :param d_title: Modified bookmark title.'''
        ...
    
    def extract_bookmarks_to_html(self, pdf_file: str, css_file: str) -> None:
        '''Exports bookmarks to HTML file.
        
        :param pdf_file: The PDF file which bookmarks will be exported.
        :param css_file: The CSS file to display HTML file, can be null.'''
        ...
    
    @staticmethod
    def export_bookmarks_to_html(self, in_pdf_file: str, out_html_file: str) -> None:
        '''Exports bookmarks to HTML file.
        
        :param in_pdf_file: Input PDF file which bookmarks will be exported.
        :param out_html_file: Output HTML file'''
        ...
    
    ...

class PdfContentEditor(aspose.pdf.facades.SaveableFacade):
    '''Represents a class to edit PDF file's content.'''
    
    @overload
    def __init__(self):
        '''The constructor of the PdfContentEditor object.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfContentEditor` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def bind_pdf(self, input_file: str) -> None:
        '''Binds a PDF file for editing.
        
        :param input_file: A PDF file to be edited.'''
        ...
    
    @overload
    def bind_pdf(self, input_stream: Any) -> None:
        '''Binds a PDF stream for editing.
        
        :param input_stream: A PDF stream to be edited.'''
        ...
    
    @overload
    def create_web_link(self, rect: aspose.pydrawing.Rectangle, url: str, original_page: int, clr: aspose.pydrawing.Color, action_name) -> None:
        '''Creates a web link in PDF document.
        
        :param rect: The rectangle for active click.
        :param url: The web link destination.
        :param original_page: The number of original page on which rectangle bound with web link will be created.
        :param clr: The colour of rectangle for active click.
        :param action_name: The array of actions (members of PredefinedAction enum) corresponding to executing menu items in Acrobat viewer.'''
        ...
    
    @overload
    def create_web_link(self, rect: aspose.pydrawing.Rectangle, url: str, original_page: int, clr: aspose.pydrawing.Color) -> None:
        '''Creates a web link in PDF document.
        
        :param rect: The rectangle for active click.
        :param url: The web link destination.
        :param original_page: The number of original page where rectangle bound with web link will be created.
        :param clr: The colour of rectangle for active click.'''
        ...
    
    @overload
    def create_web_link(self, rect: aspose.pydrawing.Rectangle, url: str, original_page: int) -> None:
        '''Creates a web link in PDF document.
        
        :param rect: The rectangle for active click.
        :param url: The web link destination.
        :param original_page: The number of original page where rectangle bound with web link will be created.'''
        ...
    
    @overload
    def create_local_link(self, rect: aspose.pydrawing.Rectangle, des_page: int, original_page: int, clr: aspose.pydrawing.Color, action_name) -> None:
        '''Creates a local link in PDF document.
        
        :param rect: The rectangle for active click.
        :param des_page: The destination page.
        :param original_page: The number of original page where rectangle bound with local link will be created.
        :param clr: The colour of rectangle for active click.
        :param action_name: The array of actions (members of PredefinedAction enum) corresponding to executing menu items in Acrobat viewer.'''
        ...
    
    @overload
    def create_local_link(self, rect: aspose.pydrawing.Rectangle, des_page: int, original_page: int, clr: aspose.pydrawing.Color) -> None:
        '''Creates a local link in PDF document.
        
        :param rect: The rectangle for active click.
        :param des_page: The destination page.
        :param original_page: The number of original page where rectangle bound with local link will be created.
        :param clr: The colour of rectangle for active click.'''
        ...
    
    @overload
    def create_local_link(self, rect: aspose.pydrawing.Rectangle, des_page: int, original_page: int) -> None:
        '''Creates a local link in PDF document.
        
        :param rect: The rectangle for active click.
        :param des_page: The destination page.
        :param original_page: The number of original page where rectangle bound with local link will be created.'''
        ...
    
    @overload
    def create_pdf_document_link(self, rect: aspose.pydrawing.Rectangle, remote_pdf: str, original_page: int, destination_page: int, clr: aspose.pydrawing.Color, action_name) -> None:
        '''Creates a link to another PDF document page.
        
        :param rect: The rectangle for active click.
        :param remote_pdf: The PDF document which page will be opened.
        :param original_page: The number of original page where rectangle bound with link will be created.
        :param destination_page: The destination page.
        :param clr: The colour of rectangle for active click.
        :param action_name: The array of actions (members of PredefinedAction enum) corresponding to executing menu items in Acrobat viewer.'''
        ...
    
    @overload
    def create_pdf_document_link(self, rect: aspose.pydrawing.Rectangle, remote_pdf: str, original_page: int, destination_page: int, clr: aspose.pydrawing.Color) -> None:
        '''Creates a link to another PDF document page.
        
        :param rect: The rectangle for active click.
        :param remote_pdf: The PDF document which page will be opened.
        :param original_page: The number of original page where rectangle bound with link will be created.
        :param destination_page: The destination page.
        :param clr: The colour of rectangle for active click.'''
        ...
    
    @overload
    def create_pdf_document_link(self, rect: aspose.pydrawing.Rectangle, remote_pdf: str, original_page: int, destination_page: int) -> None:
        '''Creates a link to another PDF document page.
        
        :param rect: The rectangle for active click.
        :param remote_pdf: The PDF document which page will be opened.
        :param original_page: The number of original page where rectangle bound with link will be created.
        :param destination_page: The destination page.'''
        ...
    
    @overload
    def create_application_link(self, rect: aspose.pydrawing.Rectangle, application: str, page: int, clr: aspose.pydrawing.Color, action_name) -> None:
        '''Creates a link to launch an application in PDF document.
        
        :param rect: The rectangle for active click.
        :param application: The path of application to be launched.
        :param page: The number of original page where rectangle bound with link will be created.
        :param clr: The colour of rectangle for active click.
        :param action_name: The array of actions (members of PredefinedAction enum) corresponding to executing menu items in Acrobat viewer.'''
        ...
    
    @overload
    def create_application_link(self, rect: aspose.pydrawing.Rectangle, application: str, page: int, clr: aspose.pydrawing.Color) -> None:
        '''Creates a link to launch an application in PDF document.
        
        :param rect: The rectangle for active click.
        :param application: The path of application to be launched.
        :param page: The number of original page where rectangle bound with link will be created.
        :param clr: The colour of rectangle for active click.'''
        ...
    
    @overload
    def create_application_link(self, rect: aspose.pydrawing.Rectangle, application: str, page: int) -> None:
        '''Creates a link to launch an application in PDF document.
        
        :param rect: The rectangle for active click.
        :param application: The path of application to be launched.
        :param page: The number of original page where rectangle bound with link will be created.'''
        ...
    
    @overload
    def create_file_attachment(self, rect: aspose.pydrawing.Rectangle, contents: str, file_path: str, page: int, name: str) -> None:
        '''Creates file attachment annotation.
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param contents: The contents of the annotation.
        :param file_path: The path of the file will be attached.
        :param page: The number of original page where the annotation will be created.
        :param name: The name of an icon will be used in displaying the annotation.
                     This value can be: "Graph", "PushPin", "Paperclip", "Tag".'''
        ...
    
    @overload
    def create_file_attachment(self, rect: aspose.pydrawing.Rectangle, contents: str, file_path: str, page: int, name: str, opacity: float) -> None:
        '''Creates file attachment annotation.
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param contents: The contents of the annotation.
        :param file_path: The path of the file will be attached.
        :param page: The number of original page where the annotation will be created.
        :param name: The name of an icon will be used in displaying the annotation.
                     This value can be: "Graph", "PushPin", "Paperclip", "Tag".
        :param opacity: Icon's opacity from 0 to 1: 0 - completely transparant, 1 - completely opaque.'''
        ...
    
    @overload
    def create_file_attachment(self, rect: aspose.pydrawing.Rectangle, contents: str, attachment_stream: Any, attachment_name: str, page: int, name: str) -> None:
        '''Creates file attachment annotation.
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param contents: The contents of the annotation.
        :param attachment_stream: The attachment file stream.
        :param attachment_name: The attachment name.
        :param page: The number of original page where the annotation will be created.
        :param name: The name of an icon will be used in displaying the annotation.
                     This value can be: "Graph", "PushPin", "Paperclip", "Tag".'''
        ...
    
    @overload
    def create_file_attachment(self, rect: aspose.pydrawing.Rectangle, contents: str, attachment_stream: Any, attachment_name: str, page: int, name: str, opacity: float) -> None:
        '''Creates file attachment annotation.
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param contents: The contents of the annotation.
        :param attachment_stream: The attachment file stream.
        :param attachment_name: The attachment name.
        :param page: The number of original page where the annotation will be created.
        :param name: The name of an icon will be used in displaying the annotation.
                     This value can be: "Graph", "PushPin", "Paperclip", "Tag".
        :param opacity: Icon's opacity from 0 to 1: 0 - completely transparant, 1 - completely opaque.'''
        ...
    
    @overload
    def add_document_attachment(self, file_attachment_path: str, description: str) -> None:
        '''Adds document attachment with no annotation.
        
        :param file_attachment_path: The path of the file will be attached.
        :param description: The description information.'''
        ...
    
    @overload
    def add_document_attachment(self, file_attachment_stream: Any, file_attachment_name: str, description: str) -> None:
        '''Adds document attachment with no annotation.
        
        :param file_attachment_stream: The stream of the file will be attached.
        :param file_attachment_name: The attachment name.
        :param description: The description information.'''
        ...
    
    @overload
    def create_rubber_stamp(self, page: int, annot_rect: aspose.pydrawing.Rectangle, icon: str, annot_contents: str, color: aspose.pydrawing.Color) -> None:
        '''Creates a rubber stamp annotation.
        
        :param page: The number of original page where the annotation will be created.
        :param annot_rect: The annotation rectangle defining the location of the annotation on the page.
        :param icon: An icon is to be used in displaying the annotation. Default value: 'Draft'.
        :param annot_contents: The contents of the annotation.
        :param color: The color of the annotation.'''
        ...
    
    @overload
    def create_rubber_stamp(self, page: int, annot_rect: aspose.pydrawing.Rectangle, annot_contents: str, color: aspose.pydrawing.Color, appearance_file: str) -> None:
        '''Creates a rubber stamp annotation.
        
        :param page: The number of original page where the annotation will be created.
        :param annot_rect: The annotation rectangle defining the location of the annotation on the page.
        :param annot_contents: The contents of the annotation.
        :param color: The colour of the annotation.
        :param appearance_file: The path of appearance file.'''
        ...
    
    @overload
    def create_rubber_stamp(self, page: int, annot_rect: aspose.pydrawing.Rectangle, annot_contents: str, color: aspose.pydrawing.Color, appearance_stream: Any) -> None:
        '''Creates a rubber stamp annotation.
        
        :param page: The number of original page where the annotation will be created.
        :param annot_rect: The annotation rectangle defining the location of the annotation on the page.
        :param annot_contents: The contents of the annotation.
        :param color: The colour of the annotation.
        :param appearance_stream: The stream of appearance file.'''
        ...
    
    @overload
    def delete_image(self, page_number: int, index: list[int]) -> None:
        '''Deletes the specified images on the specified page.
        
        :param page_number: The number of page on which images must be deleted.
        :param index: An array repsents images' indexes.'''
        ...
    
    @overload
    def delete_image(self) -> None:
        '''Deletes all images from PDF document.'''
        ...
    
    @overload
    def replace_text(self, src_string: str, the_page: int, dest_string: str, text_state: aspose.pdf.text.TextState) -> bool:
        '''Replaces text in the PDF file on the specified page. :class:`aspose.pdf.text.TextState` object (font family, color) can be specified to replaced text.
        
        :param src_string: The string to be replaced.
        :param the_page: Page number (0 means "all pages").
        :param dest_string: The replaced string.
        :param text_state: Text state (Text Color, Font etc).
        :returns: Returns true if replacement was made.'''
        ...
    
    @overload
    def replace_text(self, src_string: str, dest_string: str) -> bool:
        '''Replaces text in the PDF file.
        
        :param src_string: The string to be replaced.
        :param dest_string: Replacing string.
        :returns: Returns true if replacement was made.'''
        ...
    
    @overload
    def replace_text(self, src_string: str, the_page: int, dest_string: str) -> bool:
        '''Replaces text in the PDF file on the specified page.
        
        :param src_string: The sting to be replaced.
        :param the_page: Page number (0 for all pages)
        :param dest_string: Replacing string.
        :returns: Returns true if replacement was made.'''
        ...
    
    @overload
    def replace_text(self, src_string: str, dest_string: str, text_state: aspose.pdf.text.TextState) -> bool:
        '''Replaces text in the PDF file using specified :class:`aspose.pdf.text.TextState` object.
        
        :param src_string: String to be replaced
        :param dest_string: Replacing string
        :param text_state: Text state (Text Color, Font etc)
        :returns: Returns true if replacement was made.'''
        ...
    
    @overload
    def replace_text(self, src_string: str, dest_string: str, font_size: int) -> bool:
        '''Replaces text in the PDF file and sets font size.
        
        :param src_string: String to be replaced.
        :param dest_string: Replacing string.
        :param font_size: Font size.
        :returns: Returns true if replacement was made.'''
        ...
    
    @overload
    def delete_stamp_by_ids(self, stamp_ids: list[int]) -> None:
        '''Deletes stamps with specified IDs from all pages of the document.
        
        :param stamp_ids: Array of stamp IDs.'''
        ...
    
    @overload
    def delete_stamp_by_ids(self, page_number: int, stamp_ids: list[int]) -> None:
        '''Deletes stamps on the specified page by multiple stamp IDs.
        
        :param page_number: Page number where stamps will be deleted.
        :param stamp_ids: Array of stamp IDs.'''
        ...
    
    @overload
    def delete_stamp_by_id(self, page_number: int, stamp_id: int) -> None:
        '''Deletes stamp on the specified page by stamp ID.
        
        :param page_number: Page number where stamp will be deleted.
        :param stamp_id: Identifier of stanp which should be deleted.'''
        ...
    
    @overload
    def delete_stamp_by_id(self, stamp_id: int) -> None:
        '''Delete stamp by ID from all pages of the document.
        
        :param stamp_id: Identifier of stamp which should be deleted.'''
        ...
    
    def close(self) -> None:
        '''Closes opened document.'''
        ...
    
    def extract_link(self) -> list[aspose.pdf.annotations.Annotation]:
        '''Extracts the collection of Link instances contained in PDF document.
        
        :returns: The collection of Link objects'''
        ...
    
    def create_custom_action_link(self, rect: aspose.pydrawing.Rectangle, original_page: int, color: aspose.pydrawing.Color, action_name) -> None:
        '''Creates a link to custom actions in PDF document.
        
        :param rect: The rectangle for active click.
        :param original_page: The number of original page where rectangle bound with link will be created.
        :param color: The colour of rectangle for active click.
        :param action_name: The array of actions (members of PredefinedAction enum) corresponding to executing menu items in Acrobat viewer.'''
        ...
    
    def create_java_script_link(self, code: str, rect: aspose.pydrawing.Rectangle, original_page: int, color: aspose.pydrawing.Color) -> None:
        '''Creates a link to JavaScript in PDF document.
        
        :param code: The JavaScript code.
        :param rect: The rectangle for active click.
        :param original_page: The number of original page where rectangle bound with link will be created.
        :param color: The colour of rectangle for active click.'''
        ...
    
    def create_text(self, rect: aspose.pydrawing.Rectangle, title: str, contents: str, open: bool, icon: str, page: int) -> None:
        '''Creates text annotation in PDF document
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param title: The title of the annotation.
        :param contents: The contents of the annotation.
        :param open: A flag specifying whether the annotation should initially be displayed open.
        :param icon: The name of an icon will be used in displaying the annotation.
                     This value can be: "Comment", "Key", "Note", "Help", "NewParagraph", "Paragraph", "Insert"
        :param page: The number of original page where the text annotation will be created.'''
        ...
    
    def create_free_text(self, rect: aspose.pydrawing.Rectangle, contents: str, page: int) -> None:
        '''Creates free text annotation in PDF document
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param contents: The contents of the annotation.
        :param page: The number of original page where the text annotation will be created.'''
        ...
    
    def create_markup(self, rect: aspose.pydrawing.Rectangle, contents: str, type: int, page: int, clr: aspose.pydrawing.Color) -> None:
        '''Creates markup annotation it PDF document.
        
        :param rect: The rectangle defining the location of the annotation on the page.
        :param contents: The contents of the annotation.
        :param type: The type of markup annotation. Can be 0 (Highlight), 1 (Underline), 2 (StrikeOut), 3 (Squiggly).
        :param page: The number of original page where the annotation will be created.
        :param clr: The color of markup.'''
        ...
    
    def create_popup(self, rect: aspose.pydrawing.Rectangle, contents: str, open: bool, page: int) -> None:
        '''Creates popup annotation in PDF document.
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param contents: The contents of the annotation.
        :param open: A flag specifying whether the pop-up annotation should initially be displayed open.
        :param page: The number of original page where the annotation will be created.'''
        ...
    
    def delete_attachments(self) -> None:
        '''Deletes all attachments in PDF document.'''
        ...
    
    def create_line(self, rect: aspose.pydrawing.Rectangle, contents: str, x1: float, y1: float, x2: float, y2: float, page: int, border: int, clr: aspose.pydrawing.Color, border_style: str, dash_array: list[int], le_array: list[str]) -> None:
        '''Creates line annotation.
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param contents: The contents of the annotation.
        :param x1: The starting horizontal coordinate of the line.
        :param y1: The starting vertical coordinate of the line.
        :param x2: The ending horizontal coordinate of the line.
        :param y2: The ending vertical coordinate of the line.
        :param page: The number of original page where the annotation will be created.
        :param border: The border width in points. If this value is 0 no border is drawn. Default value is 1.
        :param clr: The color of line.
        :param border_style: The border style specifying the width and dash pattern to be used in drawing the line.
                             This value can be: "S" (Solid), "D" (Dashed), "B" (Beveled), "I" (Inset), "U" (Underline).
        :param dash_array: A dash array defining a pattern of dashes and gaps to be used in drawing a dashed border.
                           If it is used, borderSyle must be accordingly set to "D".
        :param le_array: An array of two values respectively specifying the beginning and ending style of the drawing line.
                         The values can be: "Square", "Circle", "Diamond", "OpenArrow", "ClosedArrow", "None", "Butt", "ROpenArrow", "RClosedArrow", "Slash".'''
        ...
    
    def create_square_circle(self, rect: aspose.pydrawing.Rectangle, contents: str, clr: aspose.pydrawing.Color, square: bool, page: int, border_width: int) -> None:
        '''Creates square-circle annotation.
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param contents: The contents of the annotation.
        :param clr: The colour of square or circle.
        :param square: True (square), false (sircle).
        :param page: The number of original page where the annotation will be created.
        :param border_width: The border width of square or circle.'''
        ...
    
    def draw_curve(self, line_info: aspose.pdf.facades.LineInfo, page: int, annot_rect: aspose.pydrawing.Rectangle, annot_contents: str) -> None:
        '''Creates curve annotation.
        
        :param line_info: The instance of LineInfo class.
        :param page: The number of original page where the annotation will be created.
        :param annot_rect: The annotation rectangle defining the location of the annotation on the page.
        :param annot_contents: The contents of the annotation.'''
        ...
    
    def create_polygon(self, line_info: aspose.pdf.facades.LineInfo, page: int, annot_rect: aspose.pydrawing.Rectangle, annot_contents: str) -> None:
        '''Creates polygon annotation.
        
        :param line_info: The instance of LineInfo class.
        :param page: The number of original page where the annotation will be created.
        :param annot_rect: The annotation rectangle defining the location of the annotation on the page.
        :param annot_contents: The contents of the annotation.'''
        ...
    
    def create_poly_line(self, line_info: aspose.pdf.facades.LineInfo, page: int, annot_rect: aspose.pydrawing.Rectangle, annot_contents: str) -> None:
        '''Creates polyline annotation.
        
        :param line_info: The instance of LineInfo class.
        :param page: The number of original page where the annotation will be created.
        :param annot_rect: The annotation rectangle defining the location of the annotation on the page.
        :param annot_contents: The contents of the annotation.'''
        ...
    
    def create_caret(self, page: int, annot_rect: aspose.pydrawing.Rectangle, caret_rect: aspose.pydrawing.Rectangle, symbol: str, annot_contents: str, color: aspose.pydrawing.Color) -> None:
        '''Creates caret annotation.
        
        :param page: The number of original page where the annotation will be created.
        :param annot_rect: The annotation rectangle defining the location of the annotation on the page.
        :param caret_rect: The actual boundaries of the underlying caret.
        :param symbol: A symbol will be associated with the caret. Value can be: "P" (Paragraph), "None".
        :param annot_contents: The contents of the annotation.
        :param color: The color of the annotation.'''
        ...
    
    def create_bookmarks_action(self, title: str, color: aspose.pydrawing.Color, bold_flag: bool, italic_flag: bool, file: str, action_type: str, destination: str) -> None:
        '''Creates a bookmark with the specified action.
        
        :param title: The title of the bookmark.
        :param color: The colour of the bookmark's title.
        :param bold_flag: The flag of bold attribution.
        :param italic_flag: The flag of italic attribution.
        :param file: Another file or application required when the action type is "GoToR" or "Launch".
        :param action_type: The action type. The value can be: "GoToR", "Launch", "GoTo", "URI".
        :param destination: The local destination or remote destination or URL.'''
        ...
    
    def add_document_additional_action(self, event_type: str, code: str) -> None:
        '''Adds additional action for document event.
        
        :param event_type: The document event types.
        :param code: The code of JavaScript.'''
        ...
    
    def remove_document_open_action(self) -> None:
        '''Removes open action from the document. This operation is useful when concatenating multiple documents that use explicit 'GoTo' action on startup.'''
        ...
    
    def change_viewer_preference(self, viewer_attribution: int) -> None:
        '''Changes the view preference.
        
        :param viewer_attribution: The view attribution defined in the ViewerPreference class.'''
        ...
    
    def get_viewer_preference(self) -> int:
        '''Returns the view preference.
        
        :returns: Returns set of ViewerPrefernece flags'''
        ...
    
    def replace_image(self, page_number: int, index: int, image_file: str) -> None:
        '''Replaces the specified image on the specified page of PDF document with another image.
        
        :param page_number: The number of page on which the image is replaced.
        :param index: The index of the image object must be replaced.
        :param image_file: The image file will be used for replacing.'''
        ...
    
    def create_movie(self, rect: aspose.pydrawing.Rectangle, file_path: str, page: int) -> None:
        '''Creates Movie Annotations.
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param file_path: The path of movie file to be played.
        :param page: The page in which the Line annotation is created.'''
        ...
    
    def create_sound(self, rect: aspose.pydrawing.Rectangle, file_path: str, name: str, page: int, rate: str) -> None:
        '''Creates Sound Annotations.
        
        :param rect: The annotation rectangle defining the location of the annotation on the page.
        :param file_path: The file path of sound file.
        :param name: The name of an icon to be used in displaying the annotation,include:Speaker and Mic.
        :param page: The page in which the Sound annotation is created.
        :param rate: The sampling rate, in samples per second.'''
        ...
    
    def delete_stamp(self, page_number: int, index: list[int]) -> None:
        '''Deletes multiple stamps on the specified page by stamp indexes.
        
        :param page_number: Page number where stamp will be deleted.
        :param index: Stamp indexes.'''
        ...
    
    def hide_stamp_by_id(self, page_number: int, stamp_id: int) -> None:
        '''Hides the stamp. After hiding, stamp visibility may be restored with ShowStampById method.
        
        :param page_number: Number of the page.
        :param stamp_id: Identifier of stamp which should be hidden.'''
        ...
    
    def show_stamp_by_id(self, page_number: int, stamp_id: int) -> None:
        '''Shows stamp which was hidden by HiddenStampById.
        
        :param page_number: Number of the page.
        :param stamp_id: Identifier of stamp which should be shown.'''
        ...
    
    def move_stamp_by_id(self, page_number: int, stamp_id: int, x: float, y: float) -> None:
        '''Changes position of the stamp on page.
        
        :param page_number: Numer of page.
        :param stamp_id: Identifier of stamp which should be moved.
        :param x: New stamp horizontal pozition on the page.
        :param y: New stamp vertical position on the page.'''
        ...
    
    def move_stamp(self, page_number: int, stamp_index: int, x: float, y: float) -> None:
        '''Changes position of the stamp on page.
        
        :param page_number: Number of page.
        :param stamp_index: Index of stamp on the page.
        :param x: New stamp horizontal position.
        :param y: New stamp vertical position.'''
        ...
    
    def get_stamps(self, page_number: int) -> list[aspose.pdf.facades.StampInfo]:
        '''Returns array of stamps on the page.
        
        :param page_number: Page number where stamps will be searched.
        :returns: Array of stamps.'''
        ...
    
    @property
    def text_search_options(self) -> aspose.pdf.text.TextSearchOptions:
        '''Gets or sets text search options.'''
        ...
    
    @text_search_options.setter
    def text_search_options(self, value: aspose.pdf.text.TextSearchOptions):
        ...
    
    @property
    def text_edit_options(self) -> aspose.pdf.text.TextEditOptions:
        '''Gets or sets text edit options.'''
        ...
    
    @text_edit_options.setter
    def text_edit_options(self, value: aspose.pdf.text.TextEditOptions):
        ...
    
    @property
    def text_replace_options(self) -> aspose.pdf.text.TextReplaceOptions:
        '''Gets or sets text replace options.'''
        ...
    
    @text_replace_options.setter
    def text_replace_options(self, value: aspose.pdf.text.TextReplaceOptions):
        ...
    
    @property
    def replace_text_strategy(self) -> aspose.pdf.facades.ReplaceTextStrategy:
        '''A set of parameters for replace text operation'''
        ...
    
    @replace_text_strategy.setter
    def replace_text_strategy(self, value: aspose.pdf.facades.ReplaceTextStrategy):
        ...
    
    DOCUMENT_OPEN: str
    
    DOCUMENT_CLOSE: str
    
    DOCUMENT_WILL_SAVE: str
    
    DOCUMENT_SAVED: str
    
    DOCUMENT_WILL_PRINT: str
    
    DOCUMENT_PRINTED: str
    
    ...

class PdfConverter(aspose.pdf.facades.Facade):
    '''Represents a class to convert a pdf file's each page to images, supporting BMP, JPEG, PNG and TIFF now.
    Supported content in pdfs: pictures, form, comment.'''
    
    @overload
    def __init__(self):
        '''Initializes new :class:`PdfConverter` object.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfConverter` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def bind_pdf(self, input_file: str) -> None:
        '''Binds a Pdf file for converting.
        
        :param input_file: The pdf file.'''
        ...
    
    @overload
    def bind_pdf(self, input_stream: Any) -> None:
        '''Binds a Pdf Stream for convert.
        
        :param input_stream: The pdf Stream.'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str) -> None:
        '''Converts each pages of a pdf document to images and saves images to a single TIFF file.
        
        :param output_file: The file to save the TIFF image.'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str, compression_type: aspose.pdf.devices.CompressionType) -> None:
        '''Converts each pages of a pdf document to images and saves images to a single TIFF file.
        
        :param output_file: The output file.
        :param compression_type: Type of the compression.'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str, image_width: int, image_height: int) -> None:
        '''Converts each pages of a pdf document to images with dimensions, and saves images to a single TIFF file.
        
        :param output_file: The file name to save the TIFF image
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str, page_size: aspose.pdf.PageSize) -> None:
        '''Converts each pages of a pdf document to images with page size and saves images to a single TIFF file.
        
        :param output_file: The file name to save the TIFF image
        :param page_size: The page size of the image.'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str, page_size: aspose.pdf.PageSize, settings: aspose.pdf.devices.TiffSettings) -> None:
        '''Converts each pages of a pdf document to images with page size and saves images to a single TIFF file.
        
        :param output_file: The file name to save the TIFF image
        :param page_size: The page size of the image.
        :param settings: Settings object that defines TIFF parameters.'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str, image_width: int, image_height: int, compression_type: aspose.pdf.devices.CompressionType) -> None:
        '''Converts each pages of a pdf document to images with dimensions, and saves images to a single TIFF file.
        
        :param output_file: The file name to save the TIFF image
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.
        :param compression_type: Type of the compression.'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str, image_width: int, image_height: int, settings: aspose.pdf.devices.TiffSettings) -> None:
        '''Converts each pages of a pdf document to images with dimensions, and saves images to a single TIFF file.
        
        :param output_file: The file name to save the TIFF image
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.
        :param settings: Settings object that defines TIFF parameters.'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str, image_width: int, image_height: int, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter) -> None:
        '''Converts each pages of a pdf document to images with dimensions, and saves images to a single TIFF file.
        
        :param output_file: The file name to save the TIFF image
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.
        :param settings: Settings object that defines TIFF parameters.
        :param converter: External converter'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any) -> None:
        '''Converts each pages of a pdf document to images and saves images to a single TIFF stream.
        
        :param output_stream: The stream to save the TIFF image.'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any, compression_type: aspose.pdf.devices.CompressionType) -> None:
        '''Converts each pages of a pdf document to images and saves images to a single TIFF file.
        
        :param output_stream: The output stream.
        :param compression_type: Type of the compression.'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any, page_size: aspose.pdf.PageSize) -> None:
        '''Converts each pages of a pdf document to images with page size and saves images to a single TIFF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param page_size: The page size of the image.'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any, page_size: aspose.pdf.PageSize, settings: aspose.pdf.devices.TiffSettings) -> None:
        '''Converts each pages of a pdf document to images with page size and saves images to a single TIFF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param page_size: The page size of the image.
        :param settings: Settings object that defines TIFF parameters.'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any, image_width: int, image_height: int) -> None:
        '''Converts each pages of a pdf document to images with dimensions, and saves images to a single TIFF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any, image_width: int, image_height: int, compression_type: aspose.pdf.devices.CompressionType) -> None:
        '''Converts each pages of a pdf document to images with dimensions, and saves images to a single TIFF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.
        :param compression_type: Type of the compression.'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any, image_width: int, image_height: int, settings: aspose.pdf.devices.TiffSettings) -> None:
        '''Converts each pages of a pdf document to images with dimensions, and saves images to a single TIFF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.
        :param settings: Settings object that defines TIFF parameters.'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any, image_width: int, image_height: int, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter) -> None:
        '''Converts each pages of a pdf document to images with dimensions, and saves images to a single TIFF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.
        :param settings: Settings object that defines TIFF parameters.
        :param converter: External converter'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str, settings: aspose.pdf.devices.TiffSettings) -> None:
        '''Converts each pages of a pdf document to images with and saves images to a single TIFF file.
        
        :param output_file: The file name to save the TIFF image
        :param settings: Settings object that defines TIFF parameters.'''
        ...
    
    @overload
    def save_as_tiff(self, output_file: str, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter) -> None:
        '''Converts each pages of a pdf document to images with and saves images to a single TIFF file.
        
        :param output_file: The file name to save the TIFF image
        :param settings: Settings object that defines TIFF parameters.
        :param converter: External converter'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any, settings: aspose.pdf.devices.TiffSettings) -> None:
        '''Converts each pages of a pdf document to images and saves images to a single TIFF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param settings: Settings object that defines TIFF parameters.'''
        ...
    
    @overload
    def save_as_tiff(self, output_stream: Any, settings: aspose.pdf.devices.TiffSettings, converter: aspose.pdf.IIndexBitmapConverter) -> None:
        '''Converts each pages of a pdf document to images and saves images to a single TIFF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param settings: Settings object that defines TIFF parameters.
        :param converter: External converter'''
        ...
    
    @overload
    def save_as_tiff_class_f(self, output_file: str, image_width: int, image_height: int) -> None:
        '''Converts each pages of a pdf document to images and save images to a single TIFF ClassF file.
        
        :param output_file: The stream to save the TIFF image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.'''
        ...
    
    @overload
    def save_as_tiff_class_f(self, output_file: str, page_size: aspose.pdf.PageSize) -> None:
        '''Converts each pages of a pdf document to images and save images to a single TIFF ClassF file.
        
        :param output_file: The stream to save the TIFF image.
        :param page_size: The page size of the image.'''
        ...
    
    @overload
    def save_as_tiff_class_f(self, output_stream: Any, image_width: int, image_height: int) -> None:
        '''Converts each pages of a pdf document to images and save images to a single TIFF ClassF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.'''
        ...
    
    @overload
    def save_as_tiff_class_f(self, output_stream: Any, page_size: aspose.pdf.PageSize) -> None:
        '''Converts each pages of a pdf document to images and save images to a single TIFF ClassF stream.
        
        :param output_stream: The stream to save the TIFF image.
        :param page_size: The page size of the image.'''
        ...
    
    @overload
    def save_as_tiff_class_f(self, output_file: str) -> None:
        '''Converts each pages of a pdf document to images and save images to a single TIFF ClassF file.
        
        :param output_file: The stream to save the TIFF image.'''
        ...
    
    @overload
    def save_as_tiff_class_f(self, output_stream: Any) -> None:
        '''Converts each pages of a pdf document to images and save images to a single TIFF ClassF stream.
        
        :param output_stream: The stream to save the TIFF image.'''
        ...
    
    @overload
    def get_next_image(self, output_file: str) -> None:
        '''Saves image to file with default image format - jpeg.
        
        :param output_file: The file path and name to save the image.'''
        ...
    
    @overload
    def get_next_image(self, output_file: str, page_size: aspose.pdf.PageSize) -> None:
        '''Saves image to file with ith given page size and default image format - jpeg.
        
        :param output_file: The file path and name to save the image.
        :param page_size: The page size of the image.'''
        ...
    
    @overload
    def get_next_image(self, output_file: str, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        '''Saves image to file with the givin image format.
        
        :param output_file: The file path and name to save the image.
        :param format: The format of the image.'''
        ...
    
    @overload
    def get_next_image(self, output_file: str, page_size: aspose.pdf.PageSize, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        '''Saves image to file with given page size and image format.
        
        :param output_file: The file path and name to save the image.
        :param page_size: The page size of the image.
        :param format: The format of the image.'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any) -> None:
        '''Saves image to stream with default image format - jpeg.
        
        :param output_stream: The stream to save the image.'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any, page_size: aspose.pdf.PageSize) -> None:
        '''Saves image to stream with given page size.
        
        :param output_stream: The stream to save the image.
        :param page_size: The page size of the image.'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        '''Saves image to stream with given image format.
        
        :param output_stream: The stream to save the image.
        :param format: The format of the image.'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any, page_size: aspose.pdf.PageSize, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        '''Saves image to stream with given page size.
        
        :param output_stream: The stream to save the image.
        :param page_size: The page size of the image.
        :param format: The format of the image.'''
        ...
    
    @overload
    def get_next_image(self, output_file: str, format: aspose.pydrawing.Imaging.ImageFormat, image_width: int, image_height: int, quality: int) -> None:
        '''Saves image to file with the given image format, dimensions and quality.
        
        :param output_file: The file path and name to save the image.
        :param format: The format of the image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.
        :param quality: The Jpeg file's quality (0~100), 0 is lowest and 100 is highest'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any, format: aspose.pydrawing.Imaging.ImageFormat, image_width: int, image_height: int, quality: int) -> None:
        '''Saves image to stream with the givin image format, dimensions and quality.
        
        :param output_stream: The stream to save the image.
        :param format: The format of the image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.
        :param quality: The Jpeg file's quality (0~100), 0 is lowest and 100 is highest'''
        ...
    
    @overload
    def get_next_image(self, output_file: str, format: aspose.pydrawing.Imaging.ImageFormat, image_width: float, image_height: float, quality: int) -> None:
        '''Saves image to file with the givin image format, image size,  and quality.
        
        :param output_file: The file path and name to save the image.
        :param format: The format of the image.
        :param image_width: The image width, the unit is pixels.
        :param image_height: The image height, the unit is pixels..
        :param quality: The Jpeg file's quality (0~100), 0 is lowest and 100 is highest'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any, format: aspose.pydrawing.Imaging.ImageFormat, image_width: float, image_height: float, quality: int) -> None:
        '''Saves image to stream with the givin image format, size and quality.
        
        :param output_stream: The stream to save the image.
        :param format: The format of the image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.
        :param quality: The Jpeg file's quality (0~100), 0 is lowest and 100 is highest'''
        ...
    
    @overload
    def get_next_image(self, output_file: str, format: aspose.pydrawing.Imaging.ImageFormat, image_width: int, image_height: int) -> None:
        '''Saves image to file with the given image format and dimensions.
        
        :param output_file: The file path and name to save the image.
        :param format: The format of the image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any, format: aspose.pydrawing.Imaging.ImageFormat, image_width: int, image_height: int) -> None:
        '''Saves image to stream with the givin image format, size and quality.
        
        :param output_stream: The stream to save the image.
        :param format: The format of the image.
        :param image_width: The image width, the unit is pixel.
        :param image_height: The image height, the unit is pixel.'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any, format: aspose.pydrawing.Imaging.ImageFormat, quality: int) -> None:
        '''Saves image to stream with given image format and quality.
        
        :param output_stream: The stream to save the image.
        :param format: The format of the image.
        :param quality: The Jpeg file's quality (0~100), 0 is lowest and 100 is highest'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any, page_size: aspose.pdf.PageSize, format: aspose.pydrawing.Imaging.ImageFormat, quality: int) -> None:
        '''Saves image to stream with given page size, image format and quality.
        
        :param output_stream: The stream to save the image.
        :param page_size: The page size of the image.
        :param format: The format of the image.
        :param quality: The Jpeg file's quality (0~100), 0 is lowest and 100 is highest'''
        ...
    
    @overload
    def get_next_image(self, output_file: str, format: aspose.pydrawing.Imaging.ImageFormat, quality: int) -> None:
        '''Saves image to file with given image format and quality.
        
        :param output_file: The file path and name to save the image.
        :param format: The format of the image.
        :param quality: The Jpeg file's quality (0~100), 0 is lowest and 100 is highest'''
        ...
    
    @overload
    def get_next_image(self, output_file: str, page_size: aspose.pdf.PageSize, format: aspose.pydrawing.Imaging.ImageFormat, quality: int) -> None:
        '''Saves image to file with given page size, image format and quality.
        
        :param output_file: The file path and name to save the image.
        :param page_size: The page size of the image.
        :param format: The format of the image.
        :param quality: The Jpeg file's quality (0~100), 0 is lowest and 100 is highest'''
        ...
    
    def close(self) -> None:
        '''Close the instance of PdfConverter and release the resources.'''
        ...
    
    def do_convert(self) -> None:
        '''Do some initial works for converting a pdf document to images.'''
        ...
    
    def has_next_image(self) -> bool:
        '''Indicates whether the pdf file has more images or not.
        
        :returns: Can get more images or not, true if can, or false.'''
        ...
    
    @staticmethod
    def merge_images(self, input_images_streams, output_image_format: aspose.pdf.drawing.ImageFormat, merge_mode: aspose.pdf.facades.ImageMergeMode, horizontal: int, vertical: int) -> Any:
        '''Merges list of image streams as one image stream. Png/jpg/tiff outputs formats are supported, in case of using non supported format output stream encoded as Jpeg by default.
        
        :param input_images_streams: The list of image streams to merge.
        :param output_image_format: Image output format for merged stream.
        :param merge_mode: Merge mode. Used for Png/Jpg formats.
        :param horizontal: Horizontal ratio to set canvas width for output image stream. Used for Png/Jpg formats with ImageMergeMode.Center only.
        :param vertical: Vertical ratio to set canvas height for output image stream. Used for Png/Jpg formats with ImageMergeMode.Center only.
        :returns: Image stream encoded as output image format.'''
        ...
    
    @staticmethod
    def merge_images_as_tiff(self, input_images_streams) -> Any:
        '''Merges list of tiff streams as one multiple frames tiff stream.
        
        :param input_images_streams: The list of tiff streams.
        :returns: Multiple frames tiff stream.'''
        ...
    
    @property
    def coordinate_type(self) -> aspose.pdf.PageCoordinateType:
        '''Gets or sets the page coordinate type (Media/Crop boxes). CropBox value is used by default.'''
        ...
    
    @coordinate_type.setter
    def coordinate_type(self, value: aspose.pdf.PageCoordinateType):
        ...
    
    @property
    def show_hidden_areas(self) -> bool:
        '''Gets or sets flag that controls visibility of hidden areas on the page.'''
        ...
    
    @show_hidden_areas.setter
    def show_hidden_areas(self, value: bool):
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
        '''Gets or sets resolution during convertting. The higher resolution, the slower convertting speed. The default value is 150.'''
        ...
    
    @resolution.setter
    def resolution(self, value: aspose.pdf.devices.Resolution):
        ...
    
    @property
    def start_page(self) -> int:
        '''Gets or sets start position which you want to convert. The minimal value is 1.'''
        ...
    
    @start_page.setter
    def start_page(self, value: int):
        ...
    
    @property
    def end_page(self) -> int:
        '''Gets or sets end position which you want to convert.'''
        ...
    
    @end_page.setter
    def end_page(self, value: int):
        ...
    
    @property
    def password(self) -> str:
        '''Gets or sets document OwnerPassword.'''
        ...
    
    @password.setter
    def password(self, value: str):
        ...
    
    @property
    def user_password(self) -> str:
        '''Gets or sets document UserPassword.'''
        ...
    
    @user_password.setter
    def user_password(self, value: str):
        ...
    
    @property
    def page_count(self) -> int:
        '''Gets the page count.'''
        ...
    
    ...

class PdfExtractor(aspose.pdf.facades.Facade):
    '''Class for extracting images and text from PDF document.'''
    
    @overload
    def __init__(self):
        '''Initializes new :class:`PdfExtractor` object.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfExtractor` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def bind_pdf(self, input_file: str) -> None:
        '''Bind input PDF file.
        
        :param input_file: PDF fiel to bind'''
        ...
    
    @overload
    def bind_pdf(self, input_stream: Any) -> None:
        '''Binds PDF document from stream.
        
        :param input_stream: Stream containing PDF document data'''
        ...
    
    @overload
    def extract_text(self) -> None:
        '''Extracts text from a Pdf document using Unicode encoding.'''
        ...
    
    @overload
    def extract_text(self, encoding: str) -> None:
        '''Extracts text from a Pdf document using specified encoding.
        
        :param encoding: The encoding of the extracted text.'''
        ...
    
    @overload
    def get_text(self, output_file: str) -> None:
        '''Saves text to file. see also::meth:`PdfExtractor.extract_text`
        
        :param output_file: The file path and name to save the text.'''
        ...
    
    @overload
    def get_text(self, output_stream: Any) -> None:
        '''Saves text to stream. see also::meth:`PdfExtractor.extract_text`
        
        :param output_stream: The stream to save the text.'''
        ...
    
    @overload
    def get_text(self, output_stream: Any, filter_not_ascii: bool) -> None:
        '''Saves text to stream. see also::meth:`PdfExtractor.extract_text`
        
        :param output_stream: The stream to save the text.
        :param filter_not_ascii: If this parameter is true all Not ASCII simbols will be removed'''
        ...
    
    @overload
    def get_next_image(self, output_file: str) -> bool:
        '''Retreives next image from PDF document. Note: ExtractImage must be called before using of this method.
        
        :param output_file: File where image will be stored
        :returns: True is image is successfully extracted'''
        ...
    
    @overload
    def get_next_image(self, output_file: str, format: aspose.pydrawing.Imaging.ImageFormat) -> bool:
        '''Retreives next image from PDF document with given image format. Note: ExtractImage must be called before using of this method.
        
        :param output_file: File where image will be stored
        :param format: The format of the image.
        :returns: True is image is successfully extracted'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any, format: aspose.pydrawing.Imaging.ImageFormat) -> bool:
        '''Retreive next image from PDF file and stores it into stream with given image format.
        
        :param output_stream: Stream where image data will be saved
        :param format: The format of the image.
        :returns: True in case the image is successfully extracted.'''
        ...
    
    @overload
    def get_next_image(self, output_stream: Any) -> bool:
        '''Retreive next image from PDF file and stores it into stream.
        
        :param output_stream: Stream where image data will be saved
        :returns: True in case the image is successfully extracted.'''
        ...
    
    @overload
    def extract_attachment(self) -> None:
        '''Extracts attachments from a Pdf document.'''
        ...
    
    @overload
    def extract_attachment(self, attachment_file_name: str) -> None:
        '''Extracts attachment to PDF file by attachment name.
        
        :param attachment_file_name: Name of attachment to extract'''
        ...
    
    @overload
    def get_next_page_text(self, output_file: str) -> None:
        '''Saves one page's text to file.
        
        :param output_file: The file path and name to save the text.'''
        ...
    
    @overload
    def get_next_page_text(self, output_stream: Any) -> None:
        '''Saves one page's text to stream.
        
        :param output_stream: The stream to save the text.'''
        ...
    
    def extract_image(self) -> None:
        '''Extract images from PDF file.'''
        ...
    
    def has_next_image(self) -> bool:
        '''Checks if more images are accessible in PDF document. Note: ExtractImage must be called before using of this method.
        
        :returns: Trues if more images are accessible'''
        ...
    
    def get_attach_names(self) -> list[str]:
        '''Returns list of attachments in PDF file. Note: ExtractAttachments must be called befor using this method.
        
        :returns: List of attachments'''
        ...
    
    def get_attachment(self, output_path: str) -> None:
        '''Stores attachment into file.
        
        :param output_path: Directory path where attachment(s) will be stored.
                            Null or empty string means attachment(s) will be placed in the application directory.'''
        ...
    
    def has_next_page_text(self) -> bool:
        '''Indicates that whether can get more texts or not.
        
        :returns: Can get more texts or not, true is can, or false.'''
        ...
    
    def get_attachment_info(self) -> None:
        '''Gets the list of attachments.
        
        :returns: Returns a List\<FileSpecificatio\>\>.'''
        ...
    
    @property
    def start_page(self) -> int:
        '''Gets or sets start page in the page range where extracting operation will be performed.'''
        ...
    
    @start_page.setter
    def start_page(self, value: int):
        ...
    
    @property
    def end_page(self) -> int:
        '''Gets or sets end page in the page range where extracting operation will be performed.'''
        ...
    
    @end_page.setter
    def end_page(self, value: int):
        ...
    
    @property
    def extract_text_mode(self) -> int:
        '''Sets the mode for extract text's result.'''
        ...
    
    @extract_text_mode.setter
    def extract_text_mode(self, value: int):
        ...
    
    @property
    def text_search_options(self) -> aspose.pdf.text.TextSearchOptions:
        '''Gets or sets text search options.'''
        ...
    
    @text_search_options.setter
    def text_search_options(self, value: aspose.pdf.text.TextSearchOptions):
        ...
    
    @property
    def extract_image_mode(self) -> aspose.pdf.ExtractImageMode:
        '''Sets the mode for extract images process.
        
        Default value is ExtractImageMode.DefinedInResources that extracts all images defined in resources.
        
        To extract actually shown images ExtractImageMode.ActuallyUsed mode should be used.'''
        ...
    
    @extract_image_mode.setter
    def extract_image_mode(self, value: aspose.pdf.ExtractImageMode):
        ...
    
    @property
    def is_bidi(self) -> bool:
        '''Is true when text has hebriew or arabic symbols. This case must be specially considered because
        string functions change their behaviour and start process text from right to left (except numbers
        and other non text chars).'''
        ...
    
    @property
    def resolution(self) -> int:
        '''Set or gets resolution for extracted images.
        Default value is 150.
        Images which have greater resolution value are more clear.
        However increasing resolution value results in increasing time and memory needed to extract images.
        Usually to get clear image it's enough to set resolution to 150 or 300.'''
        ...
    
    @resolution.setter
    def resolution(self, value: int):
        ...
    
    @property
    def password(self) -> str:
        '''Gets or sets input file's password.'''
        ...
    
    @password.setter
    def password(self, value: str):
        ...
    
    ...

class PdfFileEditor:
    '''Implements operations with PDF file: concatenation, splitting, extracting pages, making booklet, etc.'''
    
    def __init__(self):
        ...
    
    @overload
    def try_concatenate(self, first_input_file: str, sec_input_file: str, output_file: str) -> bool:
        '''Concatenates two files.
        
        :param first_input_file: First file to concatenate.
        :param sec_input_file: Second file to concatenate.
        :param output_file: Output file.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryConcatenate method is like the Concatenate method, except the TryConcatenate
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_concatenate(self, src: list[aspose.pdf.Document], dest: aspose.pdf.Document) -> bool:
        '''Concatenates documents.
        
        :param src: Array of source documents.
        :param dest: Destination document.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryConcatenate method is like the Concatenate method,
        except the TryConcatenate method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_concatenate(self, input_files: list[str], output_file: str) -> bool:
        '''Concatenates files into one file.
        
        :param input_files: Array of files to concatenate.
        :param output_file: Name of output file.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryConcatenate method is like the Concatenate method,
        except the TryConcatenate method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_concatenate(self, input_stream: list[Any], output_stream: Any) -> bool:
        '''Concatenates files
        
        :param input_stream: Array of streams to be concatenated.
        :param output_stream: Stream where result file will be stored.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryConcatenate method is like the Concatenate method,
        except the TryConcatenate method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_concatenate(self, first_input_file: str, sec_input_file: str, blank_page_file: str, output_file: str) -> bool:
        '''Merges two Pdf documents into a new Pdf document with pages in alternate ways and fill the blank places with blank pages.
        e.g.: document1 has 5 pages: p1, p2, p3, p4, p5. document2 has 3 pages: p1', p2', p3'.
        Merging the two Pdf document will produce the result document with pages:p1, p1', p2, p2', p3, p3', p4, blankpage, p5, blankpage.
        
        :param first_input_file: First file.
        :param sec_input_file: Second file.
        :param blank_page_file: PDF file with blank page.
        :param output_file: Result file.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryConcatenate method is like the Concatenate
        method, except the TryConcatenate method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_concatenate(self, first_input_stream: Any, sec_input_stream: Any, blank_page_stream: Any, output_stream: Any) -> bool:
        '''Merges two Pdf documents into a new Pdf document with pages in alternate ways and fill the blank places with blank pages.
        e.g.: document1 has 5 pages: p1, p2, p3, p4, p5. document2 has 3 pages: p1', p2', p3'.
        Merging the two Pdf document will produce the result document with pages:p1, p1', p2, p2', p3, p3', p4, blankpage, p5, blankpage.
        
        :param first_input_stream: The first Pdf Stream.
        :param sec_input_stream: The second Pdf Stream.
        :param blank_page_stream: The Pdf Stream with blank page.
        :param output_stream: Output Pdf Stream.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryConcatenate method is like the Concatenate
        method, except the TryConcatenate method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_append(self, input_stream: Any, port_streams: list[Any], start_page: int, end_page: int, output_stream: Any) -> bool:
        '''Appends pages, which are chosen from array of documents in portStreams.
        The result document includes firstInputFile and all portStreams documents pages in the range startPage to endPage.
        
        :param input_stream: Input Pdf stream.
        :param port_streams: Documents to copy pages from.
        :param start_page: Page starts in portStreams documents.
        :param end_page: Page ends in portStreams documents .
        :param output_stream: Output Pdf stream.
        :returns: True for success, or false.
        
        The TryAppend method is like the Append method, except the TryAppend
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_append(self, input_file: str, port_files: list[str], start_page: int, end_page: int, output_file: str) -> bool:
        '''Appends pages, which are chosen from portFiles documents.
        The result document includes firstInputFile and all portFiles documents pages in the range startPage to endPage.
        
        :param input_file: Input Pdf file.
        :param port_files: Documents to copy pages from.
        :param start_page: Page starts in portFiles documents.
        :param end_page: Page ends in portFiles documents .
        :param output_file: Output Pdf document.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryAppend method is like the Append method, except the TryAppend
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_insert(self, input_file: str, insert_location: int, port_file: str, page_number: list[int], output_file: str) -> bool:
        '''Inserts pages from an other file into the input Pdf file.
        
        :param input_file: Input Pdf file.
        :param insert_location: Insert position in input file.
        :param port_file: Pages from the Pdf file.
        :param page_number: The page number of the ported in portFile.
        :param output_file: Output Pdf file.
        :returns: True for success, or false.
        
        The TryInsert method is like the Insert method, except the TryInsert
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_insert(self, input_stream: Any, insert_location: int, port_stream: Any, page_number: list[int], output_stream: Any) -> bool:
        '''Inserts pages from an other file into the input Pdf file.
        
        :param input_stream: Input Stream of  Pdf file.
        :param insert_location: Insert position in input file.
        :param port_stream: Stream of Pdf file for pages.
        :param page_number: The page number of the ported in portFile.
        :param output_stream: Output Stream.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryInsert method is like the Insert method, except the TryInsert
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_delete(self, input_file: str, page_number: list[int], output_file: str) -> bool:
        '''Deletes pages specified by number array from input file, saves as a new Pdf file.
        
        :param input_file: Input file path.
        :param page_number: Index of page out of the input file.
        :param output_file: Output file path.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryDelete method is like the Delete method, except the TryDelete
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_delete(self, input_stream: Any, page_number: list[int], output_stream: Any) -> bool:
        '''Deletes pages specified by number array from input file, saves as a new Pdf file.
        
        :param input_stream: Input file Stream.
        :param page_number: Index of page out of the input file.
        :param output_stream: Output file stream.
        :returns: True for success, or false.
        
        The TryDelete method is like the Delete method, except the TryDelete
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_extract(self, input_file: str, start_page: int, end_page: int, output_file: str) -> bool:
        '''Extracts pages from input file,saves as a new Pdf file.
        
        :param input_file: Input Pdf file path.
        :param start_page: Start page number.
        :param end_page: End page number.
        :param output_file: Output Pdf file path.
        :returns: True for success, or false.
        
        The TryExtract method is like the Extract method, except the TryExtract
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_extract(self, input_file: str, page_number: list[int], output_file: str) -> bool:
        '''Extracts pages specified by number array, saves as a new PDF file.
        
        :param input_file: Input file path.
        :param page_number: Index of page out of the input file.
        :param output_file: Output file path.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryExtract method is like the Extract method, except the TryExtract
        method does not throw an exception if the operation fails.
        
        :returns:'''
        ...
    
    @overload
    def try_extract(self, input_stream: Any, page_number: list[int], output_stream: Any) -> bool:
        '''Extracts pages specified by number array, saves as a new Pdf file.
        
        :param input_stream: Input file Stream.
        :param page_number: Index of page out of the input file.
        :param output_stream: Output file stream.
        :returns: True for success, or false.
        
        The TryExtract method is like the Extract method, except the TryExtract
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_split_from_first(self, input_file: str, location: int, output_file: str) -> bool:
        '''Splits Pdf file from first page to specified location,and saves the front part as a new file.
        
        :param input_file: Source Pdf file.
        :param location: The splitting point.
        :param output_file: Output Pdf file.
        :returns: True for success, or false.
        
        The TrySplitFromFirst method is like the SplitFromFirst
        method, except the TrySplitFromFirst method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_split_from_first(self, input_stream: Any, location: int, output_stream: Any) -> bool:
        '''Splits from start to specified location,and saves the front part in output Stream.
        
        :param input_stream: Source Pdf file Stream.
        :param location: The splitting point.
        :param output_stream: Output file Stream.
        :returns: True for success, or false.
        
        The streams are NOT closed after this operation.
        The TrySplitFromFirst method is like the SplitFromFirst method, except the TrySplitFromFirst
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_split_to_end(self, input_file: str, location: int, output_file: str) -> bool:
        '''Splits from location, and saves the rear part as a new file.
        
        :param input_file: Source Pdf file.
        :param location: The splitting position.
        :param output_file: Output Pdf file path.
        :returns: True for success, or false.
        
        The TrySplitToEnd method is like the SplitToEnd method, except the TrySplitToEnd
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_split_to_end(self, input_stream: Any, location: int, output_stream: Any) -> bool:
        '''Splits from specified location, and saves the rear part as a new file Stream.
        
        :param input_stream: Source Pdf file Stream.
        :param location: The splitting position.
        :param output_stream: Output Pdf file Stream.
        :returns: True for success, or false.
        
        The streams are NOT closed after this operation unless CloseConcatedStreams is specified.
        The TrySplitToEnd method is like the SplitToEnd method, except the TrySplitToEnd
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_booklet(self, input_file: str, output_file: str) -> bool:
        '''Makes booklet from the input file to output file.
        
        :param input_file: Input pdf file path and name.
        :param output_file: Output pdf file path and name.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeBooklet method is like the MakeBooklet method, except the TryMakeBooklet
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_booklet(self, input_stream: Any, output_stream: Any) -> bool:
        '''Makes booklet from the InputStream to outputStream.
        
        :param input_stream: Input pdf stream.
        :param output_stream: output pdf stream.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeBooklet method is like the MakeBooklet method, except the TryMakeBooklet
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_booklet(self, input_file: str, output_file: str, page_size: aspose.pdf.PageSize) -> bool:
        '''Makes booklet from the inputFile to outputFile.
        
        :param input_file: Input pdf file path and name.
        :param output_file: Output pdf file path and name.
        :param page_size: The page size of the output pdf file.
        :returns: True if operation is succeeded.
        
        The TryMakeBooklet method is like the MakeBooklet method, except the TryMakeBooklet
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_booklet(self, input_stream: Any, output_stream: Any, page_size: aspose.pdf.PageSize) -> bool:
        '''Makes booklet from the input stream and save result into output stream.
        
        :param input_stream: Input PDF stream.
        :param output_stream: output pdf stream.
        :param page_size: The page size of the output pdf file.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeBooklet method is like the MakeBooklet method, except the TryMakeBooklet
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_booklet(self, input_file: str, output_file: str, left_pages: list[int], right_pages: list[int]) -> bool:
        '''Makes customized booklet from the firstInputFile to outputFile.
        
        :param input_file: The input file.
        :param output_file: Output pdf file path and name.
        :param left_pages: The left pages of the booklet.
        :param right_pages: The right pages of the booklet.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeBooklet method is like the MakeBooklet method, except the TryMakeBooklet
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_booklet(self, input_stream: Any, output_stream: Any, left_pages: list[int], right_pages: list[int]) -> bool:
        '''Makes customized booklet from the firstInputStream to outputStream.
        
        :param input_stream: The input stream.
        :param output_stream: output pdf stream.
        :param left_pages: The left pages.
        :param right_pages: The right pages.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeBooklet method is like the MakeBooklet method, except the TryMakeBooklet
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_booklet(self, input_file: str, output_file: str, page_size: aspose.pdf.PageSize, left_pages: list[int], right_pages: list[int]) -> bool:
        '''Makes customized booklet from the firstInputFile to outputFile.
        
        :param input_file: The input file.
        :param output_file: Output pdf file path and name.
        :param page_size: The page size of the output pdf file.
        :param left_pages: The left pages.
        :param right_pages: The right pages.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeBooklet method is like the MakeBooklet method, except the TryMakeBooklet
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_booklet(self, input_stream: Any, output_stream: Any, page_size: aspose.pdf.PageSize, left_pages: list[int], right_pages: list[int]) -> bool:
        '''Makes booklet from the firstInputStream to outputStream.
        
        :param input_stream: The input stream.
        :param output_stream: output pdf stream.
        :param page_size: The page size of the output pdf file.
        :param left_pages: The left pages.
        :param right_pages: The right pages.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeBooklet method is like the MakeBooklet method, except the TryMakeBooklet
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_n_up(self, input_file: str, output_file: str, x: int, y: int) -> bool:
        '''Makes N-Up document from the firstInputFile to outputFile.
        
        :param input_file: Input pdf file path and name.
        :param output_file: Output pdf file path and name.
        :param x: Number of columns.
        :param y: Number of rows.
        :returns: true if operation was completed successfully; otherwise, false.
        
        The TryMakeNUp method is like the MakeNUp method, except the TryMakeNUp
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_n_up(self, input_stream: Any, output_stream: Any, x: int, y: int) -> bool:
        '''Makes N-Up document from the input stream and saves result into output stream.
        
        :param input_stream: Input pdf stream.
        :param output_stream: Output pdf stream.
        :param x: Number of columns.
        :param y: Number of rows.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeNUp method is like the MakeNUp method, except the TryMakeNUp
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_n_up(self, input_stream: Any, output_stream: Any, x: int, y: int, page_size: aspose.pdf.PageSize) -> bool:
        '''Makes N-Up document from the first input stream to output stream.
        
        :param input_stream: Input pdf stream.
        :param output_stream: Output pdf stream.
        :param x: Number of columns.
        :param y: Number of rows.
        :param page_size: The page size of the output pdf file.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeNUp method is like the MakeNUp method, except the TryMakeNUp
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_n_up(self, first_input_file: str, second_input_file: str, output_file: str) -> bool:
        '''Makes N-Up document from the two input PDF files to outputFile.
        Each page of outputFile will contain two pages, one page is from the first input file
        and another is from the second input file. The two pages are piled up horizontally.
        
        :param first_input_file: first input file.
        :param second_input_file: second input file.
        :param output_file: Output pdf file path and name.
        :returns: true if operation was completed successfully; otherwise, false
        
        The TryMakeNUp method is like the MakeNUp method, except the TryMakeNUp
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_n_up(self, first_input_stream: Any, second_input_stream: Any, output_stream: Any) -> bool:
        '''Makes N-Up document from the two input PDF streams to outputStream.
        
        :param first_input_stream: first input stream.
        :param second_input_stream: second input stream.
        :param output_stream: Output pdf stream.
        :returns: true if operation was completed successfully; otherwise, false
        
        The TryMakeNUp method is like the MakeNUp method, except the TryMakeNUp
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_n_up(self, input_files: list[str], output_file: str, is_sidewise: bool) -> bool:
        '''Makes N-Up document from the multi input PDF files to outputFile.
        Each page of outputFile will contain multi pages, which are combination with pages
        in the input files of the same page number. The multi pages piled up horizontally
        if isSidewise is true and piled up vertically if isSidewise is false.
        
        :param input_files: Input Pdf files.
        :param output_file: Output pdf file path and name.
        :param is_sidewise: Piled up way, true for horizontally and false for vertically.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeNUp method is like the MakeNUp method, except the TryMakeNUp
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_n_up(self, input_streams: list[Any], output_stream: Any, is_sidewise: bool) -> bool:
        '''Makes N-Up document from the multi input PDF streams to outputStream.
        Each page of outputStream will contain multi pages, which are combination with pages
        in the input streams of the same page number. The multi-pages piled up horizontally
        if isSidewise is true and piled up vertically if isSidewise is false.
        
        :param input_streams: Input Pdf streams.
        :param output_stream: Output pdf stream.
        :param is_sidewise: Piled up way, true for horizontally and false for vertically.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeNUp method is like the MakeNUp method, except the TryMakeNUp
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_make_n_up(self, input_file: str, output_file: str, x: int, y: int, page_size: aspose.pdf.PageSize) -> bool:
        '''Makes N-Up document from the input file to outputFile.
        
        :param input_file: Input pdf file path and name.
        :param output_file: Output pdf file path and name.
        :param x: Number of columns.
        :param y: Number of rows.
        :param page_size: The page size of the output pdf file.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryMakeNUp method is like the MakeNUp method, except the TryMakeNUp
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_resize_contents(self, source: Any, destination: Any, pages: list[int], parameters) -> bool:
        '''Resizes contents of pages of the document.
        
        :param source: Stream with source document.
        :param destination: Stream with the destination document.
        :param pages: Array of page indexes.
        :param parameters: Resize parameters.
        :returns: Returns true if success.
        
        The TryResizeContents method is like the ResizeContents method, except the TryResizeContents
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_resize_contents(self, source: Any, destination: Any, pages: list[int], new_width: float, new_height: float) -> bool:
        '''Resizes contents of document pages.
        Shrinks contents of page and adds margins.
        New size of contents is specified in default space units.
        
        :param source: Stream which contains source document.
        :param destination: Stream where resultant document will be saved.
        :param pages: Array of page indexes. If null then all document pages will be processed.
        :param new_width: New width of page contents in default space units.
        :param new_height: New height of page contents in default space units.
        :returns: true if operation completed successfully; otherwise, false.
        
        The TryResizeContents method is like the ResizeContents method, except the TryResizeContents
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def try_resize_contents(self, source: str, destination: str, pages: list[int], parameters) -> bool:
        '''Resizes contents of pages in document. If page is shrinked blank margins are added around the page.
        
        :param source: Source document path.
        :param destination: Destination document path.
        :param pages: Array of page indexes (page index starts from 1).
        :param parameters: Parameters of page resize.
        :returns: true if resize was successful.
        
        The TryResizeContents method is like the ResizeContents method, except the TryResizeContents
        method does not throw an exception if the operation fails.'''
        ...
    
    @overload
    def concatenate(self, first_input_file: str, sec_input_file: str, output_file: str) -> bool:
        '''Concatenates two files.
        
        :param first_input_file: First file to concatenate.
        :param sec_input_file: Second file to concatenate.
        :param output_file: Output file.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def concatenate(self, first_input_stream: Any, sec_input_stream: Any, output_stream: Any) -> bool:
        '''Concatenates two files.
        
        :param first_input_stream: Stream of first file.
        :param sec_input_stream: Stream of second file.
        :param output_stream: Stream where result file will be stored.
        :returns: True if operation was succeeded.
        
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def concatenate(self, src: list[aspose.pdf.Document], dest: aspose.pdf.Document) -> bool:
        '''Concatenates documents.
        
        :param src: Array of source documents.
        :param dest: Destination document.
        :returns: True if concatenation is successful.'''
        ...
    
    @overload
    def concatenate(self, input_files: list[str], output_file: str) -> bool:
        '''Concatenates files into one file.
        
        :param input_files: Array of files to concatenate.
        :param output_file: Name of output file.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def concatenate(self, input_stream: list[Any], output_stream: Any) -> bool:
        '''Concatenates files
        
        :param input_stream: Array of streams to be concatenated.
        :param output_stream: Stream where result file will be stored.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def concatenate(self, first_input_file: str, sec_input_file: str, blank_page_file: str, output_file: str) -> bool:
        '''Merges two Pdf documents into a new Pdf document with pages in alternate ways and fill the blank places with blank pages.
        e.g.: document1 has 5 pages: p1, p2, p3, p4, p5. document2 has 3 pages: p1', p2', p3'.
        Merging the two Pdf document will produce the result document with pages:p1, p1', p2, p2', p3, p3', p4, blankpage, p5, blankpage.
        
        :param first_input_file: First file.
        :param sec_input_file: Second file.
        :param blank_page_file: PDF file with blank page.
        :param output_file: Result file.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def concatenate(self, first_input_stream: Any, sec_input_stream: Any, blank_page_stream: Any, output_stream: Any) -> bool:
        '''Merges two Pdf documents into a new Pdf document with pages in alternate ways and fill the blank places with blank pages.
        e.g.: document1 has 5 pages: p1, p2, p3, p4, p5. document2 has 3 pages: p1', p2', p3'.
        Merging the two Pdf document will produce the result document with pages:p1, p1', p2, p2', p3, p3', p4, blankpage, p5, blankpage.
        
        :param first_input_stream: The first Pdf Stream.
        :param sec_input_stream: The second Pdf Stream.
        :param blank_page_stream: The Pdf Stream with blank page.
        :param output_stream: Output Pdf Stream.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def append(self, input_stream: Any, port_streams: list[Any], start_page: int, end_page: int, output_stream: Any) -> bool:
        '''Appends pages, which are chosen from array of documents in portStreams.
        The result document includes firstInputFile and all portStreams documents pages in the range startPage to endPage.
        
        :param input_stream: Input Pdf stream.
        :param port_streams: Documents to copy pages from.
        :param start_page: Page starts in portStreams documents.
        :param end_page: Page ends in portStreams documents .
        :param output_stream: Output Pdf stream.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def append(self, input_file: str, port_files: list[str], start_page: int, end_page: int, output_file: str) -> bool:
        '''Appends pages, which are chosen from portFiles documents.
        The result document includes firstInputFile and all portFiles documents pages in the range startPage to endPage.
        
        :param input_file: Input Pdf file.
        :param port_files: Documents to copy pages from.
        :param start_page: Page starts in portFiles documents.
        :param end_page: Page ends in portFiles documents .
        :param output_file: Output Pdf document.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def append(self, input_file: str, port_file: str, start_page: int, end_page: int, output_file: str) -> bool:
        '''Appends pages, which are chosen from portFile within the range from startPage to endPage, in portFile at the end of firstInputFile.
        
        :param input_file: Input Pdf file.
        :param port_file: Pages from Pdf file.
        :param start_page: Page starts in portFile.
        :param end_page: Page ends in portFile.
        :param output_file: Output Pdf document.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def append(self, input_stream: Any, port_stream: Any, start_page: int, end_page: int, output_stream: Any) -> bool:
        '''Appends pages,which are chosen from portStream within the range from startPage to endPage, in portStream at the end of firstInputStream.
        
        :param input_stream: Input file Stream.
        :param port_stream: Pages from Pdf file Stream.
        :param start_page: Page starts in portFile Stream.
        :param end_page: Page ends in portFile Stream.
        :param output_stream: Output Pdf file Stream.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def insert(self, input_file: str, insert_location: int, port_file: str, start_page: int, end_page: int, output_file: str) -> bool:
        '''Inserts pages from an other file into the Pdf file at a position.
        
        :param input_file: Input Pdf file.
        :param insert_location: Position in input file.
        :param port_file: The porting Pdf file.
        :param start_page: Start position in portFile.
        :param end_page: End position in portFile.
        :param output_file: Output Pdf file.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def insert(self, input_stream: Any, insert_location: int, port_stream: Any, start_page: int, end_page: int, output_stream: Any) -> bool:
        '''Inserts pages from an other file into the input Pdf file.
        
        :param input_stream: Input Stream of  Pdf file.
        :param insert_location: Insert position in input file.
        :param port_stream: Stream of Pdf file for pages.
        :param start_page: From which page to start.
        :param end_page: To which page to end.
        :param output_stream: Output Stream.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def insert(self, input_file: str, insert_location: int, port_file: str, page_number: list[int], output_file: str) -> bool:
        '''Inserts pages from an other file into the input Pdf file.
        
        :param input_file: Input Pdf file.
        :param insert_location: Insert position in input file.
        :param port_file: Pages from the Pdf file.
        :param page_number: The page number of the ported in portFile.
        :param output_file: Output Pdf file.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def insert(self, input_stream: Any, insert_location: int, port_stream: Any, page_number: list[int], output_stream: Any) -> bool:
        '''Inserts pages from an other file into the input Pdf file.
        
        :param input_stream: Input Stream of  Pdf file.
        :param insert_location: Insert position in input file.
        :param port_stream: Stream of Pdf file for pages.
        :param page_number: The page number of the ported in portFile.
        :param output_stream: Output Stream.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def delete(self, input_file: str, page_number: list[int], output_file: str) -> bool:
        '''Deletes pages specified by number array from input file, saves as a new Pdf file.
        
        :param input_file: Input file path.
        :param page_number: Index of page out of the input file.
        :param output_file: Output file path.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def delete(self, input_stream: Any, page_number: list[int], output_stream: Any) -> bool:
        '''Deletes pages specified by number array from input file, saves as a new Pdf file.
        
        :param input_stream: Input file Stream.
        :param page_number: Index of page out of the input file.
        :param output_stream: Output file stream.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def extract(self, input_file: str, start_page: int, end_page: int, output_file: str) -> bool:
        '''Extracts pages from input file,saves as a new Pdf file.
        
        :param input_file: Input Pdf file path.
        :param start_page: Start page number.
        :param end_page: End page number.
        :param output_file: Output Pdf file path.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def extract(self, input_file: str, page_number: list[int], output_file: str) -> bool:
        '''Extracts pages specified by number array, saves as a new PDF file.
        
        :param input_file: Input file path.
        :param page_number: Index of page out of the input file.
        :param output_file: Output file path.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def extract(self, input_stream: Any, start_page: int, end_page: int, output_stream: Any) -> bool:
        '''Extracts pages from input file,saves as a new Pdf file.
        
        :param input_stream: Input file Stream.
        :param start_page: Start page number.
        :param end_page: End page number.
        :param output_stream: Output Pdf file Stream.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def extract(self, input_stream: Any, page_number: list[int], output_stream: Any) -> bool:
        '''Extracts pages specified by number array, saves as a new Pdf file.
        
        :param input_stream: Input file Stream.
        :param page_number: Index of page out of the input file.
        :param output_stream: Output file stream.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def split_from_first(self, input_file: str, location: int, output_file: str) -> bool:
        '''Splits Pdf file from first page to specified location,and saves the front part as a new file.
        
        :param input_file: Source Pdf file.
        :param location: The splitting point.
        :param output_file: Output Pdf file.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def split_from_first(self, input_stream: Any, location: int, output_stream: Any) -> bool:
        '''Splits from start to specified location,and saves the front part in output Stream.
        
        :param input_stream: Source Pdf file Stream.
        :param location: The splitting point.
        :param output_stream: Output file Stream.
        :returns: True for success, or false.
        
        The streams are NOT closed after this operation.'''
        ...
    
    @overload
    def split_to_end(self, input_file: str, location: int, output_file: str) -> bool:
        '''Splits from location, and saves the rear part as a new file.
        
        :param input_file: Source Pdf file.
        :param location: The splitting position.
        :param output_file: Output Pdf file path.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def split_to_end(self, input_stream: Any, location: int, output_stream: Any) -> bool:
        '''Splits from specified location, and saves the rear part as a new file Stream.
        
        :param input_stream: Source Pdf file Stream.
        :param location: The splitting position.
        :param output_stream: Output Pdf file Stream.
        :returns: True for success, or false.
        
        The streams are NOT closed after this operation unless CloseConcatedStreams is specified.'''
        ...
    
    @overload
    def make_booklet(self, input_file: str, output_file: str) -> bool:
        '''Makes booklet from the input file to output file.
        
        :param input_file: Input pdf file path and name.
        :param output_file: Output pdf file path and name.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_booklet(self, input_stream: Any, output_stream: Any) -> bool:
        '''Makes booklet from the InputStream to outputStream.
        
        :param input_stream: Input pdf stream.
        :param output_stream: output pdf stream.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def make_booklet(self, input_file: str, output_file: str, page_size: aspose.pdf.PageSize) -> bool:
        '''Makes booklet from the inputFile to outputFile.
        
        :param input_file: Input pdf file path and name.
        :param output_file: Output pdf file path and name.
        :param page_size: The page size of the output pdf file.
        :returns: True if operation is succeeded.'''
        ...
    
    @overload
    def make_booklet(self, input_stream: Any, output_stream: Any, page_size: aspose.pdf.PageSize) -> bool:
        '''Makes booklet from the input stream and save result into output stream.
        
        :param input_stream: Input PDF stream.
        :param output_stream: output pdf stream.
        :param page_size: The page size of the output pdf file.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def make_booklet(self, input_file: str, output_file: str, left_pages: list[int], right_pages: list[int]) -> bool:
        '''Makes customized booklet from the firstInputFile to outputFile.
        
        :param input_file: The input file.
        :param output_file: Output pdf file path and name.
        :param left_pages: The left pages of the booklet.
        :param right_pages: The right pages of the booklet.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_booklet(self, input_stream: Any, output_stream: Any, left_pages: list[int], right_pages: list[int]) -> bool:
        '''Makes customized booklet from the firstInputStream to outputStream.
        
        :param input_stream: The input stream.
        :param output_stream: output pdf stream.
        :param left_pages: The left pages.
        :param right_pages: The right pages.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_booklet(self, input_file: str, output_file: str, page_size: aspose.pdf.PageSize, left_pages: list[int], right_pages: list[int]) -> bool:
        '''Makes customized booklet from the firstInputFile to outputFile.
        
        :param input_file: The input file.
        :param output_file: Output pdf file path and name.
        :param page_size: The page size of the output pdf file.
        :param left_pages: The left pages.
        :param right_pages: The right pages.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_booklet(self, input_stream: Any, output_stream: Any, page_size: aspose.pdf.PageSize, left_pages: list[int], right_pages: list[int]) -> bool:
        '''Makes booklet from the firstInputStream to outputStream.
        
        :param input_stream: The input stream.
        :param output_stream: output pdf stream.
        :param page_size: The page size of the output pdf file.
        :param left_pages: The left pages.
        :param right_pages: The right pages.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_n_up(self, input_file: str, output_file: str, x: int, y: int) -> bool:
        '''Makes N-Up document from the firstInputFile to outputFile.
        
        :param input_file: Input pdf file path and name.
        :param output_file: Output pdf file path and name.
        :param x: Number of columns.
        :param y: Number of rows.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_n_up(self, input_stream: Any, output_stream: Any, x: int, y: int) -> bool:
        '''Makes N-Up document from the input stream and saves result into output stream.
        
        :param input_stream: Input pdf stream.
        :param output_stream: Output pdf stream.
        :param x: Number of columns.
        :param y: Number of rows.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_n_up(self, input_stream: Any, output_stream: Any, x: int, y: int, page_size: aspose.pdf.PageSize) -> bool:
        '''Makes N-Up document from the first input stream to output stream.
        
        :param input_stream: Input pdf stream.
        :param output_stream: Output pdf stream.
        :param x: Number of columns.
        :param y: Number of rows.
        :param page_size: The page size of the output pdf file.
        :returns: True if operation was succeeded.'''
        ...
    
    @overload
    def make_n_up(self, first_input_file: str, second_input_file: str, output_file: str) -> bool:
        '''Makes N-Up document from the two input PDF files to outputFile.
        Each page of outputFile will contain two pages, one page is from the first input file
        and another is from the second input file. The two pages are piled up horizontally.
        
        :param first_input_file: first input file.
        :param second_input_file: second input file.
        :param output_file: Output pdf file path and name.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_n_up(self, first_input_stream: Any, second_input_stream: Any, output_stream: Any) -> bool:
        '''Makes N-Up document from the two input PDF streams to outputStream.
        
        :param first_input_stream: first input stream.
        :param second_input_stream: second input stream.
        :param output_stream: Output pdf stream.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_n_up(self, input_files: list[str], output_file: str, is_sidewise: bool) -> bool:
        '''Makes N-Up document from the multi input PDF files to outputFile.
        Each page of outputFile will contain multi pages, which are combination with pages
        in the input files of the same page number. The multi pages piled up horizontally
        if isSidewise is true and piled up vertically if isSidewise is false.
        
        :param input_files: Input Pdf files.
        :param output_file: Output pdf file path and name.
        :param is_sidewise: Piled up way, true for horizontally and false for vertically.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_n_up(self, input_streams: list[Any], output_stream: Any, is_sidewise: bool) -> bool:
        '''Makes N-Up document from the multi input PDF streams to outputStream.
        Each page of outputStream will contain multi pages, which are combination with pages
        in the input streams of the same page number. The multi-pages piled up horizontally
        if isSidewise is true and piled up vertically if isSidewise is false.
        
        :param input_streams: Input Pdf streams.
        :param output_stream: Output pdf stream.
        :param is_sidewise: Piled up way, true for horizontally and false for vertically.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def make_n_up(self, input_file: str, output_file: str, x: int, y: int, page_size: aspose.pdf.PageSize) -> bool:
        '''Makes N-Up document from the input file to outputFile.
        
        :param input_file: Input pdf file path and name.
        :param output_file: Output pdf file path and name.
        :param x: Number of columns.
        :param y: Number of rows.
        :param page_size: The page size of the output pdf file.
        :returns: boolean - True for success, or false.'''
        ...
    
    @overload
    def split_to_pages(self, input_file: str, file_name_template: str) -> None:
        '''Split the Pdf file into single-page documents and saves it into specified path. Path is specifield by field name temaplate.
        
        :param input_file: Input file name.
        :param file_name_template: Template of resultant file name. Must contain %NUM% which is replaced with page number. For example, if c:/dir/page%NUM%.pdf is specified, resultant files will have the following names: c:/dir/page1.pdf, c:/dir/page2.pdf etc.'''
        ...
    
    @overload
    def split_to_pages(self, input_stream: Any, file_name_template: str) -> None:
        '''Split the Pdf file into single-page documents and saves it into specified path. Path is specifield by field name temaplate.
        
        :param input_stream: Stream of the soruce document.
        :param file_name_template: Template of resultant file name. Must contain %NUM% which is replaced with page number. For example, if c:/dir/page%NUM%.pdf is specified, resultant files will have the following names: c:/dir/page1.pdf, c:/dir/page2.pdf etc.'''
        ...
    
    @overload
    def resize_contents(self, source: Any, destination: Any, pages: list[int], parameters) -> bool:
        '''Resizes contents of pages of the document.
        
        :param source: Stream with source document.
        :param destination: Stream with the destination document.
        :param pages: Array of page indexes.
        :param parameters: Resize parameters.
        :returns: Returns true if success.'''
        ...
    
    @overload
    def resize_contents(self, source: Any, destination: Any, pages: list[int], new_width: float, new_height: float) -> bool:
        '''Resizes contents of document pages.
        Shrinks contents of page and adds margins.
        New size of contents is specified in default space units.
        
        :param source: Stream which contains source document.
        :param destination: Stream where resultant document will be saved.
        :param pages: Array of page indexes. If null then all document pages will be processed.
        :param new_width: New width of page contents in default space units.
        :param new_height: New height of page contents in default space units.
        :returns: True if resize was successful.'''
        ...
    
    @overload
    def resize_contents(self, source: str, destination: str, pages: list[int], new_width: float, new_height: float) -> bool:
        '''Resizes contents of document pages.
        Shrinks contents of page and adds margins.
        New size of contents is specified in default space units.
        
        :param source: Path to source document.
        :param destination: Path where resultant document will be saved.
        :param pages: Array of page indexes. If null then all document pages will be processed.
        :param new_width: New width of page contents in default space units.
        :param new_height: New height of page contents in default space units.
        :returns: true if resize was successful.'''
        ...
    
    @overload
    def resize_contents(self, source: str, destination: str, pages: list[int], parameters) -> bool:
        '''Resizes contents of pages in document. If page is shrinked blank margins are added around the page.
        
        :param source: Source document path.
        :param destination: Destination document path.
        :param pages: Array of page indexes (page index starts from 1).
        :param parameters: Parameters of page resize.
        :returns: true if resize was successful.'''
        ...
    
    @overload
    def resize_contents(self, source: aspose.pdf.Document, pages: list[int], parameters) -> None:
        '''Resizes pages of document. Blank margins are added around of shrinked page.
        
        :param source: Source document.
        :param pages: List of page indexes.
        :param parameters: Resize parameters.'''
        ...
    
    @overload
    def resize_contents(self, source: aspose.pdf.Document, parameters) -> None:
        '''Resizes pages of document. Blank margins are added around of shrinked page.
        
        :param source: Source document.
        :param parameters: Resize parameters.'''
        ...
    
    @overload
    def resize_contents_pct(self, source: Any, destination: Any, pages: list[int], new_width: float, new_height: float) -> bool:
        '''Resizes contents of document pages.
        Shrinks contents of page and adds margins.
        New contents size is specified in percents.
        
        :param source: Stream which contains source document.
        :param destination: Stream where resultant document will be saved.
        :param pages: Array of page indexes. If null then all document pages will be processed.
        :param new_width: New width of page contents in percents.
        :param new_height: New height of page contents in percetns.
        :returns: true if resized sucessfully.'''
        ...
    
    @overload
    def resize_contents_pct(self, source: str, destination: str, pages: list[int], new_width: float, new_height: float) -> bool:
        '''Resizes contents of document pages.
        Shrinks contents of page and adds margins.
        New contents size is specified in percents.
        
        :param source: Path to source document.
        :param destination: Path where resultant document will be saved.
        :param pages: Array of page indexes. If null then all document pages will be processed.
        :param new_width: New width of page contents in percents.
        :param new_height: New height of page contents in percetns.
        :returns: true if resize was successful.'''
        ...
    
    @overload
    def add_margins(self, source: Any, destination: Any, pages: list[int], left_margin: float, right_margin: float, top_margin: float, bottom_margin: float) -> bool:
        '''Resizes page contents and add specifed margins.
        Margins are specified in default space units.
        
        :param source: Stream which contains source document.
        :param destination: Stream where resultant document will be saved.
        :param pages: Array of page indexes. If null then all document pages will be processed.
        :param left_margin: Left margin.
        :param right_margin: Right margin.
        :param top_margin: Top margin.
        :param bottom_margin: Bottom margin.
        :returns: true if operation was successful.'''
        ...
    
    @overload
    def add_margins(self, source: str, destination: str, pages: list[int], left_margin: float, right_margin: float, top_margin: float, bottom_margin: float) -> bool:
        '''Resizes page contents and add specifed margins.
        Margins are specified in default space units.
        
        :param source: Path to source document.
        :param destination: Path where resultant document will be saved.
        :param pages: Array of page indexes. If null then all document pages will be processed.
        :param left_margin: Left margin.
        :param right_margin: Right margin.
        :param top_margin: Top margin.
        :param bottom_margin: Bottom margin.
        :returns: true if resize was successful.'''
        ...
    
    @overload
    def add_margins_pct(self, source: Any, destination: Any, pages: list[int], left_margin: float, right_margin: float, top_margin: float, bottom_margin: float) -> bool:
        '''Resizes page contents and add specified margins.
        Margins are specified in percents of intitial page size.
        
        :param source: Stream which contains source document.
        :param destination: Stream where resultant document will be saved.
        :param pages: Array of page indexes. If null then all document pages will be processed.
        :param left_margin: Left margin in percents of initial page size.
        :param right_margin: Right margin in percents of initial page size.
        :param top_margin: Top margin in percents of initial page size.
        :param bottom_margin: Bottom margin in percents of initial page size.
        :returns: true if action was performed successfully.'''
        ...
    
    @overload
    def add_margins_pct(self, source: str, destination: str, pages: list[int], left_margin: float, right_margin: float, top_margin: float, bottom_margin: float) -> bool:
        '''Resizes page contents and add specified margins.
        Margins are specified in percents of intitial page size.
        
        :param source: Path to source document.
        :param destination: Path where resultant document will be saved.
        :param pages: Array of page indexes. If null then all document pages will be processed.
        :param left_margin: Left margin in percents of initial page size.
        :param right_margin: Right margin in percents of initial page size.
        :param top_margin: Top margin in percents of initial page size.
        :param bottom_margin: Bottom margin in percents of initial page size.
        :returns: true if resize was successful'''
        ...
    
    @overload
    def add_page_break(self, src: aspose.pdf.Document, dest: aspose.pdf.Document, page_breaks) -> None:
        '''Adds page breaks into document pages.
        
        :param src: Source document.
        :param dest: Destination document.
        :param page_breaks: Array of PageBreak objects which describe places of page breaks.'''
        ...
    
    @overload
    def add_page_break(self, src: str, dest: str, page_breaks) -> None:
        '''Adds page breaks into document pages.
        
        :param src: Path to source document.
        :param dest: Path to destination document.
        :param page_breaks: Array of PageBreak object describing pages and places where page break will be added.'''
        ...
    
    @overload
    def add_page_break(self, src: Any, dest: Any, page_breaks) -> None:
        '''Adds page breaks into document pages.
        
        :param src: Source which contains source document.
        :param dest: Source where destination document will be saved.
        :param page_breaks: Array of PageBreak object describing pages and places where page break will be added.'''
        ...
    
    @property
    def conversion_log(self) -> str:
        '''Gets log of conversion process.'''
        ...
    
    @property
    def merge_duplicate_layers(self) -> bool:
        '''Optional contents of concatentated documents with equal names will be merged into one layer in resulstant document if this property is true.
        Else, layers with equal names will be save as different layers in resultant document.'''
        ...
    
    @merge_duplicate_layers.setter
    def merge_duplicate_layers(self, value: bool):
        ...
    
    @property
    def copy_outlines(self) -> bool:
        '''If true then outlines will be copied.'''
        ...
    
    @copy_outlines.setter
    def copy_outlines(self, value: bool):
        ...
    
    @property
    def copy_logical_structure(self) -> bool:
        '''If true then logical structure of the file is copied when concatenation is performed.'''
        ...
    
    @copy_logical_structure.setter
    def copy_logical_structure(self, value: bool):
        ...
    
    @property
    def merge_duplicate_outlines(self) -> bool:
        '''If true, duplicate outlines are merged.'''
        ...
    
    @merge_duplicate_outlines.setter
    def merge_duplicate_outlines(self, value: bool):
        ...
    
    @property
    def preserve_user_rights(self) -> bool:
        '''If true, user rights of first document are applied to concatenated document. User rights of all other documents are ignored.'''
        ...
    
    @preserve_user_rights.setter
    def preserve_user_rights(self, value: bool):
        ...
    
    @property
    def incremental_updates(self) -> bool:
        '''If true, incremental updates are made during concatenation.'''
        ...
    
    @incremental_updates.setter
    def incremental_updates(self, value: bool):
        ...
    
    @property
    def optimize_size(self) -> bool:
        '''Gets or sets optimization flag. Equal resource streams in resultant file are merged into one PDF object if this flag set.
        This allows to decrease resultant file size but may cause slower execution and larger memory requirements.
        Default value: false.'''
        ...
    
    @optimize_size.setter
    def optimize_size(self, value: bool):
        ...
    
    @property
    def corrupted_items(self) -> None:
        '''Array of encountered problems when concatenation was performed. For every corrupted document from passed to Concatenate()
        function new CorruptedItem entry is created.
        This property may be used only when CorruptedFileAction is ConcatenateIgnoringCorrupted.'''
        ...
    
    @property
    def corrupted_file_action(self) -> None:
        '''This property defines behavior when concatenating process met corrupted file.
        Possible values are: StopWithError and ConcatenateIgnoringCorrupted.'''
        ...
    
    @corrupted_file_action.setter
    def corrupted_file_action(self, value: None):
        ...
    
    @property
    def owner_password(self) -> str:
        '''Sets owner's password if the source input Pdf file is encrypted.
        This property is not implemented yet.'''
        ...
    
    @owner_password.setter
    def owner_password(self, value: str):
        ...
    
    @property
    def allow_concatenate_exceptions(self) -> bool:
        '''If set to true, exceptions are thrown if error occured. Else excetion are not thrown and methods return false if failed.'''
        ...
    
    @allow_concatenate_exceptions.setter
    def allow_concatenate_exceptions(self, value: bool):
        ...
    
    @property
    def close_concatenated_streams(self) -> bool:
        '''If set to true, streams are closed after operation.'''
        ...
    
    @close_concatenated_streams.setter
    def close_concatenated_streams(self, value: bool):
        ...
    
    @property
    def unique_suffix(self) -> str:
        '''Format of the suffix which is added to field name to make it unique when forms are concatenated.
        This string must contain %NUM% substring which will be replaced with numbers.
        For example if UniqueSuffix = "ABC%NUM%" then for field "fieldName" names will be:
        fieldNameABC1, fieldNameABC2, fieldNameABC3 etc.'''
        ...
    
    @unique_suffix.setter
    def unique_suffix(self, value: str):
        ...
    
    @property
    def keep_actions(self) -> bool:
        '''If true actions will be copied from source documents. Defaulkt value : true.'''
        ...
    
    @keep_actions.setter
    def keep_actions(self, value: bool):
        ...
    
    @property
    def keep_fields_unique(self) -> bool:
        '''If true then field names will be made unique when forms are concatenated.
        Suffixes will be added to field names, suffix template may be specified in UniqueSuffix property.'''
        ...
    
    @keep_fields_unique.setter
    def keep_fields_unique(self, value: bool):
        ...
    
    @property
    def remove_signatures(self) -> bool:
        '''If true, all signatures will be removed from fields (fields will remain); otherwise, you can get invalid signatures.'''
        ...
    
    @remove_signatures.setter
    def remove_signatures(self, value: bool):
        ...
    
    @property
    def use_disk_buffer(self) -> bool:
        '''If this option used then destination document will be saved on disk periodically and further concatenation will appllied to it as incremental updates.'''
        ...
    
    @use_disk_buffer.setter
    def use_disk_buffer(self, value: bool):
        ...
    
    @property
    def concatenation_packet_size(self) -> int:
        '''Number of documents concatenated before new incremental update was made during concatenation when UseDiskBuffer is set to true.'''
        ...
    
    @concatenation_packet_size.setter
    def concatenation_packet_size(self, value: int):
        ...
    
    class ContentsResizeParameters:
          '''Class for specifing page resize parameters. Allow to set the following parameters: 
             Size of result page (width, height) in default space units or in percents of initial pages size; 
             Left, Top, Bottom and Right margins in default space units or in percents of initial page size;
             Some values may be left null for automatic calculation. These values will be calculated 
             from rest of page size after calculation explicitly specified values.
             For example: if page width = 100 and new page width specified 60 units then 
             left and right margins are automatically calculated:(100 - 60) / 2 = 15.
             This class is used in ResizeContents method.'''

          
          def __init__(self):
              '''Creates resize parameters where al values are set to "auto". Later margins and contents size may be specified if required.'''
              ...
    
          def __init__(self, left_margin: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue, contents_width: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue, right_margin: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue, top_margin: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue, contents_height: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue, bottom_margin: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue):
              '''Creates resize parameters with specified margin values and contents size.
        
              :param left_margin: Left margin value..
              :param contents_width: Contents width.
              :param right_margin: Right margin.
              :param top_margin: Top margin.
              :param contents_height: Contents height.
              :param bottom_margin: Bottom margin.'''
              ...
    
          def margins(self, left: float, right: float, top: float, bottom: float) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeParameters: 
              '''Creates resize parameters with specifed margins value. Contents size is automatically calculated.
        
              :param left: Left margin.
              :param right: Right margin.
              :param top: Top margin.
              :param bottom: Bottom margin.
              :returns: Created resize parameters.'''
              ...

          def margins_percent(self, left: float, right: float, top: float, bottom: float) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeParameters: 
              '''Creates resize parameters. Margins are specified in percents of initial page size.
        
              :param left: Left margin (in percents of page width).
              :param right: Right margin (in percents of page height).
              :param top: Top margin (in percents of page height).
              :param bottom: Bottom margin (in percents of page height).
              :returns: Returns new resize parameters.'''
              ...

          def content_size(self, width: float, height: float) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeParameters: 
              '''Creates resize parameters with specified contents size.
        
              :param width: New width of contents.
              :param height: New height of contents.
              :returns: Returns new resize parameters.'''
              ...

          def content_size_percent(self, width: float, height: float) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeParameters: 
              '''Creates resize parameters with specified contents size in percents of initial page size. Margins are caculated automatically.
        
              :param width: New content width in percents.
              :param height: New content height in percents.
              :returns: New resize parameters.'''
              ...

          def page_resize(self, width: float, height: float) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeParameters: 
              '''Creates resize parameters for page resize. 
        
              :param width: New page width in units.
              :param height: New page height in units.
              :returns: New resize parameters.'''
              ...

          def page_resize_pct(self, width_pct: float, height_pct: float) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeParameters: 
              '''Creates resize parameters for page resize. New sizes are specified in percent. 
        
              :param width_pct: New page width in percents.
              :param height_pct: New page height in percents.
              :returns: New resize parameters.'''
              ...

          @property
          def left_margin(self) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeValue:
              '''Gets or sets left margin on the resultant page.'''
              ...
          @left_margin.setter
          def left_margin(self, value: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue):
              ...

          @property
          def right_margin(self) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeValue:
              '''Gets or sets right margin on the resultant page.'''
              ...
          @right_margin.setter
          def right_margin(self, value: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue):
              ...

          @property
          def top_margin(self) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeValue:
              '''Gets or sets top margin on the resultant page.'''
              ...
          @top_margin.setter
          def top_margin(self, value: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue):
              ...

          @property
          def bottom_margin(self) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeValue:
              '''Gets or sets bottom margin on the resultant page.'''
              ...
          @bottom_margin.setter
          def bottom_margin(self, value: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue):
              ...

          @property
          def contents_width(self) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeValue:
              '''Gets or sets width of the content of the source page on the resultant page.'''
              ...
          @contents_width.setter
          def contents_width(self, value: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue):
              ...

          @property
          def contents_height(self) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeValue:
              '''Gets or sets height of the content of the source page on the resultant page.'''
              ...
          @contents_height.setter
          def contents_height(self, value: aspose.pdf.facades.PdfFileEditor.ContentsResizeValue):
              ...

    class ContentsResizeValue:
          '''Value of margin or content size specified in percents of default space units. This class is used in ContentsResizeParameters.'''
    
          def percents(self, value: float) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeValue: 
              '''Initializes value in percents.
        
              :param value: Value in percents.
              :returns: New value instance.'''
              ...

          def units(self, value: float) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeValue: 
              '''Initializes value in default space units.
        
              :param value: Value in units.
              :returns: New value instance.'''
              ...

          def auto(self) -> aspose.pdf.facades.PdfFileEditor.ContentsResizeValue: 
              '''Initializes automatically calculated value.
     
              :returns: New value instance.'''
              ...

          @property
          def value(self) -> float:
              '''Gets specified value. Use Unit property to get value units.'''
              ...
          
          @property
          def is_percent(self) -> bool:
              '''Gets true if value is expressed in percents; False if value is expressed in default units.'''
              ...
          
          
    class CorruptedItem:
          '''Class which provides information about corrupted files in time of concatenation.'''

          @property
          def index(self) -> int:
              '''Index of corrupted file.'''
              ...
          
          
    class PageBreak:
          '''Data of page break position.'''

          def __init__(self,  page_number: int, position: float):
              '''Constructor to create PageBreak object.
        
              :param page_number: Number of page where page break is placed.
              :param position: Vertical position of page break.'''
              ...

          @property
          def page_number(self) -> int:
              '''Number of page (starting from 1) where page break must be added.'''
              ... 

          @page_number.setter
          def page_number(self, value: int):
              ...

          @property
          def position(self) -> float:
              '''Vertical position of page break.'''
              ...   

          @position.setter
          def position(self, value: float):
              ...   


    class ConcatenateCorruptedFileAction:
          '''Action performed when corrupted file was met in concatenation process.'''

          STOP_WITH_ERROR: ConcatenateCorruptedFileAction
          CONCATENATE_IGNORING_CORRUPTED: ConcatenateCorruptedFileAction
          CONCATENATE_IGNORING_CORRUPTED_OBJECTS: ConcatenateCorruptedFileAction

    ...

class PdfFileInfo(aspose.pdf.facades.SaveableFacade):
    '''Represents a class for accessing meta information of PDF document.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the Aspose.Pdf.Facades.PdfFileInfo class with default values.'''
        ...
    
    @overload
    def __init__(self, input_stream: Any):
        '''Initializes a new instance of the Aspose.Pdf.Facades.PdfFileInfo class.
        
        :param input_stream: Stream where input file is placed.'''
        ...
    
    @overload
    def __init__(self, input_stream: Any, password: str):
        '''Initializes a new instance of the Aspose.Pdf.Facades.PdfFileInfo class.
        
        :param input_stream: Stream where input file is placed.
        :param password: Password for access to file.'''
        ...
    
    @overload
    def __init__(self, input_file: str):
        '''Initializes a new instance of the Aspose.Pdf.Facades.PdfFileInfo class.
        
        :param input_file: Name of file containing input file.'''
        ...
    
    @overload
    def __init__(self, input_file: str, password: str):
        '''Initializes a new instance of the Aspose.Pdf.Facades.PdfFileInfo class.
        
        :param input_file: Name of file containing input file.
        :param password: Password for access to file.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfFileInfo` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def bind_pdf(self, src_doc: aspose.pdf.Document) -> None:
        '''Initializes the facade.
        
        :param src_doc: The Aspose.Pdf.Document object.'''
        ...
    
    @overload
    def save(self, dest_stream: Any) -> None:
        '''Saves the PDF document to the specified file.
        
        :param dest_stream: The destination stream.'''
        ...
    
    @overload
    def save(self, dest_file: str) -> None:
        '''Saves the PDF document to the specified file.
        
        :param dest_file: The destination file.'''
        ...
    
    @overload
    def save_new_info(self, output_stream: Any) -> bool:
        '''Save updated PDF document into specified stream.
        
        :param output_stream: Output stream.
        :returns: True if success otherwise is false.'''
        ...
    
    @overload
    def save_new_info(self, output_file: str) -> bool:
        '''Save updated PDF document into specified file.
        
        :param output_file: Output file.
        :returns: True if success otherwise is false.'''
        ...
    
    def close(self) -> None:
        '''Deinitializes the instance.'''
        ...
    
    def clear_info(self) -> None:
        '''Clears all meta information of PDF document.'''
        ...
    
    def get_document_privilege(self) -> aspose.pdf.facades.DocumentPrivilege:
        '''Gets the PDF document privilege settings.
        
        :returns: The PDF document privilege settings.'''
        ...
    
    def get_meta_info(self, name: str) -> str:
        '''Gets customized information of PDF document with property name. If there is no property match the name it will return a blank string.
        
        :param name: Custom meta property key.
        :returns: Custom meta property value.'''
        ...
    
    def get_page_height(self, page_num: int) -> float:
        '''Gets the height of the specified page.
        
        :param page_num: Page number.
        :returns: The height of the page.'''
        ...
    
    def get_page_rotation(self, page_num: int) -> int:
        '''Gets the rotation of the specified page.
        
        :param page_num: Page number.
        :returns: The rotation of the page. The value may be 0,90,180,270.'''
        ...
    
    def get_page_width(self, page_num: int) -> float:
        '''Gets the width of the specified page.
        
        :param page_num: Page number.
        :returns: The width of the page.'''
        ...
    
    def get_page_x_offset(self, page_num: int) -> float:
        '''Gets the horizontal offset of the specified page display area.
        
        :param page_num: Page number.
        :returns: The horizontal offset from the left side of the page.'''
        ...
    
    def get_page_y_offset(self, page_num: int) -> float:
        '''Gets the vertical offset of the specified page display area.
        
        :param page_num: Page number.
        :returns: The vertical offset of the page display area.'''
        ...
    
    def get_pdf_version(self) -> str:
        '''Gets the version info of PDF document.
        
        :returns: The version string.'''
        ...
    
    def set_meta_info(self, name: str, value: str) -> None:
        '''Sets customized information of PDF document.
        
        :param name: Custom meta property key.
        :param value: Custom meta property value.'''
        ...
    
    def save_new_info_with_xmp(self, output_file_name: str) -> bool:
        '''Changes the properties specified explicitly by setting file information, other properties remain.
        
        :param output_file_name: Output file.
        :returns: True for success, or false.'''
        ...
    
    @property
    def author(self) -> str:
        '''Gets or sets the Author information of PDF document.'''
        ...
    
    @author.setter
    def author(self, value: str):
        ...
    
    @property
    def is_encrypted(self) -> bool:
        '''Checkes whether the PDF document is encrypted.'''
        ...
    
    @property
    def is_pdf_file(self) -> bool:
        '''Checkes whether the source input is a valid PDF file.'''
        ...
    
    @property
    def use_strict_validation(self) -> bool:
        '''Uses strict validation rules via using :attr:`PdfFileInfo.is_pdf_file` property.'''
        ...
    
    @use_strict_validation.setter
    def use_strict_validation(self, value: bool):
        ...
    
    @property
    def creation_date(self) -> str:
        '''Gets or sets the CreationDate information of PDF document.'''
        ...
    
    @creation_date.setter
    def creation_date(self, value: str):
        ...
    
    @property
    def creator(self) -> str:
        '''Gets or sets the Creator information of PDF document.'''
        ...
    
    @creator.setter
    def creator(self, value: str):
        ...
    
    @property
    def has_collection(self) -> bool:
        '''Returns true if the current input file is a 'Portfolio' file containing collection of PDF files in it.'''
        ...
    
    @property
    def input_file(self) -> str:
        '''Gets or sets the input file.'''
        ...
    
    @input_file.setter
    def input_file(self, value: str):
        ...
    
    @property
    def input_stream(self) -> Any:
        '''Gets or sets the input stream.'''
        ...
    
    @input_stream.setter
    def input_stream(self, value: Any):
        ...
    
    @property
    def keywords(self) -> str:
        '''Gets or sets the Keywords information of PDF document.'''
        ...
    
    @keywords.setter
    def keywords(self, value: str):
        ...
    
    @property
    def mod_date(self) -> str:
        '''Gets or sets the ModDate date information of PDF document.'''
        ...
    
    @mod_date.setter
    def mod_date(self, value: str):
        ...
    
    @property
    def number_of_pages(self) -> int:
        '''Gets the number of document pages.'''
        ...
    
    @property
    def producer(self) -> str:
        '''Gets the Producer information of PDF document.'''
        ...
    
    @property
    def subject(self) -> str:
        '''Gets or sets the Subject information of PDF document.'''
        ...
    
    @subject.setter
    def subject(self, value: str):
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets the Title information of PDF document.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def password_type(self) -> aspose.pdf.PasswordType:
        '''Returns the type of password which was passed for creating PdfFileInfo instance. See possible values in :attr:`PdfFileInfo.password_type`.
        Pay attention that pdf document can be opened using both user (or open) password and owner (or permissions, edit) password.'''
        ...
    
    @property
    def has_open_password(self) -> bool:
        '''Returns true if password is needed to open password protected pdf document.'''
        ...
    
    @property
    def has_edit_password(self) -> bool:
        '''Returns true if password is needed to modify permissions or document security property.
        Pay attention that this property can be read only if valid password was provided in :class:`PdfFileInfo` constructor.
        In case PasswordType is Inaccessible (means that invalid password was provided) reading this property will fail with :class:`aspose.pdf.InvalidPasswordException`.'''
        ...
    
    ...

class PdfFileMend(aspose.pdf.facades.SaveableFacade):
    '''Represents a class for adding texts and images on the pages of existing PDF document.'''
    
    @overload
    def __init__(self):
        '''Constructor.'''
        ...
    
    @overload
    def __init__(self, input_file_name: str, output_file_name: str):
        '''Constructor.
        
        :param input_file_name: Input PDF file name.
        :param output_file_name: Output PDF file name.'''
        ...
    
    @overload
    def __init__(self, input_stream: Any, output_stream: Any):
        '''Constructor.
        
        :param input_stream: Input PDF stream.
        :param output_stream: Output PDF stream.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfFileMend` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, output_file_name: str):
        '''Initializes new :class:`PdfFileMend` object on base of the document.
        
        :param document: Pdf document.
        :param output_file_name: Output PDF file name.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, dest_stream: Any):
        '''Initializes new :class:`PdfFileMend` object on base of the document.
        
        :param document: Pdf document.
        :param dest_stream: Output PDF stream.'''
        ...
    
    @overload
    def save(self, dest_file: str) -> None:
        '''Saves the PDF document to the specified file.
        
        :param dest_file: The destination file.'''
        ...
    
    @overload
    def save(self, dest_stream: Any) -> None:
        '''Saves the PDF document to the specified stream.
        
        :param dest_stream: The destination stream.'''
        ...
    
    @overload
    def add_image(self, image_stream: Any, page_num: int, lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float) -> bool:
        '''Adds image to the specified page of PDF document at specified coordinates.
        
        :param image_stream: Input image stream.
        :param page_num: The number of page that will receive the image.
        :param lower_left_x: The lower left x of image rectangle.
        :param lower_left_y: The lower left y of image rectangle.
        :param upper_right_x: The upper right x of image rectangle.
        :param upper_right_y: The upper right y of image rectangle.
        :returns: True if success false otherwise.'''
        ...
    
    @overload
    def add_image(self, image_stream: Any, page_num: int, lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float, compositing_parameters: aspose.pdf.CompositingParameters) -> bool:
        '''Adds image to the specified page of PDF document at specified coordinates.
        
        :param image_stream: Input image stream.
        :param page_num: The number of page that will receive the image.
        :param lower_left_x: The lower left x of image rectangle.
        :param lower_left_y: The lower left y of image rectangle.
        :param upper_right_x: The upper right x of image rectangle.
        :param upper_right_y: The upper right y of image rectangle.
        :param compositing_parameters: The graphics compositing parameters for the image.
        :returns: True if success false otherwise.'''
        ...
    
    @overload
    def add_image(self, image_stream: Any, page_nums: list[int], lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float) -> bool:
        '''Adds image to the specified pages of PDF document at specified coordinates.
        
        :param image_stream: Input image stream.
        :param page_nums: The numbers of pages that will receive the image.
        :param lower_left_x: The lower left x of image rectangle.
        :param lower_left_y: The lower left y of image rectangle.
        :param upper_right_x: The upper right x of image rectangle.
        :param upper_right_y: The upper right y of image rectangle.
        :returns: True if success false otherwise.'''
        ...
    
    @overload
    def add_image(self, image_stream: Any, page_nums: list[int], lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float, compositing_parameters: aspose.pdf.CompositingParameters) -> bool:
        '''Adds image to the specified pages of PDF document at specified coordinates.
        
        :param image_stream: Input image stream.
        :param page_nums: The numbers of pages that will receive the image.
        :param lower_left_x: The lower left x of image rectangle.
        :param lower_left_y: The lower left y of image rectangle.
        :param upper_right_x: The upper right x of image rectangle.
        :param upper_right_y: The upper right y of image rectangle.
        :param compositing_parameters: The graphics compositing parameters for the images.
        :returns: True if success false otherwise.'''
        ...
    
    @overload
    def add_image(self, image_name: str, page_num: int, lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float) -> bool:
        '''Adds image to the specified page of PDF document at specified coordinates.
        
        :param image_name: The path of input image file.
        :param page_num: The number of page that will receive the image.
        :param lower_left_x: The lower left x of image rectangle.
        :param lower_left_y: The lower left y of image rectangle.
        :param upper_right_x: The upper right x of image rectangle.
        :param upper_right_y: The upper right y of image rectangle.
        :returns: True if success false otherwise.'''
        ...
    
    @overload
    def add_image(self, image_name: str, page_num: int, lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float, compositing_parameters: aspose.pdf.CompositingParameters) -> bool:
        '''Adds image to the specified page of PDF document at specified coordinates.
        
        :param image_name: The path of input image file.
        :param page_num: The number of page that will receive the image.
        :param lower_left_x: The lower left x of image rectangle.
        :param lower_left_y: The lower left y of image rectangle.
        :param upper_right_x: The upper right x of image rectangle.
        :param upper_right_y: The upper right y of image rectangle.
        :param compositing_parameters: The graphics compositing parameters for the images.
        :returns: True if success false otherwise.'''
        ...
    
    @overload
    def add_image(self, image_name: str, page_nums: list[int], lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float) -> bool:
        '''Adds image to the specified pages of PDF document at specified coordinates.
        
        :param image_name: The path of input image file.
        :param page_nums: The numbers of pages that will receive the image.
        :param lower_left_x: The lower left x of image rectangle.
        :param lower_left_y: The lower left y of image rectangle.
        :param upper_right_x: The upper right x of image rectangle.
        :param upper_right_y: The upper right y of image rectangle.
        :returns: True if success false otherwise.'''
        ...
    
    @overload
    def add_image(self, image_name: str, page_nums: list[int], lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float, compositing_parameters: aspose.pdf.CompositingParameters) -> bool:
        '''Adds image to the specified pages of PDF document at specified coordinates.
        
        :param image_name: The path of input image file.
        :param page_nums: The numbers of pages that will receive the image.
        :param lower_left_x: The lower left x of image rectangle.
        :param lower_left_y: The lower left y of image rectangle.
        :param upper_right_x: The upper right x of image rectangle.
        :param upper_right_y: The upper right y of image rectangle.
        :param compositing_parameters: The graphics compositing parameters for the images.
        :returns: True if success false otherwise.'''
        ...
    
    @overload
    def add_text(self, text: aspose.pdf.facades.FormattedText, page_num: int, lower_left_x: float, lower_left_y: float) -> bool:
        '''Not implemented.
        
        :param text: FormattedText object.
        :param page_num: Page number.
        :param lower_left_x: Lower left X coordinate.
        :param lower_left_y: Lower left Y coordinate.
        :returns: True in case text was successfully added.'''
        ...
    
    @overload
    def add_text(self, text: aspose.pdf.facades.FormattedText, page_num: int, lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float) -> bool:
        '''Not implemented.
        
        :param text: FormattedText object.
        :param page_num: Page number.
        :param lower_left_x: Lower left X coordinate.
        :param lower_left_y: Lower left Y coordinate.
        :param upper_right_x: Upper right X coordinate.
        :param upper_right_y: Upper right Y coordinate.
        :returns: True in case text was successfully added.'''
        ...
    
    @overload
    def add_text(self, text: aspose.pdf.facades.FormattedText, page_nums: list[int], lower_left_x: float, lower_left_y: float, upper_right_x: float, upper_right_y: float) -> bool:
        '''Not implemented.
        
        :param text: FormattedText object.
        :param page_nums: Page numbers array.
        :param lower_left_x: Lower left X coordinate.
        :param lower_left_y: Lower left Y coordinate.
        :param upper_right_x: Upper right X coordinate.
        :param upper_right_y: Upper right Y coordinate.
        :returns: True in case text was successfully added.'''
        ...
    
    def close(self) -> None:
        '''Closes PdfFileMend object.'''
        ...
    
    @property
    def input_stream(self) -> Any:
        '''Sets the input stream.'''
        ...
    
    @input_stream.setter
    def input_stream(self, value: Any):
        ...
    
    @property
    def output_stream(self) -> Any:
        '''Sets the output stream.'''
        ...
    
    @output_stream.setter
    def output_stream(self, value: Any):
        ...
    
    @property
    def input_file(self) -> str:
        '''Sets the input file.'''
        ...
    
    @input_file.setter
    def input_file(self, value: str):
        ...
    
    @property
    def output_file(self) -> str:
        '''Sets the output file.'''
        ...
    
    @output_file.setter
    def output_file(self, value: str):
        ...
    
    @property
    def wrap_mode(self) -> aspose.pdf.facades.WordWrapMode:
        '''Sets or gets word wrapping algorithm. See WordWrapMode and IsWordWrap.'''
        ...
    
    @wrap_mode.setter
    def wrap_mode(self, value: aspose.pdf.facades.WordWrapMode):
        ...
    
    @property
    def text_positioning_mode(self) -> aspose.pdf.facades.PositioningMode:
        '''Sets or gets text positioning strategy. :class:`PositioningMode`
        Default mode is Legacy.'''
        ...
    
    @text_positioning_mode.setter
    def text_positioning_mode(self, value: aspose.pdf.facades.PositioningMode):
        ...
    
    ...

class PdfFileSanitization(aspose.pdf.facades.SaveableFacade):
    '''Represents sanitization and recovery API.
    Use it if you can't create/open documents in any other way.'''
    
    def __init__(self):
        ...
    
    @overload
    def bind_pdf(self, input_file: str) -> None:
        '''Binds a Pdf file for Sanitize.
        
        :param input_file: The pdf file to be edited.'''
        ...
    
    @overload
    def bind_pdf(self, input_stream: Any) -> None:
        '''Binds a Pdf stream for Sanitize.
        
        :param input_stream: The pdf stream to be edited.'''
        ...
    
    @overload
    def bind_pdf(self, src_doc: aspose.pdf.Document) -> None:
        '''Initializes the facade.
        
        :param src_doc: The Aspose.Pdf.Document object.'''
        ...
    
    @overload
    def save(self, output_file: str) -> None:
        '''Saves the result PDF to file.
        
        :param output_file: output pdf file'''
        ...
    
    @overload
    def save(self, output_stream: Any) -> None:
        '''Saves the result PDF to stream.
        
        :param output_stream: output pdf stream'''
        ...
    
    def close(self) -> None:
        '''Closes the facade.'''
        ...
    
    def recover(self) -> None:
        '''Recovers document.
        Use properties to customize.'''
        ...
    
    def trim_top(self) -> None:
        '''Removes data before %PDF.'''
        ...
    
    def trim_bottom(self) -> None:
        '''Removes data after last %%EOF.'''
        ...
    
    def rebuild_xref_and_trailer(self) -> None:
        '''Removes old xref with trailer and creates a new xref with trailer.'''
        ...
    
    @property
    def log(self) -> None:
        '''After file has Saved you can check what was done with file.'''
        ...
    
    @property
    def use_trim_top(self) -> bool:
        '''Allows to remove data before pdf data.'''
        ...
    
    @use_trim_top.setter
    def use_trim_top(self, value: bool):
        ...
    
    @property
    def use_trim_bottom(self) -> bool:
        '''Allows to remove data after pdf data'''
        ...
    
    @use_trim_bottom.setter
    def use_trim_bottom(self, value: bool):
        ...
    
    @property
    def use_rebuild_xref_and_trailer(self) -> bool:
        '''Allows to generate new xref and trailer for document.'''
        ...
    
    @use_rebuild_xref_and_trailer.setter
    def use_rebuild_xref_and_trailer(self, value: bool):
        ...
    
    ...

class PdfFileSecurity(aspose.pdf.facades.SaveableFacade):
    '''Represents encrypting or decrypting a Pdf file with owner or user password, changing the security setting and password.'''
    
    @overload
    def __init__(self, input_stream: Any, output_stream: Any):
        '''Initialize the object of PdfFileSecurity with input and output stream.
        
        :param input_stream: Input Pdf Stream.
        :param output_stream: Output Pdf Stream.'''
        ...
    
    @overload
    def __init__(self, input_file: str, output_file: str):
        '''Initializes the object of PdfFileSecurity with input and output file.
        
        :param input_file: Source input Pdf file.
        :param output_file: Output Pdf file.'''
        ...
    
    @overload
    def __init__(self):
        '''Initialize the object of PdfFileSecurity.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfFileSecurity` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, output_file: str):
        '''Initializes new :class:`PdfFileSecurity` object on base of the document.
        
        :param document: Pdf document.
        :param output_file: Output Pdf file.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, output_stream: Any):
        '''Initializes new :class:`PdfFileSecurity` object on base of the document.
        
        :param document: Pdf document.
        :param output_stream: Output Pdf Stream.'''
        ...
    
    @overload
    def bind_pdf(self, src_file: str) -> None:
        '''Initializes the facade.
        
        :param src_file: The PDF file.'''
        ...
    
    @overload
    def bind_pdf(self, src_stream: Any) -> None:
        '''Initializes the facade.
        
        :param src_stream: The stream of PDF file.'''
        ...
    
    @overload
    def encrypt_file(self, user_password: str, owner_password: str, privilege: aspose.pdf.facades.DocumentPrivilege, key_size: aspose.pdf.facades.KeySize) -> bool:
        '''Encrypts Pdf file with userpassword and ownerpassword and sets the document's privileges to access.
        The user password and the owner password can be null or empty. The owner password will be replaced
        with a random string if the input owner password is null or empty.
        Throws exception if process failed.
        
        :param user_password: User password.
        :param owner_password: Owner password.
        :param privilege: Set privilege.
        :param key_size: KeySize.x40 for 40 bits encryption, KeySize.x128 for 128 bits encryption and KeySize.x256 for 256 bits encryption.
        :returns: True for success.'''
        ...
    
    @overload
    def encrypt_file(self, user_password: str, owner_password: str, privilege: aspose.pdf.facades.DocumentPrivilege, key_size: aspose.pdf.facades.KeySize, cipher: aspose.pdf.facades.Algorithm) -> bool:
        '''Encrypts Pdf file with userpassword and ownerpassword and sets the document's privileges to access.
        The user password and the owner password can be null or empty. The owner password will be replaced
        with a random string if the input owner password is null or empty.
        There are 6 possible combinations of KeySize and Algorithm values.
        However (KeySize.x40, Algorithm.AES) and (KeySize.x256, Algorithm.RC4) are invalid and corresponding
        exception will be raised if kit encounters this combination.
        Throws an exception if process failed.
        
        :param user_password: User password.
        :param owner_password: Owner password.
        :param privilege: Set privilege.
        :param key_size: KeySize.x40 for 40 bits encryption, KeySize.x128 for 128 bits encryption and KeySize.x256 for 256 bits encryption.
        :param cipher: Algorithm.AES to encrypt using AES algorithm or Algorithm.RC4 for RC4 encryption.
        :returns: True for success.'''
        ...
    
    @overload
    def set_privilege(self, privilege: aspose.pdf.facades.DocumentPrivilege) -> bool:
        '''Sets Pdf file security with empty user/owner passwords.
        The owner password will be added by a random string.
        Throws an exception if process failed.
        
        :param privilege: Set privilege.
        :returns: True for success.'''
        ...
    
    @overload
    def set_privilege(self, user_password: str, owner_password: str, privilege: aspose.pdf.facades.DocumentPrivilege) -> bool:
        '''Sets Pdf file security with original password.
        Throws an exception if process failed.
        
        :param user_password: Original user password.
        :param owner_password: Original owner password.
        :param privilege: Set privilege.
        :returns: True for success.'''
        ...
    
    @overload
    def change_password(self, owner_password: str, new_user_password: str, new_owner_password: str) -> bool:
        '''Changes the user password and owner password by owner password, keeps the original security settings.
        The new user password and the new owner password can be null or empty. The owner password will be replaced
        with a random string if the new owner password is null or empty.
        Throws an exception if process failed.
        
        :param owner_password: Original Owner password.
        :param new_user_password: New User password.
        :param new_owner_password: New Owner password.
        :returns: True for success.'''
        ...
    
    @overload
    def change_password(self, owner_password: str, new_user_password: str, new_owner_password: str, privilege: aspose.pdf.facades.DocumentPrivilege, key_size: aspose.pdf.facades.KeySize) -> bool:
        '''Changes the user password and password by owner password, allows to reset Pdf documnent security.
        The new user password and the new owner password can be null or empty. The owner password will be replaced
        with a random string if the new owner password is null or empty.
        Throws an exception if process failed.
        
        :param owner_password: Original owner password.
        :param new_user_password: New User password.
        :param new_owner_password: New Owner password.
        :param privilege: Reset security.
        :param key_size: KeySize.x40 for 40 bits encryption, KeySize.x128 for 128 bits encryption and KeySize.x256 for 256 bits encryption.
        :returns: True for success.'''
        ...
    
    @overload
    def change_password(self, owner_password: str, new_user_password: str, new_owner_password: str, privilege: aspose.pdf.facades.DocumentPrivilege, key_size: aspose.pdf.facades.KeySize, cipher: aspose.pdf.facades.Algorithm) -> bool:
        '''Changes the user password and password by owner password, allows to reset Pdf documnent security.
        The new user password and the new owner password can be null or empty. The owner password will be replaced
        with a random string if the new owner password is null or empty.
        There are 6 possible combinations of KeySize and Algorithm values.
        However (KeySize.x40, Algorithm.AES) and (KeySize.x256, Algorithm.RC4) are invalid and corresponding
        exception will be raised if kit encounters this combination.
        Throws an exception if process failed.
        
        :param owner_password: Original owner password.
        :param new_user_password: New User password.
        :param new_owner_password: New Owner password.
        :param privilege: Reset security.
        :param key_size: KeySize.x40 for 40 bits encryption, KeySize.x128 for 128 bits encryption and KeySize.x256 for 256 bits encryption.
        :param cipher: Algorithm.AES to encrypt using AES algorithm or Algorithm.RC4 for RC4 encryption.
        :returns: True for success.'''
        ...
    
    @overload
    def try_change_password(self, owner_password: str, new_user_password: str, new_owner_password: str) -> bool:
        '''Changes the user password and owner password by owner password, keeps the original security settings.
        The new user password and the new owner password can be null or empty. The owner password will be replaced
        Does not throw an exception if process failed.
        with a random string if the new owner password is null or empty.
        
        :param owner_password: Original Owner password.
        :param new_user_password: New User password.
        :param new_owner_password: New Owner password.
        :returns: True for success,or false.'''
        ...
    
    @overload
    def try_change_password(self, owner_password: str, new_user_password: str, new_owner_password: str, privilege: aspose.pdf.facades.DocumentPrivilege, key_size: aspose.pdf.facades.KeySize) -> bool:
        '''Changes the user password and password by owner password, allows to reset Pdf documnent security.
        The new user password and the new owner password can be null or empty. The owner password will be replaced
        with a random string if the new owner password is null or empty.
        Does not throw an exception if process failed.
        
        :param owner_password: Original owner password.
        :param new_user_password: New User password.
        :param new_owner_password: New Owner password.
        :param privilege: Reset security.
        :param key_size: KeySize.x40 for 40 bits encryption, KeySize.x128 for 128 bits encryption and KeySize.x256 for 256 bits encryption.
        :returns: True for success, or false.'''
        ...
    
    @overload
    def try_change_password(self, owner_password: str, new_user_password: str, new_owner_password: str, privilege: aspose.pdf.facades.DocumentPrivilege, key_size: aspose.pdf.facades.KeySize, cipher: aspose.pdf.facades.Algorithm) -> bool:
        '''Changes the user password and password by owner password, allows to reset Pdf documnent security.
        The new user password and the new owner password can be null or empty. The owner password will be replaced
        with a random string if the new owner password is null or empty.
        There are 6 possible combinations of KeySize and Algorithm values.
        However (KeySize.x40, Algorithm.AES) and (KeySize.x256, Algorithm.RC4) are invalid and corresponding
        exception will be raised if kit encounters this combination.
        Does not throw an exception if process failed.
        
        :param owner_password: Original owner password.
        :param new_user_password: New User password.
        :param new_owner_password: New Owner password.
        :param privilege: Reset security.
        :param key_size: KeySize.x40 for 40 bits encryption, KeySize.x128 for 128 bits encryption and KeySize.x256 for 256 bits encryption.
        :param cipher: Algorithm.AES to encrypt using AES algorithm or Algorithm.RC4 for RC4 encryption.
        :returns: True for success, or false.'''
        ...
    
    def close(self) -> None:
        '''Closes the facade.'''
        ...
    
    def try_encrypt_file(self, user_password: str, owner_password: str, privilege: aspose.pdf.facades.DocumentPrivilege, key_size: aspose.pdf.facades.KeySize) -> bool:
        '''Encrypts Pdf file with userpassword and ownerpassword and sets the document's privileges to access.
        The user password and the owner password can be null or empty. The owner password will be replaced
        with a random string if the input owner password is null or empty.
        Does not throw an exception if process failed.
        
        :param user_password: User password.
        :param owner_password: Owner password.
        :param privilege: Set privilege.
        :param key_size: KeySize.x40 for 40 bits encryption, KeySize.x128 for 128 bits encryption and KeySize.x256 for 256 bits encryption.
        :returns: True for success, or false.'''
        ...
    
    def decrypt_file(self, owner_password: str) -> bool:
        '''Decrypts an encrypted Pdf document by owner password.
        If the document hasn't owner password, it is allow to use user password.
        Throws an exception if process failed.
        
        :param owner_password: Owner password.
        :returns: True for success.'''
        ...
    
    def try_decrypt_file(self, owner_password: str) -> bool:
        '''Decrypts an encrypted Pdf document by owner password.
        If the document hasn't owner password, it is allow to use user password.
        Does not throw an exception if process failed.
        
        :param owner_password: Owner password.
        :returns: True for success,or false.'''
        ...
    
    def try_set_privilege(self, user_password: str, owner_password: str, privilege: aspose.pdf.facades.DocumentPrivilege) -> bool:
        '''Sets Pdf file security with original password.
        Does not throw an exception if process failed.
        
        :param user_password: Original user password.
        :param owner_password: Original owner password.
        :param privilege: Set privilege.
        :returns: True for success, or false.'''
        ...
    
    @property
    def allow_exceptions(self) -> bool:
        '''If this value set to true, exception will be thrown on opearation failure. Else, method returns false on failure and last exception can be checked with LastException property.'''
        ...
    
    @allow_exceptions.setter
    def allow_exceptions(self, value: bool):
        ...
    
    ...

class PdfFileSignature(aspose.pdf.facades.SaveableFacade):
    '''Represents a class to sign a pdf file with a certificate.'''
    
    @overload
    def __init__(self):
        '''The constructor of PdfFileSignature class.'''
        ...
    
    @overload
    def __init__(self, input_file: str):
        '''The constructor of PdfFileSignature class.
        
        :param input_file: The input file for signature.'''
        ...
    
    @overload
    def __init__(self, input_file: str, output_file: str):
        '''The constructor of PdfFileSignature class.
        
        :param input_file: The input file for signature.
        :param output_file: The output file.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfFileSignature` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, output_file: str):
        '''Initializes new :class:`PdfFileSignature` object on base of the document.
        
        :param document: Pdf document.
        :param output_file: The output file.'''
        ...
    
    @overload
    def bind_pdf(self, input_file: str) -> None:
        '''Binds a Pdf file for editing.
        
        :param input_file: The pdf file to be edited.'''
        ...
    
    @overload
    def bind_pdf(self, input_stream: Any) -> None:
        '''Binds a Pdf stream for editing.
        
        :param input_stream: The pdf stream to be edited.'''
        ...
    
    @overload
    def save(self, output_file: str) -> None:
        '''Saves the result PDF to file.
        
        :param output_file: output pdf file'''
        ...
    
    @overload
    def save(self, output_stream: Any) -> None:
        '''Saves the result PDF to stream.
        
        :param output_stream: output pdf stream'''
        ...
    
    @overload
    def save(self) -> None:
        '''Save signed pdf file. Output filename must be provided before with the help of coresponding PdfFileSignature constructor.'''
        ...
    
    @overload
    def sign(self, page: int, sig_reason: str, sig_contact: str, sig_location: str, visible: bool, annot_rect: aspose.pydrawing.Rectangle) -> None:
        '''Make a signature on the pdf document.
        
        :param page: The page number on which signature is made.
        :param sig_reason: The reason of signature.
        :param sig_contact: The contact of signature.
        :param sig_location: The location of signature.
        :param visible: The visiblity of signature.
        :param annot_rect: The rect of signature.'''
        ...
    
    @overload
    def sign(self, page: int, sig_reason: str, sig_contact: str, sig_location: str, visible: bool, annot_rect: aspose.pydrawing.Rectangle, sig: aspose.pdf.forms.Signature) -> None:
        '''Sign the document with the given type signature.
        
        :param page: The page number on which signature is made.
        :param sig_reason: The reason of signature.
        :param sig_contact: The contact of signature.
        :param sig_location: The location of signature.
        :param visible: The visiblity of signature.
        :param annot_rect: The rect of signature.
        :param sig: The type of the signature, could be PKCS1, PKCS7 and PKCS7Detached.'''
        ...
    
    @overload
    def sign(self, page: int, visible: bool, annot_rect: aspose.pydrawing.Rectangle, sig: aspose.pdf.forms.Signature) -> None:
        '''Sign the document with the given type signature.
        
        :param page: The page number on which signature is made.
        :param visible: The visiblity of signature.
        :param annot_rect: The rect of signature.
        :param sig: The type of the signature, could be PKCS1, PKCS7 and PKCS7Detached.
                    Such data as signature reason, contact and location must be already present in this object (see corresponding properties).'''
        ...
    
    @overload
    def sign(self, sig_name: str, sig_reason: str, sig_contact: str, sig_location: str, sig: aspose.pdf.forms.Signature) -> None:
        '''Sign the document with the given type signature which is placed in already presented signature field.
        Before signing signature field must be empty, i.e. field must not contain signature dictionary.
        Thus pdf document already has signature field, you should not supply the place to stamp the signature,
        corresponding page and rectangle are taken from signature field which is found by signature name (see SigName parameter).
        
        :param sig_name: The name of the signature field.
        :param sig_reason: The reason of signature.
        :param sig_contact: The contact of signature.
        :param sig_location: The location of signature.
        :param sig: The type of the signature, could be PKCS1, PKCS7 and PKCS7Detached.'''
        ...
    
    @overload
    def sign(self, page: int, sig_name: str, sig_reason: str, sig_contact: str, sig_location: str, visible: bool, annot_rect: aspose.pydrawing.Rectangle, sig: aspose.pdf.forms.Signature) -> None:
        '''Sign the document with the given type signature which is placed in already presented signature field.
        Before signing pdf document should already has signature field, corresponding page and rectangle are taken from
        signature field which is found by signature name (see SigName parameter).
        
        :param page: The page number on which signature is made.
        :param sig_name: The name of the signature field.
        :param sig_reason: The reason of signature.
        :param sig_contact: The contact of signature.
        :param sig_location: The location of signature.
        :param visible: The visiblity of signature.
        :param annot_rect: The rect of signature.
        :param sig: The type of the signature, could be PKCS1, PKCS7 and PKCS7Detached.'''
        ...
    
    @overload
    def sign(self, sig_name: str, sig: aspose.pdf.forms.Signature) -> None:
        '''Sign the document with the given type signature which is placed in already presented signature field.
        Before signing signature field must be empty, i.e. field must not contain signature dictionary.
        Thus pdf document already has signature field, you should not supply the place to stamp the signature,
        corresponding page and rectangle are taken from signature field which is found by signature name (see SigName parameter).
        Such data as signature reason, contact and location must be provided by corresponding properties of the Signature object sig.
        
        :param sig_name: The name of the signature field.
        :param sig: The type of the signature, could be PKCS1 (Pkcs1Signature object), PKCS7 and PKCS7 detached (Pkcs7Signature object)'''
        ...
    
    @overload
    def certify(self, page: int, sig_reason: str, sig_contact: str, sig_location: str, visible: bool, annot_rect: aspose.pydrawing.Rectangle, doc_mdp_signature: aspose.pdf.forms.DocMDPSignature) -> None:
        '''Certify the document with the MDP signature.
        Such data as signature reason, contact and location must be provided by corresponding properties of the Signature object sig.
        
        :param page: The page on which signature is made.
        :param sig_reason: The reason of signature.
        :param sig_contact: The contact of signature.
        :param sig_location: The location of signature.
        :param visible: The visiblity of signature.
        :param annot_rect: The rect of signature.
        :param doc_mdp_signature: The document MDP type of the signature.'''
        ...
    
    @overload
    def certify(self, sig_name: str, doc_mdp_signature: aspose.pdf.forms.DocMDPSignature) -> None:
        '''Certify the document with the MDP signature which is placed in already presented signature field.
        Before signing signature field must be empty, i.e. field must not contain signature dictionary.
        Thus pdf document already has signature field, you should not supply the place to stamp the signature,
        corresponding page and rectangle are taken from signature field which is found by signature name (see sigName parameter).
        
        :param sig_name: The name of the signature field.
        :param doc_mdp_signature: The type of the signature, could be
                                  :class:`aspose.pdf.forms.PKCS1`, :class:`aspose.pdf.forms.PKCS7` and  :class:`aspose.pdf.forms.PKCS7Detached`'''
        ...
    
    @overload
    def remove_signature(self, sign_name: str) -> None:
        '''Remove the signature according to the name of the signature.
        
        :param sign_name: The name of signature.'''
        ...
    
    @overload
    def remove_signature(self, sign_name: str, remove_field: bool) -> None:
        '''Removes the signature according to the name of the signature.
        
        :param sign_name: The name of signature.
        :param remove_field: If set to true, than removes both of signature and field from document; otherwise, signature only.'''
        ...
    
    def close(self) -> None:
        '''Closes the facade.'''
        ...
    
    def get_access_permissions(self) -> aspose.pdf.forms.DocMDPAccessPermissions:
        '''Returns the access permissions value of certified document by the MDP signature type.
        
        :returns: If the document is being certified, than returns access permissions value; otherwise,
                   is thrown.'''
        ...
    
    def get_sign_names(self, only_active: bool) -> list[str]:
        '''Gets the names of all not empty signatures.
        
        :param only_active: if true, return only active signatures; otherwise, return all signatures.
        :returns: Return an IList\<string\>.'''
        ...
    
    def get_blank_sign_names(self) -> list[str]:
        '''Gets the names of all empty signature fields.
        
        :returns: Return an IList.'''
        ...
    
    def is_contain_signature(self) -> bool:
        '''Checks if the pdf  has a digital signature or not.
        
        :returns: Return a  result of bool type.'''
        ...
    
    def contains_signature(self) -> bool:
        '''Checks if the pdf  has a digital signature or not.
        
        :returns: Return a  result of bool type.'''
        ...
    
    def contains_usage_rights(self) -> bool:
        '''Checks if the pdf has a usage rights or not.
        
        :returns: Returns a result of bool type.'''
        ...
    
    def is_covers_whole_document(self, sign_name: str) -> bool:
        '''Checks if the signature covers the whole document.
        
        :param sign_name: The name of signature.
        :returns: Return a  result of bool type.'''
        ...
    
    def covers_whole_document(self, sign_name: str) -> bool:
        '''Checks if the signature covers the whole document.
        
        :param sign_name: The name of signature.
        :returns: Return a  result of bool type.'''
        ...
    
    def get_revision(self, sign_name: str) -> int:
        '''Gets the revision of a signature.
        
        :param sign_name: The name of signature.
        :returns: Return the number of signature revision.'''
        ...
    
    def get_total_revision(self) -> int:
        '''Gets the toltal revision.
        
        :returns: Return the total number of signature revision.'''
        ...
    
    def remove_usage_rights(self) -> None:
        '''Removes the usage rights entry.'''
        ...

    def remove_signatures(self) -> None:
        '''Removes all signatures.'''
        ...
    
    def verify_signed(self, sign_name: str) -> bool:
        '''Checks the validity of a signature.
        
        :param sign_name: The name of signature.
        :returns: Return a result of bool type.'''
        ...
    
    def get_signer_name(self, sign_name: str) -> str:
        '''Gets the name of person or organization who signing the pdf document.
        
        :param sign_name: The name of signature.
        :returns: Returns the result of the signer's name.'''
        ...
    
    def get_date_time(self, sign_name: str) -> datetime.datetime:
        '''Gets the signature's datetime.
        
        :param sign_name: The name of signature.
        :returns: Return the result of DateTime type.'''
        ...
    
    def get_reason(self, sign_name: str) -> str:
        '''Gets the reason of a signature.
        
        :param sign_name: The name of signature.
        :returns: Returns a result of string type.'''
        ...
    
    def get_location(self, sign_name: str) -> str:
        '''Gets the location of a signature.
        
        :param sign_name: The name of signature.
        :returns: Returns a result of string type.'''
        ...
    
    def get_contact_info(self, sign_name: str) -> str:
        '''Gets the contact information of a signature.
        
        :param sign_name: The name of signature.
        :returns: Returns a result of string type.'''
        ...
    
    def verify_signature(self, sign_name: str) -> bool:
        '''Checks the validity of a signature.
        
        :param sign_name: The name of signature.
        :returns: Return a result of bool type.'''
        ...
    
    def extract_image(self, sign_name: str) -> Any:
        '''Extracts signature's image.
        
        :param sign_name: The name of signature.
        :returns: If image was successfully found than returns stream object; otherwise, null.'''
        ...
    
    def extract_certificate(self, sign_name: str) -> Any:
        '''Extracts signature's single X.509 certificate as a stream.
        
        :param sign_name: The name of signature.
        :returns: If certificate was found returns X.509 single certificate; otherwise, null.'''
        ...
    
    def set_certificate(self, pfx: str, password: str) -> None:
        '''Set certificate file and password for signing routine.
        
        :param pfx: PKCS #12 certificate file.
        :param password: Password to get access for the certificate private key.'''
        ...
    
    @property
    def signature_appearance(self) -> str:
        '''Sets or gets a graphic appearance for the signature. Property value represents image file name.'''
        ...
    
    @signature_appearance.setter
    def signature_appearance(self, value: str):
        ...
    
    @property
    def is_ltv_enabled(self) -> bool:
        '''Gets the LTV enabled flag.'''
        ...
    
    @property
    def is_certified(self) -> bool:
        '''Gets the flag determining whether a document is certified or not.'''
        ...
    
    @property
    def signature_appearance_stream(self) -> Any:
        '''Sets or gets a graphic appearance for the signature. Property value represents image stream.'''
        ...
    
    @signature_appearance_stream.setter
    def signature_appearance_stream(self, value: Any):
        ...
    
    ...

class PdfFileStamp(aspose.pdf.facades.SaveableFacade):
    '''Class for adding stamps (watermark or background) to PDF files.'''
    
    @overload
    def __init__(self, input_file: str, output_file: str):
        '''Constructor for PdfFileStamp.
        
        :param input_file: Input file name and path.
        :param output_file: Output file name and path.'''
        ...
    
    @overload
    def __init__(self, input_stream: Any, output_stream: Any):
        '''Constructor for PdfFileStamp.
        
        :param input_stream: Input stream.
        :param output_stream: Output stream.'''
        ...
    
    @overload
    def __init__(self, input_file: str, output_file: str, keep_security: bool):
        '''Constructor for PdfFileStamp.
        
        :param input_file: Input file name and path.
        :param output_file: Output file name and path.
        :param keep_security: Keep security if true.'''
        ...
    
    @overload
    def __init__(self, input_stream: Any, output_stream: Any, keep_security: bool):
        '''Constructor of PdfFileStamp.
        
        :param input_stream: Input stream.
        :param output_stream: Output stream.
        :param keep_security: Keep security if true.'''
        ...
    
    @overload
    def __init__(self):
        '''Constructor of the PdfFileStamp.
        Input file and output file may be specified via corresponding properties.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfFileStamp` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, output_file: str):
        '''Initializes new :class:`PdfFileStamp` object on base of the document.
        
        :param document: Pdf document.
        :param output_file: Output file name and path.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, output_stream: Any):
        '''Initializes new :class:`PdfFileStamp` object on base of the document.
        
        :param document: Pdf document.
        :param output_stream: Output stream.'''
        ...
    
    @overload
    def save(self, dest_file: str) -> None:
        '''Saves result into specified file.
        
        :param dest_file: Path to file where document will be saved.'''
        ...
    
    @overload
    def save(self, dest_stream: Any) -> None:
        '''Saves document into specified stream.
        
        :param dest_stream: Stream where document will be saved.'''
        ...
    
    @overload
    def add_page_number(self, format_string: str) -> None:
        '''Add page number to file. Page number text may contain # sign which will be replaced with number of the page.
        Page number is placed in the bottom of the page centered horizontally.
        
        :param format_string: Text of page number'''
        ...
    
    @overload
    def add_page_number(self, formatted_text: aspose.pdf.facades.FormattedText) -> None:
        '''Adds page number to the page. Page number may contain # sign which will be replaced with page number.
        Page number is placed in the bottom of the page centered horizontally.
        
        :param formatted_text: Format string for page number representes as FormattedText.'''
        ...
    
    @overload
    def add_page_number(self, format_string: str, position: int, left_margin: float, right_margin: float, top_margin: float, bottom_margin: float) -> None:
        '''Adds page number to the pages of document.
        
        :param format_string: Format string for page number.
        :param position: Position where page number will be placed on the page.  0-bottom middle, 1-bottom right, 2-upper right,
                         3 - sides right, 4 - upper middle,5 - bottom left,6 - sides left,7 - upper left.
                         You can use the following constants:
                         PosBottomMiddle = 0, PosBottomRight = 1, PosUpperRight = 2, PosSidesRight = 3,
                         PosUpperMiddle, PosBottomLeft = 5, PosSidesLeft, PosUpperLeft
        :param left_margin: Margin on the left edge of the page.
        :param right_margin: Margin on the right edge of the page.
        :param top_margin: Margin on the top edge of the page.
        :param bottom_margin: Margin on the bottom edge of the page.'''
        ...
    
    @overload
    def add_page_number(self, format_string: str, x: float, y: float) -> None:
        '''Adds page number at the specified position on the page.
        
        :param format_string: Format string. Format string can contain # sign which will be replaced with page number.
        :param x: X coordinate of page number.
        :param y: Y coordinate of page number.'''
        ...
    
    @overload
    def add_page_number(self, formatted_text: aspose.pdf.facades.FormattedText, position: int, left_margin: float, right_margin: float, top_margin: float, bottom_margin: float) -> None:
        '''Adds page number to the pages of document.
        
        :param formatted_text: FormattedText object which represents page number format and properties iof the text.
        :param position: Position where page number will be placed on the page.  0-bottom middle, 1-bottom right, 2-upper right,
                         3 - sides right, 4 - upper middle,5 - bottom left,6 - sides left,7 - upper left.
                         You can use the following constants:
                         PosBottomMiddle = 0, PosBottomRight = 1, PosUpperRight = 2, PosSidesRight = 3,
                         PosUpperMiddle, PosBottomLeft = 5, PosSidesLeft, PosUpperLeft
        :param left_margin: Margin on the left edge of the page.
        :param right_margin: Margin on the right edge of the page.
        :param top_margin: Margin on the top edge of the page.
        :param bottom_margin: Margin on the bottom edge of the page.'''
        ...
    
    @overload
    def add_page_number(self, formatted_text: aspose.pdf.facades.FormattedText, x: float, y: float) -> None:
        '''Adds page number at the specified position on the page.
        
        :param formatted_text: Formatted text which represents page number format and properties of the text.
                               Format string can contain # sign which will be replaced with page number.
        :param x: X coordinate of page number.
        :param y: Y coordinate of page number.'''
        ...
    
    @overload
    def add_page_number(self, format_string: str, position: int) -> None:
        '''Adds page number to the pages.
        
        :param format_string: Format of the page number. This text may contain # which will be replaced with page number.
        :param position: Position where page number will be placed on the page.  0-bottom middle, 1-bottom right, 2-upper right,
                         3 - sides right, 4 - upper middle,5 - bottom left,6 - sides left,7 - upper left.
                         You can use the following constants:
                         PosBottomMiddle = 0, PosBottomRight = 1, PosUpperRight = 2, PosSidesRight = 3,
                         PosUpperMiddle, PosBottomLeft = 5, PosSidesLeft, PosUpperLeft'''
        ...
    
    @overload
    def add_page_number(self, formatted_text: aspose.pdf.facades.FormattedText, position: int) -> None:
        '''Adds page number to the pages.
        
        :param formatted_text: FormattedText object which contains format of the page number and text properties.
                               This text may contain # which will be replaced with page number.
        :param position: Position where page number will be placed on the page.  0-bottom middle, 1-bottom right, 2-upper right,
                         3 - sides right, 4 - upper middle,5 - bottom left,6 - sides left,7 - upper left.
                         You can use the following constants:
                         PosBottomMiddle = 0, PosBottomRight = 1, PosUpperRight = 2, PosSidesRight = 3,
                         PosUpperMiddle, PosBottomLeft = 5, PosSidesLeft, PosUpperLeft'''
        ...
    
    @overload
    def add_header(self, formatted_text: aspose.pdf.facades.FormattedText, top_margin: float) -> None:
        '''Adds header to the page.
        
        :param formatted_text: Text for header and properties of the text.
        :param top_margin: Margin on the top of page.'''
        ...
    
    @overload
    def add_header(self, formatted_text: aspose.pdf.facades.FormattedText, top_margin: float, left_margin: float, right_margin: float) -> None:
        '''Adds header to the pages of file.
        
        :param formatted_text: Formatted text object which contains page text and its properties.
        :param top_margin: Margin on the top of the page.
        :param left_margin: Margin on the left of the page.
        :param right_margin: Margin on the right of the page.'''
        ...
    
    @overload
    def add_header(self, image_file: str, top_margin: float) -> None:
        '''Adds image as header to the pages of the file.
        
        :param image_file: Path to the image file.
        :param top_margin: Margin at top of the page.'''
        ...
    
    @overload
    def add_header(self, image_file: str, top_margin: float, left_margin: float, right_margin: float) -> None:
        '''Adds image as header on the pages.
        
        :param image_file: Path to the image file.
        :param top_margin: Margin at top of the page.
        :param left_margin: Margin at left side of the page.
        :param right_margin: Margin at right side of the page.'''
        ...
    
    @overload
    def add_header(self, image_stream: Any, top_margin: float) -> None:
        '''Adds image as header on the pages.
        
        :param image_stream: Stream of the image.
        :param top_margin: Margin at top of the page.'''
        ...
    
    @overload
    def add_header(self, input_stream: Any, top_margin: float, left_margin: float, right_margin: float) -> None:
        '''Adds image at the top of the page.
        
        :param input_stream: Stream which contains image data.
        :param top_margin: Margin at top of the page.
        :param left_margin: Margin at left side of the page.
        :param right_margin: Margin at right side of the page.'''
        ...
    
    @overload
    def add_footer(self, formatted_text: aspose.pdf.facades.FormattedText, bottom_margin: float) -> None:
        '''Adds footer to the pages of the document.
        
        :param formatted_text: FormattedText object which contains text of the footer and text properties.
        :param bottom_margin: Margin at the top of page.'''
        ...
    
    @overload
    def add_footer(self, formatted_text: aspose.pdf.facades.FormattedText, bottom_margin: float, left_margin: float, right_margin: float) -> None:
        '''Adds footer to the pages of the document.
        
        :param formatted_text: FormattedText object which contains footer text and text properties.
        :param bottom_margin: Margin at the bottom of the page.
        :param left_margin: Margin at the left side of the page.
        :param right_margin: Margin at the right side of the page.'''
        ...
    
    @overload
    def add_footer(self, image_file: str, bottom_margin: float) -> None:
        '''Adds image as footer to the pages of the document.
        
        :param image_file: Image file name and path.
        :param bottom_margin: Margin at the bottom of the page.'''
        ...
    
    @overload
    def add_footer(self, image_file: str, bottom_margin: float, left_margin: float, right_margin: float) -> None:
        '''Adds image as footer of the pages.
        
        :param image_file: Iamge file name and path.
        :param bottom_margin: Margin at the bottom of the page.
        :param left_margin: Margin at the left side of the page.
        :param right_margin: Margin at the right side of the page.'''
        ...
    
    @overload
    def add_footer(self, image_stream: Any, bottom_margin: float) -> None:
        '''Adds image as footer of the page.
        
        :param image_stream: Stream contains image data.
        :param bottom_margin: Margin at the bottom of the page.'''
        ...
    
    @overload
    def add_footer(self, image_stream: Any, bottom_margin: float, left_margin: float, right_margin: float) -> None:
        '''Adds image as footer of the page.
        
        :param image_stream: Stream contains image data.
        :param bottom_margin: Margin at the bottom of the page.
        :param left_margin: Margin at the left side of the page.
        :param right_margin: Margin at the right side of the page.'''
        ...
    
    def close(self) -> None:
        '''Closes opened files and saves changes.
        Warning. If input or output streams are specified they are not closed by Close() method.'''
        ...
    
    def add_stamp(self, stamp) -> None:
        '''Adds stamp to the file.
        
        :param stamp: Stamp object which.'''
        ...
    
    @property
    def optimize_size(self) -> bool:
        '''Gets or sets optimization flag. Equal resource streams in resultant file are merged into one PDF object if this flag set.
        This allows to decrease resultant file size but may cause slower execution and larger memory requirements.
        Default value: false.'''
        ...
    
    @optimize_size.setter
    def optimize_size(self, value: bool):
        ...
    
    @property
    def keep_security(self) -> bool:
        '''Keeps security if true. (This feature will be implemented in next versions).'''
        ...
    
    @keep_security.setter
    def keep_security(self, value: bool):
        ...
    
    @property
    def input_file(self) -> str:
        '''Gets or sets name and path of input file.'''
        ...
    
    @input_file.setter
    def input_file(self, value: str):
        ...
    
    @property
    def input_stream(self) -> Any:
        '''Gets or sets input stream.'''
        ...
    
    @input_stream.setter
    def input_stream(self, value: Any):
        ...
    
    @property
    def output_file(self) -> str:
        '''Gets or sets name and path of output file.'''
        ...
    
    @output_file.setter
    def output_file(self, value: str):
        ...
    
    @property
    def output_stream(self) -> Any:
        '''Gets or sets output stream.'''
        ...
    
    @output_stream.setter
    def output_stream(self, value: Any):
        ...
    
    @property
    def page_number_rotation(self) -> float:
        '''Gets or sets rotation of page number. Rotation  is in degrees. Default is 0.'''
        ...
    
    @page_number_rotation.setter
    def page_number_rotation(self, value: float):
        ...
    
    @property
    def page_height(self) -> float:
        '''Gets height of first page in souorce file.'''
        ...
    
    @property
    def page_width(self) -> float:
        '''Gets width of first page in input file.'''
        ...
    
    @property
    def starting_number(self) -> int:
        '''Gets or sets starting number for first page in input file. Next pages will be numbered starting from this value.
        For example if  StartingNumber is set to 100, document pages will have numbers 100, 101, 102...'''
        ...
    
    @starting_number.setter
    def starting_number(self, value: int):
        ...
    
    @property
    def numbering_style(self) -> aspose.pdf.NumberingStyle:
        '''Gets or sets pabge numbering style. Possible values: NumeralsArabic, NumeralsRomanUppercase, NumeralsRomanLowercase, LettersAppercase, LettersLowercase'''
        ...
    
    @numbering_style.setter
    def numbering_style(self, value: aspose.pdf.NumberingStyle):
        ...
    
    @property
    def stamp_id(self) -> int:
        '''Stamp ID of next added stamp (incluiding page headers/hooters/page numbers).'''
        ...
    
    @stamp_id.setter
    def stamp_id(self, value: int):
        ...
    
    POS_BOTTOM_MIDDLE: int
    
    POS_BOTTOM_RIGHT: int
    
    POS_UPPER_RIGHT: int
    
    POS_SIDES_RIGHT: int
    
    POS_UPPER_MIDDLE: int
    
    POS_BOTTOM_LEFT: int
    
    POS_SIDES_LEFT: int
    
    POS_UPPER_LEFT: int
    
    ...

class PdfJavaScriptStripper:
    '''Class for removing all Java Script code.'''
    
    def __init__(self):
        ...
    
    @overload
    def strip(self, input_file: str, output_file: str) -> bool:
        '''Remove Java Script from document.
        
        :param input_file: File containig the document.
        :param output_file: File where document will be stored.
        :returns: true if JavaScript was stripped successfully.'''
        ...
    
    @overload
    def strip(self, in_stream: Any, out_stream: Any) -> bool:
        '''Remove Java Script from the document.
        
        :param in_stream: Stream containing document.
        :param out_stream: Stream where the document will be stored.
        :returns: true if JavaScript was stripped successfully.'''
        ...
    
    ...

class PdfPageEditor(aspose.pdf.facades.SaveableFacade):
    '''Represents a class to edit the PDF file's page, including rotating page, zooming page, moving position and changing page size.'''
    
    @overload
    def __init__(self):
        '''Constructor for PdfPageEditor class.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Constructor for PdfPageEditor class.
        
        :param document: Document object which should be processed.'''
        ...
    
    @overload
    def save(self, output_file: str) -> None:
        '''Saves changed document into file.
        
        :param output_file: Path to file where document will be saved.'''
        ...
    
    @overload
    def save(self, output_stream: Any) -> None:
        '''Saves changed document into stream.
        
        :param output_stream: Stream where changed PDF document will be saved.'''
        ...
    
    def move_position(self, move_x: float, move_y: float) -> None:
        '''Moves the origin from (0, 0) to the point that appointted.
        The origin is left-bottom and the unit is point(1 inch = 72 points).
        
        :param move_x: X-coordinate.
        :param move_y: Y-coordinate.'''
        ...
    
    def get_pages(self) -> int:
        '''Returns total number of pages.
        
        :returns: Number of pages.'''
        ...
    
    def get_page_size(self, page: int) -> aspose.pdf.PageSize:
        '''Returns the page size of the specified page.
        
        :param page: Page index. Document pages are numbered from 1.
        :returns: Result is instance of PageSize. Use Width and Height properties of the returned object to get page width and height.'''
        ...
    
    def get_page_rotation(self, page: int) -> int:
        '''Returns the rotation of specified page.
        
        :param page: Page index. Document pages are numbered from 1.
        :returns: Page rotation in degrees.'''
        ...
    
    def get_page_box_size(self, page: int, page_box_name: str) -> aspose.pydrawing.Rectangle:
        '''Returns size of specified box in document.
        
        :param page: Page index. Document pages are numbered from 1.
        :param page_box_name: Box type name. Valid values are: "art", "bleed", "crop", "media", "trim".
        :returns: Rectangle which contains requested box.'''
        ...
    
    def apply_changes(self) -> None:
        '''Apply changes made to the document pages.'''
        ...
    
    @property
    def transition_duration(self) -> int:
        '''Gets or sets duration of the transition effect.'''
        ...
    
    @transition_duration.setter
    def transition_duration(self, value: int):
        ...
    
    @property
    def transition_type(self) -> int:
        '''Gets or sets transition style to use when moving to this page from another during a presentation.'''
        ...
    
    @transition_type.setter
    def transition_type(self, value: int):
        ...
    
    @property
    def display_duration(self) -> int:
        '''Gets or sets display duration for pages.'''
        ...
    
    @display_duration.setter
    def display_duration(self, value: int):
        ...
    
    @property
    def process_pages(self) -> list[int]:
        '''Gets or sets the page numbers to be edited. By default, each page would be edited.'''
        ...
    
    @process_pages.setter
    def process_pages(self, value: list[int]):
        ...
    
    @property
    def rotation(self) -> int:
        '''Gets or sets the rotation of the pages, the rotation must be 0, 90, 180 or 270.
        Default value is 0.'''
        ...
    
    @rotation.setter
    def rotation(self, value: int):
        ...
    
    @property
    def zoom(self) -> float:
        '''Get or sets zoom coefficient. Value 1.0 corresponds to 100%.
        Default value is 1.0.'''
        ...
    
    @zoom.setter
    def zoom(self, value: float):
        ...
    
    @property
    def page_size(self) -> aspose.pdf.PageSize:
        '''Gets or sets the output file's page size.'''
        ...
    
    @page_size.setter
    def page_size(self, value: aspose.pdf.PageSize):
        ...
    
    @property
    def alignment(self) -> aspose.pdf.facades.AlignmentType:
        '''Gets or sets the horizontal alignment of the original PDF content on the result page, default is AlignmentType.Left.'''
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.pdf.facades.AlignmentType):
        ...
    
    @property
    def horizontal_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets or sets the horizontal alignment of the original PDF content on the result page, default is AlignmentType.Left.'''
        ...
    
    @horizontal_alignment.setter
    def horizontal_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def vertical_alignment(self) -> aspose.pdf.facades.VerticalAlignmentType:
        '''Gets or Sets the vertical alignment of the original PDF content on the result page, default is VerticalAlignmentType.Bottom.'''
        ...
    
    @vertical_alignment.setter
    def vertical_alignment(self, value: aspose.pdf.facades.VerticalAlignmentType):
        ...
    
    @property
    def vertical_alignment_type(self) -> aspose.pdf.VerticalAlignment:
        '''Gets or Sets the vertical alignment of the original PDF content on the result page, default is VerticalAlignmentType.Bottom.'''
        ...
    
    @vertical_alignment_type.setter
    def vertical_alignment_type(self, value: aspose.pdf.VerticalAlignment):
        ...
    
    SPLITVOUT: int
    
    SPLITHOUT: int
    
    SPLITVIN: int
    
    SPLITHIN: int
    
    BLINDV: int
    
    BLINDH: int
    
    INBOX: int
    
    OUTBOX: int
    
    LRWIPE: int
    
    RLWIPE: int
    
    BTWIPE: int
    
    TBWIPE: int
    
    DISSOLVE: int
    
    LRGLITTER: int
    
    TBGLITTER: int
    
    DGLITTER: int
    
    ...

class PdfPrintPageInfo:
    '''Represents an object that contains current printing page info.'''
    
    @property
    def page_number(self) -> int:
        '''Gets currently printed page number;'''
        ...
    
    ...

class PdfProducer:
    '''Represents a class to produce PDF from other formats.'''
    
    @overload
    @staticmethod
    def produce(self, input_stream: Any, format: aspose.pdf.ImportFormat, output_stream: Any) -> None:
        '''Produce the PDF stream using specified import format.
        
        :param input_stream: Input stream.
        :param format: Import format.
        :param output_stream: Output PDF stream.
        :raises aspose.pdf.InvalidFileFormatException: The exception is thrown when a file is invalid.
        :raises System.ArgumentNullException: Input or output stream is null'''
        ...
    
    @overload
    @staticmethod
    def produce(self, input_file_name: str, format: aspose.pdf.ImportFormat, output_stream: Any) -> None:
        '''Produce the PDF stream using specified import format.
        
        :param input_file_name: Input file name.
        :param format: Import format.
        :param output_stream: Output PDF stream.
        :raises aspose.pdf.InvalidFileFormatException: The exception is thrown when a file is invalid.
        :raises System.ArgumentNullException: Output stream is null
        :raises System.ArgumentException: Input file name is an empty string'''
        ...
    
    @overload
    @staticmethod
    def produce(self, input_stream: Any, format: aspose.pdf.ImportFormat, output_file_name: str) -> None:
        '''Produce the PDF file using specified import format.
        
        :param input_stream: Input stream.
        :param format: Import format.
        :param output_file_name: Output PDF file
        :raises aspose.pdf.InvalidFileFormatException: The exception is thrown when a file is invalid.
        :raises System.ArgumentNullException: Input stream is null
        :raises System.ArgumentException: Output file name is an empty string'''
        ...
    
    @overload
    @staticmethod
    def produce(self, input_file_name: str, format: aspose.pdf.ImportFormat, output_file_name: str) -> None:
        '''Produce the PDF file using specified import format.
        
        :param input_file_name: Input file name.
        :param format: Import format.
        :param output_file_name: Output PDF file
        :raises aspose.pdf.InvalidFileFormatException: The exception is thrown when a file is invalid.
        :raises System.ArgumentException: Input or output file name is an empty string'''
        ...
    
    @overload
    @staticmethod
    def produce(self, input_file_name: str, options: aspose.pdf.ImportOptions, output_stream: Any) -> None:
        '''Produce the PDF stream using specified import option.
        
        :param input_file_name: Input file name.
        :param options: Import option.
        :param output_stream: Output PDF stream.
        :raises aspose.pdf.InvalidFileFormatException: The exception is thrown when a file is invalid.
        :raises System.ArgumentNullException: Output stream is null
        :raises System.ArgumentException: Input file name is an empty string'''
        ...
    
    @overload
    @staticmethod
    def produce(self, input_stream: Any, options: aspose.pdf.ImportOptions, output_file_name: str) -> None:
        '''Produce the PDF file using specified import option.
        
        :param input_stream: Input stream.
        :param options: Import option.
        :param output_file_name: Output PDF file.
        :raises aspose.pdf.InvalidFileFormatException: The exception is thrown when a file is invalid.
        :raises System.ArgumentNullException: Input stream is null
        :raises System.ArgumentException: Output file name is an empty string'''
        ...
    
    @overload
    @staticmethod
    def produce(self, input_file_name: str, options: aspose.pdf.ImportOptions, output_file_name: str) -> None:
        '''Produce the PDF file using specified import option.
        
        :param input_file_name: Input file name.
        :param options: Import option.
        :param output_file_name: Output PDF stream.
        :raises aspose.pdf.InvalidFileFormatException: The exception is thrown when a file is invalid.
        :raises System.ArgumentException: Input or output file name is an empty string'''
        ...
    
    @overload
    @staticmethod
    def produce(self, input_stream: Any, options: aspose.pdf.ImportOptions, output_stream: Any) -> None:
        '''Produce the PDF file using specified import option.
        
        :param input_stream: Input stream.
        :param options: Import option.
        :param output_stream: Output PDF stream.
        :raises aspose.pdf.InvalidFileFormatException: The exception is thrown when a file is invalid.
        :raises System.ArgumentNullException: Input or output stream is null.'''
        ...
    
    ...

class PdfViewer:
    '''Represents a class to view or print a pdf.'''
    
    @overload
    def __init__(self):
        '''Initializes new :class:`PdfViewer` object.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfViewer` object.
        
        :param document: Document object.'''
        ...
    
    @overload
    def print_large_pdf(self, file_path: str) -> None:
        '''Opens and prints a large Pdf file. If your Pdf file has hundreds of pages or more or its size is
        more than 3 MB, this method is recommended to get better performance.
        
        This method has integrated the opening and the printing of the file and you need not
        calling the OpenPdfFile() explicitly.
        
        :param file_path: The path of Pdf file.'''
        ...
    
    @overload
    def print_large_pdf(self, input_stream: Any) -> None:
        '''Opens and prints a large Pdf stream. If your Pdf file has hundreds of pages or more or its size is
        more than 3 MB, this method is recommended to get better performance.
        
        This method has integrated the opening and the printing of the file and you need not
        calling the OpenPdfFile() explicitly.
        
        :param input_stream: The pdf stream to be opened  and printed..'''
        ...
    
    @overload
    def print_large_pdf(self, file_path: str, printer_settings: aspose.pdf.printing.PrinterSettings) -> None:
        '''Opens and prints a large Pdf file with specified printer settings. If your Pdf file has hundreds
        of pages or more or its size is more than 3 MB, this method is recommended to get better performance.
        
        This method has integrated the opening and the printing of the file and you need not
        calling the OpenPdfFile() explicitly.
        
        :param file_path: The path of Pdf file.
        :param printer_settings: The printer settings.'''
        ...
    
    @overload
    def print_large_pdf(self, input_stream: Any, printer_settings: aspose.pdf.printing.PrinterSettings) -> None:
        '''Opens and prints a large Pdf stream with specified printer settings. If your Pdf file has hundreds
        of pages or more or its size is more than 3 MB, this method is recommended to get better performance.
        
        This method has integrated the opening and the printing of the file and you need not
        calling the OpenPdfFile() explicitly.
        
        :param input_stream: The pdf stream to be opened  and printed..
        :param printer_settings: The printer settings.'''
        ...
    
    @overload
    def print_large_pdf(self, file_path: str, page_settings: aspose.pdf.printing.PageSettings, printer_settings: aspose.pdf.printing.PrinterSettings) -> None:
        '''Opens and prints a large Pdf file with specified page settings and printer settings. If your Pdf
        file has hundreds of pages or more or its size is more than 3 MB, this method is recommended to
        get better performance.
        
        This method has integrated the opening and the printing of the file and you need not
        calling the OpenPdfFile() explicitly.
        
        :param file_path: The path of Pdf file.
        :param page_settings: The page settings.
        :param printer_settings: The printer settings.'''
        ...
    
    @overload
    def print_large_pdf(self, input_stream: Any, page_settings: aspose.pdf.printing.PageSettings, printer_settings: aspose.pdf.printing.PrinterSettings) -> None:
        '''Opens and prints a large Pdf stream with specified page settings and printer settings. If your Pdf
        file has hundreds of pages or more or its size is more than 3 MB, this method is recommended to
        get better performance.
        
        This method has integrated the opening and the printing of the file and you need not
        calling the OpenPdfFile() explicitly.
        
        :param input_stream: The pdf stream to be opened and printed.
        :param page_settings: The page settings.
        :param printer_settings: The printer settings.'''
        ...
    
    @overload
    def print_document_with_settings(self, page_settings: aspose.pdf.printing.PageSettings, printer_settings: aspose.pdf.printing.PrinterSettings) -> None:
        '''Prints the Pdf document with settings. If the document size is not complatible to page size, pdf.kit will extend it to fit page size.
        
        :param page_settings: The page setting of the printing document.
        :param printer_settings: The printer setting of the printing document.'''
        ...
    
    @overload
    def print_document_with_settings(self, printer_settings: aspose.pdf.printing.PrinterSettings) -> None:
        '''Prints the Pdf document with printer settings. The output page size will fit the the document first page size.
        
        :param printer_settings: The printer setting of the printing document.'''
        ...
    
    @overload
    def open_pdf_file(self, file_path: str) -> None:
        '''Opens a Pdf file, but does not actually decode the pages of the Pdf file.
        
        :param file_path: The path of Pdf file.'''
        ...
    
    @overload
    def open_pdf_file(self, input_stream: Any) -> None:
        '''Opens a Pdf file stream. But does not actually decode the pages of the Pdf file.
        
        :param input_stream: The pdf stream to be opened.'''
        ...
    
    @overload
    def bind_pdf(self, src_file: str) -> None:
        '''Initializes the facade.
        
        :param src_file: The PDF file.'''
        ...
    
    @overload
    def bind_pdf(self, src_stream: Any) -> None:
        '''Initializes the facade.
        
        :param src_stream: The stream of PDF file.'''
        ...
    
    @overload
    def bind_pdf(self, src_doc: aspose.pdf.Document) -> None:
        '''Initializes the facade.
        
        :param src_doc: The Aspose.Pdf.Document object.'''
        ...
    
    @overload
    def save(self, dest_file: str) -> None:
        '''Saves the result PDF document to file.
        
        :param dest_file: The path of output PDF document.'''
        ...
    
    @overload
    def save(self, dest_stream: Any) -> None:
        '''Saves the result PDF document to stream.
        
        :param dest_stream: The stream of output PDF document.'''
        ...
    
    def decode_all_pages(self) -> list[aspose.pydrawing.Bitmap]:
        '''Get pages of current pdf file.
        
        :returns: return the array of Pdf page images.'''
        ...
    
    def decode_page(self, page_number: int) -> aspose.pydrawing.Bitmap:
        '''Decodes a page of one Pdf file.
        
        :param page_number: The page number of one Pdf file which must be between 1 and PageCount.
        :returns: return the Pdf page image.'''
        ...
    
    def print_document_with_setup(self) -> None:
        '''Prints the Pdf document with a setup dialog. Choose a printer using the dialog.'''
        ...
    
    def print_document(self) -> None:
        '''Prints the Pdf document using default printer.'''
        ...
    
    def get_default_page_settings(self) -> aspose.pdf.printing.PageSettings:
        '''Gets the default page settings.
        
        :returns: Page settings object.'''
        ...
    
    def get_default_printer_settings(self) -> aspose.pdf.printing.PrinterSettings:
        '''Gets the default printer settings.
        
        :returns: Printer settings object.'''
        ...
    
    def close_pdf_file(self) -> None:
        '''Closes the current Pdf file.'''
        ...
    
    def close(self) -> None:
        '''Closes the facade.'''
        ...
    
    @property
    def show_hidden_areas(self) -> bool:
        '''Gets or sets flag that controls visibility of hidden areas on the page.'''
        ...
    
    @show_hidden_areas.setter
    def show_hidden_areas(self, value: bool):
        ...
    
    @property
    def print_status(self) -> object:
        '''Gets the result of printing job. If success than null; otherwise, exception object.'''
        ...
    
    @property
    def use_intermidiate_image(self) -> bool:
        '''Gets/sets the using of conversion of pdf page into intermidiate png file during printing in file mode. Use it when the size of output file is important.'''
        ...
    
    @use_intermidiate_image.setter
    def use_intermidiate_image(self, value: bool):
        ...
    
    @property
    def coordinate_type(self) -> aspose.pdf.PageCoordinateType:
        '''Gets or sets the page coordinate type (Media/Crop boxes). CropBox value is used by default.'''
        ...
    
    @coordinate_type.setter
    def coordinate_type(self, value: aspose.pdf.PageCoordinateType):
        ...
    
    @property
    def print_as_image(self) -> bool:
        '''Sets or gets a mode for PdfViewer to print as image.
        
        If true prints always as image (generates image that is printed)
        If false prints directly to device if all features are supported. In case document contains non-supported features the system may automatically decide to print as image.
        
        Default falue is false.'''
        ...
    
    @print_as_image.setter
    def print_as_image(self, value: bool):
        ...
    
    @property
    def page_count(self) -> int:
        '''Gets page count of the current Pdf file.
        
        :returns: return page count.'''
        ...
    
    @property
    def password(self) -> str:
        '''Gets or sets input document password.'''
        ...
    
    @password.setter
    def password(self, value: str):
        ...
    
    @property
    def print_page_dialog(self) -> bool:
        '''Gets or sets a bool value that indicates whether produce the page number dialog when printing.'''
        ...
    
    @print_page_dialog.setter
    def print_page_dialog(self, value: bool):
        ...
    
    @property
    def print_as_grayscale(self) -> bool:
        '''Gets or sets a bool value that indicates whether the page is being printed as grayscale. By default is false.
        
        Default falue is false.'''
        ...
    
    @print_as_grayscale.setter
    def print_as_grayscale(self, value: bool):
        ...
    
    @property
    def printer_job_name(self) -> str:
        '''Gets or sets name of document in printer queue when document is printed. Default value is file name.'''
        ...
    
    @printer_job_name.setter
    def printer_job_name(self, value: str):
        ...
    
    @property
    def form_presentation_mode(self) -> aspose.pdf.devices.FormPresentationMode:
        '''Gets or sets form presentation mode.'''
        ...
    
    @form_presentation_mode.setter
    def form_presentation_mode(self, value: aspose.pdf.devices.FormPresentationMode):
        ...
    
    @property
    def rendering_options(self) -> aspose.pdf.RenderingOptions:
        '''Gets or sets rendering options.'''
        ...
    
    @rendering_options.setter
    def rendering_options(self, value: aspose.pdf.RenderingOptions):
        ...
    
    @property
    def vertical_alignment(self) -> aspose.pdf.VerticalAlignment:
        '''Gets or sets a value that indicates vertical alignment'''
        ...
    
    @vertical_alignment.setter
    def vertical_alignment(self, value: aspose.pdf.VerticalAlignment):
        ...
    
    @property
    def horizontal_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets or sets a value that indicates horizontal alignment'''
        ...
    
    @horizontal_alignment.setter
    def horizontal_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def auto_resize(self) -> bool:
        '''Gets or sets a bool value that indicates whether the file be printed with optimized size.'''
        ...
    
    @auto_resize.setter
    def auto_resize(self, value: bool):
        ...
    
    @property
    def auto_rotate(self) -> bool:
        '''Gets or sets a bool value that indicates whether the file be printed with auto rotation'''
        ...
    
    @auto_rotate.setter
    def auto_rotate(self, value: bool):
        ...
    
    @property
    def auto_rotate_mode(self) -> aspose.pdf.facades.AutoRotateMode:
        '''Gets or sets a AutoRotateMode value that indicates direction of rotation'''
        ...
    
    @auto_rotate_mode.setter
    def auto_rotate_mode(self, value: aspose.pdf.facades.AutoRotateMode):
        ...
    
    @property
    def resolution(self) -> int:
        '''Gets or sets resolution during viewing and printing. The higher resolution, the slower speed. The default value is 150.'''
        ...
    
    @resolution.setter
    def resolution(self, value: int):
        ...
    
    @property
    def scale_factor(self) -> float:
        '''Gets or sets a floating point value that indicates scale factor. The default value is 1.0.'''
        ...
    
    @scale_factor.setter
    def scale_factor(self, value: float):
        ...
    
    ...

class PdfXmpMetadata(aspose.pdf.facades.SaveableFacade):
    '''Class for manipulation with XMP metadata.'''
    
    @overload
    def __init__(self):
        '''Constructor for PdfXmpMetadata.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Initializes new :class:`PdfXmpMetadata` object on base of the document.
        
        :param document: Pdf document.'''
        ...
    
    @overload
    def add(self, key: aspose.pdf.facades.DefaultMetadataProperties, value: aspose.pdf.XmpValue) -> None:
        '''Adds value to XMP metadata.
        
        :param key: The key name.
        :param value: Value which will be added.'''
        ...
    
    @overload
    def add(self, xmp_pdf_a_extension_object: aspose.pdf.XmpPdfAExtensionObject, namespace_prefix: str, namespace_uri: str, schema_description: str) -> None:
        '''Adds extension field into metadata.
        
        :param xmp_pdf_a_extension_object: The pdf extension object to add.
        :param namespace_prefix: The prefix of schema.
        :param namespace_uri: The namespace uri of schema.
        :param schema_description: The optional description of schema.'''
        ...
    
    @overload
    def add(self, key: str, value: aspose.pdf.XmpValue) -> None:
        '''Adds new element to the dictionary object.
        
        :param key: Key of new element.
        :param value: Value of the element.'''
        ...
    
    @overload
    def add(self, key: str, value: object) -> None:
        '''Adds new element to the dictionary object.
        
        :param key: Key of new element.
        :param value: Value of the element.'''
        ...
    
    @overload
    def remove(self, key: aspose.pdf.facades.DefaultMetadataProperties) -> None:
        '''Removes element with specified key.
        
        :param key: Key of the element which will be deleted.'''
        ...
    
    @overload
    def remove(self, key: str) -> bool:
        '''Removes key from the dictionary.
        
        :param key: Key which will be removed.
        :returns: True - if key removed; otherwise, false.'''
        ...
    
    @overload
    def contains(self, key: str) -> bool:
        '''Checks if dictionary contains the specified key.
        
        :param key: Key which will be checked.
        :returns: True - if the dictionary contains the specified key; otherwise, false.'''
        ...
    
    @overload
    def contains(self, property: aspose.pdf.facades.DefaultMetadataProperties) -> bool:
        '''Checks if dictionary contains the specified property.
        
        :param property: Property which will be checked.
        :returns: True - if the dictionary contains the specified property; otherwise, false.'''
        ...
    
    @overload
    def get_xmp_metadata(self) -> bytes:
        '''Get the XmpMetadata of the input pdf in a xml format.
        
        :returns: The bytes of the XmpMetadata.'''
        ...
    
    @overload
    def get_xmp_metadata(self, name: str) -> bytes:
        '''Get a part of the XmpMetadata of the input pdf according to a meta name.
        
        :param name: Metadata name.
        :returns: Bytes of metadata.'''
        ...
    
    def register_namespace_uri(self, prefix: str, namespace_uri: str) -> None:
        '''Registers the namespace URI.
        
        :param prefix: The prefix.
        :param namespace_uri: The namespace URI.'''
        ...
    
    def get_namespace_uri_by_prefix(self, prefix: str) -> str:
        '''Gets namespace URI by prefix.
        
        :param prefix: The prefix.
        :returns: Namespace URI.'''
        ...
    
    def get_prefix_by_namespace_uri(self, namespace_uri: str) -> str:
        '''Gets the prefix by namespace URI.
        
        :param namespace_uri: Namespace URI.
        :returns: The prefix value.'''
        ...
    
    def clear(self) -> None:
        '''Removes all elements from the object.'''
        ...
    
    def contains_key(self, key: str) -> bool:
        '''Determines does this dictionary contasins specified key.
        
        :param key: Key to search in the dictionary.
        :returns: true if key is found.'''
        ...
    
    def try_get_value(self, key: str, value: aspose.pdf.XmpValue) -> bool:
        '''Tries to find key in the dictionary and retreives value if found.
        
        :param key: Key to search in the dictionary.
        :param value: Retreived value.
        :returns: true if key was found.'''
        ...
    
    @property
    def keys(self) -> None:
        '''Gets keys from the dictionary.'''
        ...
    
    @property
    def values(self) -> None:
        '''Gets the collection of values in dictionary.'''
        ...
    
    @property
    def is_fixed_size(self) -> bool:
        '''Returns true is collection has fixed size.'''
        ...
    
    @property
    def is_read_only(self) -> bool:
        '''Returns true if collection is read-only.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets count if items in the collection.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Returns true if collection is synchronized.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets synchroniztion object of the collection.'''
        ...
    
    ...

class ReplaceTextStrategy:
    '''This class contains parameters which define PdfContentEditor behavior when ReplaceText operation is performed.'''
    
    def __init__(self):
        ...
    
    @property
    def is_regular_expression_used(self) -> bool:
        '''If false, string to find is a simple text. If true, string to find is regular expression.'''
        ...
    
    @is_regular_expression_used.setter
    def is_regular_expression_used(self, value: bool):
        ...
    
    @property
    def no_character_behavior(self) -> None:
        '''Action which is performed when no approppriate font found for changed text
        (Throw exception / Substitute other font / Replace anyway).'''
        ...
    
    @no_character_behavior.setter
    def no_character_behavior(self, value: None):
        ...
    
    @property
    def replace_scope(self) -> None:
        '''Scope of the replacement operation (replace first occurence or replace all occurences).'''
        ...
    
    @replace_scope.setter
    def replace_scope(self, value: None):
        ...
    
    class NoCharacterAction:
          '''Action to perform if font does not contain required character.'''

          THROW_EXCEPTION: NoCharacterAction
          USE_STANDARD_FONT: NoCharacterAction
          REPLACE_ANYWAY: NoCharacterAction

    class Scope:
          '''Scope where replace text operation is applied.
          REPLACE_FIRST by default'''

          REPLACE_FIRST: Scope
          REPLACE_ALL: Scope

    ...

class SaveableFacade(aspose.pdf.facades.Facade):
    '''Base class for all saveable facades.'''
    
    @overload
    def save(self, dest_file: str) -> None:
        '''Saves the PDF document to the specified file.
        
        :param dest_file: The destination file.'''
        ...
    
    @overload
    def save(self, dest_stream: Any) -> None:
        '''Saves the PDF document to the specified stream.
        
        :param dest_stream: The destination stream.'''
        ...
    
    ...

class Stamp:
    '''Class represeting stamp.'''
    
    def __init__(self):
        ...
    
    @overload
    def bind_pdf(self, pdf_file: str, page_number: int) -> None:
        '''Sets PDF file and number of page which will be used as stamp.
        
        :param pdf_file: Path to PDF file.
        :param page_number: Number of page in PDF file'''
        ...
    
    @overload
    def bind_pdf(self, pdf_stream: Any, page_number: int) -> None:
        '''Sets PDF file and number of page which will be used as stamp.
        
        :param pdf_stream: Stream which contains PDF document.
        :param page_number: Page index of the document whihc will be used as stamp.'''
        ...
    
    @overload
    def bind_image(self, image_file: str) -> None:
        '''Sets image as a stamp.
        
        :param image_file: Image file name and path.'''
        ...
    
    @overload
    def bind_image(self, image: Any) -> None:
        '''Sets image which will be used as stamp.
        
        :param image: Stream which contains image data.'''
        ...
    
    def bind_logo(self, formatted_text: aspose.pdf.facades.FormattedText) -> None:
        '''Sets text as stamp.
        
        :param formatted_text: FormattedText object which specifies text and text properties.'''
        ...
    
    def bind_text_state(self, text_state: aspose.pdf.text.TextState) -> None:
        '''Sets text state of stamp text.
        
        :param text_state: TextState object which specifies text properties.'''
        ...
    
    def set_origin(self, origin_x: float, origin_y: float) -> None:
        '''Sets position on page where stamp will be placed.
        
        :param origin_x: X coordinate of the stamp.
        :param origin_y: Y coordinate of the stamp.'''
        ...
    
    def set_image_size(self, width: float, height: float) -> None:
        '''Sets size of image stamp. Image will be scaled according to the specified values.
        
        :param width: Image width.
        :param height: Image height.'''
        ...
    
    @property
    def stamp_id(self) -> int:
        '''Gets or sets identifier of stamp.'''
        ...
    
    @stamp_id.setter
    def stamp_id(self, value: int):
        ...
    
    @property
    def quality(self) -> int:
        '''Gets or sets quality of image stamp in percent. Valiued values 0..100%.'''
        ...
    
    @quality.setter
    def quality(self, value: int):
        ...
    
    @property
    def opacity(self) -> float:
        '''Gets or sets opacity of the stamp.'''
        ...
    
    @opacity.setter
    def opacity(self, value: float):
        ...
    
    @property
    def page_number(self) -> int:
        '''Gets or sets page number.'''
        ...
    
    @page_number.setter
    def page_number(self, value: int):
        ...
    
    @property
    def pages(self) -> list[int]:
        '''Gets or sets array with numbers of pages which will be affected by stamp.
        If Pages = null all pages of the document are affected.'''
        ...
    
    @pages.setter
    def pages(self, value: list[int]):
        ...
    
    @property
    def rotation(self) -> float:
        '''Gets or sets rotation of the stamp in degrees.'''
        ...
    
    @rotation.setter
    def rotation(self, value: float):
        ...
    
    @property
    def is_background(self) -> bool:
        '''Gets or sets background status. If true stamp will be placed as background of the spamped page.
        By default is set to false.'''
        ...
    
    @is_background.setter
    def is_background(self, value: bool):
        ...
    
    @property
    def blending_space(self) -> aspose.pdf.facades.BlendingColorSpace:
        '''Gets or sets a BlendingColorSpace value that defines a color space
        that is used to perform transparency and blending operations on the page.'''
        ...
    
    @blending_space.setter
    def blending_space(self, value: aspose.pdf.facades.BlendingColorSpace):
        ...
    
    ...

class StampInfo:
    '''Class representing stamp information.'''
    
    @property
    def stamp_id(self) -> int:
        '''Gets identifier of the stamp.'''
        ...
    
    @property
    def index_on_page(self) -> int:
        '''Gets stamp index on the page.'''
        ...
    
    @property
    def stamp_type(self) -> aspose.pdf.facades.StampType:
        '''Gets stamp type (image / form).'''
        ...
    
    @property
    def rectangle(self) -> aspose.pdf.Rectangle:
        '''Gets rectangle where stamp is placed.'''
        ...
    
    @property
    def image(self) -> aspose.pydrawing.Image:
        '''Gets image of stamp. May be null if stamp does not contain images (for example for text stamp).'''
        ...
    
    @property
    def form(self) -> aspose.pdf.XForm:
        '''Gets XForm of the stamp.'''
        ...
    
    @property
    def text(self) -> str:
        '''Gets text in the stamp.'''
        ...
    
    @property
    def visible(self) -> bool:
        '''Gets visibility of stamp. If false then stamp is hidden (with HideStampById). Hidden stamp may be restored by ShowStampById.'''
        ...
    
    ...

class TextProperties:
    '''Represents text properties such as: text size, color, style etc.'''
    
    def __init__(self, text_size: float):
        '''Creates :class:`TextProperties` object for the specified text size
        
        :param text_size: Text size value.'''
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Gets or sets text color.'''
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def is_color_specified(self) -> bool:
        '''Gets or sets a value that indicates whether the :attr:`TextProperties.color` property is specified.'''
        ...
    
    @property
    def text_size(self) -> float:
        '''Gets or sets text size.'''
        ...
    
    @text_size.setter
    def text_size(self, value: float):
        ...
    
    @property
    def is_text_size_specified(self) -> bool:
        '''Gets or sets a value that indicates whether the :attr:`TextProperties.text_size` property is specified.'''
        ...
    
    ...

class VerticalAlignmentType:
    '''Class representing possible vertical alignment values.'''
    
    def __init__(self, name: str):
        '''Initializes vertical alignment by its name.
        
        :param name: Vertical alignment type name.'''
        ...
    
    top: aspose.pdf.facades.VerticalAlignmentType
    
    center: aspose.pdf.facades.VerticalAlignmentType
    
    bottom: aspose.pdf.facades.VerticalAlignmentType
    
    ...

class ViewerPreference:
    '''Describes viewer prefereces (page mode, non full screen page mode, page layout).'''
    
    def __init__(self):
        ...
    
    PAGE_MODE_USE_OC: int
    
    DISPLAY_DOC_TITLE: int
    
    NON_FULL_SCREEN_PAGE_MODE_USE_OC: int
    
    PAGE_LAYOUT_SINGLE_PAGE: int
    
    PAGE_LAYOUT_ONE_COLUMN: int
    
    PAGE_LAYOUT_TWO_COLUMN_LEFT: int
    
    PAGE_LAYOUT_TWO_COLUMN_RIGHT: int
    
    PAGE_MODE_USE_NONE: int
    
    PAGE_MODE_USE_OUTLINES: int
    
    PAGE_MODE_USE_THUMBS: int
    
    PAGE_MODE_FULL_SCREEN: int
    
    PAGE_MODE_USE_ATTACHMENT: int
    
    HIDE_TOOLBAR: int
    
    HIDE_MENUBAR: int
    
    HIDE_WINDOW_UI: int
    
    FIT_WINDOW: int
    
    CENTER_WINDOW: int
    
    NON_FULL_SCREEN_PAGE_MODE_USE_NONE: int
    
    NON_FULL_SCREEN_PAGE_MODE_USE_OUTLINES: int
    
    NON_FULL_SCREEN_PAGE_MODE_USE_THUMBS: int
    
    DIRECTION_L2R: int
    
    DIRECTION_R2L: int
    
    SIMPLEX: int
    
    DUPLEX_FLIP_SHORT_EDGE: int
    
    DUPLEX_FLIP_LONG_EDGE: int

    PRINT_SCALING_APP_DEFAULT: int

    PRINT_SCALING_NONE: int

    PICK_TRAY_BY_PDF_SIZE: int
    
    ...

class Algorithm:
    '''Represents algorithms which can be used to encrypt pdf document.'''
    
    RC4: Algorithm
    AES: Algorithm

class AutoRotateMode:
    '''Direction of the rotation when document is printed.'''
    
    NONE: AutoRotateMode
    CLOCK_WISE: AutoRotateMode
    ANTI_CLOCK_WISE: AutoRotateMode

class BlendingColorSpace:
    '''Class represents blending color space.'''
    
    DONT_CHANGE: BlendingColorSpace
    AUTO: BlendingColorSpace
    DEVICE_RGB: BlendingColorSpace
    DEVICE_CMYK: BlendingColorSpace

class DataType:
    '''Enumerates field types definitions.'''
    
    FDF: DataType
    XML: DataType
    XFDF: DataType
    PDF: DataType
    OLEDB: DataType
    ODBC: DataType

class DefaultMetadataProperties:
    '''Enumeration of standard XMP properties.'''
    
    ADVISORY: DefaultMetadataProperties
    BASE_URL: DefaultMetadataProperties
    CREATE_DATE: DefaultMetadataProperties
    CREATOR_TOOL: DefaultMetadataProperties
    IDENTIFIER: DefaultMetadataProperties
    METADATA_DATE: DefaultMetadataProperties
    MODIFY_DATE: DefaultMetadataProperties
    NICKNAME: DefaultMetadataProperties
    THUMBNAILS: DefaultMetadataProperties

class EncodingType:
    '''Enumerates encoding types of the text using.'''
    
    IDENTITY_H: EncodingType
    IDENTITY_V: EncodingType
    CP1250: EncodingType
    CP1252: EncodingType
    CP1257: EncodingType
    WINANSI: EncodingType
    MACROMAN: EncodingType

class FieldType:
    '''Enumeration of possible field types.'''
    
    TEXT: FieldType
    COMBO_BOX: FieldType
    LIST_BOX: FieldType
    RADIO: FieldType
    CHECK_BOX: FieldType
    PUSH_BUTTON: FieldType
    MULTI_LINE_TEXT: FieldType
    BARCODE: FieldType
    INVALID_NAME_OR_TYPE: FieldType
    SIGNATURE: FieldType
    IMAGE: FieldType
    NUMERIC: FieldType
    DATE_TIME: FieldType

class FontStyle:
    '''Enumerates 14 types of font.'''
    
    COURIER: FontStyle
    COURIER_BOLD: FontStyle
    COURIER_OBLIQUE: FontStyle
    COURIER_BOLD_OBLIQUE: FontStyle
    HELVETICA: FontStyle
    HELVETICA_BOLD: FontStyle
    HELVETICA_OBLIQUE: FontStyle
    HELVETICA_BOLD_OBLIQUE: FontStyle
    SYMBOL: FontStyle
    TIMES_ROMAN: FontStyle
    TIMES_BOLD: FontStyle
    TIMES_ITALIC: FontStyle
    TIMES_BOLD_ITALIC: FontStyle
    ZAPF_DINGBATS: FontStyle
    UNKNOWN: FontStyle
    CJK_FONT: FontStyle

class ImageMergeMode:
    '''Represents modes for merging images.'''
    
    VERTICAL: ImageMergeMode
    HORIZONTAL: ImageMergeMode
    CENTER: ImageMergeMode

class KeySize:
    '''Defines different key sizes which can be used to encrypt pdf documents.'''
    
    X40: KeySize
    X128: KeySize
    X256: KeySize

class PositioningMode:
    '''Defines positioning mode.
    Possible values include Legacy (backward compatibility) and
    Current (updated text position calculation method)'''
    
    LEGACY: PositioningMode
    MODERN_LINE_SPACING: PositioningMode
    CURRENT: PositioningMode

class PropertyFlag:
    '''Enumeration of possible field flags.'''
    
    READ_ONLY: PropertyFlag
    REQUIRED: PropertyFlag
    NO_EXPORT: PropertyFlag
    INVALID_FLAG: PropertyFlag

class StampType:
    '''Describes stamp types.'''
    
    FORM: StampType
    IMAGE: StampType

class SubmitFormFlag:
    '''Enumeration of possible submit form flags.'''
    
    FDF: SubmitFormFlag
    HTML: SubmitFormFlag
    XFDF: SubmitFormFlag
    FDF_WITH_COMMENTS: SubmitFormFlag
    XFDF_WITH_COMMENTS: SubmitFormFlag
    PDF: SubmitFormFlag

class WordWrapMode:
    '''Defines word wrapping strategies'''
    
    DEFAULT: WordWrapMode
    BY_WORDS: WordWrapMode

