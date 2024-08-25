from aspose.pdf import ai
from aspose.pdf import annotations
from aspose.pdf import comparison
from aspose.pdf import devices
from aspose.pdf import drawing
from aspose.pdf import facades
from aspose.pdf import forms
from aspose.pdf import groupprocessor
from aspose.pdf import logicalstructure
from aspose.pdf import multithreading
from aspose.pdf import operators
from aspose.pdf import optimization
from aspose.pdf import pdfaoptionclasses
from aspose.pdf import pdftomarkdown
from aspose.pdf import printing
from aspose.pdf import sanitization
from aspose.pdf import structure
from aspose.pdf import tagged
from aspose.pdf import text
from aspose.pdf import utils
from aspose.pdf import vector
from aspose.pdf import xfaconverter
import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

from typing import Any

def get_pyinstaller_hook_dirs() -> Any:
  """Function required by PyInstaller. Returns paths to module
  PyInstaller hooks. Not intended to be called explicitly."""
...

class ApsLoadOptions(aspose.pdf.LoadOptions):
    '''Class describes aps load options.'''
    
    def __init__(self):
        ...
    
    ...

class ApsSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to APS XML format.'''
    
    def __init__(self):
        ...
    
    ...

class Artifact:
    '''Class represents PDF Artifact object.'''
    
    @overload
    def __init__(self, type: str, sub_type: str):
        '''Constructor of artifact with specified type and subtype
        
        :param type: Name of artifact type.
        :param sub_type: NAme of artifact subtype.'''
        ...
    
    @overload
    def __init__(self, type, sub_type):
        '''Constructor of artifact with specified type and subtype
        
        :param type: Artifact type.
        :param sub_type: Artifact subtype.'''
        ...
    
    @overload
    def set_image(self, image_stream: Any) -> None:
        '''Sets image of the artifact.
        
        :param image_stream: Stream which contains image data.'''
        ...
    
    @overload
    def set_image(self, image_name: str) -> None:
        '''Sets image of the artifact.
        
        :param image_name: Name of image file.'''
        ...
    
    def set_text(self, formatted_text: aspose.pdf.facades.FormattedText) -> None:
        '''Sets text of the artifact.
        
        :param formatted_text: FormattedText object which contains artifact text.'''
        ...
    
    def set_text_and_state(self, text: str, text_state: aspose.pdf.text.TextState) -> None:
        '''Set text and text properties of the artifact.
        
        :param text: Text string.
        :param text_state: Text state.'''
        ...
    
    def set_page_number_replacement_string(self, value: str) -> None:
        '''Sets what string will be replaced with the page number.
        The default value is #.
        
        :param value: String value that should be replaced with the page number.'''
        ...

    def set_lines_and_state(self, text: list[str], text_state: aspose.pdf.text.TextState) -> None:
        '''Set text and text properties of the artifact. Allows to specify multiple lines.
        
        :param text: Array of text string.
        :param text_state: Text properties.'''
        ...
    
    def set_pdf_page(self, page: aspose.pdf.Page) -> None:
        '''Sets PDF page which is placed on the document page as artifact.
        
        :param page: Page which is placed as Artifcact.'''
        ...
    
    def get_value(self, name: str) -> str:
        '''Gets custom value of artifact.
        
        :param name: Name of value.
        :returns: Value, or null if value does not exists.'''
        ...
    
    def set_value(self, name: str, value: str) -> None:
        '''Sets custom value of artifact.
        
        :param name: Name of custom value.
        :param value: Custom value in the artifact.'''
        ...
    
    def remove_value(self, name: str) -> None:
        '''Remove custom value from the artifact.
        
        :param name: Name of custom value to be removed.'''
        ...
    
    def begin_updates(self) -> None:
        '''Start delated updates. Use this feature if you need make several changes to the same artifact to improve performance.
        Usually artifact operators are changed anytime when artifact property was changed. This causes changing of page contents
        everytime when artifact was changed. To avoid this effect put all artifact updates between StartUpdates/SaveUpdates calls.
        This allows to change page contents only once.'''
        ...
    
    def save_updates(self) -> None:
        '''Saves all updates in artifact which were made after BeginUpdates() call.'''
        ...
    
    @property
    def custom_type(self) -> str:
        '''Gets name of artifact type. May be used if artifact type is non standard.'''
        ...
    
    @custom_type.setter
    def custom_type(self, value: str):
        ...
    
    @property
    def custom_subtype(self) -> str:
        '''Gets name of artifact subtype. May be used  if artifact subtype is not standard subtype.'''
        ...
    
    @custom_subtype.setter
    def custom_subtype(self, value: str):
        ...
    
    @property
    def type(self) -> None:
        '''Gets artifact type.'''
        ...
    
    @type.setter
    def type(self, value: None):
        ...
    
    @property
    def subtype(self) -> None:
        '''Gets artifact subtype. If artifact has non-standard subtype, name of the subtype may be read via CustomSubtype.'''
        ...
    
    @subtype.setter
    def subtype(self, value: None):
        ...
    
    @property
    def contents(self) -> None:
        '''Gets collection of artifact internal operators.'''
        ...
    
    @property
    def form(self) -> aspose.pdf.XForm:
        '''Gets XForm of the artifact (if XForm is used).'''
        ...
    
    @property
    def rectangle(self) -> aspose.pdf.Rectangle:
        '''Gets rectangle of the artifact.'''
        ...
    
    @property
    def position(self) -> aspose.pdf.Point:
        '''Gets or sets artifact position.
        If this property is specified, then margins and alignments are ignored.'''
        ...
    
    @position.setter
    def position(self, value: aspose.pdf.Point):
        ...
    
    @property
    def right_margin(self) -> float:
        '''Right margin of artifact.
        If position is specified explicitly (in Position property) this value is ignored.'''
        ...
    
    @right_margin.setter
    def right_margin(self, value: float):
        ...
    
    @property
    def left_margin(self) -> float:
        '''Left margin of artifact.
        If position is specified explicitly (in Position property) this value is ignored.'''
        ...
    
    @left_margin.setter
    def left_margin(self, value: float):
        ...
    
    @property
    def top_margin(self) -> float:
        '''Top margin of artifact.
        If position is specified explicitly (in Position property) this value is ignored.'''
        ...
    
    @top_margin.setter
    def top_margin(self, value: float):
        ...
    
    @property
    def bottom_margin(self) -> float:
        '''Bottom margin of artifact.
        If position is specified explicitly (in Position property) this value is ignored.'''
        ...
    
    @bottom_margin.setter
    def bottom_margin(self, value: float):
        ...
    
    @property
    def artifact_horizontal_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Horizontal alignment of artifact.
        If position is specified explicitly (in Position property) this value is ignored.'''
        ...
    
    @artifact_horizontal_alignment.setter
    def artifact_horizontal_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def artifact_vertical_alignment(self) -> aspose.pdf.VerticalAlignment:
        '''Vertical alignment of artifact.
        If position is specified explicitly (in Position property) this value is ignored.'''
        ...
    
    @artifact_vertical_alignment.setter
    def artifact_vertical_alignment(self, value: aspose.pdf.VerticalAlignment):
        ...
    
    @property
    def rotation(self) -> float:
        '''Gets or sets artifact rotation angle.'''
        ...
    
    @rotation.setter
    def rotation(self, value: float):
        ...
    
    @property
    def text(self) -> str:
        '''Gets text of the artifact.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    @property
    def image(self) -> aspose.pdf.XImage:
        '''Gets image of the artifact (if presents).'''
        ...
    
    @property
    def opacity(self) -> float:
        '''Gets or sets opacity of the artifact. Possible values are in range 0..1.'''
        ...
    
    @opacity.setter
    def opacity(self, value: float):
        ...
    
    @property
    def lines(self) -> None:
        '''Lines of multiline text artifact.'''
        ...
    
    @property
    def text_state(self) -> aspose.pdf.text.TextState:
        '''Text state for artifact text.'''
        ...
    
    @text_state.setter
    def text_state(self, value: aspose.pdf.text.TextState):
        ...
    
    @property
    def is_background(self) -> bool:
        '''If true Artifact is placed behind page contents.'''
        ...
    
    @is_background.setter
    def is_background(self, value: bool):
        ...

    class ArtifactSubtype:
          '''Enumeration of possible artifacts subtype.'''

          HEADER: ArtifactSubtype
          FOOTER: ArtifactSubtype
          WATERMARK: ArtifactSubtype
          BACKGROUND: ArtifactSubtype
          UNDEFINED: ArtifactSubtype

    class ArtifactType:
          '''Enumeration of possuble artifact types.'''

          PAGINATION: ArtifactType
          LAYOUT: ArtifactType 
          PAGE: ArtifactType
          BACKGROUND: ArtifactType
          UNDEFINED: ArtifactType
    
    ...

class ArtifactCollection:
    '''Class represents artifact collection.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.Artifact:
        '''Gets artifact by index. Index is started from 1.
        
        :param index: Index of the artifact.
        :returns: Artifact on the page.'''
        ...
    
    @overload
    def delete(self, artifact: aspose.pdf.Artifact) -> None:
        '''Deletes specified artifact.
        
        :param artifact: Artifact which will be deleted.'''
        ...
    
    @overload
    def delete(self, index: int) -> None:
        '''Deletes artifact by its index.
        
        :param index: Index of artifact to delete.'''
        ...
    
    def find_by_value(self, name: str, expected_value: str) -> None:
        '''Finds artifacts by custom value.
        
        :param name: Name of custom value.
        :param expected_value: Value to find.
        :returns: List of found artifacts.'''
        ...
    
    def update(self, artifact: aspose.pdf.Artifact) -> None:
        '''Update artifact inside the collection.
        
        :param artifact: Artifact to be updated.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Is this object synchronized.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets synchronization object of the collection.'''
        ...
    
    ...

class BackgroundArtifact(aspose.pdf.Artifact):
    '''Class descibes background artifact. This artifact allows to set background of the page.'''
    
    def __init__(self):
        '''Initializes BackgroundArtifact object.'''
        ...
    
    @property
    def background_color(self) -> aspose.pdf.Color:
        '''Gets or sets bacground color of background artifact'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def background_image(self) -> Any:
        '''Gets or sets bacground image of background artifact'''
        ...
    
    @background_image.setter
    def background_image(self, value: Any):
        ...
    
    ...

class BaseActionCollection:
    '''Class incapsulates basic actions wuth page/annotation/field interactive actions'''
    
    def remove_actions(self) -> None:
        '''Removes all actions of the annotation.'''
        ...
    
    ...

class BaseOperatorCollection:
    '''Represents base class for operator collection.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.Operator:
        '''Gets operator by its index.
        
        :param index: Index of operator. Numbering is starts from 1.
        :returns: Operator from requested index'''
        ...
    
    def __setitem__(self, index: int, value: aspose.pdf.Operator):
        ...
    
    def suppress_update(self) -> None:
        '''Suppresses update contents data.
        The contents stream is not updated until ResumeUpdate is called.'''
        ...
    
    def resume_update(self) -> None:
        '''Resumes document update.
        Updates contents stream in case there are any pending changes.'''
        ...
    
    def insert(self, index: int, op: aspose.pdf.Operator) -> None:
        '''Inserts operator into collection.
        
        :param index: Index where new operator must be added
        :param op: Operator which will be insterted'''
        ...
    
    def cancel_update(self) -> None:
        '''Cancels last update.
        This method may be called when the change should not raise contents update.'''
        ...
    
    @property
    def is_fast_text_extraction_mode(self) -> bool:
        '''Indicates wheather collection is limited to fast text extraction'''
        ...
    
    ...

class BaseParagraph:
    '''Represents a abstract base object can be added to the page(doc.Paragraphs.Add()).'''
    
    def clone(self) -> object:
        '''Clones this instance.
        Virtual method. Always return null.
        
        :returns: Null.'''
        ...
    
    @property
    def vertical_alignment(self) -> aspose.pdf.VerticalAlignment:
        '''Gets or sets a vertical alignment of paragraph'''
        ...
    
    @vertical_alignment.setter
    def vertical_alignment(self, value: aspose.pdf.VerticalAlignment):
        ...
    
    @property
    def horizontal_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets or sets a horizontal alignment of paragraph'''
        ...
    
    @horizontal_alignment.setter
    def horizontal_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def margin(self) -> aspose.pdf.MarginInfo:
        '''Gets or sets a outer margin for paragraph (for pdf generation)'''
        ...
    
    @margin.setter
    def margin(self, value: aspose.pdf.MarginInfo):
        ...
    
    @property
    def is_first_paragraph_in_column(self) -> bool:
        '''Gets or sets a bool value that indicates whether this paragraph will be at next column.
        Default is false.(for pdf generation)'''
        ...
    
    @is_first_paragraph_in_column.setter
    def is_first_paragraph_in_column(self, value: bool):
        ...
    
    @property
    def is_kept_with_next(self) -> bool:
        '''Gets or sets a bool value that indicates whether current paragraph remains in the same page along with next paragraph.
        Default is false.(for pdf generation)'''
        ...
    
    @is_kept_with_next.setter
    def is_kept_with_next(self, value: bool):
        ...
    
    @property
    def is_in_new_page(self) -> bool:
        '''Gets or sets a bool value that force this paragraph generates at new page.
        Default is false.(for pdf generation)'''
        ...
    
    @is_in_new_page.setter
    def is_in_new_page(self, value: bool):
        ...
    
    @property
    def is_in_line_paragraph(self) -> bool:
        '''Gets or sets a paragraph is inline.
        Default is false.(for pdf generation)'''
        ...
    
    @is_in_line_paragraph.setter
    def is_in_line_paragraph(self, value: bool):
        ...
    
    @property
    def hyperlink(self) -> aspose.pdf.Hyperlink:
        '''Gets or sets the fragment hyperlink(for pdf generator).'''
        ...
    
    @hyperlink.setter
    def hyperlink(self, value: aspose.pdf.Hyperlink):
        ...
    
    @property
    def z_index(self) -> int:
        '''Gets or sets a int value that indicates the Z-order of the graph. A graph with larger ZIndex
        will be placed over the graph with smaller ZIndex. ZIndex can be negative. Graph with negative
        ZIndex will be placed behind the text in the page.'''
        ...
    
    @z_index.setter
    def z_index(self, value: int):
        ...
    
    ...

class BorderInfo:
    '''This class represents border for graphics elements.'''
    
    @overload
    def __init__(self, border_side: aspose.pdf.BorderSide, border_color: aspose.pdf.Color):
        '''Initializes a new instance of the :class:`BorderInfo` class.
        
        :param border_side: Indicates the border sides info. For example: (int)(BorderSide.Left | BorderSide.Top).
        :param border_color: The border color.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`BorderInfo` class.'''
        ...
    
    @overload
    def __init__(self, border_side: aspose.pdf.BorderSide):
        '''Initializes a new instance of the :class:`BorderInfo` class.
        
        :param border_side: Indicates the border sides info. For example: (BorderSide.Left | BorderSide.Top).'''
        ...
    
    @overload
    def __init__(self, border_side: aspose.pdf.BorderSide, border_width: float):
        '''Initializes a new instance of the :class:`BorderInfo` class.
        
        :param border_side: Indicates the border sides info. For example: (BorderSide.Left | BorderSide.Top).
        :param border_width: The width of the border.'''
        ...
    
    @overload
    def __init__(self, border_side: aspose.pdf.BorderSide, border_width: float, border_color: aspose.pdf.Color):
        '''Initializes a new instance of the :class:`BorderInfo` class.
        
        :param border_side: Indicates the border sides info. For example: (BorderSide.Left | BorderSide.Top).
        :param border_width: The width of the border.
        :param border_color: The border color.'''
        ...
    
    @overload
    def __init__(self, border_side: aspose.pdf.BorderSide, info: aspose.pdf.GraphInfo):
        '''Initializes a new instance of the :class:`BorderInfo` class.
        
        :param border_side: Indicates the border sides info. For example: (BorderSide.Left | BorderSide.Top).
        :param info: The border info.'''
        ...
    
    def clone(self) -> object:
        '''Clones a new BorderInfo object.
        
        :returns: The new BorderInfo object.'''
        ...
    
    @property
    def left(self) -> aspose.pdf.GraphInfo:
        '''Gets or sets a object that indicates left of the border.'''
        ...
    
    @left.setter
    def left(self, value: aspose.pdf.GraphInfo):
        ...
    
    @property
    def right(self) -> aspose.pdf.GraphInfo:
        '''Gets or sets a object that indicates right of the border.'''
        ...
    
    @right.setter
    def right(self, value: aspose.pdf.GraphInfo):
        ...
    
    @property
    def top(self) -> aspose.pdf.GraphInfo:
        '''Gets or sets a object that indicates the top border.'''
        ...
    
    @top.setter
    def top(self, value: aspose.pdf.GraphInfo):
        ...
    
    @property
    def bottom(self) -> aspose.pdf.GraphInfo:
        '''Gets or sets a object that indicates bottom of the border.'''
        ...
    
    @bottom.setter
    def bottom(self, value: aspose.pdf.GraphInfo):
        ...
    
    @property
    def rounded_border_radius(self) -> float:
        '''Gets or sets a rouded border radius'''
        ...
    
    @rounded_border_radius.setter
    def rounded_border_radius(self, value: float):
        ...
    
    ...

class BuildVersionInfo:
    '''This class provides information about current product build.'''
    
    def __init__(self):
        ...
    
    ASSEMBLY_VERSION: str
    
    PRODUCT: str
    
    FILE_VERSION: str
    
    ...

class CdrLoadOptions(aspose.pdf.LoadOptions):
    '''Class describes CDR load options.'''
    
    def __init__(self):
        ...
    
    ...

class Cell:
    '''Represents a cell of the table's row.'''
    
    @overload
    def __init__(self, rect: aspose.pdf.Rectangle):
        '''Initializes a new instance of the Cell class.
        
        :param rect: The rectangle of the cell in page's coordinates.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the Cell class.'''
        ...
    
    def clone(self) -> object:
        '''Clone the cell.
        
        :returns: The cloned object'''
        ...
    
    @property
    def is_no_border(self) -> bool:
        '''Gets or sets the cell have border.'''
        ...
    
    @is_no_border.setter
    def is_no_border(self, value: bool):
        ...
    
    @property
    def margin(self) -> aspose.pdf.MarginInfo:
        '''Gets or sets the padding.'''
        ...
    
    @margin.setter
    def margin(self, value: aspose.pdf.MarginInfo):
        ...
    
    @property
    def border(self) -> aspose.pdf.BorderInfo:
        '''Gets or sets the border.'''
        ...
    
    @border.setter
    def border(self, value: aspose.pdf.BorderInfo):
        ...
    
    @property
    def background_color(self) -> aspose.pdf.Color:
        '''Gets or sets the background color.'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def background_image_file(self) -> str:
        '''Gets or sets the background image file.'''
        ...
    
    @background_image_file.setter
    def background_image_file(self, value: str):
        ...
    
    @property
    def background_image(self) -> aspose.pdf.Image:
        '''Gets or sets the background image'''
        ...
    
    @background_image.setter
    def background_image(self, value: aspose.pdf.Image):
        ...
    
    @property
    def alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets or sets the alignment.'''
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def default_cell_text_state(self) -> aspose.pdf.text.TextState:
        '''Gets or sets the default cell text state.'''
        ...
    
    @default_cell_text_state.setter
    def default_cell_text_state(self, value: aspose.pdf.text.TextState):
        ...
    
    @property
    def is_override_by_fragment(self) -> bool:
        '''Sets the cell's TextState property is overriden by TextFragment TextState property.'''
        ...
    
    @is_override_by_fragment.setter
    def is_override_by_fragment(self, value: bool):
        ...
    
    @property
    def paragraphs(self) -> aspose.pdf.Paragraphs:
        '''Gets or sets the cell's formatted text.'''
        ...
    
    @paragraphs.setter
    def paragraphs(self, value: aspose.pdf.Paragraphs):
        ...
    
    @property
    def is_word_wrapped(self) -> bool:
        '''Gets or sets the cell's text word wrapped.'''
        ...
    
    @is_word_wrapped.setter
    def is_word_wrapped(self, value: bool):
        ...
    
    @property
    def vertical_alignment(self) -> aspose.pdf.VerticalAlignment:
        '''Gets or sets the vertical alignment.'''
        ...
    
    @vertical_alignment.setter
    def vertical_alignment(self, value: aspose.pdf.VerticalAlignment):
        ...
    
    @property
    def col_span(self) -> int:
        '''Gets or sets the column span.'''
        ...
    
    @col_span.setter
    def col_span(self, value: int):
        ...
    
    @property
    def row_span(self) -> int:
        '''Gets or sets the row span.'''
        ...
    
    @row_span.setter
    def row_span(self, value: int):
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets the column width.'''
        ...
    
    ...

class Cells:
    '''Represents a cells collection of row.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.Cell:
        '''Gets or sets cells.
        
        :returns:
        
        :param index: The cell index.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.pdf.Cell):
        ...
    
    @overload
    def add(self) -> aspose.pdf.Cell:
        '''Add cell to collection.
        
        :returns: The new cell'''
        ...
    
    @overload
    def add(self, text: str, ts: aspose.pdf.text.TextState) -> aspose.pdf.Cell:
        '''Add cell to collection.
        
        :param text: The text for cell.
        :param ts: The text state.
        :returns: The new cell'''
        ...
    
    @overload
    def add(self, text: str) -> aspose.pdf.Cell:
        '''Add cell to collection.
        
        :param text: The text for cell.
        :returns: The new cell'''
        ...
    
    @overload
    def add(self, cell: aspose.pdf.Cell) -> None:
        '''Add cell to collection.
        
        :param cell: The cell to collection.'''
        ...
    
    @overload
    def remove(self, obj: object) -> None:
        '''Remove cell set from collection.
        
        :param obj: The object.'''
        ...
    
    @overload
    def remove(self, cell: aspose.pdf.Cell) -> None:
        '''Remove cell set from collection.
        
        :param cell: The cell object.'''
        ...
    
    def remove_range(self, index: int, count: int) -> None:
        '''Remove cell set from collection.
        
        :param index: The collection index.
        :param count: The rows count.'''
        ...
    
    def insert(self, index: int, cell: aspose.pdf.Cell) -> None:
        '''Insert cell to collection.
        
        :param index: The selected index.
        :param cell: The selected cell.'''
        ...
    
    def dispose(self) -> None:
        '''Dispose method'''
        ...
    
    @property
    def count(self) -> int:
        '''The items count.'''
        ...
    
    ...

class CgmImportOptions(aspose.pdf.ImportOptions):
    '''Import option for import from Computer Graphics Metafile(CGM) format.'''
    
    def __init__(self):
        ...
    
    @property
    def page_size(self) -> aspose.pydrawing.SizeF:
        '''Gets or sets output page size for import.
        Default page size - A4 300dpi 2480 X 3508.'''
        ...
    
    @page_size.setter
    def page_size(self, value: aspose.pydrawing.SizeF):
        ...
    
    ...

class CgmLoadOptions(aspose.pdf.LoadOptions):
    '''Contains options for loading/importing CGM file into pdf document.'''
    
    @overload
    def __init__(self):
        '''Creates default load options for converting CGM file into pdf document.
        Default pdf page size - A4 300dpi 2480 X 3508.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pydrawing.SizeF):
        '''Creates load options with defined pageSize /\>.
        
        :param page_size: Defines pdf page width and height.'''
        ...
    
    @property
    def page_size(self) -> aspose.pydrawing.SizeF:
        '''Gets or sets output page size for import.'''
        ...
    
    ...

class Collection(aspose.pdf.EmbeddedFileCollection):
    '''Represents class for Collection(12.3.5 Collections).'''
    
    def __init__(self):
        '''Initializes new Collection object.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.FileSpecification:
        ...
    
    def get_sorted_collection(self) -> list[aspose.pdf.FileSpecification]:
        '''Gets a collection of files sorted according to the specification.
        
        :returns: The list of sorted files.'''
        ...

    @property
    def schema(self) -> aspose.pdf.CollectionSchema:
        '''Gets a "Schema" of a document collection.'''
        ...

    @property
    def default_entry(self) -> str:
        '''Default embedded file name.'''
        ...
    
    ...

class CollectionField:
    '''Represents a document collection schema field class.'''
    
    @property
    def filed_type(self) -> aspose.pdf.FieldValueType:
        '''Gets the type of a field value in a schema collection.
        This field describes the value type corresponding to :attr:`CollectionField.subtype`.'''
        ...
    
    @property
    def subtype(self) -> aspose.pdf.CollectionFieldSubtype:
        '''Gets the subtype of a field value in a schema collection.
        The subtype of collection field or file-related field that this  dictionary describes.
        This entry identifies the type of data that shall be stored in the field.'''
        ...
    
    @property
    def n(self) -> str:
        '''Gets the textual field name that shall be presented to the user by the interactive PDF processor'''
        ...
    
    @property
    def o(self) -> int:
        '''Gets the relative order of the field name in the user interface.
        Fields shall be sorted by the interactive PDF processor in ascending order.'''
        ...
    
    @property
    def v(self) -> bool:
        '''Gets the initial visibility of the field in the user interface. Default value: true.'''
        ...
    
    @property
    def e(self) -> bool:
        '''Gets a flag indicating whether the interactive PDF processor should provide support for editing the field value.
        Default value: false'''
        ...
    
    ...

class CollectionItem:
    '''Represents a collection item class.
    The collection item contains the data described by the collection schema.'''
    
    def has_name(self, name: str) -> bool:
        '''Checks if the given name exists in the collection item.
        
        :param name: The name to check.
        :returns: True if the name exists in the collection item, otherwise false.'''
        ...
    
    @property
    def is_empty(self) -> bool:
        '''Gets a value indicating whether the collection item is empty.
        
        This property returns true if the collection item does not contain any values, including string values,
        double values, integer values, and date values. If any of these value types are present in the collection item,
        this property returns false.
        
        :returns: true if the collection item is empty; otherwise, false.'''
        ...
    
    @property
    def all_names(self) -> None:
        '''Gets a collection of all the names of collection item values.'''
        ...
    
    ...

class CollectionSchema:
    '''Represents a class that describes the "Schema" of a document collection.'''
    
    def has_name(self, name: str) -> bool:
        '''Determines whether the specified name exists in the schema.
        
        :param name: The name to check.
        :returns: ``True`` if the specified name exists in the schema; otherwise, ``False``.'''
        ...
    
    def get_collection_field(self, name: str) -> aspose.pdf.CollectionField:
        '''Gets a collection field by name.
        
        :param name: The field name
        :returns:'''
        ...
    
    @property
    def all_fields(self) -> None:
        '''Gets all schema's fields.'''
        ...
    
    @property
    def all_names(self) -> None:
        '''Gets all schema's fields names.'''
        ...
    
    ...


class Color:
    '''Represents class for color value which can be expressed in different color space.'''
    
    def __init__(self):
        '''Default constructor.'''
        ...
    
    @overload
    @staticmethod
    def from_rgb(self, color: aspose.pydrawing.Color) -> aspose.pdf.Color:
        '''Gets valid pdf Color object from System.Drawing.Color value.
        
        :param color: System.Drawing.Color value.
        :returns: Color object with each component value in [0..1] range.'''
        ...
    
    @overload
    @staticmethod
    def from_rgb(self, r: float, g: float, b: float) -> aspose.pdf.Color:
        '''Gets valid pdf Color object from RGB color components.
        
        :param r: The Red color component (value 0 - 1).
        :param g: The Green color component (value 0 - 1).
        :param b: The Blue color component (value 0 - 1).
        :returns: Color object with each component value in [0..1] range.'''
        ...
    
    @overload
    @staticmethod
    def from_argb(self, r: int, g: int, b: int) -> aspose.pdf.Color:
        '''Gets valid pdf Color object from RGB color components.
        
        :param r: The Red color component (value 0 - 255).
        :param g: The Green color component (value 0 - 255).
        :param b: The Blue color component (value 0 - 255).
        :returns: Color object with each component value in [0..255] range.'''
        ...
    
    @overload
    @staticmethod
    def from_argb(self, a: int, r: int, g: int, b: int) -> aspose.pdf.Color:
        '''Gets valid pdf Color object from RGB color components.
        
        :param a: The alpha component value (value 0 - 255).
        :param r: The Red color component (value 0 - 255).
        :param g: The Green color component (value 0 - 255).
        :param b: The Blue color component (value 0 - 255).
        :returns: Color object with each component value in [0..255] range.'''
        ...
    
    @staticmethod
    def parse(self, value: str) -> aspose.pdf.Color:
        '''Extracts color components from the string.
        
        :param value: String value with color component values.
        :returns: Color object.'''
        ...
    
    def to_rgb(self) -> aspose.pydrawing.Color:
        '''Converts color into rgb.
        
        :returns: Rgb color value.'''
        ...
    
    @staticmethod
    def from_gray(self, g: float) -> aspose.pdf.Color:
        '''Gets valid pdf Color object from Gray color component.
        
        :param g: The Gray color component (value 0 - 1).
        :returns: Color object with each component value in [0..1] range.'''
        ...
    
    @staticmethod
    def from_cmyk(self, c: float, m: float, y: float, k: float) -> aspose.pdf.Color:
        '''Gets valid pdf Color object from RGB color components.
        
        :param c: The Cyan color component (value 0 - 1).
        :param m: The Magenta color component (value 0 - 1).
        :param y: The Yellow color component (value 0 - 1).
        :param k: The Key color component (value 0 - 1).
        :returns: Color object with each component value in [0..1] range.'''
        ...
    
    @property
    def a(self) -> float:
        '''Gets the alpha component value'''
        ...
    
    @property
    def data(self) -> list[float]:
        '''Gets color value.'''
        ...
    
    @property
    def color_space(self) -> aspose.pdf.ColorSpace:
        '''Gets color space that the color represents.'''
        ...
    
    @property
    def pattern_color_space(self) -> aspose.pdf.drawing.PatternColorSpace:
        '''Represents a object that indicates the pattern colorspace.'''
        ...
    
    @pattern_color_space.setter
    def pattern_color_space(self, value: aspose.pdf.drawing.PatternColorSpace):
        ...
    
    transparent: aspose.pdf.Color
    
    alice_blue: aspose.pdf.Color
    
    antique_white: aspose.pdf.Color
    
    aqua: aspose.pdf.Color
    
    aquamarine: aspose.pdf.Color
    
    azure: aspose.pdf.Color
    
    beige: aspose.pdf.Color
    
    bisque: aspose.pdf.Color
    
    black: aspose.pdf.Color
    
    blanched_almond: aspose.pdf.Color
    
    blue: aspose.pdf.Color
    
    blue_violet: aspose.pdf.Color
    
    brown: aspose.pdf.Color
    
    burly_wood: aspose.pdf.Color
    
    cadet_blue: aspose.pdf.Color
    
    chartreuse: aspose.pdf.Color
    
    chocolate: aspose.pdf.Color
    
    coral: aspose.pdf.Color
    
    cornflower_blue: aspose.pdf.Color
    
    cornsilk: aspose.pdf.Color
    
    crimson: aspose.pdf.Color
    
    cyan: aspose.pdf.Color
    
    dark_blue: aspose.pdf.Color
    
    dark_cyan: aspose.pdf.Color
    
    dark_goldenrod: aspose.pdf.Color
    
    dark_gray: aspose.pdf.Color
    
    dark_green: aspose.pdf.Color
    
    dark_khaki: aspose.pdf.Color
    
    dark_magenta: aspose.pdf.Color
    
    dark_olive_green: aspose.pdf.Color
    
    dark_orange: aspose.pdf.Color
    
    dark_orchid: aspose.pdf.Color
    
    dark_red: aspose.pdf.Color
    
    dark_salmon: aspose.pdf.Color
    
    dark_sea_green: aspose.pdf.Color
    
    dark_slate_blue: aspose.pdf.Color
    
    dark_slate_gray: aspose.pdf.Color
    
    dark_turquoise: aspose.pdf.Color
    
    dark_violet: aspose.pdf.Color
    
    deep_pink: aspose.pdf.Color
    
    deep_sky_blue: aspose.pdf.Color
    
    dim_gray: aspose.pdf.Color
    
    dodger_blue: aspose.pdf.Color
    
    firebrick: aspose.pdf.Color
    
    floral_white: aspose.pdf.Color
    
    forest_green: aspose.pdf.Color
    
    fuchsia: aspose.pdf.Color
    
    gainsboro: aspose.pdf.Color
    
    ghost_white: aspose.pdf.Color
    
    gold: aspose.pdf.Color
    
    goldenrod: aspose.pdf.Color
    
    gray: aspose.pdf.Color
    
    green: aspose.pdf.Color
    
    green_yellow: aspose.pdf.Color
    
    honeydew: aspose.pdf.Color
    
    hot_pink: aspose.pdf.Color
    
    indian_red: aspose.pdf.Color
    
    indigo: aspose.pdf.Color
    
    ivory: aspose.pdf.Color
    
    khaki: aspose.pdf.Color
    
    lavender: aspose.pdf.Color
    
    lavender_blush: aspose.pdf.Color
    
    lawn_green: aspose.pdf.Color
    
    lemon_chiffon: aspose.pdf.Color
    
    light_blue: aspose.pdf.Color
    
    light_coral: aspose.pdf.Color
    
    light_cyan: aspose.pdf.Color
    
    light_goldenrod_yellow: aspose.pdf.Color
    
    light_green: aspose.pdf.Color
    
    light_gray: aspose.pdf.Color
    
    light_pink: aspose.pdf.Color
    
    light_salmon: aspose.pdf.Color
    
    light_sea_green: aspose.pdf.Color
    
    light_sky_blue: aspose.pdf.Color
    
    light_slate_gray: aspose.pdf.Color
    
    light_steel_blue: aspose.pdf.Color
    
    light_yellow: aspose.pdf.Color
    
    lime: aspose.pdf.Color
    
    lime_green: aspose.pdf.Color
    
    linen: aspose.pdf.Color
    
    magenta: aspose.pdf.Color
    
    maroon: aspose.pdf.Color
    
    medium_aquamarine: aspose.pdf.Color
    
    medium_blue: aspose.pdf.Color
    
    medium_orchid: aspose.pdf.Color
    
    medium_purple: aspose.pdf.Color
    
    medium_sea_green: aspose.pdf.Color
    
    medium_slate_blue: aspose.pdf.Color
    
    medium_spring_green: aspose.pdf.Color
    
    medium_turquoise: aspose.pdf.Color
    
    medium_violet_red: aspose.pdf.Color
    
    midnight_blue: aspose.pdf.Color
    
    mint_cream: aspose.pdf.Color
    
    misty_rose: aspose.pdf.Color
    
    moccasin: aspose.pdf.Color
    
    navajo_white: aspose.pdf.Color
    
    navy: aspose.pdf.Color
    
    old_lace: aspose.pdf.Color
    
    olive: aspose.pdf.Color
    
    olive_drab: aspose.pdf.Color
    
    orange: aspose.pdf.Color
    
    orange_red: aspose.pdf.Color
    
    orchid: aspose.pdf.Color
    
    pale_goldenrod: aspose.pdf.Color
    
    pale_green: aspose.pdf.Color
    
    pale_turquoise: aspose.pdf.Color
    
    pale_violet_red: aspose.pdf.Color
    
    papaya_whip: aspose.pdf.Color
    
    peach_puff: aspose.pdf.Color
    
    peru: aspose.pdf.Color
    
    pink: aspose.pdf.Color
    
    plum: aspose.pdf.Color
    
    powder_blue: aspose.pdf.Color
    
    purple: aspose.pdf.Color
    
    red: aspose.pdf.Color
    
    rosy_brown: aspose.pdf.Color
    
    royal_blue: aspose.pdf.Color
    
    saddle_brown: aspose.pdf.Color
    
    salmon: aspose.pdf.Color
    
    sandy_brown: aspose.pdf.Color
    
    sea_green: aspose.pdf.Color
    
    sea_shell: aspose.pdf.Color
    
    sienna: aspose.pdf.Color
    
    silver: aspose.pdf.Color
    
    sky_blue: aspose.pdf.Color
    
    slate_blue: aspose.pdf.Color
    
    slate_gray: aspose.pdf.Color
    
    snow: aspose.pdf.Color
    
    spring_green: aspose.pdf.Color
    
    steel_blue: aspose.pdf.Color
    
    tan: aspose.pdf.Color
    
    teal: aspose.pdf.Color
    
    thistle: aspose.pdf.Color
    
    tomato: aspose.pdf.Color
    
    turquoise: aspose.pdf.Color
    
    violet: aspose.pdf.Color
    
    wheat: aspose.pdf.Color
    
    white: aspose.pdf.Color
    
    white_smoke: aspose.pdf.Color
    
    yellow: aspose.pdf.Color
    
    yellow_green: aspose.pdf.Color
    
    empty: aspose.pdf.Color
    
    ...

class ColumnInfo:
    '''This class represents a columns info.'''
    
    def __init__(self):
        ...
    
    @property
    def column_widths(self) -> str:
        '''Gets or sets a string that contains the width of columns.
        The value of each column should be separated by blank.The default unit is point,
        but cm, inch and percentage of available width are also supported.
        For example,"120 2.5cm 1.5inch"'''
        ...
    
    @column_widths.setter
    def column_widths(self, value: str):
        ...
    
    @property
    def column_spacing(self) -> str:
        '''Gets or sets a string that contains the spacing between columns.
        The value of each spacing should be separated by blank. The default unit is point,
        but cm and inch are also supported.For example,"120 2.5cm 1.5inch".
        
        If this property is not set, default value 0 will be used for each spacing.'''
        ...
    
    @column_spacing.setter
    def column_spacing(self, value: str):
        ...
    
    @property
    def column_count(self) -> int:
        '''Gets or sets a int value that indicates the number of columns.'''
        ...
    
    @column_count.setter
    def column_count(self, value: int):
        ...
    
    ...

class ComHelper:
    '''Provides methods for COM clients to load a document into Aspose.Pdf.
    
    Use the ComHelper class to load a document from a file or stream into a Document object in a COM application.
    The Document class provides a default constructor to create a new document
    and also provides overloaded constructors to load a document from a file or stream.
    If you are using Aspose.Words from a .NET application, you can use all of the Document constructors directly, but if you are using Aspose.Pdf from a COM application,
    only the default Document constructor is available.'''
    
    def __init__(self):
        ...
    
    @overload
    def open_stream(self, input: Any) -> aspose.pdf.Document:
        '''Initialize and return new Document instance from the stream.
        
        :param input: Stream with pdf document.
        :returns: Document object'''
        ...
    
    @overload
    def open_stream(self, input: Any, password: str) -> aspose.pdf.Document:
        '''Initialize and return new Document instance from the stream.
        
        :param input: Input stream object, corresponding pdf is password protected.
        :param password: User or owner password.
        :returns: Document object'''
        ...
    
    @overload
    def open_stream(self, input: Any, is_managed_stream: bool) -> aspose.pdf.Document:
        '''Initialize and return new Document instance from the stream.
        
        :param input: Stream with pdf document.
        :param is_managed_stream: if set to ``True`` inner stream is closed before exit; otherwise, is not.
        :returns: Document object'''
        ...
    
    @overload
    def open_stream(self, input: Any, password: str, is_managed_stream: bool) -> aspose.pdf.Document:
        '''Initialize and return new Document instance from the stream.
        
        :param input: Stream with pdf document.
        :param password: User or owner password.
        :param is_managed_stream: if set to ``True`` inner stream is closed before exit; otherwise, is not.
        :returns: Document object'''
        ...
    
    @overload
    def open_stream(self, input: Any, options: aspose.pdf.LoadOptions) -> aspose.pdf.Document:
        '''Open and return an existing document from a stream providing necessary converting to get pdf document.
        
        :param input: Input stream to convert into pdf document.
        :param options: Represents properties for converting into pdf document.
        :returns: Document object'''
        ...
    
    @overload
    def open_file(self, filename: str) -> aspose.pdf.Document:
        '''Just create and return Document using filename. The same as :meth:`Document.__init__`.
        
        :param filename: The name of the pdf document file.
        :returns: Document object'''
        ...
    
    @overload
    def open_file(self, filename: str, password: str) -> aspose.pdf.Document:
        '''Initialize and return new instance of the :class:`Document` class for working with encrypted document.
        
        :param filename: Document file name.
        :param password: User or owner password.
        :returns: Document object'''
        ...
    
    @overload
    def open_file(self, filename: str, password: str, is_managed_stream: bool) -> aspose.pdf.Document:
        '''Initialize new instance of the :class:`Document` class for working with encrypted document.
        
        :param filename: Document file name.
        :param password: User or owner password.
        :param is_managed_stream: if set to ``True`` inner stream is closed before exit; otherwise, is not.
        :returns: Document object'''
        ...
    
    @overload
    def open_file(self, filename: str, options: aspose.pdf.LoadOptions) -> aspose.pdf.Document:
        '''Open an existing document from a file providing necessary converting oprions to get pdf document.
        
        :param filename: Input file to convert into pdf document.
        :param options: Represents properties for converting input file into pdf document.
        :returns: Document object'''
        ...
    
    ...

class CompositingParameters:
    '''Represents an object containing graphics compositing parameters of current graphics state.'''
    
    @overload
    def __init__(self, blend_mode: aspose.pdf.BlendMode):
        '''Initializes new instance of the :class:`CompositingParameters` object.
        
        :param blend_mode: Blend mode of current graphics state.'''
        ...
    
    @overload
    def __init__(self, blend_mode: aspose.pdf.BlendMode, filter_type: aspose.pdf.ImageFilterType):
        '''Initializes new instance of the :class:`CompositingParameters` object.
        
        :param blend_mode: Blend mode of current graphics state.
        :param filter_type: The image filter type.'''
        ...
    
    @overload
    def __init__(self, blend_mode: aspose.pdf.BlendMode, filter_type: aspose.pdf.ImageFilterType, is_masked: bool):
        '''Initializes new instance of the :class:`CompositingParameters` object.
        
        :param blend_mode: Blend mode of current graphics state.
        :param filter_type: The image filter type.
        :param is_masked: The adding mask flag.'''
        ...
    
    @property
    def blend_mode(self) -> aspose.pdf.BlendMode:
        '''Gets blend mode of current graphics state.'''
        ...
    
    @property
    def filter_type(self) -> aspose.pdf.ImageFilterType:
        '''Gets the image filter type.'''
        ...
    
    @property
    def is_masked(self) -> bool:
        '''Gets the mask flag.'''
        ...
    
    ...

class DeprecatedFeatureException(aspose.pdf.PdfException):
    '''The exception that is thrown when a feature is deprecated in current pdf version.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`DeprecatedFeatureException` class.'''
        ...
    
    @overload
    def __init__(self, message: str):
        '''Constructor.
        
        :param message: Exception message.'''
        ...
    
    ...

class DestinationCollection:
    '''Class represents the collection of all destinations (a name tree mapping name strings to destinations (see 12.3.2.3, "Named Destinations") and (see 7.7.4, "Name Dictionary")) in the pdf document.'''
    
    def get_page_number(self, destiname_name: str, use_cache: bool) -> int:
        '''Returns the page number of destination by the name.
        
        :param destiname_name: The name of destination.
        :param use_cache: Determines whether cached version of collection is used or not.
        :returns: The page number if destination was found; otherwise, -1.'''
        ...
    
    def get_explicit_destination(self, destiname_name: str, use_cache: bool) -> aspose.pdf.annotations.ExplicitDestination:
        '''Returns the explicit destination by the name.
        
        :param destiname_name: The name of destination.
        :param use_cache: Determines whether cached version of collection is used or not.
        :returns: The ExplicitDestination object for destination found; otherwise, null.'''
        ...
    
    def clear(self) -> None:
        '''Collection is read-only. Always throws NotSupportedException exception.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the collection.'''
        ...
    
    @property
    def is_read_only(self) -> bool:
        '''Gets a value indicating whether the collection is read-only.'''
        ...
    
    ...

class DjvuLoadOptions(aspose.pdf.LoadOptions):
    '''Class describes DJVU load options.'''
    
    def __init__(self):
        ...
    
    ...

class DocSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to Doc format'''
    
    def __init__(self):
        ...
    
    @property
    def mode(self) -> None:
        '''Recognition mode.'''
        ...
    
    @mode.setter
    def mode(self, value: None):
        ...
    
    @property
    def relative_horizontal_proximity(self) -> float:
        '''In Pdf words may be innerly represented with operators that prints words
        by independently printing their letters or syllables. So, to detect words sometimes we need detect groups
        of independent chars that are in fact words.
        This setting defines width of space between text elements(letters, syllables)
        that must be treated as distance between words during recognition of words in source PDF.
        (presence of empty space at least with this width between letters means that
        textual elements pertain to different words).
        It's normed to font size -  1.0 means 100% of supposed word's font size.
        ATTENTION!It's used only in cases when source PDF contains specific rarely used fonts
        for which optimal value cannot be calculated from font.
        So, in vast majority of cases this parameter changes nothing in result document.'''
        ...
    
    @relative_horizontal_proximity.setter
    def relative_horizontal_proximity(self, value: float):
        ...
    
    @property
    def max_distance_between_text_lines(self) -> float:
        '''This parameter is used for grouping text lines into paragraphs.
        Determines how far apart can be two relative text lines. Specified in hundreds of percent of the text lines height.'''
        ...
    
    @max_distance_between_text_lines.setter
    def max_distance_between_text_lines(self, value: float):
        ...
    
    @property
    def recognize_bullets(self) -> bool:
        '''Switch on the recognition of bullets'''
        ...
    
    @recognize_bullets.setter
    def recognize_bullets(self, value: bool):
        ...
    
    @property
    def add_return_to_line_end(self) -> bool:
        '''Use paragraph or line breaks'''
        ...
    
    @add_return_to_line_end.setter
    def add_return_to_line_end(self, value: bool):
        ...
    
    @property
    def image_resolution_x(self) -> int:
        '''Converted images X resolution.'''
        ...
    
    @image_resolution_x.setter
    def image_resolution_x(self, value: int):
        ...
    
    @property
    def image_resolution_y(self) -> int:
        '''Converted images Y resolution.'''
        ...
    
    @image_resolution_y.setter
    def image_resolution_y(self, value: int):
        ...
    
    @property
    def format(self) -> None:
        '''Output format'''
        ...
    
    @format.setter
    def format(self, value: None):
        ...
    
    @property
    def batch_size(self) -> int:
        '''Defines batch size if batched conversion is applicable
        to source and destination formats pair.'''
        ...
    
    @batch_size.setter
    def batch_size(self, value: int):
        ...
    
    @property
    def memory_save_mode_path(self) -> str:
        '''Defines the path (file name or directory name) to hold
        temporary data when converting in memory save mode.'''
        ...
    
    @memory_save_mode_path.setter
    def memory_save_mode_path(self, value: str):
        ...

    @property
    def convert_type_3_fonts(self) -> bool:
        '''Gets or sets conversion for Type3 fonts.
        In Type 3 fonts, glyphs shall be defined by streams of graphics operators.
        This means that in the DOC/DOCX output we see images instead of text.
        Set this flag to true to convert Type3 fonts to TTF and get text in the resulting file.'''
        ...
    
    @convert_type_3_fonts.setter
    def convert_type_3_fonts(self, value: bool):
        ...
    
    @property
    def re_save_fonts(self) -> bool:
        '''Gets or sets the procedure for resaving fonts.
        If set to true, we reload fonts on every page
        to avoid the influence of previous font properties and load the newly created font from scratch.
        Set this option to false if you want to improve performance.
        The default value is true;'''
        ...
    
    @re_save_fonts.setter
    def re_save_fonts(self, value: bool):
        ...

    class DocFormat:
          '''Allows to specify .doc or .docx file format. '''

          DOC: DocFormat
          DOC_X: DocFormat

    class RecognitionMode:
          '''Allows to control how a PDF document is converted into a word processing document.'''
          
          TEXTBOX: RecognitionMode
          FLOW: RecognitionMode
          ENHANCED_FLOW: RecognitionMode

    ...

class Document:
    '''Class representing PDF document'''
    
    @overload
    def __init__(self, input: Any):
        '''Initialize new Document instance from the stream.
        
        :param input: Stream with pdf document.'''
        ...
    
    @overload
    def __init__(self, input: Any, password: str, is_managed_stream: bool):
        '''Initialize new Document instance from the stream.
        
        :param input: Stream with pdf document.
        :param password: User or owner password.
        :param is_managed_stream: if set to ``True`` inner stream is closed before exit; otherwise, is not.'''
        ...
    
    @overload
    def __init__(self, input: Any, is_managed_stream: bool):
        '''Initialize new Document instance from the stream.
        
        :param input: Stream with pdf document.
        :param is_managed_stream: if set to ``True`` inner stream is closed before exit; otherwise, is not.'''
        ...
    
    @overload
    def __init__(self, filename: str):
        '''Just init Document using filename. The same as :meth:`Document.__init__`.
        
        :param filename: The name of the pdf document file.'''
        ...
    
    @overload
    def __init__(self, filename: str, is_managed_stream: bool):
        '''Just init Document using . The same as:meth:`Document.__init__`.
        
        :param filename: The name of the pdf document file.
        :param is_managed_stream: If set to true inner stream is closed before exit; otherwise, is not.'''
        ...

    @overload
    def __init__(self, input: Any, password: str):
        '''Initialize new Document instance from the stream.
        
        :param input: Input stream object, corresponding pdf is password protected.
        :param password: User or owner password.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes empty document.'''
        ...
    
    @overload
    def __init__(self, filename: str, password: str):
        '''Initializes new instance of the :class:`Document` class for working with encrypted document.
        
        :param filename: Document file name.
        :param password: User or owner password.'''
        ...
    
    @overload
    def __init__(self, filename: str, password: str, is_managed_stream: bool):
        '''Initializes new instance of the :class:`Document` class for working with encrypted document.
        
        :param filename: Document file name.
        :param password: User or owner password.
        :param is_managed_stream: if set to ``True`` inner stream is closed before exit; otherwise, is not.'''
        ...
    
    @overload
    def __init__(self, filename: str, options: aspose.pdf.LoadOptions):
        '''Opens an existing document from a file providing necessary converting options to get pdf document.
        
        :param filename: Input file to convert into pdf document.
        :param options: Represents properties for converting input file into pdf document.'''
        ...
    
    @overload
    def __init__(self, input: Any, options: aspose.pdf.LoadOptions):
        '''Opens an existing document from a stream providing necessary converting to get pdf document.
        
        :param input: Input stream to convert into pdf document.
        :param options: Represents properties for converting input stream into pdf document.'''
        ...
    
    @overload
    def save(self, output: Any) -> None:
        '''Stores document into stream.
        
        :param output: Stream where document shell be stored.'''
        ...
    
    @overload
    def save(self, output_file_name: str) -> None:
        '''Saves document into the specified file.
        
        :param output_file_name: Path to file where the document will be stored.'''
        ...
    
    @overload
    def save(self) -> None:
        '''Save document incrementally (i.e. using incremental update technique).
        
        In order to save document incrementally we should open the document file for writing.
        Therefore Document must be initialized with writable stream like in the next code snippet:
        Document doc = new Document(new FileStream("document.pdf", FileMode.Open, FileAccess.ReadWrite));
        // make some changes and save the document incrementally
        doc.Save();'''
        ...
    
    @overload
    def save(self, options: aspose.pdf.SaveOptions) -> None:
        '''Saves the document with save options.
        
        :param options: Save options.'''
        ...
    
    @overload
    def save(self, output_file_name: str, format: aspose.pdf.SaveFormat) -> None:
        '''Saves the document with a new name along with a file format.
        
        :param output_file_name: Path to file where the document will be stored.
        :param format: Format options.'''
        ...
    
    @overload
    def save(self, output_stream: Any, format: aspose.pdf.SaveFormat) -> None:
        '''Saves the document with a new name along with a file format.
        
        :raises System.ArgumentException: System.ArgumentException when :class:`HtmlSaveOptions` is passed to a method. Save a document to the html stream is not supported. Please use method save to the file.
        :param output_stream: Stream where the document will be stored.
        :param format: Format options.'''
        ...
    
    @overload
    def save(self, output_file_name: str, options: aspose.pdf.SaveOptions) -> None:
        '''Saves the document with a new name setting its save options.
        
        :param output_file_name: Path to file where the document will be stored.
        :param options: Save options.'''
        ...
    
    @overload
    def save(self, output_stream: Any, options: aspose.pdf.SaveOptions) -> None:
        '''Saves the document to a stream with a save options.
        
        :raises System.ArgumentException: System.ArgumentException when :class:`HtmlSaveOptions` is passed to a method. Save a document to the html stream is not supported. Please use method save to the file.
        :param output_stream: Stream where the document will be stored.
        :param options: Save options.'''
        ...
    
    @overload
    def export_annotations_to_xfdf(self, file_name: str) -> None:
        '''Exports all document annotations to XFDF file
        
        :param file_name: XFDF file name'''
        ...
    
    @overload
    def export_annotations_to_xfdf(self, stream: Any) -> None:
        '''Export all document annotations into stream.
        
        :param stream: Stream where store XFDF.'''
        ...
    
    @overload
    def send_to(self, device: aspose.pdf.devices.DocumentDevice, output: Any) -> None:
        '''Sends the whole document to the document device for processing.
        
        :param device: Document device which is used to process the document.
        :param output: Output stream contains the results of the document processing with given device.'''
        ...
    
    @overload
    def send_to(self, device: aspose.pdf.devices.DocumentDevice, from_page: int, to_page: int, output: Any) -> None:
        '''Sends the certain pages of the document to the document device for processing.
        
        :param device: Document device which is used to process the document.
        :param from_page: The first page for processing.
        :param to_page: The last page for processing.
        :param output: Output stream contains the results of the document pages processing with given device.'''
        ...
    
    @overload
    def send_to(self, device: aspose.pdf.devices.DocumentDevice, output_file_name: str) -> None:
        '''Sends the whole document to the document device for processing.
        
        :param device: Document device which is used to process the document.
        :param output_file_name: Output file name with the results of processing.'''
        ...
    
    @overload
    def send_to(self, device: aspose.pdf.devices.DocumentDevice, from_page: int, to_page: int, output_file_name: str) -> None:
        '''Sends the whole document to the document device for processing.
        
        :param device: Document device which is used to process the document.
        :param from_page: The first page for processing.
        :param to_page: The last page for processing.
        :param output_file_name: Output file name with the results of processing.'''
        ...
    
    @overload
    def import_annotations_from_xfdf(self, file_name: str) -> None:
        '''Imports annotations from XFDF file to document.
        
        :param file_name: XFDF file name'''
        ...
    
    @overload
    def import_annotations_from_xfdf(self, stream: Any) -> None:
        '''Imports annotations from stream to document.
        
        :param stream: Stream contains XFDF data.'''
        ...
    
    @overload
    def validate(self, output_log_file_name: str, format: aspose.pdf.PdfFormat) -> bool:
        '''Validate document into the specified file.
        
        :param output_log_file_name: Path to file where the comments will be stored.
        :param format: The pdf format.
        :returns: The operation result'''
        ...
    
    @overload
    def validate(self, output_log_stream: Any, format: aspose.pdf.PdfFormat) -> bool:
        '''Validate document into the specified file.
        
        :param output_log_stream: Stream where the comments will be stored.
        :param format: The pdf format.
        :returns: The operation result'''
        ...
    
    @overload
    def validate(self, options: aspose.pdf.PdfFormatConversionOptions) -> bool:
        '''Validate document into the specified file.
        
        :param options: set of options for convert PDF document
        :returns: The operation result'''
        ...
    
    @overload
    def convert(self, output_log_file_name: str, format: aspose.pdf.PdfFormat, action: aspose.pdf.ConvertErrorAction, transparency_action: aspose.pdf.ConvertTransparencyAction) -> bool:
        '''Convert document and save errors into the specified file.
        
        :param output_log_file_name: Path to file where the comments will be stored.
        :param format: The pdf format.
        :param action: Action for objects that can not be converted
        :param transparency_action: Action for image masked objects
        :returns: The operation result'''
        ...
    
    @overload
    def convert(self, output_log_stream: Any, format: aspose.pdf.PdfFormat, action: aspose.pdf.ConvertErrorAction, transparency_action: aspose.pdf.ConvertTransparencyAction) -> bool:
        '''Convert document and save errors into the specified file.
        
        :param output_log_stream: Stream where the comments will be stored.
        :param format: The pdf format.
        :param action: Action for objects that can not be converted
        :param transparency_action: Action for image masked objects
        :returns: The operation result'''
        ...
    
    @overload
    def convert(self, output_log_file_name: str, format: aspose.pdf.PdfFormat, action: aspose.pdf.ConvertErrorAction) -> bool:
        '''Convert document and save errors into the specified file.
        
        :param output_log_file_name: Path to file where the comments will be stored.
        :param format: The pdf format.
        :param action: Action for objects that can not be converted
        :returns: The operation result'''
        ...
    
    @overload
    def convert(self, options: aspose.pdf.PdfFormatConversionOptions) -> bool:
        '''Convert document using specified conversion options
        
        :param options: set of options for convert PDF document
        :returns: The operation result'''
        ...
    
    @overload
    def convert(self, output_log_stream: Any, format: aspose.pdf.PdfFormat, action: aspose.pdf.ConvertErrorAction) -> bool:
        '''Convert document and save errors into the specified stream.
        
        :param output_log_stream: Stream where the comments will be stored.
        :param format: Pdf format.
        :param action: Action for objects that can not be converted
        :returns: The operation result'''
        ...
    
    @overload
    def convert(self, fixup: aspose.pdf.Fixup, output_log: Any, only_validation: bool, parameters: list[object]) -> bool:
        '''Convert document by applying the Fixup.
        
        :param fixup: The Fixup type.
        :param output_log: The log of process.
        :param only_validation: Only document validation.
        :param parameters: Properties for Fixup that can not be set.
        :returns: The operation result.'''
        ...
    
    @overload
    def convert(self, fixup: aspose.pdf.Fixup, output_log: str, only_validation: bool, parameters: list[object]) -> bool:
        '''Convert document by applying the Fixup.
        
        :param fixup: The Fixup type.
        :param output_log: The log of process.
        :param only_validation: Only document validation.
        :param parameters: Properties for Fixup that can not be set.
        :returns: The operation result.'''
        ...
    
    @overload
    @staticmethod
    def convert(self, src_file_name: str, load_options: aspose.pdf.LoadOptions, dst_file_name: str, save_options: aspose.pdf.SaveOptions) -> None:
        '''Converts source file in source format into destination file in destination format.
        
        :param src_file_name: The source file name.
        :param load_options: The source file format.
        :param dst_file_name: The destination file name.
        :param save_options: The destination file format.'''
        ...
    
    @overload
    @staticmethod
    def convert(self, src_stream: Any, load_options: aspose.pdf.LoadOptions, dst_file_name: str, save_options: aspose.pdf.SaveOptions) -> None:
        '''Converts stream in source format into destination file in destination format.
        
        :param src_stream: The source stream.
        :param load_options: The source stream format.
        :param dst_file_name: The destination file name.
        :param save_options: The destination file format.'''
        ...
    
    @overload
    @staticmethod
    def convert(self, src_file_name: str, load_options: aspose.pdf.LoadOptions, dst_stream: Any, save_options: aspose.pdf.SaveOptions) -> None:
        '''Converts source file in source format into stream in destination format.
        
        :param src_file_name: The source file name.
        :param load_options: The source file format.
        :param dst_stream: The destination stream.
        :param save_options: The destination stream format.'''
        ...
    
    @overload
    @staticmethod
    def convert(self, src_stream: Any, load_options: aspose.pdf.LoadOptions, dst_stream: Any, save_options: aspose.pdf.SaveOptions) -> None:
        '''Converts stream in source format into stream in destination format.
        
        :param src_stream: The source stream.
        :param load_options: The source stream format.
        :param dst_stream: The destination stream.
        :param save_options: The destination file format.'''
        ...
    
    @overload
    def flatten(self) -> None:
        '''Removes all fields from the document and place their values instead.'''
        ...
    
    @overload
    def flatten(self, flatten_settings) -> None:
        '''Removes all fields (and annotations) from the document and place their values instead.
        
        :param flatten_settings: Settings for flattening process.'''
        ...
    
    @overload
    def encrypt(self, user_password: str, owner_password: str, privileges: aspose.pdf.facades.DocumentPrivilege, crypto_algorithm: aspose.pdf.CryptoAlgorithm, use_pdf20: bool) -> None:
        '''Encrypts the document. Call then Save to get encrypted version of the document.
        
        :param user_password: User password.
        :param owner_password: Owner password.
        :param privileges: Document permissions, see :attr:`Document.permissions` for details.
        :param crypto_algorithm: Cryptographic algorithm, see :attr:`Document.crypto_algorithm` for details.
        :param use_pdf20: Support for revision 6 (Extension 8).'''
        ...
    
    @overload
    def encrypt(self, user_password: str, owner_password: str, permissions: aspose.pdf.Permissions, crypto_algorithm: aspose.pdf.CryptoAlgorithm) -> None:
        '''Encrypts the document. Call then Save to get encrypted version of the document.
        
        :param user_password: User password.
        :param owner_password: Owner password.
        :param permissions: Document permissions, see :attr:`Document.permissions` for details.
        :param crypto_algorithm: Cryptographic algorithm, see :attr:`Document.crypto_algorithm` for details.'''
        ...
    
    @overload
    def encrypt(self, user_password: str, owner_password: str, permissions: aspose.pdf.Permissions, crypto_algorithm: aspose.pdf.CryptoAlgorithm, use_pdf20: bool) -> None:
        '''Encrypts the document. Call then Save to get encrypted version of the document.
        
        :param user_password: User password.
        :param owner_password: Owner password.
        :param permissions: Document permissions, see :attr:`Document.permissions` for details.
        :param crypto_algorithm: Cryptographic algorithm, see :attr:`Document.crypto_algorithm` for details.
        :param use_pdf20: Support for revision 6 (Extension 8).'''
        ...
    
    @overload
    def optimize_resources(self) -> None:
        '''Optimize resources in the document:
        1. Resources which are not used on the document pages are removed;
        2. Equal resources are joined into one object;
        3. Unused objects are deleted.'''
        ...
    
    @overload
    def optimize_resources(self, strategy: aspose.pdf.optimization.OptimizationOptions) -> None:
        '''Optimize resources in the document according to defined optimization strategy.
        
        :param strategy: Optimization strategy.'''
        ...
    
    @overload
    def bind_xml(self, file: str) -> None:
        '''Bind xml to document
        
        :param file: The xml file'''
        ...
    
    @overload
    def bind_xml(self, xml_file: str, xsl_file: str) -> None:
        '''Bind xml/xsl to document
        
        :param xml_file: The xml file.
        :param xsl_file: The xsl file if XSLT is used.'''
        ...
    
    @overload
    def bind_xml(self, xml_stream: Any, xsl_stream: Any) -> None:
        '''Bind xml/xsl to document
        
        :param xml_stream: The xml stream.
        :param xsl_stream: The xsl stream if XSLT is used.'''
        ...
    
    @overload
    def bind_xml(self, stream: Any) -> None:
        '''Bind xml to document
        
        :param stream: The xml stream.'''
        ...

    @overload
    def merge(self, merge_options, documents: list[aspose.pdf.Document]) -> None:
        '''Merges documents.
        
        :param merge_options: The merge options.
        :param documents: The documents to merge.'''
        ...
    
    @overload
    def merge(self, merge_options, files: list[str]) -> None:
        '''Merges documents.
        
        :param merge_options: The merge options.
        :param files: The pdf-files to merge.'''
        ...
    
    @overload
    def merge(self, documents: list[aspose.pdf.Document]) -> None:
        '''Merges documents.
        
        :param documents: The documents to merge.'''
        ...
    
    @overload
    def merge(self, files: list[str]) -> None:
        '''Merges pdf files.
        
        :param files: The pdf-files to merge.'''
        ...
    
    @overload
    @staticmethod
    def merge_documents(self, merge_options, files: list[str]) -> aspose.pdf.Document:
        '''Merges documents.
        
        :param merge_options: The merge options.
        :param files: The pdf-files to merge.
        :returns: The merged document.'''
        ...
    
    @overload
    @staticmethod
    def merge_documents(self, merge_options, files: list[aspose.pdf.Document]) -> aspose.pdf.Document:
        '''Merges documents.
        
        :param merge_options:
        :param files: The documents to merge.
        :returns: The merged document.'''
        ...
    
    @overload
    @staticmethod
    def merge_documents(self, files: list[str]) -> aspose.pdf.Document:
        '''Merges pdf files.
        
        :param files: The pdf-files to merge.
        :returns: The merged document.'''
        ...
    
    @overload
    @staticmethod
    def merge_documents(self, documents: list[aspose.pdf.Document]) -> aspose.pdf.Document:
        '''Merges documents.
        
        :param documents: The documents to merge.
        :returns: The merged document.'''
        ...
    
    def remove_pdfa_compliance(self) -> None:
        '''Remove pdfa compliance from the document'''
        ...
    
    def remove_pdf_ua_compliance(self) -> None:
        '''Remove pdfUa compliance from the document'''
        ...
    
    def set_title(self, title: str) -> None:
        '''Set Title for Pdf Document
        
        :param title: Document's title'''
        ...
    
    def process_paragraphs(self) -> None:
        '''Process paragraphs for generator.'''
        ...
    
    def remove_metadata(self) -> None:
        '''Removes metadata from the document.'''
        ...
    
    def load_from(self, filename: str, options: aspose.pdf.LoadOptions) -> None:
        '''Loads a file, converting it to PDF.
        
        :param filename: The path to the file to open.
        :param options: The load options.'''
        ...
    
    def flatten_transparency(self) -> None:
        '''Replaces transparent content with non-transparent raster and vector graphics.'''
        ...
    
    def change_passwords(self, owner_password: str, new_user_password: str, new_owner_password: str) -> None:
        '''Changes document passwords. This action can be done only using owner password.
        
        :param owner_password: Owner password.
        :param new_user_password: New user password.
        :param new_owner_password: New owner password.'''
        ...
    
    def decrypt(self) -> None:
        '''Decrypts the document. Call then Save to obtain decrypted version of the document.'''
        ...
    
    def optimize(self) -> None:
        '''Linearize document in order to
        - open the first page as quickly as possible;
        - display next page or follow by link to the next page as quickly as possible;
        - display the page incrementally as it arrives when data for a page is delivered over a slow channel (display the most useful data first);
        - permit user interaction, such as following a link, to be performed even before the entire page has been received and displayed.
        Invoking this method doesn't actually saves the document. On the contrary the document only is prepared to have optimized structure,
        call then Save to get optimized document.'''
        ...
    
    def get_catalog_value(self, key: str) -> object:
        '''Returns item value from catalog dictionary.
        
        :param key: The key of item.
        :returns: Item value - if key was successfully found; otherwise, null.'''
        ...
    
    def free_memory(self) -> None:
        '''Clears memory'''
        ...
    
    def save_xml(self, file: str) -> None:
        '''Save document to XML.
        
        :param file: The document model xml file'''
        ...
    
    def get_object_by_id(self, id: str) -> object:
        '''Gets a object with specified ID in the document.
        
        :param id: The object id.
        :returns: The object with specified id. Null if the id is not found.'''
        ...
    
    def repair(self, options) -> None:
        '''Repairs broken document.
        
        :param options: An optional parameter of type Aspose.Pdf.Document.RepairOptions to specify repair settings.
                        If not provided, default settings will be used.'''
        ...
    
    def get_xmp_metadata(self, stream: Any) -> None:
        '''Get XMP metadata from document.
        
        :param stream: Stream where metadata will be stored.'''
        ...
    
    def set_xmp_metadata(self, stream: Any) -> None:
        '''Set XMP metadata of document.
        
        :param stream: Stream which contains XMP metadata.'''
        ...
    
    def check(self, do_repair: bool) -> bool:
        '''Validates document.
        
        :param do_repair: If true found issues will be repaired.
        :returns: True - if document repaired; otherwise, false.'''
        ...
    
    def page_nodes_to_balanced_tree(self, nodes_num_in_subtrees: int) -> None:
        '''Organizes page tree nodes in a document into a balanced tree.
        Only if the document has more than nodesNumInSubtrees page objects, otherwise it does nothing.
        
        :param nodes_num_in_subtrees: Desired number of subnodes.'''
        ...

    @staticmethod
    def set_default_file_size_limit_to_memory_loading(self) -> None:
        '''Sets the file size limit for loading an entire file into memory to default value equals 210 Mb.'''
        ...

    def has_incremental_update(self) -> bool:
        '''Checks if the current PDF document has been saved with incremental updates.
        
        :returns: ``True`` if the PDF document has incremental updates; otherwise, ``False``.'''
        ...

    @property
    def java_script(self) -> aspose.pdf.JavaScriptCollection:
        '''Collection of JavaScript of document level.'''
        ...
    
    @property
    def output_intents(self) -> aspose.pdf.OutputIntents:
        '''Gets the collection of Output intents in the document.'''
        ...

    is_licensed: bool
    
    @property
    def page_info(self) -> aspose.pdf.PageInfo:
        '''Gets or sets the page info.(for generator only, not filled in when reading document)'''
        ...
    
    @page_info.setter
    def page_info(self, value: aspose.pdf.PageInfo):
        ...
    
    @property
    def enable_signature_sanitization(self) -> bool:
        '''Gets or sets flag to manage signature fields sanitization. Enabled by default.'''
        ...
    
    @enable_signature_sanitization.setter
    def enable_signature_sanitization(self, value: bool):
        ...
    
    @property
    def is_pdfa_compliant(self) -> bool:
        '''Gets the is document pdfa compliant.'''
        ...
    
    @property
    def is_pdf_ua_compliant(self) -> bool:
        '''Gets the is document pdfua compliant.'''
        ...
    
    @property
    def is_xref_gaps_allowed(self) -> bool:
        '''Gets or sets  the is document pdfa compliant.'''
        ...
    
    @is_xref_gaps_allowed.setter
    def is_xref_gaps_allowed(self, value: bool):
        ...
    
    @property
    def named_destinations(self) -> aspose.pdf.NamedDestinationCollection:
        '''Collection of Named Destination in the document.'''
        ...
    
    @property
    def destinations(self) -> aspose.pdf.DestinationCollection:
        '''Gets the collection of destinations.
        Obsolete. Please use NamedDestinations.'''
        ...
    
    @property
    def pdf_format(self) -> aspose.pdf.PdfFormat:
        '''Gets PDF format'''
        ...
    
    @property
    def embed_standard_fonts(self) -> bool:
        '''Property which declares that document must embed all standard Type1 fonts
        which  has flag IsEmbedded set into true. All PDF fonts can be embedded
        into document simply via setting of flag IsEmbedded into true, but PDF standard Type1 fonts is an exception from this rule.
        Standard Type1 font embedding requires much time, so to embed these fonts it's necessary
        not only set flag IsEmbedded into true for specified font but also set
        an additiona flag on document's level - EmbedStandardFonts = true;
        This property can be set only one time for all fonts.
        By default false.'''
        ...
    
    @embed_standard_fonts.setter
    def embed_standard_fonts(self, value: bool):
        ...
    
    @property
    def disable_font_license_verifications(self) -> bool:
        '''Many operations with font can't be executed if these operations are prohibited by license of this font.
        For example some font can't be embedded into PDF document if license rules disable embedding for this font.
        This flag is used to disable any license restrictions for all fonts in current PDF document.
        Be careful when using this flag. When it is set it means that person who sets this flag,
        takes all responsibility of possible license/law violations on himself.
        So He takes it on it's own risk.
        It's strongly recommended to use this flag only when you are fully confident that you are not breaking
        the copyright law.
        By default false.'''
        ...
    
    @disable_font_license_verifications.setter
    def disable_font_license_verifications(self, value: bool):
        ...
    
    @property
    def font_utilities(self) -> None:
        '''IDocumentFontUtilities instance'''
        ...
    
    @property
    def collection(self) -> aspose.pdf.Collection:
        '''Gets collection of document.'''
        ...
    
    @collection.setter
    def collection(self, value: aspose.pdf.Collection):
        ...
    
    @property
    def version(self) -> str:
        '''Gets a version of Pdf from Pdf file header.'''
        ...
    
    @property
    def open_action(self) -> aspose.pdf.annotations.IAppointment:
        '''Gets or sets action performed at document opening.'''
        ...
    
    @open_action.setter
    def open_action(self, value: aspose.pdf.annotations.IAppointment):
        ...
    
    @property
    def hide_tool_bar(self) -> bool:
        '''Gets or sets flag specifying whether toolbar should be hidden when document is active.'''
        ...
    
    @hide_tool_bar.setter
    def hide_tool_bar(self, value: bool):
        ...
    
    @property
    def hide_menubar(self) -> bool:
        '''Gets or sets flag specifying whether menu bar should be hidden when document is active.'''
        ...
    
    @hide_menubar.setter
    def hide_menubar(self, value: bool):
        ...
    
    @property
    def hide_window_ui(self) -> bool:
        '''Gets or sets flag specifying whether user interface elements should be hidden when document is active.'''
        ...
    
    @hide_window_ui.setter
    def hide_window_ui(self, value: bool):
        ...
    
    @property
    def fit_window(self) -> bool:
        '''Gets or sets flag specifying whether document window must be resized to fit the first displayed page.'''
        ...
    
    @fit_window.setter
    def fit_window(self, value: bool):
        ...
    
    @property
    def center_window(self) -> bool:
        '''Gets or sets flag specifying whether position of the document's window will be centerd on the screen.'''
        ...
    
    @center_window.setter
    def center_window(self, value: bool):
        ...
    
    @property
    def display_doc_title(self) -> bool:
        '''Gets or sets flag specifying whether document's window title bar should display document title.'''
        ...
    
    @display_doc_title.setter
    def display_doc_title(self, value: bool):
        ...
    
    @property
    def pages(self) -> aspose.pdf.PageCollection:
        '''Gets or sets collection of document pages.
        Note that pages are numbered from 1 in collection.'''
        ...
    
    @property
    def outlines(self) -> aspose.pdf.OutlineCollection:
        '''Gets document outlines.'''
        ...
    
    @property
    def actions(self) -> aspose.pdf.annotations.DocumentActionCollection:
        '''Gets document actions. This property is instance of DocumentActions class which allows to get/set BeforClosing, BeforSaving, etc. actions.'''
        ...
    
    @property
    def form(self) -> aspose.pdf.forms.Form:
        '''Gets Acro Form of the document.'''
        ...
    
    @property
    def embedded_files(self) -> aspose.pdf.EmbeddedFileCollection:
        '''Gets collection of files embedded to document.'''
        ...
    
    @property
    def direction(self) -> aspose.pdf.Direction:
        '''Gets or sets reading order of text: L2R (left to right) or R2L (right to left).'''
        ...
    
    @direction.setter
    def direction(self, value: aspose.pdf.Direction):
        ...
    
    @property
    def page_mode(self) -> aspose.pdf.PageMode:
        '''Gets or sets page mode, specifying how document should be displayed when opened.'''
        ...
    
    @page_mode.setter
    def page_mode(self, value: aspose.pdf.PageMode):
        ...
    
    @property
    def non_full_screen_page_mode(self) -> aspose.pdf.PageMode:
        '''Gets or sets page mode, specifying how to display the document on exiting full-screen mode.'''
        ...
    
    @non_full_screen_page_mode.setter
    def non_full_screen_page_mode(self, value: aspose.pdf.PageMode):
        ...
    
    @property
    def page_layout(self) -> aspose.pdf.PageLayout:
        '''Gets or sets page layout which shall be used when the document is opened.'''
        ...
    
    @page_layout.setter
    def page_layout(self, value: aspose.pdf.PageLayout):
        ...
    
    @property
    def duplex(self) -> aspose.pdf.PrintDuplex:
        '''Gets or sets print duplex mode handling option to use when printing the file from the print dialog.'''
        ...
    
    @duplex.setter
    def duplex(self, value: aspose.pdf.PrintDuplex):
        ...
    
    @property
    def print_scaling(self) -> aspose.pdf.PrintScaling:
        '''Gets or sets the page scaling option that shall be selected when a print dialog is displayed for this document.'''
        ...
    
    @print_scaling.setter
    def print_scaling(self, value: aspose.pdf.PrintScaling):
        ...
   
    @property
    def pick_tray_by_pdf_size(self) -> bool:
        '''Gets or sets a flag specifying whether the PDF page size shall be used to select the input paper tray.'''
        ...
    
    @pick_tray_by_pdf_size.setter
    def pick_tray_by_pdf_size(self, value: bool):
        ...

    @property
    def file_name(self) -> str:
        '''Name of the PDF file that caused this document'''
        ...
    
    @property
    def info(self) -> aspose.pdf.DocumentInfo:
        '''Gets document info.'''
        ...
    
    @property
    def metadata(self) -> aspose.pdf.Metadata:
        '''Document metadata.
        (A PDF document may include general information,
        such as the document's title, author, and creation and modification dates.
        Such global information about the document (as opposed to its content or structure) is called metadata
        and is intended to assist in cataloguing and searching for documents in external databases.)'''
        ...
    
    @property
    def logical_structure(self) -> aspose.pdf.structure.RootElement:
        '''Gets logical structure of the document.'''
        ...
    
    @property
    def handle_signature_change(self) -> bool:
        '''Throw Exception if the document will save with changes and have signature'''
        ...
    
    @handle_signature_change.setter
    def handle_signature_change(self, value: bool):
        ...
    
    @property
    def crypto_algorithm(self) -> aspose.pdf.CryptoAlgorithm:
        '''Gets security settings if document is encrypted.
        If document is not encrypted then corresponding exception will be raised in .net 1.1
        or CryptoAlgorithm will be null for other .net versions.'''
        ...
    
    @property
    def is_linearized(self) -> bool:
        '''Gets or sets a value indicating whether document is linearized.'''
        ...
    
    @is_linearized.setter
    def is_linearized(self, value: bool):
        ...
    
    @property
    def permissions(self) -> int:
        '''Gets permissions of the document.'''
        ...
    
    @property
    def is_encrypted(self) -> bool:
        '''Gets encrypted status of the document. True if document is encrypted.'''
        ...
    
    @property
    def id(self) -> aspose.pdf.Id:
        '''Gets the ID.'''
        ...
    
    @property
    def background(self) -> aspose.pdf.Color:
        '''Gets or sets the background color of the document.'''
        ...
    
    @background.setter
    def background(self, value: aspose.pdf.Color):
        ...
    
    @property
    def optimize_size(self) -> bool:
        '''Gets or sets optimization flag. When pages are added to document, equal resource streams in resultant file are
        merged into one PDF object if this flag set.
        This allows to decrease resultant file size but may cause slower execution and larger memory requirements.
        Default value: false.'''
        ...
    
    @optimize_size.setter
    def optimize_size(self, value: bool):
        ...
    
    @property
    def allow_reuse_page_content(self) -> bool:
        '''Allows to merge page contents to optimize docuement size. If used then differnet but duplicated pages may reference to the
        same content object. Please note that this mode may cause side effects like changing page content when other page is changed.'''
        ...
    
    @allow_reuse_page_content.setter
    def allow_reuse_page_content(self, value: bool):
        ...
    
    @property
    def ignore_corrupted_objects(self) -> bool:
        '''Gets or sets flag of ignoring errors in source files.
        When pages from source document copied into destination document, copying process is stopped with exception
        if some objects in source files are corrupted when this flag is false.
        example: dest.Pages.Add(src.Pages);
        If this flag is set to true then corrupted objects will be replaced with empty values.
        By default: true.'''
        ...
    
    @ignore_corrupted_objects.setter
    def ignore_corrupted_objects(self, value: bool):
        ...
    
    @property
    def page_labels(self) -> aspose.pdf.PageLabelCollection:
        '''Gets page labels in the document.'''
        ...
    
    @property
    def enable_object_unload(self) -> bool:
        '''Get or sets flag which enables document partially be unloaded from memory.
        This allow to decrease memory usage but may have negative effect on perfomance.'''
        ...
    
    @enable_object_unload.setter
    def enable_object_unload(self, value: bool):
        ...
    
    @property
    def tagged_content(self) -> aspose.pdf.tagged.ITaggedContent:
        '''Gets access to TaggedPdf content.'''
        ...

    file_size_limit_to_memory_loading: int

    class OptimizationOptions(aspose.pdf.Document.OptimizationOptions):
          '''Class which describes document optimization algorithm. Instance of this class may be used as parameter of OptimizeResources() method.'''
    
          def __init__(self):
              ...
        
          def all(self) -> aspose.pdf.Document.OptimizationOptions:
              '''Creates optimization strategy will all options activated.
              :returns: OptimizationOptions object.'''
              ...

    class RepairOptions:
          '''Represents options for repairing a PDF document. This class provides a way to customize the repair process of a PDF document.'''
    
          def __init__(self):
              ...
        
          @property
          def restore_indirect_object_generations(self) -> bool:
              '''Gets or sets a value indicating whether to restore wrong generation numbers in references to indirect objects
                 during the repair process.'''
              ...
    
          @restore_indirect_object_generations.setter
          def restore_indirect_object_generations(self, value: bool):
              ...

    class MergeOptions:
          '''Represents the options to Merge methods.'''
    
          def __init__(self):
              ...
        
          @property
          def maximum_nodes_in_level(self) -> Any:
              '''Gets and sets the maximum nodes in pages tree level.
                 Default is 10.'''
              ...
    
          @maximum_nodes_in_level.setter
          def maximum_nodes_in_level(self, value: Any):
              ...

          @property
          def is_need_page_tree_balance(self) -> bool:
              '''Gets and sets the requirement for page tree balancing
                 The entire page tree in the resulting document will be rebalanced.
                 It creates balanced pages tree to speed up pages access.'''
              ...
    
          @is_need_page_tree_balance.setter
          def is_need_page_tree_balance(self, value: bool):
              ...
  
    ...

class DocumentExtensions:
    '''Provides additional capabilities for the Document class.'''
    
    @staticmethod
    def split_shared_images(self, doc: aspose.pdf.Document, page_1: aspose.pdf.Page, page_2: aspose.pdf.Page) -> None:
        '''For Images in Resources if two pages checks for common XImages and for similar cases splits them, by creating duplicate XImages.
        
        :param doc: The document containing both collections.
        :param page_1: First page for compare.
        :param page_2: Second page for compare/'''
        ...
    
    ...

class DocumentFactory:
    '''Class which allows to create/load documents of different types.'''
    
    def __init__(self):
        ...
    
    @overload
    def create_document(self, input: Any, options: aspose.pdf.LoadOptions) -> aspose.pdf.Document:
        '''Create document.
        
        :param input: Input stream.
        :param options: Document load options.
        :returns: Created document.'''
        ...
    
    @overload
    def create_document(self) -> aspose.pdf.Document:
        '''Create empty document.
        
        :returns: Created document.'''
        ...
    
    @overload
    def create_document(self, input: Any) -> aspose.pdf.Document:
        '''Load document from a stream.
        
        :param input: Input stream.
        :returns: Created document.'''
        ...
    
    @overload
    def create_document(self, input: Any, password: str) -> aspose.pdf.Document:
        '''Load password protected document from a stream.
        
        :param input: Source stream.
        :param password: Passowrd for access to document.
        :returns: Created document.'''
        ...
    
    @overload
    def create_document(self, file_name: str) -> aspose.pdf.Document:
        '''Load document from a file.
        
        :param file_name: Name of PDF file.
        :returns: Created document.'''
        ...
    
    ...

class DocumentInfo:
    '''Represents meta information of PDF document.'''
    
    def __init__(self, document: aspose.pdf.Document):
        '''Initialize DocumentInfo instance.
        
        :param document: The info of this document will be used for initialization.'''
        ...
    
    def clear(self) -> None:
        '''Clears the document info.'''
        ...
    
    def add(self, key: str, value: str) -> None:
        '''Adds an element with the specified key and value into the collection.
        
        :param key: The key of the element to add.
        :param value: The value of the element to add. The value can be null.'''
        ...
    
    def remove(self, key: str) -> None:
        '''Removes the element with the specified key from the collection.
        
        :param key: The key of the element to remove.'''
        ...
    
    def clear_custom_data(self) -> None:
        '''Clears custom data only, leaves all other predefined values (Title, Author, etc.).'''
        ...
    
    @staticmethod
    def is_predefined_key(self, key: str) -> bool:
        '''Determines if the key is predefined (Title, Author, etc.), not custom.
        
        :param key: Selected key
        :returns: True in case the key is predefined.'''
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets document title.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def creator(self) -> str:
        '''Gets or sets document creator.'''
        ...
    
    @creator.setter
    def creator(self, value: str):
        ...
    
    @property
    def author(self) -> str:
        '''Gets or sets document author.'''
        ...
    
    @author.setter
    def author(self, value: str):
        ...
    
    @property
    def subject(self) -> str:
        '''Gets or sets the subject of the document.'''
        ...
    
    @subject.setter
    def subject(self, value: str):
        ...
    
    @property
    def keywords(self) -> str:
        '''Gets or set the keywords of the document.'''
        ...
    
    @keywords.setter
    def keywords(self, value: str):
        ...
    
    @property
    def producer(self) -> str:
        '''Gets or sets the document producer.'''
        ...
    
    @producer.setter
    def producer(self, value: str):
        ...
    
    @property
    def creation_date(self) -> datetime.datetime:
        '''Gets or sets the date of document creation.'''
        ...
    
    @creation_date.setter
    def creation_date(self, value: datetime.datetime):
        ...
    
    @property
    def creation_time_zone(self) -> datetime.timespan:
        '''Time zone of creation date.'''
        ...
    
    @creation_time_zone.setter
    def creation_time_zone(self, value: datetime.timespan):
        ...
    
    @property
    def mod_time_zone(self) -> datetime.timespan:
        '''Time zone of modification date.'''
        ...
    
    @mod_time_zone.setter
    def mod_time_zone(self, value: datetime.timespan):
        ...
    
    @property
    def mod_date(self) -> datetime.datetime:
        '''Gets or sets the date of document modification.'''
        ...
    
    @mod_date.setter
    def mod_date(self, value: datetime.datetime):
        ...
    
    @property
    def trapped(self) -> str:
        '''Gets or sets the trapped flag.'''
        ...
    
    @trapped.setter
    def trapped(self, value: str):
        ...
    
    ...

class EmbeddedFileCollection:
    '''Class representing embedded files collection.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.FileSpecification:
        '''Gets embedded file by its index.
        
        :param index: Index of embedded file. Numbering is started from 1.
        :returns: Retreived embedded file specification'''
        ...
    
    @overload
    def delete(self, name: str) -> None:
        '''Delete embedded file by name.
        
        :param name: Name of the embedded file which should be deleted.'''
        ...
    
    @overload
    def delete(self) -> None:
        '''Remove all embedded files from document.'''
        ...
    
    def add(self, key: str, file: aspose.pdf.FileSpecification) -> None:
        '''Adds file to embedded files with the specified key.
        
        :param key: Key in the embedded files.
        :param file: File specification.'''
        ...
    
    def delete_by_key(self, key: str) -> None:
        '''Deletes file from the collection by its key in the collection.
        
        :param key: Key name.'''
        ...
    
    def find_by_name(self, name: str) -> aspose.pdf.FileSpecification:
        '''Returns embedded file by its name.
        
        :param name: Name of the file.
        :returns: File specification object if found; otherwise, null.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Gets a value indicating whether access to this collection is synchronized (thread safe).'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets an object that can be used to synchronize access to this collection.'''
        ...
    
    @property
    def keys(self) -> None:
        '''Returns list of file attachment keys.'''
        ...
    
    ...

class EmptyValueException(aspose.pdf.PdfException):
    '''Exception which thrown when requirested value does not exists.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`EmptyValueException` class.'''
        ...
    
    @overload
    def __init__(self, message: str):
        '''Constructor.
        
        :param message: Exception message.'''
        ...
    
    ...

class EncryptedPayload:
    '''Represents encrypted payload in file specification.'''
    
    def __init__(self, file_specification: aspose.pdf.FileSpecification):
        '''Initialize Encrypted payload instance.
        
        :param file_specification: The file specification used for initialization.'''
        ...
    
    @property
    def type(self) -> str:
        '''Gets type.'''
        ...
    
    @property
    def subtype(self) -> str:
        '''Gets subtype.'''
        ...
    
    @property
    def version(self) -> str:
        '''Gets version number.'''
        ...
    
    ...

class EpubLoadOptions(aspose.pdf.LoadOptions):
    '''Contains options for loading/importing EPUB file into pdf document.'''
    
    @overload
    def __init__(self):
        '''Creates default load options for converting EPUB file into pdf document.
        Default pdf page size - A4 300dpi 2480 X 3508.'''
        ...
    
    @overload
    def __init__(self, page_size: aspose.pydrawing.SizeF):
        '''Creates load options with specified page size.
        
        :param page_size: Defines pdf page width and height.'''
        ...
    
    @property
    def page_size(self) -> aspose.pydrawing.SizeF:
        '''Gets or sets output page size for import.'''
        ...
    
    @property
    def margin(self) -> aspose.pdf.MarginInfo:
        '''Gets reference on object that represent marging info.'''
        ...
    
    @margin.setter
    def margin(self, value: aspose.pdf.MarginInfo):
        ...
    
    @property
    def margins_area_usage_mode(self) -> None:
        '''Represents mode of usage of margins area - defines treatement
        of instructions (if any) of CSS of imported document
        related to usage of margins.'''
        ...
    
    @margins_area_usage_mode.setter
    def margins_area_usage_mode(self, value: None):
        ...
    
    @property
    def page_size_adjustment_mode(self) -> None:
        '''ATTENTION! The feature implemented but did not put yet to public API since blocker issue in
        OSHARED layer revealed for sample document.
        
        Represents mode of usage of page size during conversion.
        Formats (like HTML, EPUB etc), usually have float design, so, it allows to fit required
        pagesize. But sometimes content has specified horizontal positions or size that
        does not allow put content into required page size.
        In such case we can define what should be done in this case (i.e when size of content does not fit
        required initial page size of result PDF document).'''
        ...
    
    @page_size_adjustment_mode.setter
    def page_size_adjustment_mode(self, value: None):
        ...
    
    ...

class EpubSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to EPUB format'''
    
    def __init__(self):
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets EPUB document title.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...

    @property
    def content_recognition_mode(self) -> None:
        '''When PDF file (that usually has fixed layout) is being converted,
        the conversion engine tries to perform grouping and multi-level analysis to restore
        the original document author's intent and produce result in flow layout.
        This property tunes that conversion for this or that
        desirable method of recognition of content.'''
        ...
    
    @content_recognition_mode.setter
    def content_recognition_mode(self, value: None):
        ...
    
    class RecognitionMode:
          '''When PDF file (that usually has fixed layout) is being converted,
          the conversion engine tries to perform grouping and multi-level analysis to restore the original document author's intent and produce result in flow layout.
          This property tunes that conversion for this or that desirable method of recognition of content.'''

          FLOW: RecognitionMode
          PDF_FLOW: RecognitionMode
          FIXED: RecognitionMode

    ...

class ExcelSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to Excel format'''
    
    def __init__(self):
        ...
    
    @property
    def minimize_the_number_of_worksheets(self) -> bool:
        '''Set true if you need to minimize the number of worksheets in resultant workbook.
        Default value is false; it means save of each PDF page as separated worksheet.'''
        ...
    
    @minimize_the_number_of_worksheets.setter
    def minimize_the_number_of_worksheets(self, value: bool):
        ...
    
    @property
    def insert_blank_column_at_first(self) -> bool:
        '''Set true if you need inserting of blank column as the first column of worksheet.
        Default value is false; it means that blank column will not be inserted.'''
        ...
    
    @insert_blank_column_at_first.setter
    def insert_blank_column_at_first(self, value: bool):
        ...
    
    @property
    def uniform_worksheets(self) -> bool:
        '''Set true for using uniform columns division through the document.
        Default value is false; it means that columns division will independent for each page.'''
        ...
    
    @uniform_worksheets.setter
    def uniform_worksheets(self, value: bool):
        ...
    
    @property
    def format(self) -> None:
        '''Output format'''
        ...
    
    @format.setter
    def format(self, value: None):
        ...
    
    class ExcelFormat:
          '''Allows to specify .xlsx, .xls/xml or csv file format. Default value is XLSX.'''

          XML_SPREAD_SHEET2003: RecognitionMode
          XLSX: ExcelFormat
          CSV: ExcelFormat
          XLSM: ExcelFormat
          ODS: ExcelFormat

    ...

class FileHyperlink(aspose.pdf.Hyperlink):
    '''Represents file hyperlink object.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`FileHyperlink` class.'''
        ...
    
    @overload
    def __init__(self, path: str):
        '''Initializes a new instance of the :class:`FileHyperlink` class.
        
        :param path: Path to file.'''
        ...
    
    @property
    def new_window(self) -> aspose.pdf.ExtendedBoolean:
        '''Gets or sets a flag specifying whether to open the destination document in a new window (affect PDF documents only).'''
        ...
    
    @new_window.setter
    def new_window(self, value: aspose.pdf.ExtendedBoolean):
        ...

    @property
    def path(self) -> str:
        '''Gets or sets the path to file.'''
        ...
    
    @path.setter
    def path(self, value: str):
        ...
    
    ...

class FileParams:
    '''Defines an embedded file parameter dictionary that shall contain additional file-specific information.'''
    
    def __init__(self, spec: aspose.pdf.FileSpecification):
        '''Constructor for FileParams class.
        
        :param spec: File specification.'''
        ...
    
    @property
    def size(self) -> int:
        '''The size of the uncompressed embedded file, in bytes.'''
        ...
    
    @property
    def creation_date(self) -> datetime.datetime:
        '''The date and time when the embedded file was created.'''
        ...
    
    @creation_date.setter
    def creation_date(self, value: datetime.datetime):
        ...
    
    @property
    def mod_date(self) -> datetime.datetime:
        '''The date and time when the embedded file was last modified.'''
        ...
    
    @mod_date.setter
    def mod_date(self, value: datetime.datetime):
        ...
    
    @property
    def check_sum(self) -> str:
        '''A 16-byte string that is the checksum of the bytes of the uncompressed embedded file.
        The checksum is calculated by applying the standard MD5 message-digest algorithm
        to the bytes of the embedded file stream.'''
        ...
    
    ...

class FileSpecification:
    '''Class representing embedded file.'''
    
    @overload
    def __init__(self, file: str):
        '''Constructor for FileSpecification
        
        :param file: File path.'''
        ...
    
    @overload
    def __init__(self, stream: Any, name: str):
        '''Constructor for file specification.
        
        :param stream: Stream containing data file.
        :param name: File specification.'''
        ...
    
    @overload
    def __init__(self, file: str, description: str):
        '''Constructor for FileSpecification.
        
        :param file: File path.
        :param description: File description.'''
        ...
    
    @overload
    def __init__(self, stream: Any, name: str, description: str):
        '''Constructor for FileSpecification.
        
        :param stream: Stream to be used in the document.
        :param name: A file specification string.
        :param description: File description.'''
        ...
    
    @overload
    def __init__(self, file_name: str, annot: aspose.pdf.annotations.Annotation):
        '''Constructor for FileSpecification.
        
        :param file_name: File path.
        :param annot: The annotation.'''
        ...
    
    @overload
    def __init__(self):
        '''Create new empty file specification.'''
        ...
    
    def get_value(self, key: str) -> str:
        '''Gets application-specific parameter.
        
        :param key: Parameter name.
        :returns: Value - if parameter found; otherwise, null.'''
        ...
    
    def set_value(self, key: str, value: str) -> None:
        '''Sets application-specific parameter.
        
        :param key: Parameter name.
        :param value: New parameter value.'''
        ...
    
    @property
    def encoding(self) -> aspose.pdf.FileEncoding:
        '''Gets or sets encoding format.
        Possible values: Zip - file is compressed with ZIP,
        None - file is not compressed.'''
        ...
    
    @encoding.setter
    def encoding(self, value: aspose.pdf.FileEncoding):
        ...
    
    @property
    def include_contents(self) -> bool:
        '''If true, contents of the file will be included in the file specification.'''
        ...
    
    @include_contents.setter
    def include_contents(self, value: bool):
        ...
    
    @property
    def collection_item(self) -> aspose.pdf.CollectionItem:
        '''Gets a collection item of the file specification.'''
        ...

    @property
    def encrypted_payload(self) -> aspose.pdf.EncryptedPayload:
        '''Gets encrypted payload.'''
        ...
    
    @property
    def description(self) -> str:
        '''Gets or sets text associated with the file specification.'''
        ...
    
    @description.setter
    def description(self, value: str):
        ...
    
    @property
    def af_relationship(self) -> aspose.pdf.AFRelationship:
        '''Associated file Relationship.'''
        ...
    
    @af_relationship.setter
    def af_relationship(self, value: aspose.pdf.AFRelationship):
        ...
    
    @property
    def stream_contents(self) -> Any:
        '''Gets contents of file as stream.
        Contents is not loaded into memory which allows to decrease memory usage.
        But this stream does not support positioning and Length property. If you need this features please use Contents property instead.'''
        ...
    
    @property
    def contents(self) -> Any:
        '''Gets or sets contents file.
        This property returns data loaded in memory which may cause Out of memory exception for large data.
        To decrease memory usage please use StreamContents.'''
        ...
    
    @contents.setter
    def contents(self, value: Any):
        ...
    
    @property
    def params(self) -> aspose.pdf.FileParams:
        '''Gets file paramteres.'''
        ...
    
    @params.setter
    def params(self, value: aspose.pdf.FileParams):
        ...
    
    @property
    def mime_type(self) -> str:
        '''Gets subtype of the embedded file'''
        ...
    
    @mime_type.setter
    def mime_type(self, value: str):
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets file specification name.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def unicode_name(self) -> str:
        '''Gets or sets file specification unicode name.'''
        ...
    
    @unicode_name.setter
    def unicode_name(self, value: str):
        ...
    
    @property
    def file_system(self) -> str:
        '''Gets or sets name of the file system.'''
        ...
    
    @file_system.setter
    def file_system(self, value: str):
        ...
    
    ...

class FloatingBox(aspose.pdf.BaseParagraph):
    '''Represents a FloatingBox in a Pdf document. FloatingBox is custom positioned.'''
    
    @overload
    def __init__(self, width: float, height: float):
        '''Initializes a new instance of the :class:`FloatingBox` class with specified width and height.
        
        :param width: The width of the box.
        :param height: The height of the box.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`FloatingBox` class.'''
        ...
    
    def clone(self) -> object:
        '''Clones a new :class:`FloatingBox` object. Paragraphs in the floating box are not cloned.
        
        :returns: The new :class:`FloatingBox` object.'''
        ...
    
    @property
    def column_info(self) -> aspose.pdf.ColumnInfo:
        '''Gets or sets a column info'''
        ...
    
    @column_info.setter
    def column_info(self, value: aspose.pdf.ColumnInfo):
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets a float value that indicates the width of the floating box.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets a float value that indicates the height of the floating box.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def is_need_repeating(self) -> bool:
        '''Gets or sets a bool value that indicates whether the paragraph need to be repeated on next page.
        Default value is false.The attribute is only valid when the paragraph itself and the object its ReferenceParagraphID referred to both are included in RepeatingRows.'''
        ...
    
    @is_need_repeating.setter
    def is_need_repeating(self, value: bool):
        ...
    
    @property
    def paragraphs(self) -> aspose.pdf.Paragraphs:
        '''Gets or sets a :attr:`FloatingBox.paragraphs` collection that indicates all paragraphs in the cell.'''
        ...
    
    @paragraphs.setter
    def paragraphs(self, value: aspose.pdf.Paragraphs):
        ...
    
    @property
    def border(self) -> aspose.pdf.BorderInfo:
        '''Gets or sets a :class:`BorderInfo` object that indicates the border info of the floating box.'''
        ...
    
    @border.setter
    def border(self, value: aspose.pdf.BorderInfo):
        ...
    
    @property
    def background_color(self) -> aspose.pdf.Color:
        '''Gets or sets a :class:`Color` object that indicates the background color of the floating box.'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def background_image(self) -> aspose.pdf.Image:
        '''Gets or sets background image for page (for generator only, not filled in when reading document).'''
        ...
    
    @background_image.setter
    def background_image(self, value: aspose.pdf.Image):
        ...
    
    @property
    def padding(self) -> aspose.pdf.MarginInfo:
        '''Gets or sets a :class:`MarginInfo` object that indicates the padding of the floating box.'''
        ...
    
    @padding.setter
    def padding(self, value: aspose.pdf.MarginInfo):
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
    
    ...

class FontEmbeddingException(RuntimeError):
    '''The exception that is thrown when an attempt to embed font became failed'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`FontEmbeddingException` class.
        
        :param message: The message.'''
        ...
    
    ...

class FontNotFoundException(RuntimeError):
    '''The exception that is thrown when a font is not found.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`FontNotFoundException` class.
        
        :param message: The message.'''
        ...
    
    ...

class FooterArtifact(aspose.pdf.Artifact):
    '''Describes footer artifact. This may be used to set footer of the page.'''
    
    def __init__(self):
        '''Creates Footer Artifact instance.'''
        ...
    
    ...

class FormattedFragment(aspose.pdf.BaseParagraph):
    '''Represents abstract formatted fragment.'''
    
    ...

class GraphInfo:
    '''Represents graphics info.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> object:
        '''Clone the graphics info.
        
        :returns: The cloned object'''
        ...
    
    @property
    def line_width(self) -> float:
        '''Gets or sets a float value that indicates the line width of the graph.'''
        ...
    
    @line_width.setter
    def line_width(self, value: float):
        ...
    
    @property
    def color(self) -> aspose.pdf.Color:
        '''Gets or sets a :attr:`GraphInfo.color` object that indicates the color of the graph.'''
        ...
    
    @color.setter
    def color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def dash_array(self) -> list[int]:
        '''Gets or sets a dash array.'''
        ...
    
    @dash_array.setter
    def dash_array(self, value: list[int]):
        ...
    
    @property
    def dash_phase(self) -> int:
        '''Gets or sets a dash phase.'''
        ...
    
    @dash_phase.setter
    def dash_phase(self, value: int):
        ...
    
    @property
    def fill_color(self) -> aspose.pdf.Color:
        '''Gets or sets a :attr:`GraphInfo.color` object that indicates the fill color of the graph.'''
        ...
    
    @fill_color.setter
    def fill_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def is_doubled(self) -> bool:
        '''Gets or sets is border doubled.'''
        ...
    
    @is_doubled.setter
    def is_doubled(self, value: bool):
        ...
    
    @property
    def skew_angle_x(self) -> float:
        '''Gets or sets a float value that indicates the skew angle of the x-coordinate when transforming a coordinate system.'''
        ...
    
    @skew_angle_x.setter
    def skew_angle_x(self, value: float):
        ...
    
    @property
    def skew_angle_y(self) -> float:
        '''Gets or sets a float value that indicates the skew angle of the y-coordinate when transforming a coordinate system.'''
        ...
    
    @skew_angle_y.setter
    def skew_angle_y(self, value: float):
        ...
    
    @property
    def scaling_rate_x(self) -> float:
        '''Gets or sets a float value that indicates the scaling rate of the x-coordinate when transforming a coordinate system.'''
        ...
    
    @scaling_rate_x.setter
    def scaling_rate_x(self, value: float):
        ...
    
    @property
    def scaling_rate_y(self) -> float:
        '''Gets or sets a float value that indicates the scaling rate of the y-coordinate when transforming a coordinate system.'''
        ...
    
    @scaling_rate_y.setter
    def scaling_rate_y(self, value: float):
        ...
    
    @property
    def rotation_angle(self) -> float:
        '''Gets or sets a float value that indicates the rotation angle of the coordinate system
        when transforming a coordinate system.'''
        ...
    
    @rotation_angle.setter
    def rotation_angle(self, value: float):
        ...
    
    ...

class Group:
    '''A group attributes class specifying the attributes of the page’s page group for use in the transparent imaging model.'''
    
    def __init__(self, page: aspose.pdf.Page):
        '''The constructor.
        
        :param page: Pdf page object.'''
        ...
    
    @property
    def color_space(self) -> aspose.pdf.ColorSpace:
        '''The group color space.'''
        ...
    
    @color_space.setter
    def color_space(self, value: aspose.pdf.ColorSpace):
        ...
    
    ...

class HeaderArtifact(aspose.pdf.Artifact):
    '''Class describes Heaader artifact. This artifacgt may be used to set heading of the page.'''
    
    def __init__(self):
        '''Creates Header Artifact instance.'''
        ...
    
    ...

class HeaderFooter:
    '''Class represents header or footer pdf page.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> object:
        '''Clones a new object.
        
        :returns: The new object.'''
        ...
    
    @property
    def is_clip_extra_content(self) -> bool:
        '''Gets or sets is clip extra content.'''
        ...
    
    @is_clip_extra_content.setter
    def is_clip_extra_content(self, value: bool):
        ...
    
    @property
    def paragraphs(self) -> aspose.pdf.Paragraphs:
        '''Gets or sets the end note paragraphs.'''
        ...
    
    @paragraphs.setter
    def paragraphs(self, value: aspose.pdf.Paragraphs):
        ...
    
    @property
    def margin(self) -> aspose.pdf.MarginInfo:
        '''Gets or sets the margin info.'''
        ...
    
    @margin.setter
    def margin(self, value: aspose.pdf.MarginInfo):
        ...
    
    ...

class Heading(aspose.pdf.text.TextFragment):
    '''Represents heading.'''
    
    def __init__(self, level: int):
        '''Initializes a new instance of the Cell class.
        
        :param level: The headings level.'''
        ...
    
    def clone(self) -> object:
        '''Clone the heading.
        
        :returns: The cloned object'''
        ...
    
    def clone_with_segments(self) -> object:
        '''Clone the heading with all segments.
        
        :returns: The cloned object'''
        ...
    
    @property
    def toc_page(self) -> aspose.pdf.Page:
        '''Gets the page that contains this heading.'''
        ...
    
    @toc_page.setter
    def toc_page(self, value: aspose.pdf.Page):
        ...
    
    @property
    def top(self) -> float:
        '''Gets the top Y of this headings.'''
        ...
    
    @top.setter
    def top(self, value: float):
        ...
    
    @property
    def start_number(self) -> int:
        '''Gets the heading start number.'''
        ...
    
    @start_number.setter
    def start_number(self, value: int):
        ...
    
    @property
    def is_auto_sequence(self) -> bool:
        '''Gets the heading should be numered automatically.'''
        ...
    
    @is_auto_sequence.setter
    def is_auto_sequence(self, value: bool):
        ...
    
    @property
    def is_in_list(self) -> bool:
        '''Gets the heading should be in toc list.'''
        ...
    
    @is_in_list.setter
    def is_in_list(self, value: bool):
        ...
    
    @property
    def destination_page(self) -> aspose.pdf.Page:
        '''Gets the destination page.'''
        ...
    
    @destination_page.setter
    def destination_page(self, value: aspose.pdf.Page):
        ...
    
    @property
    def level(self) -> int:
        '''Gets the level.'''
        ...
    
    @level.setter
    def level(self, value: int):
        ...
    
    @property
    def style(self) -> aspose.pdf.NumberingStyle:
        '''Gets or sets style.'''
        ...
    
    @style.setter
    def style(self, value: aspose.pdf.NumberingStyle):
        ...
    
    @property
    def user_label(self) -> aspose.pdf.text.TextSegment:
        '''Gets or sets user label.'''
        ...
    
    @user_label.setter
    def user_label(self, value: aspose.pdf.text.TextSegment):
        ...
    
    ...

class HtmlFragment(aspose.pdf.FormattedFragment):
    '''Represents html fragment.'''
    
    def __init__(self, text: str):
        '''Initializes a new instance of the HtmlFragment class.
        
        :param text: The fragment text'''
        ...
    
    def clone(self) -> object:
        '''Clones html fragment.
        
        :returns: Cloned html fragment object.'''
        ...
    
    @property
    def rectangle(self) -> aspose.pydrawing.RectangleF:
        '''Gets rectangle of the HtmlFragment'''
        ...
    
    @property
    def is_paragraph_has_margin(self) -> bool:
        '''Gets or sets is paragraph has default margin otherwise margin is 0'''
        ...
    
    @is_paragraph_has_margin.setter
    def is_paragraph_has_margin(self, value: bool):
        ...
    
    @property
    def is_break_words(self) -> bool:
        '''Gets or sets words break'''
        ...
    
    @is_break_words.setter
    def is_break_words(self, value: bool):
        ...
    
    @property
    def text_state(self) -> aspose.pdf.text.TextState:
        '''Gets or sets font'''
        ...
    
    @text_state.setter
    def text_state(self, value: aspose.pdf.text.TextState):
        ...
    
    @property
    def html_load_options(self) -> aspose.pdf.HtmlLoadOptions:
        '''Gets or sets HtmlLoadOptions that will be used for loading (and rendering) of HTML into this instance of class.
        Please use it when it's necessary use specific setting for import of HTML for this or that instance
        (f.e when this or that instance should use specific BasePath for imported HTML or should use specific loader of external resources)
        If parameter is default (null), then standard HTML loading options will be used.'''
        ...
    
    @html_load_options.setter
    def html_load_options(self, value: aspose.pdf.HtmlLoadOptions):
        ...
    
    ...

class HtmlLoadOptions(aspose.pdf.LoadOptions):
    '''Represents options for loading/importing html file into pdf document.'''
    
    @overload
    def __init__(self):
        '''Creates load options for converting html into pdf document with empty base path.'''
        ...
    
    @overload
    def __init__(self, base_path: str):
        '''Creates load options for converting html into pdf document with defined base path.
        
        :param base_path: The base path/url for the html file.'''
        ...
    
    @property
    def is_render_to_single_page(self) -> bool:
        '''Gets or sets rendering all document to single page'''
        ...
    
    @is_render_to_single_page.setter
    def is_render_to_single_page(self, value: bool):
        ...
    
    @property
    def is_embed_fonts(self) -> bool:
        '''Gets or sets fonts embedding to result document'''
        ...
    
    @is_embed_fonts.setter
    def is_embed_fonts(self, value: bool):
        ...
    
    @property
    def page_layout_option(self) -> aspose.pdf.HtmlPageLayoutOption:
        '''Gets or sets layout option.'''
        ...
    
    @page_layout_option.setter
    def page_layout_option(self, value: aspose.pdf.HtmlPageLayoutOption):
        ...
    
    @property
    def html_media_type(self) -> aspose.pdf.HtmlMediaType:
        '''Gets or sets possible media types used during rendering.'''
        ...
    
    @html_media_type.setter
    def html_media_type(self, value: aspose.pdf.HtmlMediaType):
        ...
    
    @property
    def input_encoding(self) -> str:
        '''Gets or sets the attribute specifying the encoding used for this document at the time of the parsing. If this attribute is null the encoding will determine from document character set atribute.'''
        ...
    
    @input_encoding.setter
    def input_encoding(self, value: str):
        ...
    
    @property
    def base_path(self) -> str:
        '''The base path/url for the html file.'''
        ...
    
    @property
    def is_priority_css_page_rule(self) -> bool:
        '''Gets or sets the flag that specifies that @page rules defined in css will override values defined in PageInfo.'''
        ...
    
    @is_priority_css_page_rule.setter
    def is_priority_css_page_rule(self, value: bool):
        ...

    @property
    def page_info(self) -> aspose.pdf.PageInfo:
        '''Gets or sets document page info'''
        ...
    
    @page_info.setter
    def page_info(self, value: aspose.pdf.PageInfo):
        ...
    
    ...

class HtmlSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to Html format'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`HtmlSaveOptions` class.'''
        ...
    
    @overload
    def __init__(self, document_type: aspose.pdf.HtmlDocumentType):
        '''Initializes a new instance of the :class:`HtmlSaveOptions` class.
        
        :param document_type: The :class:`HtmlDocumentType`.'''
        ...
    
    @overload
    def __init__(self, fixed_layout: bool):
        '''Initializes a new instance of the :class:`HtmlSaveOptions` class.
        
        :param fixed_layout: if set to ``True`` HTML is created as fixed layout.'''
        ...
    
    @overload
    def __init__(self, document_type: aspose.pdf.HtmlDocumentType, fixed_layout: bool):
        '''Initializes a new instance of the :class:`HtmlSaveOptions` class.
        
        :param document_type: The :class:`HtmlDocumentType`.
        :param fixed_layout: if set to ``True`` HTML is created as fixed layout.'''
        ...
    
    @property
    def document_type(self) -> aspose.pdf.HtmlDocumentType:
        '''Gets or sets the :class:`HtmlDocumentType`.'''
        ...
    
    @document_type.setter
    def document_type(self, value: aspose.pdf.HtmlDocumentType):
        ...
    
    @property
    def compress_svg_graphics_if_any(self) -> bool:
        '''Gets or sets the flag that indicates whether
        found SVG graphics(if any) will be compressed(zipped)
        into SVGZ format during saving'''
        ...
    
    @compress_svg_graphics_if_any.setter
    def compress_svg_graphics_if_any(self, value: bool):
        ...
    
    @property
    def split_css_into_pages(self) -> bool:
        '''When multipage-mode selected(i.e 'SplitIntoPages' is 'true'),
        then this attribute defines whether should be created separate CSS-file
        for each result HTML page.
        By default this attribute is false, so, will be created
        one  big common CSS for all created pages. Summary size of all
        CSSes generated in this mode(one CSS per page) usually
        much more than size of one big CSS file, because in former case
        CSS classes are duplicates in such case in several CSS files for each page.
        So, this setting is worse to be used only when You are interested
        in future processing of each HTML page independently, and therefore size
        of CSS of each one page taken apart is the most critical issue.'''
        ...
    
    @split_css_into_pages.setter
    def split_css_into_pages(self, value: bool):
        ...
    
    @property
    def split_into_pages(self) -> bool:
        '''Gets or sets the flag that indicates whether each page of source
        document will be converted into it's own target HTML document,
        i.e whether result HTML will be splitted into several HTML-pages.'''
        ...
    
    @split_into_pages.setter
    def split_into_pages(self, value: bool):
        ...
    
    @property
    def explicit_list_of_saved_pages(self) -> list[int]:
        '''With this property You can explicitely define
        what pages of document should be converted.
        Pages in this list must have 1-based numbers. I.e.
        valid numbers of pages must be taken from range (1...[NumberOfPagesInConvertedDocument])
        Order of appearing of pages in this list does not affect their
        order in result HTML page(s) - in result pages allways will go in order in which they are
        present in source PDF.
        If this list is null (as it is by default), all pages will be converted.
        If any page number of this list will go out of range of present pages(1-[amountOfPagesInDocument])
        exception will be thrown.'''
        ...
    
    @explicit_list_of_saved_pages.setter
    def explicit_list_of_saved_pages(self, value: list[int]):
        ...
    
    @property
    def fixed_layout(self) -> bool:
        '''Gets or sets a value indicating whether that HTML is created as fixed layout.'''
        ...
    
    @fixed_layout.setter
    def fixed_layout(self, value: bool):
        ...
    
    @property
    def image_resolution(self) -> int:
        '''Gets or sets resolution for image rendering.'''
        ...
    
    @image_resolution.setter
    def image_resolution(self, value: int):
        ...
    
    @property
    def default_font_name(self) -> str:
        '''Specifies the name of an installed font which is used to substitute
        any document font that is not embedded and not installed in the system.
        If null then default substitution font is used.'''
        ...
    
    @default_font_name.setter
    def default_font_name(self, value: str):
        ...
    
    @property
    def ignore_resource_font_errors(self) -> bool:
        '''Gets or sets indication that errors related to absence of font will be ignored.
        true - means that errors of absence of font will be ignored. Text segments that refer to incorrect resources will be skipped during processing.
        false by default'''
        ...
    
    @ignore_resource_font_errors.setter
    def ignore_resource_font_errors(self, value: bool):
        ...

    @property
    def batch_size(self) -> int:
        '''Defines batch size if batched conversion is applicable
        to source and destination formats pair.'''
        ...
    
    @batch_size.setter
    def batch_size(self, value: int):
        ...
    
    @property
    def ignored_text_font_size(self) -> float:
        '''Text with the specified size or less will be ignored during conversion.
           We do not remove this text, we ignore it and do not transfer it to the output file'''
        ...
    
    @ignored_text_font_size.setter
    def ignored_text_font_size(self, value: float):
        ...

    @property
    def font_sources(self) -> aspose.pdf.text.FontSourceCollection:
        '''Font sources of pre-saved fonts.
        
        Fonts may be saved preliminarily for cache purpose and then passed into Html conversion process.
        For example it may be useful in document splitting scenario and processing document pages in multiple threads with single set of fonts.'''
        ...
    
    @property
    def additional_margin_width_in_points(self) -> int:
        '''If attribute 'SplitOnPages=false', than whole HTML representing all input PDF pages wont
        be not split into different HTML pages, but will be put into one big result HTML file.
        But each source PDF page will be represented with it's own
        rectangle  area in HTML (if necessary that areas can be bordered to show page paper edges
        with special attribute 'PageBorderIfAny'.
        This parameter defines width of margin that will be forcibly left around that output HTML-areas
        that represent pages of source PDF document.In essence it defines guaranteed interval between
        HTML-representations of PDF "paper" pages such mode of conversion.'''
        ...
    
    @additional_margin_width_in_points.setter
    def additional_margin_width_in_points(self, value: int):
        ...
    
    @property
    def use_z_order(self) -> bool:
        '''If attribute UseZORder set to true, graphics and text are added to resultant HTML document
        accordingly Z-order in original PDF document. If this attribute is false all graphics is put
        as single layer which may cause some unnecessary effects for overlapped objects.'''
        ...
    
    @use_z_order.setter
    def use_z_order(self, value: bool):
        ...
    
    @property
    def convert_marked_content_to_layers(self) -> bool:
        '''If attribute ConvertMarkedContentToLayers set to true then an all elements inside a PDF marked
        content (layer) will be put into an HTML div with "data-pdflayer" attribute specifying a layer name.
        This layer name will be extracted from optional properties of PDF marked content.
        If this attribute is false (by default) then no any layers will be created from PDF marked content.'''
        ...
    
    @convert_marked_content_to_layers.setter
    def convert_marked_content_to_layers(self, value: bool):
        ...
    
    @property
    def minimal_line_width(self) -> float:
        '''This attribute sets minimal width of graphic path line.
        If thickness of line is less than 1px Adobe Acrobat rounds it to this value. So this attribute can
        be used to emulate this behavior for HTML browsers.'''
        ...
    
    @minimal_line_width.setter
    def minimal_line_width(self, value: float):
        ...
    
    @property
    def prevent_glyphs_grouping(self) -> bool:
        '''This attribute switch on the mode when text glyphs will not be grouped into words and strings
        This mode allows to keep maximum precision during positioning of glyphs on the page and it can be
        used for conversion documents with music notes or glyphs that should be placed separately each other.
        This parameter will be applied to document only when the value of FixedLayout attribute is true.'''
        ...
    
    @prevent_glyphs_grouping.setter
    def prevent_glyphs_grouping(self, value: bool):
        ...
    
    @property
    def simple_textbox_mode_grouping(self) -> bool:
        '''This attribute specifies a sequential grouping of glyphs and words into strings
        For example tags and words has different order in converted HTML and you want them to match.
        This parameter will be applied to document only when the value of FixedLayout attribute is true.'''
        ...
    
    @simple_textbox_mode_grouping.setter
    def simple_textbox_mode_grouping(self, value: bool):
        ...
    
    @property
    def flow_layout_paragraph_full_width(self) -> bool:
        '''This attribute specifies full width paragraph text for Flow mode, FixedLayout = false'''
        ...
    
    @flow_layout_paragraph_full_width.setter
    def flow_layout_paragraph_full_width(self, value: bool):
        ...
    
    @property
    def render_text_as_image(self) -> bool:
        '''If attribute RenderTextAsImage set to true, the text from the source becomes an image in HTML.
        May be useful to make text unselectable
        or HTML text is not rendered properly.'''
        ...
    
    @render_text_as_image.setter
    def render_text_as_image(self, value: bool):
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets HTML page title.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...

    @property
    def save_full_font(self) -> bool:
        '''Indicates that full font will be saved, supports only True Type Fonts.
        By default SaveFullFont = false and the converter saves the subset of the initial font
        needed to display the text of the document.'''
        ...
    
    @save_full_font.setter
    def save_full_font(self, value: bool):
        ...
    
    @property
    def antialiasing_processing(self) -> None:
        '''This parameter defines required antialiasing measures during conversion of compound background images from PDF to HTML'''
        ...
    
    @antialiasing_processing.setter
    def antialiasing_processing(self, value: None):
        ...
    
    @property
    def save_transparent_texts(self) -> bool:
        '''Pdf can contain transparent texts that can be selected to clipboard (usually it happen when document contains images and OCRed texts extracted from it).
        This settings tells to converter whether we need save such texts as transparent
        selectable texts in result HTML'''
        ...
    
    @save_transparent_texts.setter
    def save_transparent_texts(self, value: bool):
        ...
    
    @property
    def save_shadowed_texts_as_transparent_texts(self) -> bool:
        '''Pdf can contain texts that are shadowed by another elements (f.e. by images) but
        can be selected to clipboard in Acrobat Reader (usually it happen when document contains images and OCRed texts extracted from it).
        This settings tells to converter whether we need save such texts as transparent
        selectable texts in result HTML to mimic behaviour of Acrobat Reader (othervise such texts are usually saved as hidden, not available for copying to clipboard)'''
        ...
    
    @save_shadowed_texts_as_transparent_texts.setter
    def save_shadowed_texts_as_transparent_texts(self, value: bool):
        ...
    
    @property
    def font_saving_mode(self) -> None:
        '''Defines font saving mode that will be used during saving of PDF to desirable format'''
        ...
    
    @font_saving_mode.setter
    def font_saving_mode(self, value: None):
        ...
    
    @property
    def page_border_if_any(self) -> None:
        '''This attribute represents set of settings used for drawing border (if any)
        in result HTML document around area that represent source PDF page.
        In essence it concerns of showing of page's paper edges,
        not page border referenced in PDF page itself.'''
        ...
    
    @page_border_if_any.setter
    def page_border_if_any(self, value: None):
        ...
    
    @property
    def page_margin_if_any(self) -> None:
        '''This attribute represents set of extra page margin (if any)
        in result HTML document around area that represent source PDF page.'''
        ...
    
    @page_margin_if_any.setter
    def page_margin_if_any(self, value: None):
        ...
    
    @property
    def letters_positioning_method(self) -> None:
        '''Sets mode of positioning of letters in words in result HTML'''
        ...
    
    @letters_positioning_method.setter
    def letters_positioning_method(self, value: None):
        ...
    
    @property
    def exclude_font_name_list(self) -> list[str]:
        '''List of PDF embedded font names that not be embedded in HTML.'''
        ...
    
    @exclude_font_name_list.setter
    def exclude_font_name_list(self, value: list[str]):
        ...
    
    @property
    def special_folder_for_svg_images(self) -> str:
        '''Gets or sets path to directory to which must be saved only SVG-images if they
        are encountered during saving of document as HTML. If parameter is empty or null
        then SVG files(if any) wil be saved together with other image-files (near to output file)
        or in special folder for images (if it specified in SpecialImagesFolderIfAny option).
        It does not affect anything if CustomImageSavingStrategy
        property was successfully used to process relevant image file.'''
        ...
    
    @special_folder_for_svg_images.setter
    def special_folder_for_svg_images(self, value: str):
        ...
    
    @property
    def special_folder_for_all_images(self) -> str:
        '''Gets or sets path to directory to which must be saved any images if they
        are encountered during saving of document as HTML. If parameter is empty or null
        then image files(if any) wil be saved together with other files linked to HTML
        It does not affect anything if CustomImageSavingStrategy
        property was successfully used to process relevant image file.'''
        ...
    
    @special_folder_for_all_images.setter
    def special_folder_for_all_images(self, value: str):
        ...
    
    @property
    def css_class_names_prefix(self) -> str:
        '''When PDFtoHTML converter generates result CSSs, CSS class names
        (something like ".stl_01 {}" ... ".stl_NN {}) are generated
        and used in result CSS. This property allows forcibly set class name prefix
        For example, if You want that all class names start with 'my_prefix_'
        (i.e. were something like 'my_prefix_1' ... 'my_prefix_NNN' ) ,
        then just assign 'my_prefix_' to this property before conversion.
        If this property will stay untouched(i.e. null will be leaved as value ), then
        converter will generate class names itself
        (it wil be something like ".stl_01 {}" ... ".stl_NN {}")'''
        ...
    
    @css_class_names_prefix.setter
    def css_class_names_prefix(self, value: str):
        ...
    
    @property
    def parts_embedding_mode(self) -> None:
        '''It defines whether referenced files (HTML, Fonts,Images, CSSes)
        will be embedded into main HTML file or will be generated as apart binary entities'''
        ...
    
    @parts_embedding_mode.setter
    def parts_embedding_mode(self, value: None):
        ...
    
    @property
    def html_markup_generation_mode(self) -> None:
        '''Sometimes specific reqirments to generation of HTML markup are present.
        This parameter defines HTML preparing modes that can be used
        during conversion of PDF to HTML to match such specific requirments.'''
        ...
    
    @html_markup_generation_mode.setter
    def html_markup_generation_mode(self, value: None):
        ...
    
    @property
    def raster_images_saving_mode(self) -> None:
        '''Converted PDF can contain raster images
        This parameter defines how they should be handled
        during conversion of PDF to HTML'''
        ...
    
    @raster_images_saving_mode.setter
    def raster_images_saving_mode(self, value: None):
        ...
    
    @property
    def remove_empty_areas_on_top_and_bottom(self) -> bool:
        '''Defines whether in created HTML will be removed top and bottom empty area without any content (if any).'''
        ...
    
    @remove_empty_areas_on_top_and_bottom.setter
    def remove_empty_areas_on_top_and_bottom(self, value: bool):
        ...
    
    @property
    def font_encoding_strategy(self) -> None:
        '''Defines encoding special rule to tune PDF decoding for current document'''
        ...
    
    @font_encoding_strategy.setter
    def font_encoding_strategy(self, value: None):
        ...
    
    @property
    def pages_flow_type_depends_on_viewers_screen_size(self) -> bool:
        '''If attribute 'SplitOnPages=false', than whole HTML representing all input PDF pages will be
        put into one big result HTML file.
        This flag defines whether result HTML will be generated in such way
        that flow of areas that represent PDF pages in result HTML will depend
        on screen resolution of viewer.
        Suppose width of screen on viewer side is big enough to put 2 or more pages one near
        other in horizontal direction. If this flag set to true, then this opportunity
        will be used (as many pages will be shown  in horizontal direction one near another
        as it possible, then next horizontal group of pages will be shown under first one ).
        Otherwise pages will flow in such way: next page goes always under previous one.'''
        ...
    
    @pages_flow_type_depends_on_viewers_screen_size.setter
    def pages_flow_type_depends_on_viewers_screen_size(self, value: bool):
        ...
    
    @property
    def try_save_text_underlining_and_strikeouting_in_css(self) -> bool:
        '''PDF itself does not contain underlining markers for texts. It emulated with line situated under text.
        This option allows converter try guess that this or that line is a text's underlining
        and put this info into CSS instead of drawing of underlining graphically'''
        ...
    
    @try_save_text_underlining_and_strikeouting_in_css.setter
    def try_save_text_underlining_and_strikeouting_in_css(self, value: bool):
        ...
    

    class CssSavingInfo:
          '''This class represents set of data that related to custom saving of CSS  during conversion
          of PDF to HTML format'''
        
          @property
          def css_number(self) -> int:
              '''Set by converter.
              During conversion several CSS-files are created . This properties shows ordinal
              of saved CSS-file during conversion.
              It can be used in logic of custom code to decide how to process or where to save CSS content'''
              ...
    
          @css_number.setter
          def css_number(self, value: int):
              ...

          @property
          def supposed_url(self) -> str:
              '''Set by converter.
              Supposed file name that goes from converter to code of custom method
              Can be used in custom code to decide how to process or where to save content'''
              ...
    
          @supposed_url.setter
          def supposed_url(self, value: str):
              ...
  
          @property
          def content_stream(self) -> Any:
              '''Set by converter. Represents binary content of saved CSS.'''
              ...
    
          @content_stream.setter
          def content_stream(self, value: Any):
              ...


    class CssUrlRequestInfo:
          '''Represents set of data that related to request from converter to 
          custom code aimed to get desirable URL (or URL template)of subject CSS '''
        
          def __init__(self):
              ...
        
          @property
          def custom_processing_cancelled(self) -> bool:
              '''Should be set by custom code if it cannot or should not define URL that 
              will be used in generated HTML for referencing of that CSS.
              If it's 'true', then CSS file will be saved in standard way in standard place. '''
              ...
    
          @custom_processing_cancelled.setter
          def custom_processing_cancelled(self, value: bool):
              ...

      
    
    class HtmlImageSavingInfo(aspose.pdf.SaveOptions.ResourceSavingInfo):
          '''This class represents set of data that related to external resource image file's saving
          during PDF to HTML conversion.'''
        
          def __init__(self):
              ...

          @property
          def image_type(self) -> aspose.pdf.HtmlSaveOptions.HtmlImageType:
              '''Represents type of saved image referenced in HTML. Set by converter and can be used in custom code 
              to decide what should be done'''
              ...
    
          @image_type.setter
          def image_type(self, value: aspose.pdf.HtmlSaveOptions.HtmlImageType):
              ...

          @property
          def parent_type(self) -> aspose.pdf.HtmlSaveOptions.ImageParentTypes:
              '''Saved image can pertain to HTML itself or can be extracted from SVG embedded to HTML. 
              This property can tell to custom code what's that type of parent of processed image.  
              It set by converter and can be used in custom code to decide what should be done with that image 
              (f.e. custom code can decide where to save image or how it must be referenced in parent's content). '''
              ...
    
          @parent_type.setter
          def parent_type(self, value: aspose.pdf.HtmlSaveOptions.ImageParentTypes):
              ...
  
          @property
          def pdf_host_page_number(self) -> int:
              '''Tells to custom code to what page of original PDF document pertains saved image
              Since it's possible that will be saved not all pages of original document,
              this value tells us about host page number in original PDF. If original page number for some reason
              is inknown, it allways return 1'''
              ...
    
          @pdf_host_page_number.setter
          def pdf_host_page_number(self, value: int):
              ...

          @property
          def html_host_page_number(self) -> int:
              '''Tells to custom code to what page of generated set of HTML page-files pertains saved image.
              If splitting on pages turned off this value always contains '1' since in such case 
              Only one HTML page is generated.'''
              ...
    
          @html_host_page_number.setter
          def html_host_page_number(self, value: int):
              ...


    class HtmlPageMarkupSavingInfo:
          '''If SplitToPages property of HtmlSaveOptions, then several HTML-files (one HTML file per converted page)
          are created during conversion of PDF to HTML. 
          This class represents set of data  that related to custom saving of one HTML-page's markup 
          during conversion of PDF to HTML '''

          @property
          def supposed_file_name(self) -> str:
              '''Set by converter. Supposed file name that goes from converter to code of custom method
              Can be used in custom code to decide how to process or where to save content'''
              ...
    
          @supposed_file_name.setter
          def supposed_file_name(self, value: str):
              ...

          @property
          def content_stream(self) -> Any:
              '''Set by converter. Represents saved HTML as stream '''
              ...
    
          @content_stream.setter
          def content_stream(self, value: Any):
              ...
  
          @property
          def pdf_host_page_number(self) -> int:
              '''Set by converter. If SplitToPages property set, then several HTML-files(one HTML file per converted page)
              are created during conversion  created .
              This property tells to custom code from what page of original PDF was created saved HTML-markup.
              If original page number for some reason is inknown or SplitOnPages=false,then this property allways contains '0'
              that signals that converter cannot supply exact original PDF's page number for supplied HTML-markup file.'''
              ...
    
          @pdf_host_page_number.setter
          def pdf_host_page_number(self, value: int):
              ...

          @property
          def html_host_page_number(self) -> int:
              '''Set by converter. If set SplitToPages property, then several HTML-files(one HTML file per converted page)
              are created during conversion  created . This property contains ordinal of saved HTML page's file.
              The property can be used in logic of custom code to decide how to process or where to save HTML page and 
              If splitting on pages turned off this value always contains '1'
              since in such case  only one big HTML page is generated for whole source document.'''
              ...
    
          @html_host_page_number.setter
          def html_host_page_number(self, value: int):
              ...

          @property
          def custom_processing_cancelled(self) -> bool:
              '''Should be set in custom code when necessary. This flag must be set to "true" in custom code if for some reasons
              supplied html-markup should be processed not with custom code but with converter's code itself in standard for converter way. 
              So, setting if this flag in custom code  means that custom code did not process referenced file and 
              converter must handle it itself'''
              ...
    
          @custom_processing_cancelled.setter
          def custom_processing_cancelled(self, value: bool):
              ...
  
        
    class AntialiasingProcessingType:
          '''This enum describes possible antialiasing measures during conversion.'''

          NO_ADDITIONAL_PROCESSING: AntialiasingProcessingType
          TRY_CORRECT_RESULT_HTML: AntialiasingProcessingType

    class FontEncodingRules:
          '''This enumeration defines rules which tune encoding logic'''

          DEFAULT: FontEncodingRules
          DECREASE_TO_UNICODE_PRIORITY_LEVEL: FontEncodingRules

    class FontSavingModes:
          '''Enumerates modes that can be used for saving of fonts referenced in saved PDF. '''

          ALWAYS_SAVE_AS_WOFF: FontSavingModes
          ALWAYS_SAVE_AS_TTF: FontSavingModes
          ALWAYS_SAVE_AS_EOT: FontSavingModes
          SAVE_IN_ALL_FORMATS: FontSavingModes 
          DONT_SAVE: FontSavingModes

    class HtmlImageType:
          '''Enumerates possible types of image files that can be saved as external resources during Pdf to Html conversion.'''

          JPEG: HtmlImageType
          PNG: HtmlImageType
          BMP: HtmlImageType
          GIF: HtmlImageType
          TIFF: HtmlImageType
          SVG: HtmlImageType
          ZIPPED_SVG: HtmlImageType
          UNKNOWN: HtmlImageType

    class HtmlMarkupGenerationModes:
          '''Sometimes specific reqirments to created HTML are present.This enum defines HTML preparing modes that can be used during conversion of PDF to HTML to match such specific requirments.'''

          WRITE_ALL_HTML: HtmlMarkupGenerationModes
          WRITE_ONLY_BODY_CONTENT: HtmlMarkupGenerationModes

    class ImageParentTypes:
          '''Enumerates possible types of image's parents. Image can pertain to HTML page or to SVG parent image'''

          HTML_PAGE: ImageParentTypes
          SVG_IMAGE: ImageParentTypes

    class LettersPositioningMethods:
          '''It enumerates possible modes of positioning of letters in words in result HTML.'''

          USE_EM_UNITS_AND_COMPENSATION_OF_ROUNDING_ERRORS_IN_CSS: LettersPositioningMethods
          USE_PIXEL_UNITS_IN_CSS_LETTER_SPACING_FOR_IE: LettersPositioningMethods

    class PartsEmbeddingModes:
          '''This enum enumerates possible modes of embedding of files referenced in HTML
          It allows to control whether referenced files (HTML, Fonts,Images, CSSes)
          will be embedded into main HTML file or will be generated as apart binary entities.'''

          EMBED_ALL_INTO_HTML: PartsEmbeddingModes
          EMBED_CSS_ONLY: PartsEmbeddingModes
          NO_EMBEDDING: PartsEmbeddingModes

    class RasterImagesSavingModes:
          '''Converted PDF can contain raster images(.png, *.jpeg etc.)
          This enum defines methods of how raster images can be handled during conversion of PDF to HTML'''

          AS_PNG_IMAGES_EMBEDDED_INTO_SVG: RasterImagesSavingModes
          AS_EXTERNAL_PNG_FILES_REFERENCED_VIA_SVG: RasterImagesSavingModes
          AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND: RasterImagesSavingModes

    ...

class Hyperlink:
    '''Represents abstract hyperlink.'''
    
    ...

class IColorSpaceConversionStrategy:
    '''Interface for color space conversion strategies.'''
    
    def convert(self, page: aspose.pdf.Page) -> None:
        '''Converts the page of document.
        
        :param page: The page of document.'''
        ...
    
    ...

class IIndexBitmapConverter:
    '''This interface declared for customization algorithms of quantization.
    Users can implement their own realization of this algorithms (for example algorithms based on unmanaged code).'''
    
    def get_1_bpp_image(self, src: aspose.pydrawing.Bitmap) -> aspose.pydrawing.Bitmap:
        '''Returns 1Bpp bitmap representation
        
        :param src: Source bitmap.
        :returns: Bitmap in 1 bpp image format.'''
        ...
    
    def get_4_bpp_image(self, src: aspose.pydrawing.Bitmap) -> aspose.pydrawing.Bitmap:
        '''Returns 4Bpp bitmap representation
        
        :param src: Source bitmap.
        :returns: Bitmap in 4 bpp image format.'''
        ...
    
    def get_8_bpp_image(self, src: aspose.pydrawing.Bitmap) -> aspose.pydrawing.Bitmap:
        '''Returns 8Bpp bitmap representation
        
        :param src: Source bitmap.
        :returns: Bitmap in 8 bpp image format.'''
        ...
    
    ...

class INamedDestinationCollection:
    '''Collection of Named Destinations.'''
    
    def remove(self, name: str) -> None:
        '''Removes destination by its name.
        
        :param name: Name value.'''
        ...
    
    def add(self, name: str, appointment: aspose.pdf.annotations.IAppointment) -> None:
        '''Adds new named destination.
        
        :param name: Name value.
        :param appointment: Appointment object.'''
        ...
    
    @property
    def count(self) -> int:
        '''Returns count of the destinations.'''
        ...
    
    @property
    def names(self) -> list[str]:
        '''Gets array of names of the destinations.'''
        ...
    
    ...

class IOperatorSelector:
    '''Defines Visitor for visiting different pdf operators.'''
    
    @overload
    def visit(self, f: aspose.pdf.operators.Fill) -> None:
        '''Visit/select f operator.
        
        :param f: Fill path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, f: aspose.pdf.operators.ObsoleteFill) -> None:
        '''Visit/select F operator.
        
        :param f: Fill path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, f_: aspose.pdf.operators.EOFill) -> None:
        '''Visit/select operator f\*.
        
        :param f_: Fill path operator (even-odd rule).'''
        ...
    
    @overload
    def visit(self, g: aspose.pdf.operators.SetGrayStroke) -> None:
        '''Visit/select G operator.
        
        :param g: Set gray level operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, g: aspose.pdf.operators.SetGray) -> None:
        '''Visit/select g operator.
        
        :param g: Set gray level operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, gs: aspose.pdf.operators.GS) -> None:
        '''Visit/select gs operator.
        
        :param gs: Set graphics state operator.'''
        ...
    
    @overload
    def visit(self, h: aspose.pdf.operators.ClosePath) -> None:
        '''Visit/select h operator.
        
        :param h: Close subpath operator.'''
        ...
    
    @overload
    def visit(self, i: aspose.pdf.operators.SetFlat) -> None:
        '''Visit/select i operator.
        
        :param i: Set flatness tolerance operator.'''
        ...
    
    @overload
    def visit(self, id: aspose.pdf.operators.ID) -> None:
        '''Visit/select ID operator.
        
        :param id: Begin inline image data operator.'''
        ...
    
    @overload
    def visit(self, ri: aspose.pdf.operators.SetColorRenderingIntent) -> None:
        '''Visit/select ri operator.
        
        :param ri: Set color rendering intent operator.'''
        ...
    
    @overload
    def visit(self, j: aspose.pdf.operators.SetLineCap) -> None:
        '''Visit/select J operator.
        
        :param j: Set line cap style operator.'''
        ...
    
    @overload
    def visit(self, m: aspose.pdf.operators.SetMiterLimit) -> None:
        '''Visit/select M operator.
        
        :param m: Set miter limit operator.'''
        ...
    
    @overload
    def visit(self, mp: aspose.pdf.operators.MP) -> None:
        '''Visit/select MP operator.
        
        :param mp: Define marked-content point operator.'''
        ...
    
    @overload
    def visit(self, n: aspose.pdf.operators.EndPath) -> None:
        '''Visit/select n operator.
        
        :param n: End path operator (without filling or stroking).'''
        ...
    
    @overload
    def visit(self, q: aspose.pdf.operators.GSave) -> None:
        '''Visit/select q operator.
        
        :param q: Save graphics state operator.'''
        ...
    
    @overload
    def visit(self, q: aspose.pdf.operators.GRestore) -> None:
        '''Visit/select Q operator.
        
        :param q: Restore graphics state operator.'''
        ...
    
    @overload
    def visit(self, re: aspose.pdf.operators.Re) -> None:
        '''Visit/select re operator.
        
        :param re: Append rectangle to path operator.'''
        ...
    
    @overload
    def visit(self, rg: aspose.pdf.operators.SetRGBColorStroke) -> None:
        '''Visit/select RG operator.
        
        :param rg: Set RGB color operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, rg: aspose.pdf.operators.SetRGBColor) -> None:
        '''Visit/select rg operator.
        
        :param rg: Set RGB color operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, k: aspose.pdf.operators.SetCMYKColorStroke) -> None:
        '''Visit/select K operator.
        
        :param k: Set CMYK color operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, k: aspose.pdf.operators.SetCMYKColor) -> None:
        '''Visit/select k operator.
        
        :param k: Set CMYK color operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, l: aspose.pdf.operators.LineTo) -> None:
        '''Visit/select l operator.
        
        :param l: Append straight line segment to path operator.'''
        ...
    
    @overload
    def visit(self, m: aspose.pdf.operators.MoveTo) -> None:
        '''Visit/select m operator.
        
        :param m: Begin new subpath operator.'''
        ...
    
    @overload
    def visit(self, tw: aspose.pdf.operators.SetWordSpacing) -> None:
        '''Visit/select Tw operator.
        
        :param tw: Set word spacing operator.'''
        ...
    
    @overload
    def visit(self, s: aspose.pdf.operators.ClosePathStroke) -> None:
        '''Visit/select s operator.
        
        :param s: Close and stroke path operator.'''
        ...
    
    @overload
    def visit(self, td: aspose.pdf.operators.MoveTextPositionSetLeading) -> None:
        '''Visit/select TD operator.
        
        :param td: Move text position and set leading operator.'''
        ...
    
    @overload
    def visit(self, tf: aspose.pdf.operators.SelectFont) -> None:
        '''Visit/select Tf operator.
        
        :param tf: Set text font and size operator.'''
        ...
    
    @overload
    def visit(self, tj: aspose.pdf.operators.ShowText) -> None:
        '''Visit/select Tj operator.
        
        :param tj: Show text operator.'''
        ...
    
    @overload
    def visit(self, tj: aspose.pdf.operators.SetGlyphsPositionShowText) -> None:
        '''Visit/select TJ operator.
        
        :param tj: Show text operator (allowing individual glyph positioning).'''
        ...
    
    @overload
    def visit(self, tl: aspose.pdf.operators.SetTextLeading) -> None:
        '''Visit/select TL operator.
        
        :param tl: Set text leading operator.'''
        ...
    
    @overload
    def visit(self, tm: aspose.pdf.operators.SetTextMatrix) -> None:
        '''Visit/select Tm operator.
        
        :param tm: Set text matrix and text line matrix operator.'''
        ...
    
    @overload
    def visit(self, tr: aspose.pdf.operators.SetTextRenderingMode) -> None:
        '''Visit/select Tr operator.
        
        :param tr: Set text rendering mode operator.'''
        ...
    
    @overload
    def visit(self, ts: aspose.pdf.operators.SetTextRise) -> None:
        '''Visit/select Ts operator.
        
        :param ts: Set text rise operator.'''
        ...
    
    @overload
    def visit(self, s: aspose.pdf.operators.Stroke) -> None:
        '''Visit/select S operator.
        
        :param s: Stroke path operator.'''
        ...
    
    @overload
    def visit(self, sc: aspose.pdf.operators.SetColorStroke) -> None:
        '''Visit/select SC operator.
        
        :param sc: Set color operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, sc: aspose.pdf.operators.SetColor) -> None:
        '''Visit/select sc operator.
        
        :param sc: Set color operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, scn: aspose.pdf.operators.SetAdvancedColorStroke) -> None:
        '''Visit/select SCN operator.
        
        :param scn: Set color operator (for stroking operations, ICCBasedand special colour spaces).'''
        ...
    
    @overload
    def visit(self, scn: aspose.pdf.operators.SetAdvancedColor) -> None:
        '''Visit/select scn operator.
        
        :param scn: Set color operator (for nonstroking operations, ICCBased and special colour spaces).'''
        ...
    
    @overload
    def visit(self, sh: aspose.pdf.operators.ShFill) -> None:
        '''Visit/select sh operator.
        
        :param sh: Paint area defined by shading pattern operator.'''
        ...
    
    @overload
    def visit(self, t_: aspose.pdf.operators.MoveToNextLine) -> None:
        '''Visit/select T\* operator.
        
        :param t_: Move to start of next text line operator.'''
        ...
    
    @overload
    def visit(self, tc: aspose.pdf.operators.SetCharacterSpacing) -> None:
        '''Visit/select Tc operator.
        
        :param tc: Set character spacing operator.'''
        ...
    
    @overload
    def visit(self, td: aspose.pdf.operators.MoveTextPosition) -> None:
        '''Visit/select Td operator.
        
        :param td: Move text position operator.'''
        ...
    
    @overload
    def visit(self, y: aspose.pdf.operators.CurveTo2) -> None:
        '''Visit/select y operator.
        
        :param y: Append curved segment to path operator (final point replicated).'''
        ...
    
    @overload
    def visit(self, w_: aspose.pdf.operators.EOClip) -> None:
        '''Visit/select W\* operator.
        
        :param w_: Set clipping path operator (even-odd rule).'''
        ...
    
    @overload
    def visit(self, tz: aspose.pdf.operators.SetHorizontalTextScaling) -> None:
        '''Visit/select Tz operator.
        
        :param tz: Set horizontal text scaling operator.'''
        ...
    
    @overload
    def visit(self, v: aspose.pdf.operators.CurveTo1) -> None:
        '''Visit/select v operator.
        
        :param v: Append curved segment to path operator (initial point replicated).'''
        ...
    
    @overload
    def visit(self, w: aspose.pdf.operators.Clip) -> None:
        '''Visit/select W operator.
        
        :param w: Set clipping path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, w: aspose.pdf.operators.SetLineWidth) -> None:
        '''Visit/select w operator.
        
        :param w: Set line width operator.'''
        ...
    
    @overload
    def visit(self, j: aspose.pdf.operators.SetLineJoin) -> None:
        '''Visit/select j operator.
        
        :param j: Set line join style operator.'''
        ...
    
    @overload
    def visit(self, ex: aspose.pdf.operators.EX) -> None:
        '''Visit/select EX operator.
        
        :param ex: End compatibility section operator.'''
        ...
    
    @overload
    def visit(self, et: aspose.pdf.operators.ET) -> None:
        '''Visit/select ET operator.
        
        :param et: End text object operator.'''
        ...
    
    @overload
    def visit(self, emc: aspose.pdf.operators.EMC) -> None:
        '''Visit/select EMC operator.
        
        :param emc: End marked-content sequence operator.'''
        ...
    
    @overload
    def visit(self, ei: aspose.pdf.operators.EI) -> None:
        '''Visit/select EI operator.
        
        :param ei: End inline image object operator.'''
        ...
    
    @overload
    def visit(self, dp: aspose.pdf.operators.DP) -> None:
        '''Visit/select DP operator.
        
        :param dp: Define marked-content point operator (with property list).'''
        ...
    
    @overload
    def visit(self, do: aspose.pdf.operators.Do) -> None:
        '''Visit/select Do operator.
        
        :param do: Invoke named XObject operator.'''
        ...
    
    @overload
    def visit(self, d: aspose.pdf.operators.SetDash) -> None:
        '''Visit/select d operator.
        
        :param d: Set line dash pattern operator.'''
        ...
    
    @overload
    def visit(self, d0: aspose.pdf.operators.SetCharWidth) -> None:
        '''Visit/select d0 operator.
        
        :param d0: Set glyph width in Type 3 font operator.'''
        ...
    
    @overload
    def visit(self, d1: aspose.pdf.operators.SetCharWidthBoundingBox) -> None:
        '''Visit/select d1 operator.
        
        :param d1: Set glyph width and bounding box in Type 3 font operator.'''
        ...
    
    @overload
    def visit(self, cs: aspose.pdf.operators.SetColorSpaceStroke) -> None:
        '''Visit/select CS operator.
        
        :param cs: Set color space operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, cs: aspose.pdf.operators.SetColorSpace) -> None:
        '''Visit/select cs operator.
        
        :param cs: Set color space operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, cm: aspose.pdf.operators.ConcatenateMatrix) -> None:
        '''Visit/select cm operator.
        
        :param cm: Concatenate matrix to current transformation matrix operator.'''
        ...
    
    @overload
    def visit(self, c: aspose.pdf.operators.CurveTo) -> None:
        '''Visit/select c operator.
        
        :param c: Append curved segment to path operator (three control points).'''
        ...
    
    @overload
    def visit(self, bx: aspose.pdf.operators.BX) -> None:
        '''Visit/select BX operator.
        
        :param bx: Begin compatibility section operator.'''
        ...
    
    @overload
    def visit(self, bt: aspose.pdf.operators.BT) -> None:
        '''Visit/select BT operator.
        
        :param bt: Begin text object operator.'''
        ...
    
    @overload
    def visit(self, bmc: aspose.pdf.operators.BMC) -> None:
        '''Visit/select BMC operator.
        
        :param bmc: Begin marked-content sequence operator.'''
        ...
    
    @overload
    def visit(self, bi: aspose.pdf.operators.BI) -> None:
        '''Visit/select BI operator.
        
        :param bi: Begin inline image object operator.'''
        ...
    
    @overload
    def visit(self, bdc: aspose.pdf.operators.BDC) -> None:
        '''Visit/select BDC operator.
        
        :param bdc: Begin marked-content sequence operator (with property list).'''
        ...
    
    @overload
    def visit(self, b: aspose.pdf.operators.FillStroke) -> None:
        '''Visit/select B operator.
        
        :param b: Fill and stroke path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, b: aspose.pdf.operators.ClosePathFillStroke) -> None:
        '''Visit/select b operator.
        
        :param b: Close, fill, and stroke path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, b_: aspose.pdf.operators.EOFillStroke) -> None:
        '''Visit/select B\* operator.
        
        :param b_: Fill and stroke path operator (even-odd rule).'''
        ...
    
    @overload
    def visit(self, b_: aspose.pdf.operators.ClosePathEOFillStroke) -> None:
        '''Visit/select b\* operator.
        
        :param b_: Close, fill, and stroke path operator (even-odd rule).'''
        ...
    
    @overload
    def visit(self, text_operator: aspose.pdf.operators.TextOperator) -> None:
        '''Visit/select any text operator operator.
        
        :param text_operator: General text operator which is used to select the set of corresponding pdf operators.'''
        ...
    
    ...

class IPageSetOptions:
    '''Defines conversion options related to a set of pages to convert.'''
    
    @property
    def explicit_list_of_saved_pages(self) -> list[int]:
        '''Specifies the array of numbers of pages to convert.'''
        ...
    
    @explicit_list_of_saved_pages.setter
    def explicit_list_of_saved_pages(self, value: list[int]):
        ...
    
    ...

class IPipelineOptions:
    '''Defines conversion options related to pipeline configuration.'''
    
    @property
    def batch_size(self) -> int:
        '''Specifies the size of a portion of pages to pass from node to node.'''
        ...
    
    @batch_size.setter
    def batch_size(self, value: int):
        ...
    
    ...

class ITeXInputDirectory:
    '''Interface of generalized TeX input directory.'''
    
    def get_file(self, file_name: str, full_name: str, search_subdirectories: bool) -> Any:
        '''Returns the stream to read from or to write to.
        
        :param file_name: The file name.
        :param full_name: The full file name.
        :param search_subdirectories: Indicates whether to look for a file in subdirectories.
        :returns: The stream.'''
        ...
    
    ...

class ITeXOutputDirectory:
    '''Interface of generalized TeX output directory.'''
    
    def get_output_file(self, file_name: str, full_name: str) -> Any:
        '''Returns the stream to write to.
        
        :param file_name: The file name.
        :param full_name: The full file name.
        :returns: The stream.'''
        ...
    
    ...

class IWarningCallback:
    '''Interface for user's callback mechanism support.'''
    
    def warning(self, warning: aspose.pdf.WarningInfo) -> aspose.pdf.ReturnAction:
        '''The callback method for some program notifications.
        
        :param warning: the warning information for some happened warning
        :returns: the result of further program workflow'''
        ...
    
    ...

class Id:
    '''Represents file identifier structure.'''
    
    @property
    def original(self) -> str:
        '''Permanent identifier based on the contents of the document at the time it was originally created.'''
        ...
    
    @property
    def modified(self) -> str:
        '''Changing identifier based on the document's contents at the time it was last updated.'''
        ...
    
    ...

class Image(aspose.pdf.BaseParagraph):
    '''Represents image.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> object:
        '''Clone the image.
        
        :returns: The cloned object'''
        ...
    
    @staticmethod
    def get_mime_type(self, i: aspose.pydrawing.Image) -> str:
        '''Returns mime type for image.
        
        :param i: Image object.
        :returns: Mime type as string if found; otherwise, "image/unknown" value.'''
        ...
    
    @property
    def file(self) -> str:
        '''Gets or sets the image file.'''
        ...
    
    @file.setter
    def file(self, value: str):
        ...

    @property
    def bitmap_size(self) -> aspose.pdf.Rectangle:
        '''Gets the image bitmap size.'''
        ...

    @property
    def fix_width(self) -> float:
        '''Gets or sets the image width.'''
        ...
    
    @fix_width.setter
    def fix_width(self, value: float):
        ...
    
    @property
    def fix_height(self) -> float:
        '''Gets or sets the image height.'''
        ...
    
    @fix_height.setter
    def fix_height(self, value: float):
        ...
    
    @property
    def file_type(self) -> aspose.pdf.ImageFileType:
        '''Gets or sets the image file type.'''
        ...
    
    @file_type.setter
    def file_type(self, value: aspose.pdf.ImageFileType):
        ...
    
    @property
    def image_scale(self) -> float:
        '''Gets or sets the image scale.'''
        ...
    
    @image_scale.setter
    def image_scale(self, value: float):
        ...
    
    @property
    def image_stream(self) -> Any:
        '''Gets or sets the image stream.'''
        ...
    
    @image_stream.setter
    def image_stream(self, value: Any):
        ...
    
    @property
    def is_apply_resolution(self) -> bool:
        '''Gets or sets a bool value that indicates whether the image use resolution during generation'''
        ...
    
    @is_apply_resolution.setter
    def is_apply_resolution(self, value: bool):
        ...
    
    @property
    def is_black_white(self) -> bool:
        '''Gets or sets a bool value that indicates whether the image is forced to be black-and-white. If TIFF
        image of CCITT subformat is used, this property must be set to true.'''
        ...
    
    @is_black_white.setter
    def is_black_white(self, value: bool):
        ...
    
    @property
    def title(self) -> aspose.pdf.text.TextFragment:
        '''Gets or sets a string value that indicates the title of the image.'''
        ...
    
    @title.setter
    def title(self, value: aspose.pdf.text.TextFragment):
        ...
    
    ...

class ImagePlacement:
    '''Represents characteristics of an image placed to Pdf document page.
    
    When an image is placed to a page it may have dimensions other than physical dimensions defined in :class:`Resources`.
    The object :class:`ImagePlacement` is intended to provide such information like dimensions, resolution and so on.'''
    
    @overload
    def save(self, stream: Any) -> None:
        '''Saves image with corresponding transformations: scaling, rotation and resolution.
        
        :param stream: Stream where image will be saved'''
        ...
    
    @overload
    def save(self, stream: Any, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        '''Saves image with corresponding transformations: scaling, rotation and resolution.
        
        :param stream: Stream where image will be saved
        :param format: Format which will be used for image enconding.'''
        ...
    
    def hide(self) -> None:
        '''Delete image from the page.'''
        ...
    
    def replace(self, image: Any) -> None:
        '''Replace image in collection with another image.
        
        :param image: Stream containing image data.'''
        ...
    
    @property
    def matrix(self) -> aspose.pdf.Matrix:
        '''Current transformation matrix for this image.'''
        ...
    
    @property
    def rectangle(self) -> aspose.pdf.Rectangle:
        '''Gets rectangle of the Image.'''
        ...
    
    @property
    def operator(self) -> aspose.pdf.Operator:
        '''Operator used for displaying the image.'''
        ...
    
    @property
    def rotation(self) -> float:
        '''Gets rotation angle of the Image.'''
        ...
    
    @property
    def resolution(self) -> aspose.pdf.devices.Resolution:
        '''Gets resolution of the Image.'''
        ...
    
    @property
    def image(self) -> aspose.pdf.XImage:
        '''Gets related XImage resource object.'''
        ...
    
    @property
    def page(self) -> aspose.pdf.Page:
        '''Gets the page containing the image.'''
        ...
    
    @property
    def compositing_parameters(self) -> aspose.pdf.CompositingParameters:
        '''Gets compositing parameters of graphics state active for the image placed to the page.'''
        ...
    
    ...

class ImagePlacementAbsorber:
    '''Represents an absorber object of image placement objects.
    Performs search of image usages and provides access to search results via :attr:`ImagePlacementAbsorber.image_placements` collection.
    
    The :class:`ImagePlacementAbsorber` object is basically used in images search scenario.
    When the search is completed the occurrences are represented with :class:`ImagePlacement` objects that the :attr:`ImagePlacementAbsorber.image_placements` collection contains.
    The :class:`ImagePlacement` object provides access to the image placement properties: dimensions, resolution etc.'''
    
    def __init__(self):
        ...
    
    @overload
    def visit(self, page: aspose.pdf.Page) -> None:
        '''Performs search on the specified page.
        
        :param page: Pdf pocument page object.'''
        ...
    
    @overload
    def visit(self, pdf: aspose.pdf.Document) -> None:
        '''Performs search on the specified document.
        
        :param pdf: Pdf pocument object.'''
        ...
    
    @property
    def is_read_only_mode(self) -> bool:
        '''Gets/sets read only mode for parsing operations collection. It may help against out of memory
        exceptions.'''
        ...
    
    @is_read_only_mode.setter
    def is_read_only_mode(self, value: bool):
        ...
    
    @property
    def image_placements(self) -> aspose.pdf.ImagePlacementCollection:
        '''Gets collection of image placement occurrences that are presented with :class:`ImagePlacement` objects.'''
        ...
    
    ...

class ImagePlacementCollection:
    '''Represents an image placements collection'''
    
    def __getitem__(self, index: int) -> aspose.pdf.ImagePlacement:
        '''Gets the text fragment element at the specified index.
        
        :param index: Index of image placement.
        :returns: ImagePlacement object.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets an object that can be used to synchronize access to the collection.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Gets a value indicating whether access to the collection is synchronized (thread safe).'''
        ...
    
    ...

class ImageStamp(aspose.pdf.Stamp):
    '''Reresents graphic stamp.'''
    
    @overload
    def __init__(self, image: Any):
        '''Initializes a new instance of the :class:`ImageStamp` class.
        
        :param image: Stream which contains image data.'''
        ...
    
    @overload
    def __init__(self, file_name: str):
        '''Creates image stamp by image in the specified file.
        
        :param file_name: Name of the file which contains image.'''
        ...
    
    def put(self, page: aspose.pdf.Page) -> None:
        '''Adds graphic stamp on the page.
        
        :param page: Page for stamping.'''
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets image width. Setting this property allos to scal image horizontally.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets image height. Setting this image allows to scale image vertically.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def image(self) -> Any:
        '''Gets image stream used for stamping.'''
        ...
    
    @property
    def quality(self) -> int:
        '''Gets or sets quality of image stamp in percent. Valid values are 0..100%.'''
        ...
    
    @quality.setter
    def quality(self, value: int):
        ...

    @property
    def alternative_text(self) -> str:
        '''Gets or sets Alternative Text for image stamp.'''
        ...
    
    @alternative_text.setter
    def alternative_text(self, value: str):
        ...
    
    ...

class ImportOptions:
    '''ImportOptions type hold level of abstraction on individual import options.'''
    
    @property
    def import_format(self) -> aspose.pdf.ImportFormat:
        '''Import format.'''
        ...
    
    ...

class IncorrectCMapUsageException(RuntimeError):
    '''The exception that is thrown when font usage is incorrect.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`IncorrectCMapUsageException` class.
        
        :param message: The message.'''
        ...
    
    ...

class IncorrectFontUsageException(aspose.pdf.InvalidFileFormatException):
    '''The exception that is thrown when font usage is incorrect.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`IncorrectFontUsageException` class.
        
        :param message: The message.'''
        ...
    
    ...

class InvalidCgmFileFormatException(aspose.pdf.InvalidFileFormatException):
    '''The exception that is thrown when a Cgm file is invalid.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`InvalidCgmFileFormatException` class.'''
        ...
    
    @overload
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`InvalidCgmFileFormatException` class.
        
        :param message: The message.'''
        ...
    
    ...

class InvalidFileFormatException(aspose.pdf.PdfException):
    '''The exception that is thrown when a file is invalid.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`InvalidFileFormatException` class.'''
        ...
    
    @overload
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`InvalidFileFormatException` class.
        
        :param message: The message.'''
        ...
    
    ...

class InvalidFormTypeOperationException(RuntimeError):
    '''The exception that is thrown when an operation with form type is not valid.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`InvalidFormTypeOperationException` class.'''
        ...
    
    @overload
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`InvalidFormTypeOperationException` class.
        
        :param message: The message.'''
        ...
    
    ...

class InvalidPasswordException(aspose.pdf.PdfException):
    '''The exception that is thrown when invalid password is provided by user.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`InvalidPasswordException` class.
        
        :param message: The message.'''
        ...
    
    ...

class InvalidPdfFileFormatException(aspose.pdf.InvalidFileFormatException):
    '''The exception that is thrown when a pdf file is invalid.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`InvalidPdfFileFormatException` class.
        
        :param message: The message.'''
        ...
    
    ...

class InvalidValueFormatException(aspose.pdf.PdfException):
    '''Exception which thrown when requested value has incorrect format.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`InvalidValueFormatException` class.'''
        ...
    
    @overload
    def __init__(self, message: str):
        '''Constructor.
        
        :param message: Exception message.'''
        ...
    
    ...

class JavaScriptCollection:
    '''This class represents collection of JavaScript.'''
    
    def remove(self, key: str) -> bool:
        '''Removes JavaScript by its name.
        
        :param key: Key value.
        :returns: True - if javascript removed; otherwise, false.'''
        ...
    
    @property
    def keys(self) -> list[str]:
        '''List of keys in JavaScript collection.'''
        ...
    
    ...

class JavascriptExtensionsException(aspose.pdf.PdfException):
    '''The exception that is thrown on errors when working with JavascriptExtensions.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`JavascriptExtensionsException` class.
        
        :param message: The message.'''
        ...
    
    ...

class LaTeXSaveOptions(aspose.pdf.TeXSaveOptions):
    '''Save options for export to TeX format.'''
    
    def __init__(self):
        ...
    
    ...

class LatexFragment(aspose.pdf.TeXFragment):
    '''Represents TeX fragment.'''
    
    @overload
    def __init__(self, text: str):
        '''Initializes a new instance of the HtmlFragment class.
        
        :param text: The fragment text'''
        ...
    
    @overload
    def __init__(self, text: str, remove_indents: bool):
        '''Initializes a new instance of the HtmlFragment class.
        
        :param text: The fragment text
        :param remove_indents: Determines whether not to make indents while typesetting LaTeX fragment'''
        ...
    
    ...

class LatexLoadOptions(aspose.pdf.TeXLoadOptions):
    '''Represents options for loading/importing TeX file into PDF document.'''
    
    def __init__(self):
        ...
    
    ...

class Layer:
    '''Represents page layer.'''
    
    def __init__(self, id: str, name: str):
        '''Initializes a new instance of the :class:`Layer` class.
        
        :param id: The layer id
        :param name: The layer name'''
        ...
    
    def save(self, output_path: str) -> None:
        '''Saves the current layer to a PDF document.
        
        :param output_path: The file path where the PDF document will be saved.'''
        ...
    
    def flatten(self, cleanup_content_stream: bool) -> None:
        '''Flattens the specified layer.
        
        :param cleanup_content_stream: Specifies whether to remove optional content group markers from the content stream.
        
        Setting the  parameter to false speeds up the process of flattening.'''
        ...
    
    def lock(self) -> None:
        '''Locks the layer.'''
        ...
    
    def unlock(self) -> None:
        '''Unlocks the layer.'''
        ...
    
    def delete(self) -> None:
        '''Deletes the current layer from the PDF document.'''
        ...

    @property
    def name(self) -> str:
        '''Gets the layer name.'''
        ...
    
    @property
    def id(self) -> str:
        '''Gets the layer id.'''
        ...
    
    @property
    def contents(self) -> None:
        '''Gets the layer content.'''
        ...

    @property
    def locked(self) -> bool:
        '''Gets a value indicating whether the layer is locked.'''
        ...
    
    ...

class LevelFormat:
    '''Represents format of the table of contents.'''
    
    def __init__(self):
        ...
    
    @property
    def line_dash(self) -> aspose.pdf.text.TabLeaderType:
        '''Gets or sets TOC line dash.'''
        ...
    
    @line_dash.setter
    def line_dash(self, value: aspose.pdf.text.TabLeaderType):
        ...
    
    @property
    def margin(self) -> aspose.pdf.MarginInfo:
        '''Gets or sets a list level margin'''
        ...
    
    @margin.setter
    def margin(self, value: aspose.pdf.MarginInfo):
        ...
    
    @property
    def subsequent_lines_indent(self) -> float:
        '''Gets or sets a subsequent lines indent'''
        ...
    
    @subsequent_lines_indent.setter
    def subsequent_lines_indent(self, value: float):
        ...
    
    @property
    def text_state(self) -> aspose.pdf.text.TextState:
        '''Gets or sets a list level text state'''
        ...
    
    @text_state.setter
    def text_state(self, value: aspose.pdf.text.TextState):
        ...
    
    ...

class License:
    '''Provides methods to license the component.'''
    
    def __init__(self):
        ...
    
    @overload
    def set_license(self, license_name: str) -> None:
        '''Licenses the component.
        
        Tries to find the license in the following locations:
        
        1. Explicit path.
        
        2. The folder that contains the Aspose component assembly.
        
        3. The folder that contains the client's calling assembly.
        
        4. The folder that contains the entry (startup) assembly.
        
        5. An embedded resource in the client's calling assembly.
        
        **Note:** On the .NET Compact Framework, tries to find the license only in these locations:
        
        1. Explicit path.
        
        2. An embedded resource in the client's calling assembly.
        
        [Java]2. The folder that contains the Aspose component JAR file.
        
        3. The folder that contains the client's calling JAR file.
        
        :param license_name: Can be a full or short file name or name of an embedded resource.
                             Use an empty string to switch to evaluation mode.'''
        ...
    
    @overload
    def set_license(self, stream: Any) -> None:
        '''Licenses the component.
        
        :param stream: A stream that contains the license.
        
        Use this method to load a license from a stream.'''
        ...
    
    @property
    def embedded(self) -> bool:
        '''License number was added as embedded resource.'''
        ...
    
    @embedded.setter
    def embedded(self, value: bool):
        ...
    
    ...

class LoadOptions:
    '''LoadOptions type holds level of abstraction on individual load options'''
    
    @property
    def warning_handler(self) -> aspose.pdf.IWarningCallback:
        '''Callback to handle any warnings generated.
        The WarningHandler returns ReturnAction enum item specifying either Continue or Abort.
        Continue is the default action and the Load operation continues, however the user may also return Abort in which case the Load operation should cease.'''
        ...
    
    @warning_handler.setter
    def warning_handler(self, value: aspose.pdf.IWarningCallback):
        ...
    
    @property
    def load_format(self) -> aspose.pdf.LoadFormat:
        '''Represents file format which :class:`LoadOptions` describes.'''
        ...
    
    @property
    def disable_font_license_verifications(self) -> bool:
        '''Gets or sets flag to disable any license restrictions for all fonts while loading the file.
        When true, allows to execute operations with font that are prohibited by a license
        of this font, for example allows to embed a font into a PDF document even if license rules
        disable embedding for this font.
        By default false.
        
        Be careful when using this flag. When it is set it means that person who sets this flag,
        takes all responsibility of possible license/law violations on himself.
        So he takes it on it's own risk.
        It's strongly recommended to use this flag only when you are fully confident that you are not breaking
        the copyright law.'''
        ...
    
    @disable_font_license_verifications.setter
    def disable_font_license_verifications(self, value: bool):
        ...

    class ResourceLoadingResult:
          '''Result of custom loading of resource'''

          def __init__(self, data: Any):
              '''Creates instance of loading result.
              :param data: result of custom loading must be allways provided, it can be zero-length array if it's impossible to get any result'''
              ...
    
          @property
          def data(self) -> Any:
              '''Bynary data that loaded with custom loader - it must be set after loading.'''
              ...

          @property
          def encoding_if_known(self) -> Any:
              '''Sometimes encoding of resource is known after or during loading.
                 In such case  custom code can provide converter with that knowledge via 
                 this parameter. You can leave null in this parameter if encoding is unknown or does not matter.'''
              ...

          @property
          def mime_type_if_known(self) -> str:
              '''Sometimes knowledge about MIME type of loaded resource is usefull for converter
                 You can provide MIME type(if it'd known after loading) in this parameter. Please
                 leave parameter equal to null when MIME type unknown or it's not necessary to supply it.'''
              ...

          @property
          def loading_cancelled(self) -> bool:
              '''Sometimes for some reasons loading should not occure custom code. In such case 
                 please set this flag as True. In such case converter will try use internal default
                 resource loader to get that result(as it behave in situation when custom strategy not supplied).'''
              ...
    
    
    class MarginsAreaUsageModes:
          '''Represents mode of usage of margins area during conversion (like HTML, EPUB etc), defines treatement of instructions of imported format related to usage of margins.'''
          
          PUT_CONTENT_ON_MARGIN_AREA_IF_NECESSARY: MarginsAreaUsageModes
          NEVER_PUT_CONTENT_ON_MARGIN_AREA: MarginsAreaUsageModes

    class PageSizeAdjustmentModes:
          '''Represents mode of usage of page size during conversion.
          Formats (like HTML, EPUB etc), usually have float design, so, it allows to fit required pagesize.
          But sometimes content has specifies horizontal positions or size that 
          does not allow put content into required page size.
          In such case we can define what should be done in this case (i.e when size of content does not fit 
          required initial page size of result PDF document).'''

          NO_AJUSTMENT_ALLWAYS_USE_PREDEFINED_SIZE: PageSizeAdjustmentModes
          ENLARGE_REQUIRED_VIEWPORT_WIDTH_AND_DO_CONVERSION_AGAIN: PageSizeAdjustmentModes

    ...

class LocalHyperlink(aspose.pdf.Hyperlink):
    '''Represents local hyperlink object.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`LocalHyperlink` class.'''
        ...
    
    @overload
    def __init__(self, target: aspose.pdf.BaseParagraph):
        '''Initializes a new instance of the :class:`LocalHyperlink` class.
        
        :param target: Target paragraph.'''
        ...
    
    @property
    def target(self) -> aspose.pdf.BaseParagraph:
        '''Gets or sets the target paragraph.'''
        ...
    
    @target.setter
    def target(self, value: aspose.pdf.BaseParagraph):
        ...
    
    @property
    def target_page_number(self) -> int:
        '''Gets or sets the target page number.'''
        ...
    
    @target_page_number.setter
    def target_page_number(self, value: int):
        ...
    
    ...

class MarginInfo:
    '''This class represents a margin for different objects.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`MarginInfo` class.'''
        ...
    
    @overload
    def __init__(self, left: float, bottom: float, right: float, top: float):
        '''Constructor of Rectangle.
        
        :param left: Left margin.
        :param bottom: Bottom margin
        :param right: Right margin.
        :param top: Top margin.'''
        ...
    
    def clone(self) -> object:
        '''Clones a new :class:`MarginInfo` object.
        
        :returns: The new object.'''
        ...
    
    @property
    def left(self) -> float:
        '''Gets or sets a float value that indicates the left margin.'''
        ...
    
    @left.setter
    def left(self, value: float):
        ...
    
    @property
    def right(self) -> float:
        '''Gets or sets a float value that indicates the right margin.'''
        ...
    
    @right.setter
    def right(self, value: float):
        ...
    
    @property
    def top(self) -> float:
        '''Gets or sets a float value that indicates the top margin.'''
        ...
    
    @top.setter
    def top(self, value: float):
        ...
    
    @property
    def bottom(self) -> float:
        '''Gets or sets a float value that indicates the bottom margin.'''
        ...
    
    @bottom.setter
    def bottom(self, value: float):
        ...
    
    ...

class Matrix:
    '''Class represents transformation matrix.'''
    
    @overload
    def __init__(self):
        '''Constructor
        creates stanrard 1 to 1 matrix:
        [ A B C D E F ] = [ 1, 0, 0, 1, 0, 0]'''
        ...
    
    @overload
    def __init__(self, matrix_array: list[float]):
        '''Constructor
        accepts a matrix with following array representation:
        [ A B C D E F ]
        
        :param matrix_array: Matrix data array.'''
        ...
    
    @overload
    def __init__(self, matrix_array: list[float]):
        '''Constructor
        accepts a matrix with following array representation:
        [ A B C D E F ]
        
        :param matrix_array: Matrix data array.'''
        ...
    
    @overload
    def __init__(self, matrix: aspose.pdf.Matrix):
        '''Constructor
        accepts a matrix to create a copy
        
        :param matrix: Matrix object.'''
        ...
    
    @overload
    def __init__(self, a: float, b: float, c: float, d: float, e: float, f: float):
        '''Initializes transformation matrix with specified coefficients.
        
        :param a: A matrix value.
        :param b: B matrix value.
        :param c: C matrix value.
        :param d: D matrix value.
        :param e: E matrix value.
        :param f: F matrix value.'''
        ...
    
    @overload
    @staticmethod
    def rotation(self, alpha: float) -> aspose.pdf.Matrix:
        '''Creates matrix for given rotation angle.
        
        :param alpha: Rotation angle in radians.
        :returns: Transformation matrix.'''
        ...
    
    @overload
    @staticmethod
    def rotation(self, rotation: aspose.pdf.Rotation) -> aspose.pdf.Matrix:
        '''Creates matrix for given rotation.
        
        :param rotation: Rotation. Valid values are: None, on90, on180, on270
        :returns: Matrix with rotation.'''
        ...
    
    @overload
    def transform(self, p: aspose.pdf.Point) -> aspose.pdf.Point:
        '''Transforms point using this matrix.
        
        :param p: Point which will be transformed.
        :returns: Transformation result.'''
        ...
    
    @overload
    def transform(self, rect: aspose.pdf.Rectangle) -> aspose.pdf.Rectangle:
        '''Transformes rectangle.
        If angle is not 90 \* N degrees then bounding rectangle is returned.
        
        :param rect: Rectangle to be transformed.
        :returns: Transformed rectangle.'''
        ...
    
    @staticmethod
    def skew(self, alpha: float, beta: float) -> aspose.pdf.Matrix:
        '''Creates matrix for given rotation angle.
        
        :param alpha: Skew x angle in radians.
        :param beta: Skew y angle in radians.
        :returns: Transformation matrix.'''
        ...
    
    def scale(self, x: float, y: float, x1, y1) -> None:
        '''Scales x and y with the matrix using the following formula:
        x1 = A\*x + C\*y;
        y1 = B\*x + D\*y;
        
        :param x: Input X coordinate
        :param y: Input Y coordinate
        :param x1: Output X coordinate
        :param y1: Output Y coordinate'''
        ...

    @overload
    @staticmethod
    def scale(self, sx: float, sy: float, source: aspose.pdf.Matrix) -> aspose.pdf.Matrix:
        '''Applies scaling to the given matrix.
        
        :param sx: The scaling factor for the X-axis.
        :param sy: The scaling factor for the Y-axis.
        :param source: The matrix to scale.
        :returns: A new matrix that is the result of scaling the source matrix.'''
        ...
    
    def un_scale(self, x1: float, y1: float, x, y) -> None:
        '''Scales back x1 and y1 and returns x and y before the matrix transformation using the following formula:
        x = (D \* x1 - C \* y1) / (A \* D - C \* B);
        y = (A\* y1 - B\* x1) / (A\* D - C\* B);
        
        :param x1: Input X coordinate
        :param y1: Input Y coordinate
        :param x: Output X coordinate
        :param y: Output Y coordinate'''
        ...

    @staticmethod
    def get_angle(self, rotation: aspose.pdf.Rotation) -> float:
        '''Transaltes rotation into angle (degrees)
        
        :param rotation: Rotation value.
        :returns: Angle value.'''
        ...
    
    def multiply(self, other: aspose.pdf.Matrix) -> aspose.pdf.Matrix:
        '''Multiplies the matrix by other matrix.
        
        :param other: Multiplier matrix.
        :returns: Result of multiplication.'''
        ...
    
    def add(self, other: aspose.pdf.Matrix) -> aspose.pdf.Matrix:
        '''Adds matrix to other matrix.
        
        :param other: Matrix to be added.
        :returns: Result of matrix add.'''
        ...
    
    def reverse(self) -> aspose.pdf.Matrix:
        '''Calculates reverse matrix.
        
        :returns: Reverse matrix.'''
        ...
    
    @staticmethod
    def translate(self, dx: float, dy: float, source: aspose.pdf.Matrix) -> aspose.pdf.Matrix:
        '''Translates a matrix by the specified amount in the x and y direction.
        
        :param dx: The amount to translate in the x direction.
        :param dy: The amount to translate in the y direction.
        :param source: The matrix to translate.
        :returns: A new matrix that is the result of the translation.'''
        ...

    @property
    def data(self) -> list[float]:
        '''Gets data of Matrix as array.'''
        ...
    
    @property
    def a(self) -> float:
        '''A member of the transformation matrix.'''
        ...
    
    @a.setter
    def a(self, value: float):
        ...
    
    @property
    def b(self) -> float:
        '''B member of the transformation matrix.'''
        ...
    
    @b.setter
    def b(self, value: float):
        ...
    
    @property
    def c(self) -> float:
        '''C member of the transformation matrix.'''
        ...
    
    @c.setter
    def c(self, value: float):
        ...
    
    @property
    def d(self) -> float:
        '''D member of the transformation matrix.'''
        ...
    
    @d.setter
    def d(self, value: float):
        ...
    
    @property
    def e(self) -> float:
        '''E member of the transformation matrix.'''
        ...
    
    @e.setter
    def e(self, value: float):
        ...
    
    @property
    def f(self) -> float:
        '''F member of the transformation matrix.'''
        ...
    
    @f.setter
    def f(self, value: float):
        ...
    
    @property
    def elements(self) -> list[float]:
        '''Elements of the matrix.'''
        ...
    
    ...

class Matrix3D:
    '''Class represents transformation matrix.'''
    
    @overload
    def __init__(self):
        '''Constructor
        creates standard 1 to 1 matrix:
        [ A B C D E F G H I Tx Ty Tz] = [ 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0 , 0]'''
        ...
    
    @overload
    def __init__(self, matrix_3d_array: list[float]):
        '''Constructor
        accepts a matrix with following array representation:
        [ A B C D E F G H I Tx Ty Tz]
        
        :param matrix_3d_array: Matrix data array.'''
        ...
    
    @overload
    def __init__(self, matrix: aspose.pdf.Matrix3D):
        '''Constructor
        accepts a matrix to create a copy
        
        :param matrix: Matrix3D object.'''
        ...
    
    @overload
    def __init__(self, a: float, b: float, c: float, d: float, e: float, f: float, g: float, h: float, i: float, tx: float, ty: float, tz: float):
        '''Initializes transformation matrix with specified coefficients.
        
        :param a: A matrix value.
        :param b: B matrix value.
        :param c: C matrix value.
        :param d: D matrix value.
        :param e: E matrix value.
        :param f: F matrix value.
        :param g: G matrix value.
        :param h: H matrix value.
        :param i: I matrix value.
        :param tx: TX matrix value.
        :param ty: TY matrix value.
        :param tz: TZ matrix value.'''
        ...
    
    @staticmethod
    def get_angle(self, rotation: aspose.pdf.Rotation) -> float:
        '''Translates rotation into angle (degrees)
        
        :param rotation: Rotation value.
        :returns: Angle value.'''
        ...
    
    def add(self, other: aspose.pdf.Matrix3D) -> aspose.pdf.Matrix3D:
        '''Adds matrix to other matrix.
        
        :param other: Matrix to be added.
        :returns: Result of matrix add.'''
        ...
    
    @property
    def a(self) -> float:
        '''A member of the transformation matrix.'''
        ...
    
    @a.setter
    def a(self, value: float):
        ...
    
    @property
    def b(self) -> float:
        '''B member of the transformation matrix.'''
        ...
    
    @b.setter
    def b(self, value: float):
        ...
    
    @property
    def c(self) -> float:
        '''C member of the transformation matrix.'''
        ...
    
    @c.setter
    def c(self, value: float):
        ...
    
    @property
    def d(self) -> float:
        '''D member of the transformation matrix.'''
        ...
    
    @d.setter
    def d(self, value: float):
        ...
    
    @property
    def e(self) -> float:
        '''E member of the transformation matrix.'''
        ...
    
    @e.setter
    def e(self, value: float):
        ...
    
    @property
    def f(self) -> float:
        '''F member of the transformation matrix.'''
        ...
    
    @f.setter
    def f(self, value: float):
        ...
    
    @property
    def g(self) -> float:
        '''G member of the transformation matrix.'''
        ...
    
    @g.setter
    def g(self, value: float):
        ...
    
    @property
    def h(self) -> float:
        '''H member of the transformation matrix.'''
        ...
    
    @h.setter
    def h(self, value: float):
        ...
    
    @property
    def i(self) -> float:
        '''I member of the transformation matrix.'''
        ...
    
    @i.setter
    def i(self, value: float):
        ...
    
    @property
    def tx(self) -> float:
        '''Tx member of the transformation matrix.'''
        ...
    
    @tx.setter
    def tx(self, value: float):
        ...
    
    @property
    def ty(self) -> float:
        '''Ty member of the transformation matrix.'''
        ...
    
    @ty.setter
    def ty(self, value: float):
        ...
    
    @property
    def tz(self) -> float:
        '''Tz member of the transformation matrix.'''
        ...
    
    @tz.setter
    def tz(self, value: float):
        ...
    
    ...

class MdLoadOptions(aspose.pdf.LoadOptions):
    '''Load options for Markdown format conversion.'''
    
    def __init__(self):
        ...

    @property
    def page_info(self) -> aspose.pdf.PageInfo:
        '''Gets or sets document page info'''
        ...
    
    @page_info.setter
    def page_info(self, value: aspose.pdf.PageInfo):
        ...
    
    @property
    def is_priority_css_page_rule(self) -> bool:
        '''Gets or sets the flag that specifies that @page rules defined in css will override values defined in PageInfo.'''
        ...
    
    @is_priority_css_page_rule.setter
    def is_priority_css_page_rule(self, value: bool):
        ...

    
    ...

class Metadata:
    '''Provides access to XMP metadata stream.'''
    
    @overload
    def register_namespace_uri(self, prefix: str, namespace_uri: str) -> None:
        '''Registers namespace URI.
        
        :param prefix: The value of prefix.
        :param namespace_uri: The value of namespace URI.'''
        ...
    
    @overload
    def register_namespace_uri(self, prefix: str, namespace_uri: str, schema_description: str) -> None:
        '''Registers namespace URI.
        
        :param prefix: The value of prefix.
        :param namespace_uri: The value of namespace URI.
        :param schema_description: The value of schema description.'''
        ...
    
    @overload
    def add(self, key: str, value: aspose.pdf.XmpValue) -> None:
        '''Adds value to metadata.
        
        :param key: The key to add.
        :param value: Value which will be added.'''
        ...
    
    @overload
    def add(self, key: str, value: object) -> None:
        '''Adds value to metadata.
        
        :param key: The key to add.
        :param value: Value which will be added.'''
        ...
    
    @overload
    def add(self, prefix: str, value: aspose.pdf.XmpPdfAExtensionObject) -> None:
        '''Adds pdf extension to metadata.
        
        :param prefix: The prefix of extension.
        :param value: Value which will be added.'''
        ...
    
    def get_namespace_uri_by_prefix(self, prefix: str) -> str:
        '''Returns  namespace URI by prefix.
        
        :param prefix: The value of prefix.
        :returns: The value of namespace URI.'''
        ...
    
    def get_prefix_by_namespace_uri(self, namespace_uri: str) -> str:
        '''Returns prefix by namespace URI.
        
        :param namespace_uri: Namespace URI.
        :returns: The value of prefix.'''
        ...
    
    def clear(self) -> None:
        '''Clears metadata.'''
        ...
    
    def contains(self, key: str) -> bool:
        '''Checks does key is contained in metadata.
        
        :param key: The key of entry to find.
        :returns: True if key is contained in the metadata.'''
        ...
    
    def remove(self, key: str) -> bool:
        '''Removes entry from metadata.
        
        :param key: The key of entry to remove.
        :returns: True - if key removed; otherwise, false.'''
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
    def is_fixed_size(self) -> bool:
        '''Checks if colleciton has fixed size.'''
        ...
    
    @property
    def is_read_only(self) -> bool:
        '''Checks if collection is read-only.'''
        ...
    
    @property
    def keys(self) -> None:
        '''Gets collection of metadata keys.'''
        ...
    
    @property
    def values(self) -> None:
        '''Gets values in the metadata.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets count of elements in the collection.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Checks if collection is synchronized.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets collection synchronization object.'''
        ...
    
    ...

class Metered:
    '''Provides methods to set metered key.'''
    
    def __init__(self):
        ...
    
    def set_metered_key(self, public_key: str, private_key: str) -> None:
        '''Sets metered public and private key.
        If you purchase metered license, when start application, this API should be called, normally, this is enough.
        However, if always fail to upload consumption data and exceed 24 hours, the license will be set to evaluation status,
        to avoid such case, you should regularly check the license status, if it is evaluation status, call this API again.
        
        :param public_key: public key
        :param private_key: private key'''
        ...
    
    @staticmethod
    def get_consumption_quantity(self) -> decimal.Decimal:
        '''Gets consumption file size
        
        :returns: consumption quantity'''
        ...
    
    @staticmethod
    def get_consumption_credit(self) -> decimal.Decimal:
        '''Gets consumption credit
        
        :returns: consumption quantity'''
        ...

    def get_product_name(self) -> str:
        '''Get the Product Name.
        
        :returns: Product Name'''
        ...
    
    @staticmethod
    def is_metered_licensed(self) -> bool:
        '''Check whether metered is licensed.
        
        :returns: True or false'''
        ...
    
    ...

class MhtLoadOptions(aspose.pdf.LoadOptions):
    '''Represents options for loading/importing of .mht-file into pdf document.'''
    
    def __init__(self):
        ...
    
    @property
    def page_info(self) -> aspose.pdf.PageInfo:
        '''Gets or sets document page info'''
        ...
    
    ...

class MobiXmlSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to Xml format'''
    
    def __init__(self):
        ...
    
    ...

class NamedDestinationCollection:
    '''Class represents the collection of all destinations (a name tree mapping name strings to destinations (see 12.3.2.3, "Named Destinations") and (see 7.7.4, "Name Dictionary")) in the pdf document.'''
    
    def remove(self, name: str) -> None:
        '''Delete named destination.
        
        :param name: Name of the destination to delete.'''
        ...
    
    def add(self, name: str, appointment: aspose.pdf.annotations.IAppointment) -> None:
        '''Add new named destination.
        
        :param name: Destination name.
        :param appointment: Appointment to add.'''
        ...
    
    @property
    def count(self) -> int:
        '''Count of named destinations.'''
        ...
    
    @property
    def names(self) -> list[str]:
        '''List of names of the destinations.'''
        ...
    
    ...

class Note:
    '''This class represents generator paragraph note.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`Note` class.'''
        ...
    
    @overload
    def __init__(self, content: str):
        '''Initializes a new instance of the :class:`Note` class.
        
        :param content: The note content.'''
        ...
    
    @property
    def paragraphs(self) -> aspose.pdf.Paragraphs:
        '''Gets or sets a collection that indicates all paragraphs in the FootNote.'''
        ...
    
    @paragraphs.setter
    def paragraphs(self, value: aspose.pdf.Paragraphs):
        ...
    
    @property
    def text(self) -> str:
        '''Gets or sets a note text.'''
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    @property
    def text_state(self) -> aspose.pdf.text.TextState:
        '''Gets or sets a note text state.'''
        ...
    
    @text_state.setter
    def text_state(self, value: aspose.pdf.text.TextState):
        ...
    
    ...

class OcspSettings:
    '''Represents the ocsp settings using during signing process.'''
    
    def __init__(self, server_url: str):
        '''Initializes a new instance of the :class:`OcspSettings` class.
        
        :param server_url: The ocsp server url.'''
        ...
    
    @property
    def server_url(self) -> str:
        '''Gets/sets the ocsp server url.'''
        ...
    
    @server_url.setter
    def server_url(self, value: str):
        ...
    
    ...

class OfdLoadOptions(aspose.pdf.LoadOptions):
    '''Load options for OFD format.'''
    
    def __init__(self):
        ...
    
    ...

class Operator:
    '''Abstract class representing operator.'''
    
    def accept(self, visitor: aspose.pdf.IOperatorSelector) -> None:
        '''Accepts visitor IOperatorSelector which provides operators processing.
        
        :param visitor: Visitor object'''
        ...
    
    def value_equals(self, op: aspose.pdf.Operator) -> bool:
        '''Compares this instance with the given object.
        
        :param op: Operator to compare.
        :returns: True if objects are equal, otherwise false.'''
        ...

    @staticmethod
    def is_text_show_operator(self, op: aspose.pdf.Operator) -> bool:
        '''Determines if the operator is operator which responsible for text output (Tj, TJ, etc)
        
        :param op: Operator object
        :returns: True if this is text output operator'''
        ...
    
    @property
    def index(self) -> int:
        '''Operator index in page operators list.'''
        ...
    
    @index.setter
    def index(self, value: int):
        ...
    
    ...

class OperatorCollection(aspose.pdf.BaseOperatorCollection):
    '''Class represents collection of operators'''
    
    def __getitem__(self, index: int) -> aspose.pdf.Operator:
        '''Gets operator by its index.
        
        :param index: Index of operator. Numbering is starts from 1.
        :returns: Operator from requested index'''
        ...
    
    def __setitem__(self, index: int, value: aspose.pdf.Operator):
        ...
    
    @overload
    def resume_update(self, update_all: bool) -> None:
        '''Resumes document update.
        Updates contents stream in case there are any pending changes.
        Marks all operators as "changed" if invalidate parameter is true.
        
        :param update_all: If true, all operators in the collection marked as updated.'''
        ...
    
    @overload
    def resume_update(self) -> None:
        '''Resumes document update.
        Updates contents stream in case there are any pending changes.'''
        ...
    
    @overload
    def insert(self, index: int, op: aspose.pdf.Operator) -> None:
        '''Inserts operator into collection.
        
        :param index: Index where new operator must be added
        :param op: Operator which will be insterted'''
        ...
    
    @overload
    def insert(self, at: int, ops: list[aspose.pdf.Operator]) -> None:
        '''Insert operators at the the given position.
        
        :param at: Index from which operators are being started to insert.
        :param ops: Array of operators to be inserted. Each operator can have any index (by default -1) because their indices adjusted automatically starting from at.'''
        ...
    
    @overload
    def insert(self, at: int, ops: list[aspose.pdf.Operator]) -> None:
        '''Insert operators at the the given position.
        
        :param at: Index from which operators are being started to insert.
        :param ops: Array of operators to be inserted.'''
        ...
    
    @overload
    def delete(self, index: int) -> None:
        '''Deletes operator from collection.
        
        :param index: Index of operator which must be deleted. Operators numbering starts from 1.'''
        ...
    
    @overload
    def delete(self, ops: list[aspose.pdf.Operator]) -> None:
        '''Deletes operators from collection.
        
        :param ops: Array of operators to delete'''
        ...
    
    @overload
    def delete(self, list: list[aspose.pdf.Operator]) -> None:
        '''Deletes operators from collection.
        
        :param list: The list of operators to delete'''
        ...
    
    @overload
    def add(self, ops: list[aspose.pdf.Operator]) -> None:
        '''Add operators at the end of the contents operators.
        
        :param ops: Array of operators to be added. Each operator can have any index (by default -1) because they come to the end of the contents operators i.e. indices are assigned automatically.'''
        ...
    
    @overload
    def add(self, ops) -> None:
        '''Adds to collection all operators from other collection.
        
        :param ops: collection whitch contains operators which will be added.'''
        ...
    
    def suppress_update(self) -> None:
        '''Suppresses update contents data.
        The contents stream is not updated until ResumeUpdate is called.'''
        ...
    
    def cancel_update(self) -> None:
        '''Cancels last update.
        This method may be called when the change should not raise contents update.'''
        ...
    
    def accept(self, visitor: aspose.pdf.IOperatorSelector) -> None:
        '''Accepts IOperatorSelector visitor object to process operators.
        
        :param visitor: Visitor object'''
        ...
    
    def replace(self, operators: list[aspose.pdf.Operator]) -> None:
        '''Replace operators in collection with other operators.
        
        :param operators: Operators list which will replace operators currently contained in the collection. Eash operator from the list must have correct index in range [1..N] where N is count of operators in the collection'''
        ...
    
    @property
    def is_fast_text_extraction_mode(self) -> bool:
        '''Indicates wheather collection is limited to fast text extraction'''
        ...
    
    ...

class OperatorSelector:
    '''This class is used for selecting operators using Visitor template idea.'''
    
    @overload
    def __init__(self):
        '''Initializes new instance of the :class:`OperatorSelector` class.'''
        ...
    
    @overload
    def __init__(self, op: aspose.pdf.Operator):
        '''Initializes new :class:`OperatorSelector`.
        
        :param op: The operator to visit/select.'''
        ...
    
    @overload
    def visit(self, j: aspose.pdf.operators.SetLineJoin) -> None:
        '''Visit/select j operator.
        
        :param j: Set line join style operator.'''
        ...
    
    @overload
    def visit(self, ex: aspose.pdf.operators.EX) -> None:
        '''Visit/select EX operator.
        
        :param ex: End compatibility section operator.'''
        ...
    
    @overload
    def visit(self, et: aspose.pdf.operators.ET) -> None:
        '''Visit/select ET operator.
        
        :param et: End text object operator.'''
        ...
    
    @overload
    def visit(self, emc: aspose.pdf.operators.EMC) -> None:
        '''Visit/select EMC operator.
        
        :param emc: End marked-content sequence operator.'''
        ...
    
    @overload
    def visit(self, ei: aspose.pdf.operators.EI) -> None:
        '''Visit/select EI operator.
        
        :param ei: End inline image object operator.'''
        ...
    
    @overload
    def visit(self, dp: aspose.pdf.operators.DP) -> None:
        '''Visit/select DP operator.
        
        :param dp: Define marked-content point operator (with property list).'''
        ...
    
    @overload
    def visit(self, do: aspose.pdf.operators.Do) -> None:
        '''Visit/select Do operator.
        
        :param do: Invoke named XObject operator.'''
        ...
    
    @overload
    def visit(self, d1: aspose.pdf.operators.SetCharWidthBoundingBox) -> None:
        '''Visit/select d1 operator.
        
        :param d1: Set glyph width and bounding box in Type 3 font operator.'''
        ...
    
    @overload
    def visit(self, d0: aspose.pdf.operators.SetCharWidth) -> None:
        '''Visit/select d0 operator.
        
        :param d0: Set glyph width in Type 3 font operator.'''
        ...
    
    @overload
    def visit(self, d: aspose.pdf.operators.SetDash) -> None:
        '''Visit/select d operator.
        
        :param d: Set line dash pattern operator.'''
        ...
    
    @overload
    def visit(self, cs: aspose.pdf.operators.SetColorSpaceStroke) -> None:
        '''Visit/select CS operator.
        
        :param cs: Set color space operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, cs: aspose.pdf.operators.SetColorSpace) -> None:
        '''Visit/select cs operator.
        
        :param cs: Set color space operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, cm: aspose.pdf.operators.ConcatenateMatrix) -> None:
        '''Visit/select cm operator.
        
        :param cm: Concatenate matrix to current transformation matrix operator.'''
        ...
    
    @overload
    def visit(self, c: aspose.pdf.operators.CurveTo) -> None:
        '''Visit/select c operator.
        
        :param c: Append curved segment to path operator (three control points).'''
        ...
    
    @overload
    def visit(self, bx: aspose.pdf.operators.BX) -> None:
        '''Visit/select BX operator.
        
        :param bx: Begin compatibility section operator.'''
        ...
    
    @overload
    def visit(self, bt: aspose.pdf.operators.BT) -> None:
        '''Visit/select BT operator.
        
        :param bt: Begin text object operator.'''
        ...
    
    @overload
    def visit(self, bmc: aspose.pdf.operators.BMC) -> None:
        '''Visit/select BMC operator.
        
        :param bmc: Begin marked-content sequence operator.'''
        ...
    
    @overload
    def visit(self, bi: aspose.pdf.operators.BI) -> None:
        '''Visit/select BI operator.
        
        :param bi: Begin inline image object operator.'''
        ...
    
    @overload
    def visit(self, bdc: aspose.pdf.operators.BDC) -> None:
        '''Visit/select BDC operator.
        
        :param bdc: Begin marked-content sequence operator (with property list).'''
        ...
    
    @overload
    def visit(self, b: aspose.pdf.operators.FillStroke) -> None:
        '''Visit/select B operator.
        
        :param b: Fill and stroke path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, b: aspose.pdf.operators.ClosePathFillStroke) -> None:
        '''Visit/select b operator.
        
        :param b: Close, fill, and stroke path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, b_: aspose.pdf.operators.EOFillStroke) -> None:
        '''Visit/select B\* operator.
        
        :param b_: Fill and stroke path operator (even-odd rule).'''
        ...
    
    @overload
    def visit(self, b_: aspose.pdf.operators.ClosePathEOFillStroke) -> None:
        '''Visit/select b\* operator.
        
        :param b_: Close, fill, and stroke path operator (even-odd rule).'''
        ...
    
    @overload
    def visit(self, f_: aspose.pdf.operators.EOFill) -> None:
        '''Visit/select operator f\*.
        
        :param f_: Fill path operator (even-odd rule).'''
        ...
    
    @overload
    def visit(self, f: aspose.pdf.operators.Fill) -> None:
        '''Visit/select f operator.
        
        :param f: Fill path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, f: aspose.pdf.operators.ObsoleteFill) -> None:
        '''Visit/select F operator.
        
        :param f: Fill path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, g: aspose.pdf.operators.SetGray) -> None:
        '''Visit/select g operator.
        
        :param g: Set gray level operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, g: aspose.pdf.operators.SetGrayStroke) -> None:
        '''Visit/select G operator.
        
        :param g: Set gray level operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, gs: aspose.pdf.operators.GS) -> None:
        '''Visit/select gs operator.
        
        :param gs: Set graphics state operator.'''
        ...
    
    @overload
    def visit(self, h: aspose.pdf.operators.ClosePath) -> None:
        '''Visit/select h operator.
        
        :param h: Close subpath operator.'''
        ...
    
    @overload
    def visit(self, i: aspose.pdf.operators.SetFlat) -> None:
        '''Visit/select i operator.
        
        :param i: Set flatness tolerance operator.'''
        ...
    
    @overload
    def visit(self, id: aspose.pdf.operators.ID) -> None:
        '''Visit/select ID operator.
        
        :param id: Begin inline image data operator.'''
        ...
    
    @overload
    def visit(self, j: aspose.pdf.operators.SetLineCap) -> None:
        '''Visit/select J operator.
        
        :param j: Set line cap style operator.'''
        ...
    
    @overload
    def visit(self, k: aspose.pdf.operators.SetCMYKColor) -> None:
        '''Visit/select k operator.
        
        :param k: Set CMYK color operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, k: aspose.pdf.operators.SetCMYKColorStroke) -> None:
        '''Visit/select K operator.
        
        :param k: Set CMYK color operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, l: aspose.pdf.operators.LineTo) -> None:
        '''Visit/select l operator.
        
        :param l: Append straight line segment to path operator.'''
        ...
    
    @overload
    def visit(self, m: aspose.pdf.operators.MoveTo) -> None:
        '''Visit/select m operator.
        
        :param m: Begin new subpath operator.'''
        ...
    
    @overload
    def visit(self, m: aspose.pdf.operators.SetMiterLimit) -> None:
        '''Visit/select M operator.
        
        :param m: Set miter limit operator.'''
        ...
    
    @overload
    def visit(self, mp: aspose.pdf.operators.MP) -> None:
        '''Visit/select MP operator.
        
        :param mp: Define marked-content point operator.'''
        ...
    
    @overload
    def visit(self, n: aspose.pdf.operators.EndPath) -> None:
        '''Visit/select n operator.
        
        :param n: End path operator (without filling or stroking).'''
        ...
    
    @overload
    def visit(self, q: aspose.pdf.operators.GSave) -> None:
        '''Visit/select q operator.
        
        :param q: Save graphics state operator.'''
        ...
    
    @overload
    def visit(self, q: aspose.pdf.operators.GRestore) -> None:
        '''Visit/select Q operator.
        
        :param q: Restore graphics state operator.'''
        ...
    
    @overload
    def visit(self, re: aspose.pdf.operators.Re) -> None:
        '''Visit/select re operator.
        
        :param re: Append rectangle to path operator.'''
        ...
    
    @overload
    def visit(self, rg: aspose.pdf.operators.SetRGBColor) -> None:
        '''Visit/select rg operator.
        
        :param rg: Set RGB color operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, rg: aspose.pdf.operators.SetRGBColorStroke) -> None:
        '''Visit/select RG operator.
        
        :param rg: Set RGB color operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, ri: aspose.pdf.operators.SetColorRenderingIntent) -> None:
        '''Visit/select ri operator.
        
        :param ri: Set color rendering intent operator.'''
        ...
    
    @overload
    def visit(self, s: aspose.pdf.operators.ClosePathStroke) -> None:
        '''Visit/select s operator.
        
        :param s: Close and stroke path operator.'''
        ...
    
    @overload
    def visit(self, s: aspose.pdf.operators.Stroke) -> None:
        '''Visit/select S operator.
        
        :param s: Stroke path operator.'''
        ...
    
    @overload
    def visit(self, sc: aspose.pdf.operators.SetColor) -> None:
        '''Visit/select sc operator.
        
        :param sc: Set color operator (for nonstroking operations).'''
        ...
    
    @overload
    def visit(self, sc: aspose.pdf.operators.SetColorStroke) -> None:
        '''Visit/select SC operator.
        
        :param sc: Set color operator (for stroking operations).'''
        ...
    
    @overload
    def visit(self, scn: aspose.pdf.operators.SetAdvancedColor) -> None:
        '''Visit/select scn operator.
        
        :param scn: Set color operator (for nonstroking operations, ICCBased and special colour spaces).'''
        ...
    
    @overload
    def visit(self, scn: aspose.pdf.operators.SetAdvancedColorStroke) -> None:
        '''Visit/select SCN operator.
        
        :param scn: Set color operator (for stroking operations, ICCBasedand special colour spaces).'''
        ...
    
    @overload
    def visit(self, sh: aspose.pdf.operators.ShFill) -> None:
        '''Visit/select sh operator.
        
        :param sh: Paint area defined by shading pattern operator.'''
        ...
    
    @overload
    def visit(self, t_: aspose.pdf.operators.MoveToNextLine) -> None:
        '''Visit/select T\* operator.
        
        :param t_: Move to start of next text line operator.'''
        ...
    
    @overload
    def visit(self, tc: aspose.pdf.operators.SetCharacterSpacing) -> None:
        '''Visit/select Tc operator.
        
        :param tc: Set character spacing operator.'''
        ...
    
    @overload
    def visit(self, td: aspose.pdf.operators.MoveTextPosition) -> None:
        '''Visit/select Td operator.
        
        :param td: Move text position operator.'''
        ...
    
    @overload
    def visit(self, td: aspose.pdf.operators.MoveTextPositionSetLeading) -> None:
        '''Visit/select TD operator.
        
        :param td: Move text position and set leading operator.'''
        ...
    
    @overload
    def visit(self, tf: aspose.pdf.operators.SelectFont) -> None:
        '''Visit/select Tf operator.
        
        :param tf: Set text font and size operator.'''
        ...
    
    @overload
    def visit(self, tj: aspose.pdf.operators.ShowText) -> None:
        '''Visit/select Tj operator.
        
        :param tj: Show text operator.'''
        ...
    
    @overload
    def visit(self, tj: aspose.pdf.operators.SetGlyphsPositionShowText) -> None:
        '''Visit/select TJ operator.
        
        :param tj: Show text operator (allowing individual glyph positioning).'''
        ...
    
    @overload
    def visit(self, tl: aspose.pdf.operators.SetTextLeading) -> None:
        '''Visit/select TL operator.
        
        :param tl: Set text leading operator.'''
        ...
    
    @overload
    def visit(self, tm: aspose.pdf.operators.SetTextMatrix) -> None:
        '''Visit/select Tm operator.
        
        :param tm: Set text matrix and text line matrix operator.'''
        ...
    
    @overload
    def visit(self, tr: aspose.pdf.operators.SetTextRenderingMode) -> None:
        '''Visit/select Tr operator.
        
        :param tr: Set text rendering mode operator.'''
        ...
    
    @overload
    def visit(self, ts: aspose.pdf.operators.SetTextRise) -> None:
        '''Visit/select Ts operator.
        
        :param ts: Set text rise operator.'''
        ...
    
    @overload
    def visit(self, tw: aspose.pdf.operators.SetWordSpacing) -> None:
        '''Visit/select Tw operator.
        
        :param tw: Set word spacing operator.'''
        ...
    
    @overload
    def visit(self, tz: aspose.pdf.operators.SetHorizontalTextScaling) -> None:
        '''Visit/select Tz operator.
        
        :param tz: Set horizontal text scaling operator.'''
        ...
    
    @overload
    def visit(self, v: aspose.pdf.operators.CurveTo1) -> None:
        '''Visit/select v operator.
        
        :param v: Append curved segment to path operator (initial point replicated).'''
        ...
    
    @overload
    def visit(self, w_: aspose.pdf.operators.EOClip) -> None:
        '''Visit/select W\* operator.
        
        :param w_: Set clipping path operator (even-odd rule).'''
        ...
    
    @overload
    def visit(self, w: aspose.pdf.operators.SetLineWidth) -> None:
        '''Visit/select w operator.
        
        :param w: Set line width operator.'''
        ...
    
    @overload
    def visit(self, w: aspose.pdf.operators.Clip) -> None:
        '''Visit/select W operator.
        
        :param w: Set clipping path operator (nonzero winding number rule).'''
        ...
    
    @overload
    def visit(self, y: aspose.pdf.operators.CurveTo2) -> None:
        '''Visit/select y operator.
        
        :param y: Append curved segment to path operator (final point replicated).'''
        ...
    
    @overload
    def visit(self, text_operator: aspose.pdf.operators.TextOperator) -> None:
        '''Visit/select any text operator operator.
        
        :param text_operator: General text operator which is used to select the set of corresponding pdf operators.'''
        ...
    
    @property
    def selected(self) -> list[aspose.pdf.Operator]:
        '''The list of selected objects.'''
        ...
    
    ...

class Opi:
    '''Represents The Open Prepress Interface (OPI) is a mechanism for creating low-resolution placeholders, or proxies,
    for such high-resolution images.'''
    
    def __init__(self, xform: aspose.pdf.XForm):
        '''The constructor.
        
        :param xform: Xform object.'''
        ...
    
    @property
    def version(self) -> str:
        '''Gets the version of OPI to which this dictionary refers.'''
        ...
    
    @property
    def file_specification(self) -> str:
        '''Gets the external file containing the low- resolution proxy image.'''
        ...
    
    @property
    def position(self) -> list[float]:
        '''Gets an array of eight numbers of the form specifying the location on the page of the cropped image.'''
        ...
    
    ...

class OptimizedMemoryStream:
    '''Defines a MemoryStream that can contains more standard capacity'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`OptimizedMemoryStream` class.'''
        ...
    
    @overload
    def __init__(self, buffer_size: int, buffer: bytes):
        '''Initializes a new instance of the :class:`OptimizedMemoryStream` class based on the specified byte array.
        
        :param buffer_size: Size of the underlying buffers.
        :param buffer: The array of unsigned bytes from which to create the current stream.'''
        ...
    
    @overload
    def __init__(self, buffer_size: int):
        '''Initializes a new instance of the :class:`OptimizedMemoryStream` class.
        
        :param buffer_size: Size of the underlying buffers.'''
        ...
    
    @overload
    def __init__(self, buffer: bytes):
        '''Initializes a new instance of the :class:`OptimizedMemoryStream` class based on the specified byte array.
        
        :param buffer: The array of unsigned bytes from which to create the current stream.'''
        ...
    
    def to_array(self) -> bytes:
        '''Converts the current stream to a byte array.
        
        :returns: An array of bytes'''
        ...
    
    def write_to(self, stream: Any) -> None:
        '''Writes to the specified stream.
        
        :param stream: The stream.'''
        ...
    
    @property
    def buffer_size(self) -> int:
        '''Gets or sets the size of the underlying buffers.'''
        ...
    
    @buffer_size.setter
    def buffer_size(self, value: int):
        ...
    
    @property
    def free_on_dispose(self) -> bool:
        '''Gets or sets a value indicating whether to free the underlying buffers on dispose.'''
        ...
    
    @free_on_dispose.setter
    def free_on_dispose(self, value: bool):
        ...
    
    DEFAULT_BUFFER_SIZE: int
    
    ...

class OutlineCollection(aspose.pdf.Outlines):
    '''Represents document outline hierarchy.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.OutlineItemCollection:
        '''Gets outline item from collection by index.
        
        :param index: Index of requested item.
        :returns:'''
        ...
    
    @overload
    def delete(self) -> None:
        '''Deletes all outline items from the document outline.'''
        ...
    
    @overload
    def delete(self, name: str) -> None:
        '''Deletes the outline item with specified title from the document outline.
        
        :param name: The title of outline item to be deleted'''
        ...
    
    @property
    def visible_count(self) -> int:
        '''Count is the sum of the number of visible descendent outline items at all levels. Note: please don't confuse with Count which is number if items in collection.'''
        ...
    
    @property
    def first(self) -> aspose.pdf.OutlineItemCollection:
        '''Gets an outline item representing the first top-level item in the outline.'''
        ...
    
    @property
    def last(self) -> aspose.pdf.OutlineItemCollection:
        '''Gets an outline item representing the last top-level item in the outline.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Gets a value indicating whether access to this collection is synchronized (thread safe).'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets an object that can be used to synchronize access to this collection.'''
        ...
    
    ...

class OutlineItemCollection(aspose.pdf.Outlines):
    '''Represents outline entry in outline hierarchy of PDF document.'''
    
    def __init__(self, outlines: aspose.pdf.OutlineCollection):
        '''Initializes outline item instance using root hierarchy object.
        
        :param outlines: Outlune collection.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.OutlineItemCollection:
        '''Gets outline item from the collection using index.
        
        :param index: Index within the collection.
        :returns: OutlineItemCollection object.'''
        ...
    
    @overload
    def delete(self) -> None:
        '''Deletes this outline item from the document outline hierarchy.'''
        ...
    
    @overload
    def delete(self, name: str) -> None:
        '''Deletes outline entry with specified name from the document outline hierarchy.
        
        :param name: Title of outline entry will be deleted.'''
        ...
    
    def insert(self, index: int, outline: aspose.pdf.OutlineItemCollection) -> None:
        '''Inserts the outline item into collection at the specified place.
        
        :param index: The index specifying place for inserting.
        :param outline: The outline item should be inserted.'''
        ...
    
    @property
    def visible_count(self) -> int:
        '''Gets the total number of outline items at all levels in the document outline hierarchy.'''
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets the title for this outline item.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def destination(self) -> aspose.pdf.annotations.IAppointment:
        '''Gets or sets the destination for this outline item.'''
        ...
    
    @destination.setter
    def destination(self, value: aspose.pdf.annotations.IAppointment):
        ...
    
    @property
    def action(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets the action for this outline item.'''
        ...
    
    @action.setter
    def action(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Gets or sets the color for the title text of this outline item.'''
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def italic(self) -> bool:
        '''Gets or sets italic flag for the title text of this outline item'''
        ...
    
    @italic.setter
    def italic(self, value: bool):
        ...
    
    @property
    def bold(self) -> bool:
        '''Gets or sets bold flag for the title text of this outline item'''
        ...
    
    @bold.setter
    def bold(self, value: bool):
        ...
    
    @property
    def first(self) -> aspose.pdf.OutlineItemCollection:
        '''Gets the outline item representing the first top-level item in the outline hierarchy.'''
        ...
    
    @property
    def last(self) -> aspose.pdf.OutlineItemCollection:
        '''Gets the outline item representing the last top-level item in the outline hierarchy.'''
        ...
    
    @property
    def prev(self) -> aspose.pdf.OutlineItemCollection:
        '''Gets the outline item representing previous item relatively this item in the outline hierarchy.'''
        ...
    
    @property
    def next(self) -> aspose.pdf.OutlineItemCollection:
        '''Gets the outline item representing next item relatively this item in the outline hierarchy.'''
        ...
    
    @property
    def has_next(self) -> bool:
        '''Check if outline item representing next item relatively this item in the outline hierarchy.'''
        ...
    
    @property
    def parent(self) -> aspose.pdf.Outlines:
        '''Gets the parent object of this outline item in the outline hierarchy.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Gets the value indicating whether access to this collection is synchronized (thread safe).'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets the object that can be used to synchronize access to this collection.'''
        ...
    
    @property
    def open(self) -> bool:
        '''Get or sets open status (true/false) for outline item.'''
        ...
    
    @open.setter
    def open(self, value: bool):
        ...
    
    @property
    def level(self) -> int:
        '''Gets hierarchy level of outline item.'''
        ...
    
    ...

class Outlines:
    '''Class describes collection of outlines.'''
    
    @property
    def visible_count(self) -> int:
        '''Gets the total number of outline items at all levels in the document outline hierarchy.'''
        ...
    
    ...

class OutputIntent:
    '''Represents an output intent that matches the color characteristics of a PDF document with those
    of a target output device or production environment in which the document will be printed.'''
    
    @property
    def subtype(self) -> str:
        '''Gets the output intent subtype.'''
        ...
    
    @property
    def output_condition(self) -> str:
        '''Gets a text that concisely identifies the intended output device or production condition
        in human-readable form.'''
        ...
    
    @property
    def output_condition_identifier(self) -> str:
        '''Gets a text that identifies the intended output device or production condition in human-
        or machine-readable form.'''
        ...
    
    @property
    def registry_name(self) -> str:
        '''Gets a text that identifies the registry in which the condition designated
        by :attr:`OutputIntent.output_condition_identifier` is defined.'''
        ...
    
    @property
    def info(self) -> str:
        '''Gets a human-readable text that contains additional information or comments about the intended target device
        or production condition.'''
        ...
    
    ...

class OutputIntents:
    '''Represents the collection of :class:`OutputIntent`.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.OutputIntent:
        '''Gets the output intent at the specified .
        
        :param index: The zero-based index of the output intent to get.
        :returns: The output intent at the specified .
        
        :raises System.ArgumentOutOfRangeException: is less than 0 or is equal to or greater
                                                    thanAspose.Pdf.OutputIntents.Count.
        :raises System.InvalidOperationException: The document that contains the collection has no catalog to access the OutputIntents.'''
        ...
    
    ...

class Page:
    '''Class representing page of PDF document.'''
    
    @overload
    def merge_layers(self, new_layer_name: str) -> None:
        '''Merges all layers on the page into a single layer with the specified new layer name.
        
        :param new_layer_name: The name of the new layer after merging.'''
        ...
    
    @overload
    def merge_layers(self, new_layer_name: str, new_optional_content_group_id: str) -> None:
        '''Merges all layers on the page into a single layer with the specified new layer name and optional content group Id.
        
        :param new_layer_name: The name of the new layer after merging.
        :param new_optional_content_group_id: The optional content group Id for the merged layer.'''
        ...

    @overload
    def send_to(self, device: aspose.pdf.devices.PageDevice, output: Any) -> None:
        '''Sends page to process with given page device.
        
        :param device: The device to process page.
        :param output: Result stream which is used with device to save its output.'''
        ...
    
    @overload
    def send_to(self, device: aspose.pdf.devices.PageDevice, output_file_name: str) -> None:
        '''Sends page to process with given page device.
        
        :param device: The device to process page.
        :param output_file_name: File which is used with device to save its output.'''
        ...
    
    @overload
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts :class:`aspose.pdf.annotations.AnnotationSelector` visitor object that provides functionality to work with annotations.
        
        :param visitor: Annotation selector sobject.'''
        ...
    
    @overload
    def accept(self, visitor: aspose.pdf.text.TextFragmentAbsorber) -> None:
        '''Accepts :class:`aspose.pdf.text.TextFragmentAbsorber` visitor object that provides functionality to work with text objects.
        
        :param visitor: Text absorber object.'''
        ...
    
    @overload
    def accept(self, visitor: aspose.pdf.ImagePlacementAbsorber) -> None:
        '''Accepts :class:`ImagePlacementAbsorber` visitor object that provides functionality to work with image placement objects.
        
        :param visitor: Image placement absorber object.'''
        ...
    
    @overload
    def accept(self, visitor: aspose.pdf.text.TextAbsorber) -> None:
        '''Accepts :class:`aspose.pdf.text.TextAbsorber` visitor object that provides functionality to work with text objects.
        
        :param visitor: Text absorber object.'''
        ...
    
    @overload
    def add_image(self, image_stream: Any, image_rect: aspose.pdf.Rectangle) -> None:
        '''Adds image onto the page and locates it in the middle of specified rectangle saving image's proportion.
        
        :param image_stream: The stream of the image.
        :param image_rect: The position of the image.'''
        ...
    
    @overload
    def add_image(self, hocr: str, image_stream: Any, image_rect: aspose.pdf.Rectangle) -> None:
        '''Adds searchable image onto the page and locates it in the middle of specified rectangle saving image's proportion.
        
        :param hocr: The hocr of the image.
        :param image_stream: The stream of the image.
        :param image_rect: The position of the image.'''
        ...
    
    @overload
    def add_image(self, image_stream: Any, image_rect: aspose.pdf.Rectangle, image_width: int, image_height: int, save_image_proportions: bool) -> None:
        '''Adds image on page and places it depend on image rectangle position.
        
        :param image_stream: The stream of the image.
        :param image_rect: The default position of the image on page.
        :param image_width: The width of the image.
        :param image_height: The height of the image.
        :param save_image_proportions: If the flag set to true than image placed in rectangle position; otherwise, the size of rectange is becoming equal to image size.'''
        ...
    
    @overload
    def add_image(self, image_path: str, rectangle: aspose.pdf.Rectangle) -> None:
        '''Adds image onto the page and locates it in the middle of specified rectangle saving image's proportion.
        
        :param image_path: The path to image.
        :param rectangle: The position of the image.'''
        ...
    
    def add_graphics(self, elements: aspose.pdf.vector.GraphicElementCollection, rectangle: aspose.pdf.Rectangle) -> None:
        '''Adds graphics to the page.
        Works faster than adding elements one by one with :meth:`aspose.pdf.vector.GraphicElement.add_on_page` method.
        
        :param elements: Graphics collection.
        :param rectangle: Elements will be added to the page if it's  is inside the rectangle area.
                          If rectangle is null, all graphic elements will be added'''
        ...
    
    def delete_graphics(self, elements_to_delete: aspose.pdf.vector.GraphicElementCollection) -> None:
        '''Deletes graphics from the page.
        Works faster than deleting elements one by one with :meth:`aspose.pdf.vector.GraphicElement.remove` method.
        
        :param elements_to_delete: Graphics collection that will be deleted from the page.'''
        ...

    def try_save_vector_graphics(self, path_to_save: str) -> bool:
        '''Tries to save vector graphics if they are present on the page. The save format is SVG.
        
        :param path_to_save: Output file
        :returns: True if the page contains path construction operators; otherwise, False.'''
        ...
    
    def has_vector_graphics(self) -> bool:
        '''Detect of the presence of vector graphics, if it is present on the page.
        
        :returns: True if the page contains path construction operators; otherwise, False.'''
        ...
    
    def is_blank(self, fill_threshold_factor: float) -> bool:
        '''Gets the flag whether page is blank or not.
        
        :param fill_threshold_factor: The fill threshold value that manages the sensitivity of detection. Should be equal or greater than 0.01.
        :returns: True - if page is blank; otherwise, false.'''
        ...
    
    def get_page_rect(self, consider_rotation: bool) -> aspose.pdf.Rectangle:
        '''Returns rectangle of the page according to its CropBox (or MediaBox if CropBox null).
        
        :param consider_rotation: If true then rotation of the page will be considered in rect calculation.
        :returns: Rectangle of the page.'''
        ...
    
    def calculate_content_b_box(self) -> aspose.pdf.Rectangle:
        '''Calculates bbox value - rectangle containing contents without visible margins.
        
        :returns: Bbox value - rectangle containing contents without visible margins'''
        ...
    
    @staticmethod
    def rotation_to_int(self, rotation: aspose.pdf.Rotation) -> int:
        '''Translates rotation enumeration member into integer value.
        
        :param rotation: Rotation enumeratioom member.
        :returns: Corresponding integer value'''
        ...
    
    @staticmethod
    def int_to_rotation(self, rotation: int) -> aspose.pdf.Rotation:
        '''Translates integer value into corresponding rotation enumeration member.
        
        :param rotation: Integer value to convert
        :returns: Rotation enumeration member'''
        ...
    
    def add_stamp(self, stamp) -> None:
        '''Put stamp into page. Stamp can be page number, image or simple text, e.g. some logo.
        
        :param stamp: Stamp to add on the page.
                      Each stamp has its coordinates and corresponding properties regarding to the kind of stamp,
                      i.e. image or text value.'''
        ...
    
    def flatten(self) -> None:
        '''Removes all fields located on the page and place their values instead.'''
        ...
    
    def set_page_size(self, width: float, height: float) -> None:
        '''Sets page size for page.
        
        :param width: Page width.
        :param height: Page size.'''
        ...
    
    def make_grayscale(self) -> None:
        '''Converts the page to grayscale.'''
        ...
    
    def free_memory(self) -> None:
        '''Clears cached data'''
        ...
    
    def get_notifications(self) -> str:
        '''Returns notifications about inside operations with page content. (Only notifications about paragraph events in text adding scenarios are supported now.)
        
        :returns: String representing notifications about inside operations with page content.'''
        ...
    
    def as_byte_array(self, resolution: aspose.pdf.devices.Resolution) -> bytes:
        '''Converts current page as bitmap and than returns array of bytes.
        
        :param resolution: The resolution.
        :returns: Converted array of image bytes.'''
        ...
    
    def as_xml(self) -> str:
        '''Converts current page as xml in utf8 encoding.
        
        :returns: Converted xml string.'''
        ...
   
    def resize(self, target_size: aspose.pdf.PageSize) -> None:
        '''Resizes the page.
        
        :param target_size: The target size.'''
        ...
 
    @property
    def is_add_paragraphs_after_last(self) -> bool:
        '''Gets or sets the addition of paragraphs after the last paragraph of the page'''
        ...
    
    @is_add_paragraphs_after_last.setter
    def is_add_paragraphs_after_last(self, value: bool):
        ...
    
    @property
    def background_image(self) -> aspose.pdf.Image:
        '''Gets or sets background image for page (for generator only, not filled in when reading document).'''
        ...
    
    @background_image.setter
    def background_image(self, value: aspose.pdf.Image):
        ...
    
    @property
    def toc_info(self) -> aspose.pdf.TocInfo:
        '''Gets or sets table of contents info.'''
        ...
    
    @toc_info.setter
    def toc_info(self, value: aspose.pdf.TocInfo):
        ...
    
    @property
    def header(self) -> aspose.pdf.HeaderFooter:
        '''Gets or sets page header.'''
        ...
    
    @header.setter
    def header(self, value: aspose.pdf.HeaderFooter):
        ...
    
    @property
    def layers(self) -> None:
        '''Gets or sets layers collection.'''
        ...
    
    @layers.setter
    def layers(self, value: None):
        ...
    
    @property
    def footer(self) -> aspose.pdf.HeaderFooter:
        '''Gets or sets page footer.'''
        ...
    
    @footer.setter
    def footer(self, value: aspose.pdf.HeaderFooter):
        ...
    
    @property
    def paragraphs(self) -> aspose.pdf.Paragraphs:
        '''Gets the paragraphs.'''
        ...
    
    @paragraphs.setter
    def paragraphs(self, value: aspose.pdf.Paragraphs):
        ...
    
    @property
    def page_info(self) -> aspose.pdf.PageInfo:
        '''Gets or sets the page info (for generator only, not filled in when reading document).'''
        ...
    
    @page_info.setter
    def page_info(self, value: aspose.pdf.PageInfo):
        ...
    
    @property
    def rect(self) -> aspose.pdf.Rectangle:
        '''Gets or sets rectangle of the page.
        For get: page crop box is returned if specified, otherwise page media box is returned.
        For set: page media box always set.
        Please note that this property don't consider page rotation. To get page rectangle considering rotation please use ActualRect.'''
        ...
    
    @rect.setter
    def rect(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def color_type(self) -> aspose.pdf.ColorType:
        '''Sets color type of the pages based on information getting from operators SetColor,
        images and forms.'''
        ...
    
    @property
    def note_line_style(self) -> aspose.pdf.GraphInfo:
        '''Gets or sets the line style for notes.(for generator only, not filled in when reading document)'''
        ...
    
    @note_line_style.setter
    def note_line_style(self, value: aspose.pdf.GraphInfo):
        ...
    
    @property
    def tab_order(self) -> aspose.pdf.TabOrder:
        '''Gets or sets tab order of the page.
        Possible values: Row, Column. Default, Manual'''
        ...
    
    @tab_order.setter
    def tab_order(self, value: aspose.pdf.TabOrder):
        ...
    
    @property
    def duration(self) -> float:
        '''Gets of set page display duration. This is time in seconds that page shall be displayed during presentation.
        Returns -1 if duration is not defined.'''
        ...
    
    @duration.setter
    def duration(self, value: float):
        ...
    
    @property
    def contents(self) -> aspose.pdf.OperatorCollection:
        '''Gets collection of operators in the content stream of the page.
        :class:`OperatorCollection`'''
        ...
    
    @property
    def group(self) -> aspose.pdf.Group:
        '''Gets or sets a group attributes class specifying the attributes of the page�s page group for use in the transparent imaging model.'''
        ...
    
    @group.setter
    def group(self, value: aspose.pdf.Group):
        ...
    
    @property
    def annotations(self) -> aspose.pdf.annotations.AnnotationCollection:
        '''Gets collection of page annotations.
        :attr:`Page.annotations`'''
        ...
    
    @property
    def resources(self) -> aspose.pdf.Resources:
        '''Gets page resources. Resources object contains collections of images, forms and fonts.
        :attr:`Page.resources`'''
        ...
    
    @property
    def rotate(self) -> aspose.pdf.Rotation:
        '''Gets or sets rotation of the page.'''
        ...
    
    @rotate.setter
    def rotate(self, value: aspose.pdf.Rotation):
        ...
    
    @property
    def trim_box(self) -> aspose.pdf.Rectangle:
        '''Gets or sets trim box of the page.'''
        ...
    
    @trim_box.setter
    def trim_box(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def art_box(self) -> aspose.pdf.Rectangle:
        '''Gets or sets art box of the page.'''
        ...
    
    @art_box.setter
    def art_box(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def bleed_box(self) -> aspose.pdf.Rectangle:
        '''Gets or sets bleed box of the page.'''
        ...
    
    @bleed_box.setter
    def bleed_box(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def crop_box(self) -> aspose.pdf.Rectangle:
        '''Gets or sets crop box of the page.'''
        ...
    
    @crop_box.setter
    def crop_box(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def media_box(self) -> aspose.pdf.Rectangle:
        '''Gets or sets media box of the page.'''
        ...
    
    @media_box.setter
    def media_box(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def number(self) -> int:
        '''Get number of the page.'''
        ...
    
    @property
    def rotation_matrix(self) -> aspose.pdf.Matrix:
        '''Gets transofmation matrix for the page.'''
        ...
    
    @property
    def background(self) -> aspose.pdf.Color:
        '''Gets or sets the background color of the page.'''
        ...
    
    @background.setter
    def background(self, value: aspose.pdf.Color):
        ...
    
    @property
    def watermark(self) -> aspose.pdf.Watermark:
        '''Gets or sets the watermark of the page.'''
        ...
    
    @watermark.setter
    def watermark(self, value: aspose.pdf.Watermark):
        ...
    
    @property
    def artifacts(self) -> aspose.pdf.ArtifactCollection:
        '''Gets collection of artifacts on the page.'''
        ...
    
    @property
    def actions(self) -> aspose.pdf.PageActionCollection:
        '''Gets collection of page properties.'''
        ...
    
    @property
    def fields_in_tab_order(self) -> list[aspose.pdf.forms.Field]:
        '''Gets list of Field object in Tab order on this page.'''
        ...
    
    @property
    def user_unit(self) -> float:
        '''Gets or sets UserUnit value. A positive number giving the size of default user space units, in multiples of 1 ⁄ 72 inch.
        Default value is 1. Please set zero or negative value in order to clear this entry in page.'''
        ...
    
    @user_unit.setter
    def user_unit(self, value: float):
        ...
    
    ...

class PageActionCollection(aspose.pdf.BaseActionCollection):
    '''This class describes page actions'''
    
    @property
    def on_open(self) -> aspose.pdf.annotations.PdfAction:
        '''An action that shall be performed when the page is opened.'''
        ...
    
    @on_open.setter
    def on_open(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_close(self) -> aspose.pdf.annotations.PdfAction:
        '''An action that shall be performed when the page is closed.'''
        ...
    
    @on_close.setter
    def on_close(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    ...

class PageCollection:
    '''Collection of PDF document pages.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.Page:
        '''Gets page by index.
        
        :param index: Index of page.
        :returns: Retreived page.'''
        ...
    
    @overload
    def add(self, entity: aspose.pdf.Page) -> aspose.pdf.Page:
        '''Adds page to collection.
        
        :param entity: Page which should be added.
        :returns: Added page.'''
        ...
    
    @overload
    def add(self) -> aspose.pdf.Page:
        '''Adds empty page
        
        :returns: Added page.'''
        ...
    
    @overload
    def add(self, pages) -> None:
        '''Adds to collection all pages from list.
        
        :param pages: List which contains all pages which must be added.'''
        ...
    
    @overload
    def add(self, pages: list[aspose.pdf.Page]) -> None:
        '''Adds to collection all pages from array.
        
        :param pages: Array of pages which will be added.'''
        ...
    
    @overload
    def delete(self, index: int) -> None:
        '''Delete specified page.
        
        :param index: Number of page that will be deleted. Pages numbers start from 1.'''
        ...
    
    @overload
    def delete(self) -> None:
        '''Deletes all pages from collection.'''
        ...
    
    @overload
    def delete(self, pages: list[int]) -> None:
        '''Delete pages specified which numbers are specified in array.
        
        :param pages: Array of pages to be deleted.'''
        ...
    
    @overload
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts :class:`aspose.pdf.annotations.AnnotationSelector` visitor object that provides functionality to work with annotations.
        
        :param visitor: AnnotationSelector Visitor'''
        ...
    
    @overload
    def accept(self, visitor: aspose.pdf.ImagePlacementAbsorber) -> None:
        '''Accepts :class:`ImagePlacementAbsorber` visitor object that provides functionality to work with image placement objects.
        
        :param visitor: Image placement object.'''
        ...
    
    @overload
    def accept(self, visitor: aspose.pdf.text.TextFragmentAbsorber) -> None:
        '''Accepts :class:`aspose.pdf.text.TextFragmentAbsorber` visitor object that provides functionality to work with text objects.
        
        :param visitor: Text fragment absorber object.'''
        ...
    
    @overload
    def accept(self, visitor: aspose.pdf.text.TextAbsorber) -> None:
        '''Accepts :class:`aspose.pdf.text.TextAbsorber` visitor object that provides functionality to work with text objects.
        
        :param visitor: Text absorber object.'''
        ...
    
    @overload
    def insert(self, page_number: int) -> aspose.pdf.Page:
        '''Insert empty apge into collection at the specified position.
        
        :param page_number: Position of the new page.
        :returns: Inserted page.'''
        ...
    
    @overload
    def insert(self, page_number: int, entity: aspose.pdf.Page) -> aspose.pdf.Page:
        '''Inserts page into page collection at specified place.
        
        :param page_number: Required page index in collection.
        :param entity: Page to be inserted.
        :returns: Inserted page.'''
        ...
    
    @overload
    def insert(self, page_number: int, pages) -> None:
        '''Inserts pages from the collection into document.
        
        :param page_number: Starting position of the new pages.
        :param pages: Pages collection.'''
        ...
    
    @overload
    def insert(self, page_number: int, pages: list[aspose.pdf.Page]) -> None:
        '''Inserts pages of the array into document.
        
        :param page_number: Starting number of the new pages.
        :param pages: Array of pages which will be inserted.'''
        ...
    
    def index_of(self, entity: aspose.pdf.Page) -> int:
        '''Returns index of the specified page.
        
        Pages numbers start from 1.
        Returns 0 in case collection doesn't contain the page.
        
        :param entity: Page object. Pages numbers start from 1.
        :returns: Index of the page in collection.'''
        ...
    
    def flatten(self) -> None:
        '''Removes all fields located on the pages and place their values instead.'''
        ...
    
    def free_memory(self) -> None:
        '''Clears cached data'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Returns true of object is synchorinzed.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets synchronization object of the collection.'''
        ...
    
    ...

class PageInfo:
    '''Represents the page information.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> object:
        '''Clone page info.
        
        :returns: The cloned object'''
        ...
    
    @property
    def any_margin(self) -> aspose.pdf.MarginInfo:
        '''Gets or sets page margin for any page except first.'''
        ...
    
    @any_margin.setter
    def any_margin(self, value: aspose.pdf.MarginInfo):
        ...
    
    @property
    def default_text_state(self) -> aspose.pdf.text.TextState:
        '''Gets or sets default font.'''
        ...
    
    @default_text_state.setter
    def default_text_state(self, value: aspose.pdf.text.TextState):
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets page height.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def pure_height(self) -> float:
        '''Gets or sets page pure height without margins.'''
        ...
    
    @property
    def is_landscape(self) -> bool:
        '''Gets or sets is page landscaped.'''
        ...
    
    @is_landscape.setter
    def is_landscape(self, value: bool):
        ...
    
    @property
    def margin(self) -> aspose.pdf.MarginInfo:
        '''Gets or sets page margin.'''
        ...
    
    @margin.setter
    def margin(self, value: aspose.pdf.MarginInfo):
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets page width.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    ...

class PageLabel:
    '''Class representing Page Label range.'''
    
    def __init__(self):
        '''Constructor for page label.'''
        ...
    
    @property
    def starting_value(self) -> int:
        '''Gets or sets starting value of the page numbering range.'''
        ...
    
    @starting_value.setter
    def starting_value(self, value: int):
        ...
    
    @property
    def numbering_style(self) -> aspose.pdf.NumberingStyle:
        '''Gets or sets numbering style.'''
        ...
    
    @numbering_style.setter
    def numbering_style(self, value: aspose.pdf.NumberingStyle):
        ...
    
    @property
    def prefix(self) -> str:
        '''Gets or sets page number prefix.'''
        ...
    
    @prefix.setter
    def prefix(self, value: str):
        ...
    
    ...

class PageLabelCollection:
    '''Class represeingting page label collection.'''
    
    def get_label(self, page_index: int) -> aspose.pdf.PageLabel:
        '''Gets page label by page index (page index is started from 0).
        
        :param page_index: Index of the page.
        :returns: Page label for specified page index or null if page label does not exist.'''
        ...
    
    def update_label(self, page_index: int, page_label: aspose.pdf.PageLabel) -> None:
        '''Update label for given page index (page index is started from 0).
        
        :param page_index: Index of page to change lable of the page.
        :param page_label: New label of the page.'''
        ...
    
    def remove_label(self, page_index: int) -> bool:
        '''Remove label by page index (page index is started from 0).
        
        :param page_index: Index of page where label must be deleted.
        :returns: true if operation was executed successfully.'''
        ...
    
    def get_pages(self) -> list[int]:
        '''Gets page indexes in collection.
        
        :returns: Array of integers which contains indexes of the pages.'''
        ...
    
    ...

class PageNumberStamp(aspose.pdf.TextStamp):
    '''Represents page number stamp and used to number pages.'''
    
    @overload
    def __init__(self, format: str):
        '''Initializes a new instance of the :class:`PageNumberStamp` class.
        
        :param format: String value used for stamping. See :attr:`PageNumberStamp.format` property for details.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PageNumberStamp` class. Format is set to "#".'''
        ...
    
    @overload
    def __init__(self, formatted_text: aspose.pdf.facades.FormattedText):
        '''Creates PageNumberStamp by formatted text.
        
        :param formatted_text: Formatted text which used to create Page Number Stamp.'''
        ...
    
    def put(self, page: aspose.pdf.Page) -> None:
        '''Adds page number.
        
        :param page: Page for stamping.'''
        ...
    
    @property
    def format(self) -> str:
        '''String value for stamping page numbers.
        Value must include char '#' which is replaced with the page number in the process of stamping.'''
        ...
    
    @format.setter
    def format(self, value: str):
        ...
    
    @property
    def starting_number(self) -> int:
        '''Gets or sets value of the number of starting page. Other pages will be numbered starting from this value.'''
        ...
    
    @starting_number.setter
    def starting_number(self, value: int):
        ...
    
    @property
    def numbering_style(self) -> aspose.pdf.NumberingStyle:
        '''Numbering style which used by this stamp.'''
        ...
    
    @numbering_style.setter
    def numbering_style(self, value: aspose.pdf.NumberingStyle):
        ...
    
    ...

class PageSize:
    '''Class representing size of page in PDF document.'''
    
    def __init__(self, x: float, y: float):
        '''Constructor for PageSize.
        
        :param x: Width of the page.
        :param y: Height of the page.'''
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets page width.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets page height.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def is_landscape(self) -> bool:
        '''Gets page orientation. Returns true of this is landscape orientation and false if this is portrait.'''
        ...
    
    @is_landscape.setter
    def is_landscape(self, value: bool):
        ...
    
    a0: aspose.pdf.PageSize
    
    a1: aspose.pdf.PageSize
    
    a2: aspose.pdf.PageSize
    
    a3: aspose.pdf.PageSize
    
    a4: aspose.pdf.PageSize
    
    a5: aspose.pdf.PageSize
    
    a6: aspose.pdf.PageSize
    
    b5: aspose.pdf.PageSize
    
    page_letter: aspose.pdf.PageSize
    
    page_legal: aspose.pdf.PageSize
    
    page_ledger: aspose.pdf.PageSize
    
    p11x17: aspose.pdf.PageSize
    
    ...

class Paragraphs:
    '''This class represents paragraph collection.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.BaseParagraph:
        '''Gets or sets paragraph from or to collection.
        
        :param index: The paragraph index.
        :returns:'''
        ...
    
    def __setitem__(self, index: int, value: aspose.pdf.BaseParagraph):
        ...
    
    def add(self, paragraph: aspose.pdf.BaseParagraph) -> None:
        '''Add paragraph to collection.
        
        :param paragraph: The paragraph.'''
        ...
    
    def get_range(self, index: int, count: int) -> aspose.pdf.Paragraphs:
        '''Remove paragraphs range.
        
        :param index: The first paragraph index.
        :param count: The paragraphs count.
        :returns: The paragraphs collection'''
        ...
    
    def remove_range(self, index: int, count: int) -> None:
        '''Remove paragraphs range.
        
        :param index: The first paragraph index.
        :param count: The paragraphs count.'''
        ...
    
    def remove(self, paragraph: aspose.pdf.BaseParagraph) -> None:
        '''Remove paragraph from collection.
        
        :param paragraph: The paragraph.'''
        ...
    
    def insert(self, index: int, paragraph: aspose.pdf.BaseParagraph) -> None:
        '''Insert paragraph to collection.
        
        :param index: The index for paragraph.
        :param paragraph: The paragraph.'''
        ...
    
    def clear(self) -> None:
        '''Clear paragraphs.'''
        ...
    
    def insert_range(self, index: int, collection: Iterable[aspose.pdf.BaseParagraph]) -> None:
        '''Inserts the elements of a collection into the list at the specified index.
        
        :param index: Index value.
        :param collection: Collection.'''
        ...
    
    def clone(self) -> object:
        '''Clones a new :meth:`Paragraphs.clone` object.
        
        :returns: The new :meth:`Paragraphs.clone` object.'''
        ...
    
    @property
    def count(self) -> int:
        '''Get paragraphs count.'''
        ...
    
    ...

class PclLoadOptions(aspose.pdf.LoadOptions):
    '''Represents options for loading(import) PCL file into pdf document.'''
    
    def __init__(self):
        ...
    
    @property
    def batch_size(self) -> int:
        '''Defines batch size if batched conversion is applicable
        to source and destination formats pair.'''
        ...
    
    @batch_size.setter
    def batch_size(self, value: int):
        ...
    
    @property
    def conversion_engine(self) -> None:
        '''Defines conversion engine that will be used for conversion'''
        ...
    
    @conversion_engine.setter
    def conversion_engine(self, value: None):
        ...
    
    @property
    def supress_errors(self) -> bool:
        '''Gets or sets boolean value which indicates will PCL conversion errors should be supressed.'''
        ...
    
    @supress_errors.setter
    def supress_errors(self, value: bool):
        ...
    
    class ConversionEngines:
          '''Enumerates conversion engines that can be used for conversion.'''

          LEGACY_ENGINE: ConversionEngines
          NEW_ENGINE: ConversionEngines

    ...

class PdfANonSpecificationFlags:
    '''This class holds flags to control PDF/A conversion for cases when source PDF document doesn't
    correspond to PDF specification. If flags of this clas are used it decreases performance
    but it's necessary when source PDF document can't be convert into PDF/A format by usual way.
    By default all flags are set to false.'''
    
    def __init__(self):
        ...
    
    @property
    def check_different_names_in_font_dictionaries(self) -> bool:
        '''Some PDF documents contain fonts which have different names in internal data.
        Use of this flag enforces special processing logic for cases when fields
        BaseFont and FontDescriptor.FontName are different.'''
        ...
    
    @check_different_names_in_font_dictionaries.setter
    def check_different_names_in_font_dictionaries(self, value: bool):
        ...
    
    ...

class PdfASymbolicFontEncodingStrategy:
    '''This class describes rules which can be used to tune process of copy encoding data for cases
    when TrueType symbolic font has more than one encoding.
    Some PDF documents after conversion into PDF/A format could have error
    "More than one encoding in symbolic TrueType font's cmap".
    What is a reason of this error? All TrueType symbolic fonts have special table "cmap"
    in it's internal data. This table maps character codes to glyph indices.
    And this table could contain different encoding subtables which
    describe encodings used. See advanced info about cmap tables at
    https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6cmap.html.
    Usually cmap table contains several encoding subtables, but PDF/A standard requires
    that only one encoding subtable (3,0) must be leaved for this font in PDF/A document.
    And key question here - what data must be taken from another subtables to copy into
    destination encoding table (3,0)? Majority of fonts have 'well-formed' cmap tables where
    every encoding subtable is fully consistent with another subtable. But some fonts
    have cmap tables with collisions - where for example one subtable has glyph index
    100 for unicode 100, but another subtable has glyph index 200 for the same unicode 100.
    To solve this problems special strategy needed.
    By default following strategy used:
    mac subtable(1,0) is looked for. If this table is found, only this data used to fill destination
    table (3,0). If mac subtable is not found then all subtables except (3,0) are iterated
    and used to copy data into destination (3,0) subtable. Also mapping for every unicode(unicode, glyph index)
    is copied into destination table only if destination table has no this unicode at current moment.
    So, for example if first subtabe has glyph index 100 for unicode 100, and next subtable has glyph
    index 200 for the same unicode 100, only data from first subtable (unicode=100, glyph index = 100) will be copied.
    So each previous subtable takes precedence over the next.
    Properties of this class :class:`PdfASymbolicFontEncodingStrategy` help tune default behaviour.
    If property :attr:`PdfASymbolicFontEncodingStrategy.preferred_cmap_encoding_table` of type Aspose.Pdf.PdfASymbolicFontEncodingStrategy.QueueItem.CMapEncodingTableType
    is set, then relevant subtable will be used in precedence to mac subtable(1,0). Value 'MacTable' from
    enumeration Aspose.Pdf.PdfASymbolicFontEncodingStrategy.QueueItem.CMapEncodingTableType has no sense in this case, cause it
    points on the same mac subtable (1,0) which will be used by default.
    Property Aspose.Pdf.PdfASymbolicFontEncodingStrategy.CmapEncodingTablesPriorityQueue discards all priorities for any subtable.
    If this property is set, then only subtables from declared queue will be used in specified order.
    If subtables specified are not found then default iteration of all subtables and copy strategy described above
    will be used.
    Object Aspose.Pdf.PdfASymbolicFontEncodingStrategy.QueueItem specifies encoding subtable used. This subtable can be set
    via combination of members(PlatformID, PlatformSpecificId) or via Aspose.Pdf.PdfASymbolicFontEncodingStrategy.QueueItem.CMapEncodingTableType
    enumeration.'''
    
    @overload
    def __init__(self):
        '''Constructor. Sets default subtable (mac 1,0)'''
        ...
    
    @overload
    def __init__(self, preferred_encoding_table):
        '''Constructor
        
        :param preferred_encoding_table: encoding subtable which will be used in precedence to mac subtable(1,0)'''
        ...
    
    @property
    def preferred_cmap_encoding_table(self) -> None:
        '''Specifies subtable which will be used in precedence to mac subtable(1,0). Value 'MacTable' from
        enumeration Aspose.Pdf.PdfASymbolicFontEncodingStrategy.QueueItem.CMapEncodingTableType has no sense in this case.'''
        ...
    
    @preferred_cmap_encoding_table.setter
    def preferred_cmap_encoding_table(self, value: None):
        ...

    class QueueItem:
          '''Specifies encoding subtable. Each encoding subtable has unique combination
             of parameters (PlatformID, PlatformSpecificId). Enumeration aspose.pdf.PdfASymbolicFontEncodingStrategy.QueueItem.CMapEncodingTableType
             and property c_map_encoding_table were implemented to make easier set of encoding subtable needed.'''

          def __init__(self, cmap_table: aspose.pdf.PdfASymbolicFontEncodingStrategy.QueueItem.CMapEncodingTableType):
              '''Constructor.
              :param cmap_table: encoding subtable'''
              ...
    
          @property
          def c_map_encoding_table(self) -> aspose.pdf.PdfASymbolicFontEncodingStrategy.QueueItem.CMapEncodingTableType:
              '''Specifies encoding subtable via aspose.pdf.PdfASymbolicFontEncodingStrategy.QueueItem.CMapEncodingTableType enumeration'''
              ...
          
          @c_map_encoding_table.setter
          def c_map_encoding_table(self, value: aspose.pdf.PdfASymbolicFontEncodingStrategy.QueueItem.CMapEncodingTableType):
              ...

          @property
          def platform_id(self) -> Any:
              '''Platform identifier for encoding subtable'''
              ...

          @platform_id.setter
          def platform_id(self, value: Any):
              ...

          @property
          def platform_specific_id(self) -> str:
              '''Platform-specific encoding identifier for encoding subtable'''
              ...

          @platform_specific_id.setter
          def platform_specific_id(self, value: Any):
              ...

          class CMapEncodingTableType:
                '''Declares set of some known encoding subtables.'''

                WINDOWS_UNICODE_TABLE: CMapEncodingTableType
                WINDOWS_SYMBOLIC_TABLE: CMapEncodingTableType
                MAC_TABLE: CMapEncodingTableType
                UNICODE_TABLE: CMapEncodingTableType

    
    ...

class PdfException(RuntimeError):
    '''Represents errors that occur during PDF application execution.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PdfException` class.'''
        ...
    
    @overload
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`PdfException` class.
        
        :param message: The message.'''
        ...
    
    ...

class PdfFormatConversionOptions:
    '''represents set of options for convert PDF document'''
    
    @overload
    def __init__(self, output_log_file_name: str, format: aspose.pdf.PdfFormat, action: aspose.pdf.ConvertErrorAction):
        '''Constructor
        
        :param output_log_file_name: Path to file where comments will be stored.
        :param format: The pdf format.
        :param action: Action for objects that can not be converted'''
        ...
    
    @overload
    def __init__(self, output_log_file_name: str, format: aspose.pdf.PdfFormat):
        '''Constructor
        
        :param output_log_file_name: Path to file where comments will be stored.
        :param format: The pdf format.'''
        ...
    
    @overload
    def __init__(self, format: aspose.pdf.PdfFormat):
        '''Constructor
        
        :param format: The pdf format.'''
        ...
    
    @overload
    def __init__(self, format: aspose.pdf.PdfFormat, action: aspose.pdf.ConvertErrorAction):
        '''Constructor
        
        :param format: The pdf format.
        :param action: Action for objects that can not be converted'''
        ...
    
    @overload
    def __init__(self, output_log_file_name: str, format: aspose.pdf.PdfFormat, action: aspose.pdf.ConvertErrorAction, transparency_action: aspose.pdf.ConvertTransparencyAction):
        '''Constructor
        
        :param output_log_file_name: Path to file where comments will be stored.
        :param format: The pdf format.
        :param action: Action for objects that can not be converted
        :param transparency_action: Action for image masked objects'''
        ...
    
    @overload
    def __init__(self, output_log_stream: Any, format: aspose.pdf.PdfFormat, action: aspose.pdf.ConvertErrorAction):
        '''Constructor
        
        :param output_log_stream: Stream where comments will be stored
        :param format: The pdf format
        :param action: Action for objects that can not be converted'''
        ...
    
    @property
    def is_async_image_streams_conversion_mode(self) -> bool:
        '''Gets/sets run of image streams in async mode.'''
        ...
    
    @is_async_image_streams_conversion_mode.setter
    def is_async_image_streams_conversion_mode(self, value: bool):
        ...
    
    @property
    def is_low_memory_mode(self) -> bool:
        '''Is low memory conversion mode enabled'''
        ...
    
    @is_low_memory_mode.setter
    def is_low_memory_mode(self, value: bool):
        ...
    
    @property
    def format(self) -> aspose.pdf.PdfFormat:
        '''PDF format.'''
        ...
    
    @format.setter
    def format(self, value: aspose.pdf.PdfFormat):
        ...
    
    @property
    def log_file_name(self) -> str:
        '''Path to file where comments will be stored.'''
        ...
    
    @log_file_name.setter
    def log_file_name(self, value: str):
        ...
    
    @property
    def log_stream(self) -> Any:
        '''Stream where comments will be stored.'''
        ...
    
    @log_stream.setter
    def log_stream(self, value: Any):
        ...
    
    @property
    def error_action(self) -> aspose.pdf.ConvertErrorAction:
        '''Action for objects that can not be converted'''
        ...
    
    @error_action.setter
    def error_action(self, value: aspose.pdf.ConvertErrorAction):
        ...
    
    @property
    def transparency_action(self) -> aspose.pdf.ConvertTransparencyAction:
        '''Action for image masked objects'''
        ...
    
    @transparency_action.setter
    def transparency_action(self, value: aspose.pdf.ConvertTransparencyAction):
        ...
    
    @property
    def convert_soft_mask_action(self) -> aspose.pdf.ConvertSoftMaskAction:
        '''Action for images with soft mask.'''
        ...
    
    @convert_soft_mask_action.setter
    def convert_soft_mask_action(self, value: aspose.pdf.ConvertSoftMaskAction):
        ...
    
    default: aspose.pdf.PdfFormatConversionOptions
    
    @property
    def non_specification_cases(self) -> aspose.pdf.PdfANonSpecificationFlags:
        '''Holds flags to control PDF/A conversion process for cases when source document
        doesn't correspond to PDF/A specification.'''
        ...
    
    @property
    def symbolic_font_encoding_strategy(self) -> aspose.pdf.PdfASymbolicFontEncodingStrategy:
        '''Strategy to copy encoding data for symbolic fonts if symbolic TrueType font
        has more than one encoding subtable.'''
        ...
    
    @symbolic_font_encoding_strategy.setter
    def symbolic_font_encoding_strategy(self, value: aspose.pdf.PdfASymbolicFontEncodingStrategy):
        ...
    
    @property
    def align_text(self) -> bool:
        '''This flag controls text alignment in converted document. By default document conversion
        doesn't affect text alignment and leave text as is. But in some cases font substitution
        causes text overlapping or extra spaces in converted document. When  this flag is set
        special alignment operations will be performed. This flag should be set only for documents
        which have problems with overlapped text or extra text spaces cause using of this flag decrease
        performance and in some cases could corrupt text content.'''
        ...
    
    @align_text.setter
    def align_text(self, value: bool):
        ...
    
    @property
    def pua_text_processing_strategy(self) -> None:
        '''Strategy to process symbols from unicode Private Use Area (PUA).'''
        ...
    
    @pua_text_processing_strategy.setter
    def pua_text_processing_strategy(self, value: None):
        ...
    
    @property
    def optimize_file_size(self) -> bool:
        '''Gets or sets a flag which enables/disables special conversion mode to get PDF/A document with reduced file size.
        Now this flag impacts on optimization of fonts used in PDF document, possibly, in future, this flag
        also will be used to switch on optimization for another data structures, such as graphic.
        Set of this flag and mode could significantly reduce file size but at the same time it could
        significantly decrease performance of conversion.'''
        ...
    
    @optimize_file_size.setter
    def optimize_file_size(self, value: bool):
        ...
    
    @property
    def exclude_fonts_strategy(self) -> None:
        '''Strategy(ies) to exclude superfluous fonts and reduce document file size.
        This parameter has sense only when flag :attr:`PdfFormatConversionOptions.optimize_file_size` is set to true.
        By default combination of strategies Aspose.Pdf.PdfFormatConversionOptions.SubsetFonts and
        Aspose.Pdf.PdfFormatConversionOptions.RemoveDuplicatedFonts is used.'''
        ...
    
    @exclude_fonts_strategy.setter
    def exclude_fonts_strategy(self, value: None):
        ...
    
    @property
    def font_embedding_options(self) -> aspose.pdf.pdfaoptionclasses.FontEmbeddingOptions:
        '''Options for cases when it's not possible to embed some fonts into PDF document.'''
        ...
    
    @property
    def unicode_processing_rules(self) -> aspose.pdf.pdfaoptionclasses.ToUnicodeProcessingRules:
        '''Rules to solve problems with unicode mapping. Can be null.'''
        ...
    
    @unicode_processing_rules.setter
    def unicode_processing_rules(self, value: aspose.pdf.pdfaoptionclasses.ToUnicodeProcessingRules):
        ...
    
    @property
    def icc_profile_file_name(self) -> str:
        '''Gets or sets the filename of icc profile name. In case of null the default icc profile used.'''
        ...
    
    @icc_profile_file_name.setter
    def icc_profile_file_name(self, value: str):
        ...
    
    @property
    def not_accessible_fonts(self) -> list[str]:
        '''This property is out-property. It holds all the fonts(font names) which were not found on computer
        at last PDF/A conversion.'''
        ...
    
    @property
    def is_transfer_info(self) -> bool:
        '''Gets or sets whether to pass data from Info to Metadata when converted to PDF 2.0. True by default.'''
        ...
    
    @is_transfer_info.setter
    def is_transfer_info(self, value: bool):
        ...
    
    @property
    def align_strategy(self) -> None:
        '''Strategy to align text. This parameter has sense only when flag :attr:`PdfFormatConversionOptions.align_text`  is set to true.'''
        ...
    
    @align_strategy.setter
    def align_strategy(self, value: None):
        ...

    class PuaProcessingStrategy:
          '''Some PDF documents have special unicode symbols, which are belonged to Private Use Area (PUA), 
          see description at https://en.wikipedia.org/wiki/Private_Use_Areas.
          This symbols cause an PDF/A compliant errors like "Text is mapped to Unicode Private Use Area but no ActualText entry is present".
          This enumeration declares a strategies which can be used to handle PUA symbols.'''

          NONE: PuaProcessingStrategy
          SURROUND_PUA_TEXT_WITH_EMPTY_ACTUAL_TEXT: PuaProcessingStrategy
          SUBSTITUTE_PUA_SYMBOLS: PuaProcessingStrategy

    class RemoveFontsStrategy:
          '''Some documens have large size after converison into PDF/A format. To reduce file size for these
          documents it's necessary to define a strategy of fonts removing. 
          This enumeration declares a strategies which can be used to optimize fonts usage.
          Every strategy from this enumeration has sense only when flag <see cref="OptimizeFileSize"/> is set.'''

          REMOVE_DUPLICATED_FONTS: RemoveFontsStrategy
          REMOVE_SIMILAR_FONTS_WITH_DIFFERENT_WIDTHS: RemoveFontsStrategy
          SUBSET_FONTS: RemoveFontsStrategy

    class SegmentAlignStrategy:
          ''' Describes strategies used to align document text segments.
          Now only strategy to restore segments to original bounds is supported.
          In future another strategies could be added.'''

          NONE: SegmentAlignStrategy
          RESTORE_SEGMENT_BOUNDS: SegmentAlignStrategy
    
    ...

class PdfPageStamp(aspose.pdf.Stamp):
    '''Class represents stamp which uses PDF page as stamp.'''
    
    @overload
    def __init__(self, pdf_page: aspose.pdf.Page):
        '''Constructor of PdfPageStamp.
        
        :param pdf_page: Page which is used for stamping.'''
        ...
    
    @overload
    def __init__(self, file_name: str, page_index: int):
        '''Creates Pdf page stamp from specifed page of the document in specified file.
        
        :param file_name: Name and page of PDF file.
        :param page_index: Index of the page.'''
        ...
    
    @overload
    def __init__(self, stream: Any, page_index: int):
        '''Creates Pdf page stamp from specifed page in the document from the stream.
        
        :param stream: Stream which contains PDF
        :param page_index: Index of the page.'''
        ...
    
    def put(self, page: aspose.pdf.Page) -> None:
        '''Put stamp on the specified page.
        
        :param page: Page where stamp will be placed.'''
        ...
    
    @property
    def pdf_page(self) -> aspose.pdf.Page:
        '''Gets or sets page which will be used as stamp.'''
        ...
    
    @pdf_page.setter
    def pdf_page(self, value: aspose.pdf.Page):
        ...
    
    ...

class PdfSaveOptions(aspose.pdf.SaveOptions):
    '''Save options for export to Pdf format'''
    
    def __init__(self):
        ...
    
    @property
    def temp_path(self) -> str:
        '''Path for temporary files.'''
        ...
    
    @temp_path.setter
    def temp_path(self, value: str):
        ...
    
    @property
    def default_font_name(self) -> str:
        '''Font name used by default for fonts which are absent on computer.
        When the PDF document that is saved into PDF contains fonts, that are not available
        in the document itself and on the device, API replaces this fonts with the
        default font(if font with :attr:`PdfSaveOptions.default_font_name` is found on device)'''
        ...
    
    @default_font_name.setter
    def default_font_name(self, value: str):
        ...
    
    ...

class PdfXmlLoadOptions(aspose.pdf.LoadOptions):
    '''Load options for PdfXml format.'''
    
    def __init__(self):
        ...
    
    ...

class PdfXmlSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for PdfXml format.'''
    
    def __init__(self):
        ...
    
    ...

class Point:
    '''Represent point with fractional coordinates.'''
    
    def __init__(self, x: float, y: float):
        '''Initializes new instance of the :class:`Point`.
        
        :param x: x coordinate value.
        :param y: y coordinate value.'''
        ...
    
    def to_point(self) -> aspose.pydrawing.PointF:
        '''Converts point into System.Drawing.PointF object.
        
        :returns: PointF structure.'''
        ...
    
    @staticmethod
    def distance(self, point1: aspose.pdf.Point, point2: aspose.pdf.Point) -> float:
        '''Calculates distance between two points.
        
        :param point1: The first point.
        :param point2: The second point.
        :returns: Distance between two points.'''
        ...

    @property
    def x(self) -> float:
        '''X coordinate value.'''
        ...
    
    @x.setter
    def x(self, value: float):
        ...
    
    @property
    def y(self) -> float:
        '''Y coordinate value.'''
        ...
    
    @y.setter
    def y(self, value: float):
        ...
    
    trivial: aspose.pdf.Point
    
    ...

class Point3D:
    '''Represent point with fractional coordinates.'''
    
    def __init__(self, x: float, y: float, z: float):
        '''Initializes new instance of the :class:`Point3D`.
        
        :param x: x coordinate value.
        :param y: y coordinate value.
        :param z: z coordinate value.'''
        ...
    
    @property
    def x(self) -> float:
        '''X coordinate value.'''
        ...
    
    @x.setter
    def x(self, value: float):
        ...
    
    @property
    def y(self) -> float:
        '''Y coordinate value.'''
        ...
    
    @y.setter
    def y(self, value: float):
        ...
    
    @property
    def z(self) -> float:
        '''Z coordinate value.'''
        ...
    
    @z.setter
    def z(self, value: float):
        ...
    
    trivial: aspose.pdf.Point3D
    
    ...

class PptxSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to SVG format'''
    
    def __init__(self):
        ...
    
    @property
    def slides_as_images(self) -> bool:
        '''If set to true then all the content is recognized as images (one per page)'''
        ...
    
    @slides_as_images.setter
    def slides_as_images(self, value: bool):
        ...
    
    @property
    def image_resolution(self) -> int:
        '''Gets or sets the image resolution (dpi). Default is 192 dpi.'''
        ...
    
    @image_resolution.setter
    def image_resolution(self, value: int):
        ...
    
    @property
    def separate_images(self) -> bool:
        '''If set to true then images are separated from all other graphics'''
        ...
    
    @separate_images.setter
    def separate_images(self, value: bool):
        ...
    
    @property
    def optimize_text_boxes(self) -> bool:
        '''Toggles text columns recognition'''
        ...
    
    @optimize_text_boxes.setter
    def optimize_text_boxes(self, value: bool):
        ...
    
    ...

class PsLoadOptions(aspose.pdf.LoadOptions):
    '''Represents options for loading/importing of .mht-file into pdf document.'''
    
    def __init__(self):
        ...
    
    @property
    def fonts_folders(self) -> list[str]:
        '''Gets or sets fonts folders paths.'''
        ...
    
    @fonts_folders.setter
    def fonts_folders(self, value: list[str]):
        ...
    
    ...

class PsSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to PS (PostScript) or EPS format.'''
    
    @overload
    def __init__(self):
        '''Constructor.'''
        ...
    
    @overload
    def __init__(self, save_format: aspose.pdf.SaveFormat):
        '''Constructor.
        
        :param save_format: Save format.'''
        ...
    
    @property
    def embed_font(self) -> bool:
        '''Gets/sets flag that indicates if fonts must be embedded in resulting PS document.'''
        ...
    
    @embed_font.setter
    def embed_font(self, value: bool):
        ...
    
    @property
    def embed_font_as(self) -> str:
        '''Gets/sets type in which fonts must be embedded in resulting PS document.'''
        ...
    
    @embed_font_as.setter
    def embed_font_as(self, value: str):
        ...
    
    ...

class Rectangle:
    '''Class represents rectangle.'''
    
    def __init__(self, llx: float, lly: float, urx: float, ury: float, normalize_coordinates: bool):
        '''Constructor of Rectangle.
        
        :param llx: X of lower left corner.
        :param lly: Y of lower left corner.
        :param urx: X of upper right corner.
        :param ury: Y of upper right corner.
        :param normalize_coordinates: Normalize coordinates of rectangle.'''
        ...
    
    @overload
    def rotate(self, angle: aspose.pdf.Rotation) -> None:
        '''Rotate rectangle by the specified angle.
        
        :param angle: Angle of rotation. Member of Rotation enumeration.'''
        ...
    
    @overload
    def rotate(self, angle: int) -> None:
        '''Rotate rectangle by the specified angle.
        
        :param angle: Angle of rotation in degrees between 0 and 360.'''
        ...
    
    def to_rect(self) -> aspose.pydrawing.Rectangle:
        '''Converts rectangle to instance of System.Drawing.Rectangle. Floating-point positions and size are truncated.
        
        :returns: Result of conversion.'''
        ...
    
    @staticmethod
    def from_rect(self, src: aspose.pydrawing.Rectangle) -> aspose.pdf.Rectangle:
        '''Initializes new rectangle from given instance of System.Drawing.Rectangle.
        
        :param src: Source rectangle which position and size will be set to new rectangle.
        :returns: New rectangle.'''
        ...
    
    @staticmethod
    def parse(self, value: str) -> aspose.pdf.Rectangle:
        '''Try to parse string and extract from it rectangle components llx, lly, urx, ury.
        
        :param value: String to parse.
        :returns: Rectangle object.'''
        ...
    
    def equals(self, other: aspose.pdf.Rectangle) -> bool:
        '''Check if rectangles are equal i.e. have same position and sizes.
        
        :param other: Rectangle which will be compared.
        :returns: True if rectangles are eqals, false otherwise.'''
        ...
    
    def near_equals(self, other: aspose.pdf.Rectangle, delta: float) -> bool:
        '''Check if rectangles are near equal i.e. have near same (up to delta) position and sizes.
        
        :param other: Rectangle which will be compared.
        :param delta: Value of comparation tollerance.
        :returns: True if rectangles are eqals, false otherwise.'''
        ...
    
    def intersect(self, other_rect: aspose.pdf.Rectangle) -> aspose.pdf.Rectangle:
        '''Intersects to rectangles.
        
        :param other_rect: Rectangle to which this recatangle be intersected.
        :returns: Intersection of rectangles; null if rectangles are not intersected.'''
        ...
    
    def join(self, other_rect: aspose.pdf.Rectangle) -> aspose.pdf.Rectangle:
        '''Joins rectangles.
        
        :param other_rect: Rectangle to which this recatangle be joined.
        :returns: Described rectangle.'''
        ...
    
    def is_intersect(self, other_rect: aspose.pdf.Rectangle) -> bool:
        '''Determines whether this rectangle intersects with other rectangle.
        
        :param other_rect: Intersection will be tested with specified rectangle.
        :returns: True if this rectangle intersects with specified rectangle. Otherwise false.'''
        ...
    
    def contains(self, point: aspose.pdf.Point) -> bool:
        '''Determinces whether given point is inside of the rectangle.
        
        :param point: Point to check.
        :returns: True if point is inside of the recatngle.'''
        ...
    
    def contains_line(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        '''Determines whether the rectangle contains a line represented by two points.
        
        :param x1: The X coordinate of the start point of the line.
        :param y1: The Y coordinate of the start point of the line.
        :param x2: The X coordinate of the end point of the line.
        :param y2: The Y coordinate of the end point of the line.
        :returns: true if the rectangle contains the line; otherwise, false.'''
        ...
    
    def contains_point(self, x: float, y: float) -> bool:
        '''Determines whether the given point is contained within the rectangle.
        
        :param x: X-coordinate of the point.
        :param y: Y-coordinate of the point.
        :returns: true if the point is contained within the rectangle; otherwise, false.'''
        ...

    def center(self) -> aspose.pdf.Point:
        '''Returncs coordinates of center of the rectangle.
        
        :returns: Point which is center of the rectangle.'''
        ...
    
    def clone(self) -> object:
        '''Clones the Rectangle object.
        
        :returns: Clone object.'''
        ...
    
    def to_points(self) -> list[aspose.pdf.Point]:
        '''Converts rectangle into array of points ("QuadPoints").
        
        :returns: Array of points.'''
        ...
    
    @property
    def width(self) -> float:
        '''Width of rectangle.'''
        ...
    
    @property
    def height(self) -> float:
        '''Height of rectangle.'''
        ...
    
    @property
    def llx(self) -> float:
        '''X-coordinate of lower - left corner.'''
        ...
    
    @llx.setter
    def llx(self, value: float):
        ...
    
    @property
    def lly(self) -> float:
        '''Y - coordinate of lower-left corner.'''
        ...
    
    @lly.setter
    def lly(self, value: float):
        ...
    
    @property
    def urx(self) -> float:
        '''X - coordinate of upper-right corner.'''
        ...
    
    @urx.setter
    def urx(self, value: float):
        ...
    
    @property
    def ury(self) -> float:
        '''Y - coordinate of upper-right corner.'''
        ...
    
    @ury.setter
    def ury(self, value: float):
        ...
    
    trivial: aspose.pdf.Rectangle
    
    @property
    def is_trivial(self) -> bool:
        '''Checks if rectangle is trivial i.e. has zero size and position.'''
        ...
    
    @property
    def is_empty(self) -> bool:
        '''Checks if rectangle is empty.'''
        ...
    
    @property
    def is_point(self) -> bool:
        '''Checks if rectangle is point i.e. LLX is equal URX and LLY is equal URY.'''
        ...
    
    empty: aspose.pdf.Rectangle
    
    ...

class RenderingOptions:
    '''Represents rendering options.'''
    
    def __init__(self):
        ...
    
    @property
    def barcode_optimization(self) -> bool:
        '''Gets or sets barcode optimization mode.'''
        ...
    
    @barcode_optimization.setter
    def barcode_optimization(self, value: bool):
        ...
    
    @property
    def optimize_dimensions(self) -> bool:
        '''Gets or sets optimize dimensions mode.'''
        ...
    
    @optimize_dimensions.setter
    def optimize_dimensions(self, value: bool):
        ...
    
    @property
    def system_fonts_native_rendering(self) -> bool:
        '''Gets or sets a mode where system fonts are rendered natively.'''
        ...
    
    @system_fonts_native_rendering.setter
    def system_fonts_native_rendering(self, value: bool):
        ...
    
    @property
    def use_new_imaging_engine(self) -> bool:
        '''Gets or sets a flag determines whether new imaging engine is used or not.'''
        ...
    
    @use_new_imaging_engine.setter
    def use_new_imaging_engine(self, value: bool):
        ...
    
    @property
    def width_extra_units(self) -> float:
        '''Gets or sets a value used to increase or decrease the width of rectangle for AppendRectangle operator.'''
        ...
    
    @width_extra_units.setter
    def width_extra_units(self, value: float):
        ...
    
    @property
    def height_extra_units(self) -> float:
        '''Gets or sets a value used to increase or decrease the width of rectangle for AppendRectangle operator.'''
        ...
    
    @height_extra_units.setter
    def height_extra_units(self, value: float):
        ...
    
    @property
    def convert_fonts_to_unicode_ttf(self) -> bool:
        '''Indicates that all fonts will be converted to TTF unicode versions. That is useful for compatibility
        reasons and to optimize font usage, cause every new TTF font will have not all the symbols
        from source font, but only symbols which are used in text.'''
        ...
    
    @convert_fonts_to_unicode_ttf.setter
    def convert_fonts_to_unicode_ttf(self, value: bool):
        ...
    
    @property
    def use_font_hinting(self) -> bool:
        '''Usage of this flag turn on font hinting mechanism. Font hinting is the use of mathematical instructions to adjust the display
        of an outline font. In some cases turning this flag on may solve problems with text legibility.
        At current moment usage of this flag could give effect only for TTF fonts, if these fonts are used in source document.'''
        ...
    
    @use_font_hinting.setter
    def use_font_hinting(self, value: bool):
        ...
    
    @property
    def scale_images_to_fit_page_width(self) -> bool:
        '''Gets or sets a values used to scale all images on the page to fit page's width.'''
        ...
    
    @scale_images_to_fit_page_width.setter
    def scale_images_to_fit_page_width(self, value: bool):
        ...
    
    @property
    def interpolation_high_quality(self) -> bool:
        '''Gets or sets hiqh quality mode for interpolation.'''
        ...
    
    @interpolation_high_quality.setter
    def interpolation_high_quality(self, value: bool):
        ...
    
    @property
    def max_fonts_cache_size(self) -> int:
        '''Maximum count of fonts in fonts cache. Default value is 10.'''
        ...
    
    @max_fonts_cache_size.setter
    def max_fonts_cache_size(self, value: int):
        ...
    
    @property
    def max_symbols_cache_size(self) -> int:
        '''Maximum count of symbols in symbol cache. Default value is 100.'''
        ...
    
    @max_symbols_cache_size.setter
    def max_symbols_cache_size(self, value: int):
        ...
    
    @property
    def default_font_name(self) -> str:
        '''Gets/sets the default name of font used to substitute of missing fonts.'''
        ...
    
    @default_font_name.setter
    def default_font_name(self, value: str):
        ...
    
    @property
    def ignore_resource_font_errors(self) -> bool:
        '''Gets or sets indication that errors related to absence of font will be ignored.
        true - means that errors of absence of font will be ignored. Text segments that refer to incorrect resources will be skipped during processing.
        false by default'''
        ...
    
    @ignore_resource_font_errors.setter
    def ignore_resource_font_errors(self, value: bool):
        ...
    
    ...

class Resources:
    '''Class representing page resources.'''
    
    def get_fonts(self, create_if_absent: bool) -> aspose.pdf.text.FontCollection:
        '''Returns fonts collection. If resources don't contain fonts entry it will be created in depends of CreateIfAbsent flag.
        
        :param create_if_absent: If this flag is true then fonts will be created if this entry is absent.
        :returns: Fonts collection.'''
        ...
    
    def free_memory(self) -> None:
        '''Clears cached data, frees memory etc.'''
        ...

    @property
    def forms(self) -> aspose.pdf.XFormCollection:
        '''Gets :attr:`Resources.forms` forms collection'''
        ...
    
    @property
    def images(self) -> aspose.pdf.XImageCollection:
        '''Gets :attr:`Resources.images` images collection'''
        ...
    
    @property
    def fonts(self) -> aspose.pdf.text.FontCollection:
        '''Gets :attr:`Resources.fonts` resources collection'''
        ...

    class ExtGStateValue:
          '''Represents ExtGStates with some values.'''

          def __init__(self, name: str):
               
              ...
    
          @property
          def name(self) -> str:
            
              ...
          
    ...

class RgbToDeviceGrayConversionStrategy:
    '''Represents rgb to device gray color spaces conversion strategy.'''
    
    def __init__(self):
        ...
    
    def convert(self, page: aspose.pdf.Page) -> None:
        '''Converts the page of document.
        
        :param page: The page of document.'''
        ...
    
    ...

class Row:
    '''Represents a row of the table.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> object:
        '''Clone the row.
        
        :returns: The cloned object'''
        ...
    
    @property
    def background_color(self) -> aspose.pdf.Color:
        '''Gets or sets the background color.'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def border(self) -> aspose.pdf.BorderInfo:
        '''Gets or sets the border.'''
        ...
    
    @border.setter
    def border(self, value: aspose.pdf.BorderInfo):
        ...
    
    @property
    def cells(self) -> aspose.pdf.Cells:
        '''Gets the cells of the row.'''
        ...
    
    @cells.setter
    def cells(self, value: aspose.pdf.Cells):
        ...
    
    @property
    def default_cell_border(self) -> aspose.pdf.BorderInfo:
        '''Gets default cell border;'''
        ...
    
    @default_cell_border.setter
    def default_cell_border(self, value: aspose.pdf.BorderInfo):
        ...
    
    @property
    def min_row_height(self) -> float:
        '''Gets height for row;'''
        ...
    
    @min_row_height.setter
    def min_row_height(self, value: float):
        ...
    
    @property
    def fixed_row_height(self) -> float:
        '''Gets fixed row height - row may have fixed height;'''
        ...
    
    @fixed_row_height.setter
    def fixed_row_height(self, value: float):
        ...
    
    @property
    def is_in_new_page(self) -> bool:
        '''Gets fixed row is in new page - page with this property should be printed to next page Default false;'''
        ...
    
    @is_in_new_page.setter
    def is_in_new_page(self, value: bool):
        ...
    
    @property
    def is_row_broken(self) -> bool:
        '''Gets is row can be broken between two pages'''
        ...
    
    @is_row_broken.setter
    def is_row_broken(self, value: bool):
        ...
    
    @property
    def default_cell_text_state(self) -> aspose.pdf.text.TextState:
        '''Gets or sets default text state for row cells'''
        ...
    
    @default_cell_text_state.setter
    def default_cell_text_state(self, value: aspose.pdf.text.TextState):
        ...
    
    @property
    def default_cell_padding(self) -> aspose.pdf.MarginInfo:
        '''Gets or sets default margin for row cells'''
        ...
    
    @default_cell_padding.setter
    def default_cell_padding(self, value: aspose.pdf.MarginInfo):
        ...
    
    @property
    def vertical_alignment(self) -> aspose.pdf.VerticalAlignment:
        '''Gets or sets the vertical alignment.'''
        ...
    
    @vertical_alignment.setter
    def vertical_alignment(self, value: aspose.pdf.VerticalAlignment):
        ...
    
    ...

class Rows:
    '''Represents a rows collection of table.'''
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.Row:
        '''Gets or sets row.
        
        :param index: The row index.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.pdf.Row):
        ...
    
    @overload
    def add(self) -> aspose.pdf.Row:
        '''Add row to collection.
        
        :returns: The new row'''
        ...
    
    @overload
    def add(self, row: aspose.pdf.Row) -> None:
        '''Add row to cellection.
        
        :param row: The new row.'''
        ...
    
    def index_of(self, row: aspose.pdf.Row) -> int:
        '''Returns index of row in collection.
        
        :param row: The existing row.
        :returns: The row index'''
        ...
    
    def remove(self, row: aspose.pdf.Row) -> None:
        '''Remove row from collection.
        
        :param row: The existing row.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Remove row at position from collection.
        
        :param index: The collection index.'''
        ...
    
    def remove_range(self, index: int, count: int) -> None:
        '''Remove row set from collection.
        
        :param index: The collection index.
        :param count: The rows count.'''
        ...
    
    def dispose(self) -> None:
        '''Dispose.'''
        ...
    
    @property
    def count(self) -> int:
        '''The items count.'''
        ...
    
    ...

class SaveOptions:
    '''SaveOptions type hold level of abstraction on individual save options'''
    
    @property
    def warning_handler(self) -> aspose.pdf.IWarningCallback:
        '''Callback to handle any warnings generated.
        The WarningHandler returns ReturnAction enum item specifying either Continue or Abort.
        Continue is the default action and the Save operation continues, however the user may also return Abort in which case the Save operation should cease.'''
        ...
    
    @warning_handler.setter
    def warning_handler(self, value: aspose.pdf.IWarningCallback):
        ...
    
    @property
    def save_format(self) -> aspose.pdf.SaveFormat:
        '''Format of data save.'''
        ...
    
    @property
    def close_response(self) -> bool:
        '''Gets or sets boolean value which indicates will Response object be closed after document saved into response.'''
        ...
    
    @close_response.setter
    def close_response(self, value: bool):
        ...

    @property
    def cache_glyphs(self) -> bool:
        '''Gets or sets boolean value which indicates if will font glyphs be cached while preparing aps pages.
        Improves performance of conversion pdf to other formats but increases memory consumption.'''
        ...
    
    @cache_glyphs.setter
    def cache_glyphs(self, value: bool):
        ...
    
    class BorderInfo:
          '''Instance of this class represents information about border. That can be drown on some result document.'''

          def __init__(self):
              '''Creates instance of BorderInfo class'''
               
              ...

          def __init__(self, common_style: aspose.pdf.SaveOptions.BorderPartStyle):
              '''Creates instance of BorderInfo class and initializes all elements of border(Top, Left, Right, Bottom) with attributes copied from supplied border style
              :param common_style: style of border parts that will be used for all elements of border(left, right, top, bottom).'''
              ...
    
          @property
          def top_style_if_any(self) -> aspose.pdf.SaveOptions.BorderPartStyle:
              '''Represents top part(if any) of border'''
              ...

          @property
          def left_style_if_any(self) -> aspose.pdf.SaveOptions.BorderPartStyle:
              '''Represents left part(if any) of border'''
              ...

          @property
          def right_style_if_any(self) -> aspose.pdf.SaveOptions.BorderPartStyle:
              '''Represents right part(if any) of border'''
              ...

          @property
          def bottom_style_if_any(self) -> aspose.pdf.SaveOptions.BorderPartStyle:
              '''Represents bottom part(if any) of border'''
              ...


    class BorderPartStyle:
          '''Represents information of one part of border(top, bottom, left side or right side).'''

          def __init__(self):
               
              ...
    
          @property
          def width_in_points(self) -> int:
              '''Represents border line's width in points. Must be number greater then zero.'''
              ...

          @width_in_points.setter
          def width_in_points(self, value: int):
              ...

          @property
          def color(self) -> Any:
              '''Represents border line's line color'''
              ...

          @property
          def line_type(self) -> aspose.pdf.SaveOptions.HtmlBorderLineType:
              '''Represents border line's type - f.e. Dashed or Solid'''
              ...

    class MarginInfo:
          '''Instance of this class represents information about page margin. That can be drown on some result document.'''

          def __init__(self):
              '''Creates instance of MarginInfo'''
               
              ...

          def __init__(self, common_margin: aspose.pdf.SaveOptions.MarginPartStyle):
              '''Creates instance of MarginInfo class and initializes all elements of page margin(Top, Left, Right, Bottom) with attributes copied from supplied margin style
              :param common_margin: style of margin parts that will be used for all elements of margin(left, right, top, bottom)'''
              ...
    
          @property
          def top_margin_if_any(self) -> aspose.pdf.SaveOptions.MarginPartStyle:
              '''Represents top page margin(if any)'''
              ...

          @property
          def left_margin_if_any(self) -> aspose.pdf.SaveOptions.MarginPartStyle:
              '''Represents left page margin(if any)'''
              ...

          @property
          def right_margin_if_any(self) -> aspose.pdf.SaveOptions.MarginPartStyle:
              '''Represents right page margin(if any)'''
              ...

          @property
          def bottom_margin_if_any(self) -> aspose.pdf.SaveOptions.MarginPartStyle:
              '''Represents bottom page margin(if any)'''
              ...

    class MarginPartStyle:
          '''Represents information of one part of margin(top, botom, left side or right side)'''

          def __init__(self, value_in_points: int):
               '''Creates instance of MarginPartStyle class and set its value in points
                  :param value_in_points: Integer value in points'''
               ...

          def __init__(self, is_auto: bool):
               '''Creates instance of MarginPartStyle class and initializes its value in points 
                  :param is_auto: Mark margin auto.'''
               ...
    
          @property
          def is_auto(self) -> bool:
              '''Gets or sets a value indicating whether this instance is auto. True if this instance is auto; otherwise, false.'''
              ...

          @is_auto.setter
          def is_auto(self, value: bool):
              ...

          @property
          def value_in_points(self) -> int:
              '''Represents margin in points. Must be number greater then zero.'''
              ...

          @value_in_points.setter
          def value_in_points(self, value: bool):
              ...

    
    class ResourceSavingInfo:
          '''This class represents set of data that related to external resource file's saving that occures during conversion of PDF to some other format (f.e. HTML)'''
    
          @property
          def resource_type(self) -> aspose.pdf.SaveOptions.NodeLevelResourceType:
              '''Set by converter. Supposed file name that goes from converter to code of custom method
                 Can be use in custom code to decide how to process or where save that file'''
              ...

          @property
          def supposed_file_name(self) -> str:
              '''Set by converter. Supposed file name that goes from converter to code of custom method
                 Can be use in custom code to decide how to process or where save that file'''
              ...

          @property
          def content_stream(self) -> Any:
              '''Set by converter. Represents binary content of saved file.'''
              ...

          @property
          def custom_processing_cancelled(self) -> bool:
              '''this flag must set to "true" in custom code if for some reasons proposed file should be processed not with custom code but 
                 with converter's code itself in standard for converter way. 
                 So, it' setting set to true  means that custom code did not process referenced file and 
                 converter must handle it itself (in both sences - for saving somewhere and for naming in referencing file).'''
              ...
          

    class HtmlBorderLineType:
          '''Represents line types that can be used in result document for drawing borders or another lines.'''

          NONE: HtmlBorderLineType
          DOTTED: HtmlBorderLineType
          DASHED: HtmlBorderLineType
          SOLID: HtmlBorderLineType
          DOUBLE: HtmlBorderLineType
          GROOVE: HtmlBorderLineType
          RIDGE: HtmlBorderLineType
          INSET: HtmlBorderLineType
          OUTSET: HtmlBorderLineType

    class NodeLevelResourceType:
          '''Enumerates possible types of saved external resources'''

          IMAGE: NodeLevelResourceType
          FONT: NodeLevelResourceType

    ...

class Stamp:
    '''An abstract class for various kinds of stamps which come as descendants.'''
    
    def put(self, page: aspose.pdf.Page) -> None:
        '''Adds stamp on the page.
        
        :param page: The page to add stamp.'''
        ...
    
    def set_stamp_id(self, value: int) -> None:
        '''Sets stamp Id.
        
        :param value: New value of Stamp ID.'''
        ...
    
    def get_stamp_id(self) -> int:
        '''Returns stamp ID.
        
        :returns: Identifier of the stamp.'''
        ...
    
    @property
    def background(self) -> bool:
        '''Sets or gets a bool value that indicates the content is stamped as background.
        If the value is true, the stamp content is layed at the bottom.
        By defalt, the value is false, the stamp content is layed at the top.'''
        ...
    
    @background.setter
    def background(self, value: bool):
        ...
    
    @property
    def opacity(self) -> float:
        '''Gets or sets a value to indicate the stamp opacity. The value is from 0.0 to 1.0.
        By default the value is 1.0.'''
        ...
    
    @opacity.setter
    def opacity(self, value: float):
        ...
    
    @property
    def outline_opacity(self) -> float:
        '''Gets or sets a value to indicate the stamp outline opacity. The value is from 0.0 to 1.0.
        By default the value is 1.0.'''
        ...
    
    @outline_opacity.setter
    def outline_opacity(self, value: float):
        ...
    
    @property
    def outline_width(self) -> float:
        '''Gets or sets a value of the stamp outline width.
        By default the value is 1.0.'''
        ...
    
    @outline_width.setter
    def outline_width(self, value: float):
        ...
    
    @property
    def rotate(self) -> aspose.pdf.Rotation:
        '''Sets or gets the rotation of stamp content according :class:`Rotation` values.
        Note. This property is for set angles which are multiples of 90 degrees (0, 90, 180, 270 degrees).
        To set arbitrary angle use RotateAngle property.
        If angle set by ArbitraryAngle is not multiple of 90 then Rotate property returns Rotation.None.'''
        ...
    
    @rotate.setter
    def rotate(self, value: aspose.pdf.Rotation):
        ...
    
    @property
    def x_indent(self) -> float:
        '''Horizontal stamp coordinate, starting from the left.'''
        ...
    
    @x_indent.setter
    def x_indent(self, value: float):
        ...
    
    @property
    def y_indent(self) -> float:
        '''Vertical stamp coordinate, starting from the bottom.'''
        ...
    
    @y_indent.setter
    def y_indent(self, value: float):
        ...
    
    @property
    def horizontal_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets or sets Horizontal alignment of stamp on the page.'''
        ...
    
    @horizontal_alignment.setter
    def horizontal_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def vertical_alignment(self) -> aspose.pdf.VerticalAlignment:
        '''Gets or sets vertical alignment of stamp on page.'''
        ...
    
    @vertical_alignment.setter
    def vertical_alignment(self, value: aspose.pdf.VerticalAlignment):
        ...
    
    @property
    def left_margin(self) -> float:
        '''Gets or sets left margin of stamp.'''
        ...
    
    @left_margin.setter
    def left_margin(self, value: float):
        ...
    
    @property
    def right_margin(self) -> float:
        '''Gets or sets right margin of stamp.'''
        ...
    
    @right_margin.setter
    def right_margin(self, value: float):
        ...
    
    @property
    def bottom_margin(self) -> float:
        '''Gets or sets bottom margin of stamp.'''
        ...
    
    @bottom_margin.setter
    def bottom_margin(self, value: float):
        ...
    
    @property
    def top_margin(self) -> float:
        '''Gets or sets top margin of stamp.'''
        ...
    
    @top_margin.setter
    def top_margin(self, value: float):
        ...
    
    @property
    def zoom_x(self) -> float:
        '''Horizontal zooming factor of the stamp. Allows to scale stamp horizontally.'''
        ...
    
    @zoom_x.setter
    def zoom_x(self, value: float):
        ...
    
    @property
    def width(self) -> float:
        '''Desired width of the stamp on the page.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def height(self) -> float:
        '''Desired height of the stamp on the page.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def zoom_y(self) -> float:
        '''Vertical zooming factor of the stamp. Allows to scale stamp vertically.'''
        ...
    
    @zoom_y.setter
    def zoom_y(self, value: float):
        ...
    
    @property
    def zoom(self) -> float:
        '''Zooming factor of the stamp. Allows to scale stamp.
        Please note that pair of properties ZoomX and ZoomY allows to set zoom factor for every axe separately.
        Setting of this property changes both ZoomX and ZoomY properties.
        If ZoomX and ZoomY are different then Zoom property returns ZoomX value.'''
        ...
    
    @zoom.setter
    def zoom(self, value: float):
        ...
    
    @property
    def rotate_angle(self) -> float:
        '''Gets or sets rotate angle of stamp in degrees.
        This property allows to set arbitrary rotate angle.'''
        ...
    
    @rotate_angle.setter
    def rotate_angle(self, value: float):
        ...
    
    ...

class SvgLoadOptions(aspose.pdf.LoadOptions):
    '''Represents options for loading/importing SVG file into pdf document.'''
    
    def __init__(self):
        ...
    
    @property
    def page_info(self) -> aspose.pdf.PageInfo:
        '''Gets or sets page info that should be applied during loading of document.
        NOTE that this parameter only works when ConversionEngine == ConversionEngines.NewEngine'''
        ...
    
    @page_info.setter
    def page_info(self, value: aspose.pdf.PageInfo):
        ...
    
    @property
    def adjust_page_size(self) -> bool:
        '''Adust pdf page size to svg size'''
        ...
    
    @adjust_page_size.setter
    def adjust_page_size(self, value: bool):
        ...
    
    @property
    def conversion_engine(self) -> None:
        '''Allows select conversion engine that will be in use during conversion.
        Currently new engine is in B-testing stage, so this value by default set to
        ConversionEngines.LegacyEngine'''
        ...
    
    @conversion_engine.setter
    def conversion_engine(self, value: None):
        ...

    class ConversionEngines:
          '''Enumerates conversion engines that can be used for conversion.'''

          LEGACY_ENGINE: ConversionEngines
          NEW_ENGINE: ConversionEngines 
    
    ...

class SvgSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to SVG format'''
    
    def __init__(self):
        ...
    
    @property
    def treat_target_file_name_as_directory(self) -> bool:
        '''This options defines whether will be created target directory
        (if absent yet) with same name as requested output file
        instead of requested output file itself.
        It so, that directory will contain all output SVG-images of pages (like described below).
        If no, output files of pages other then first one will be created exactly in requested directory
        as main output file, but will contain in file name suffix _[2...n], that
        is defined by page number, f.e. if You define output file "C:\\AsposeTests\\output.svg"
        and output will contain several svg-files of pages,
        then files of pages will be created also in directory "C:\\AsposeTests\\" and have names 'output.svg', 'output_2.svg', 'output_3.svg' etc.'''
        ...
    
    @treat_target_file_name_as_directory.setter
    def treat_target_file_name_as_directory(self, value: bool):
        ...
    
    @property
    def compress_output_to_zip_archive(self) -> bool:
        '''Specifies whether output will be created as one zip-archive.
        Please refer comment to 'TreatTargetFileNameAsDirectory' options to see rules of naming
        of svg-files of pages for multipage source document, that are also applied to zipped set of output files.'''
        ...
    
    @compress_output_to_zip_archive.setter
    def compress_output_to_zip_archive(self, value: bool):
        ...
    
    @property
    def scale_to_pixels(self) -> bool:
        '''Specifies whether to scale the output document from typographic points to pixels.'''
        ...
    
    @scale_to_pixels.setter
    def scale_to_pixels(self, value: bool):
        ...
    
    
    class SvgImageSavingInfo(aspose.pdf.SaveOptions.ResourceSavingInfo):
          '''This class represents set of data that related to external resource image file's saving during PDF to HTML conversion.'''

          def __init__(self):
              '''creates new instance of SvgImageSavingInfo'''
               
              ...
    
          @property
          def image_type(self) -> aspose.pdf.SvgSaveOptions.SvgExternalImageType:
              '''represent type os saved image referenced in HTML. Set by converter and can be used in custom code to decide what should be done'''
              ...


    class SvgExternalImageType:
          '''Enumerates possible types of image files that can be saved as external resources during Pdf to SVG conversion.'''

          JPEG: SvgExternalImageType
          PNG: SvgExternalImageType
          BMP: SvgExternalImageType
          GIF: SvgExternalImageType
          TIFF: SvgExternalImageType
          UNKNOWN: SvgExternalImageType

    ...

class Table(aspose.pdf.BaseParagraph):
    '''Represents a table that can be added to the page.'''
    
    def __init__(self):
        ...
    
    def clone(self) -> object:
        '''Clone the table.
        
        :returns: The cloned object'''
        ...
    
    def get_width(self) -> float:
        '''Get width.
        
        :returns: The table width'''
        ...
    
    def get_height(self, parent_page: aspose.pdf.Page) -> float:
        '''Get height.
        
        :param parent_page: The table's parent page (optional).
        :returns: The table height.'''
        ...
    
    def set_column_text_state(self, col_number: int, text_state: aspose.pdf.text.TextState) -> None:
        '''Set height.
        
        :param col_number: The column number.
        :param text_state: The text state for column.'''
        ...
    
    def import_array(self, imported_array: list[object], first_filled_row: int, first_filled_column: int, is_left_columns_filled: bool) -> None:
        '''Imports one-dimensional array of data into table. Import goes one cell per each array's item and
        starts from row and column defined in parameters. During import, if detected that necessary rows
        are still absent(i.e. target table is too small to absorb all data), necessary rows will be created
        
        :param imported_array: imported data, nulls will be imported as empty strings
        :param first_filled_row: define number of first target row in target table from wich import will start.
                                 If amount of rows in target table less then required, missing rows will be created first.
        :param first_filled_column: specifies number of first target column in target table , column must be present in target table before start of import
        :param is_left_columns_filled: If 'isLeftColumnsFilled'=false, then in second and all subsequent filled rows cells that are on the left hand from
                                       firstFilledColumn will be skipped'''
        ...
    
    @property
    def background_color(self) -> aspose.pdf.Color:
        '''Gets or sets table background color'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def break_text(self) -> aspose.pdf.text.TextFragment:
        '''Gets or sets break text for table'''
        ...
    
    @break_text.setter
    def break_text(self, value: aspose.pdf.text.TextFragment):
        ...
    
    @property
    def corner_style(self) -> aspose.pdf.BorderCornerStyle:
        '''Gets or sets the styles of the border corners'''
        ...
    
    @corner_style.setter
    def corner_style(self, value: aspose.pdf.BorderCornerStyle):
        ...
    
    @property
    def repeating_rows_style(self) -> aspose.pdf.text.TextState:
        '''Gets the style for repeating rows'''
        ...
    
    @repeating_rows_style.setter
    def repeating_rows_style(self, value: aspose.pdf.text.TextState):
        ...
    
    @property
    def repeating_columns_count(self) -> int:
        '''Gets or sets the maximum columns count for table'''
        ...
    
    @repeating_columns_count.setter
    def repeating_columns_count(self, value: int):
        ...
    
    @property
    def repeating_rows_count(self) -> int:
        '''Gets the first rows count repeated for several pages'''
        ...
    
    @repeating_rows_count.setter
    def repeating_rows_count(self, value: int):
        ...
    
    @property
    def column_widths(self) -> str:
        '''Gets the column widths of the table.'''
        ...
    
    @column_widths.setter
    def column_widths(self, value: str):
        ...
    
    @property
    def broken(self) -> aspose.pdf.TableBroken:
        '''Gets or sets table vertial broken;'''
        ...
    
    @broken.setter
    def broken(self, value: aspose.pdf.TableBroken):
        ...
    
    @property
    def default_cell_border(self) -> aspose.pdf.BorderInfo:
        '''Gets default cell border;'''
        ...
    
    @default_cell_border.setter
    def default_cell_border(self, value: aspose.pdf.BorderInfo):
        ...
    
    @property
    def default_column_width(self) -> str:
        '''Gets default cell border;'''
        ...
    
    @default_column_width.setter
    def default_column_width(self, value: str):
        ...
    
    @property
    def rows(self) -> aspose.pdf.Rows:
        '''Gets the rows of the table.'''
        ...
    
    @property
    def border(self) -> aspose.pdf.BorderInfo:
        '''Gets or sets the border.'''
        ...
    
    @border.setter
    def border(self, value: aspose.pdf.BorderInfo):
        ...
    
    @property
    def default_cell_padding(self) -> aspose.pdf.MarginInfo:
        '''Gets or sets the default cell padding.'''
        ...
    
    @default_cell_padding.setter
    def default_cell_padding(self, value: aspose.pdf.MarginInfo):
        ...
    
    @property
    def default_cell_text_state(self) -> aspose.pdf.text.TextState:
        '''Gets or sets the default cell text state.'''
        ...
    
    @default_cell_text_state.setter
    def default_cell_text_state(self, value: aspose.pdf.text.TextState):
        ...
    
    @property
    def alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets or sets the table alignment.'''
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.pdf.HorizontalAlignment):
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
    def is_broken(self) -> bool:
        '''Gets or sets the table is broken - will be truncated for next page.'''
        ...
    
    @is_broken.setter
    def is_broken(self, value: bool):
        ...
    
    @property
    def is_borders_included(self) -> bool:
        '''Gets or sets border included in column widhts.'''
        ...
    
    @is_borders_included.setter
    def is_borders_included(self, value: bool):
        ...
    
    @property
    def column_adjustment(self) -> aspose.pdf.ColumnAdjustment:
        '''Gets or sets the table column adjustment.'''
        ...
    
    @column_adjustment.setter
    def column_adjustment(self, value: aspose.pdf.ColumnAdjustment):
        ...
    
    ...

class TeXFileSystemInputDirectory:
    '''Implements the regular file system's method for getting a file stream to read from.'''
    
    def __init__(self, base_path: str):
        '''Creates new instance.
        
        :param base_path: The base path of the directory.'''
        ...
    
    ...

class TeXFileSystemOutputDirectory(aspose.pdf.TeXFileSystemInputDirectory):
    '''Implements the regular file system's method for getting a file stream to write to.'''
    
    def __init__(self, base_path: str):
        '''Creates new instance.
        
        :param base_path: The base path of the directory.'''
        ...
    
    ...

class TeXFragment(aspose.pdf.FormattedFragment):
    '''Represents TeX fragment.'''
    
    @overload
    def __init__(self, text: str):
        '''Initializes a new instance of the HtmlFragment class.
        
        :param text: The fragment text'''
        ...
    
    @overload
    def __init__(self, text: str, remove_indents: bool):
        '''Initializes a new instance of the HtmlFragment class.
        
        :param text: The fragment text
        :param remove_indents: Determines whether not to make indents while typesetting LaTeX fragment'''
        ...
    
    def clone(self) -> object:
        '''Clones fragment.
        
        :returns: Cloned fragment.'''
        ...
    
    @property
    def te_x_load_options_of_instance(self) -> aspose.pdf.TeXLoadOptions:
        '''Gets or sets TeXLoadOptions that will be used for loading (and rendering) of LaTeX into this instance of class.
        Please use it when it's necessary use specific setting for import of LaTeX for this or that instance
        (f.e when this or that instance should use specific BasePath for imported LaTeX or should use specific loader of external resources)
        If parameter is default (null), then standard LaTeX loading options will be used.'''
        ...
    
    @te_x_load_options_of_instance.setter
    def te_x_load_options_of_instance(self, value: aspose.pdf.TeXLoadOptions):
        ...
    
    @property
    def latex_load_options_of_instance(self) -> aspose.pdf.TeXLoadOptions:
        '''Gets or sets TeXLoadOptions that will be used for loading (and rendering) of LaTeX into this instance of class.
        Please use it when it's necessary use specific setting for import of LaTeX for this or that instance
        (f.e when this or that instance should use specific BasePath for imported LaTeX or should use specific loader of external resources)
        If parameter is default (null), then standard LaTeX loading options will be used.'''
        ...
    
    @latex_load_options_of_instance.setter
    def latex_load_options_of_instance(self, value: aspose.pdf.TeXLoadOptions):
        ...
    
    ...

class TeXLoadOptions(aspose.pdf.LoadOptions):
    '''Represents options for loading/importing TeX file into PDF document.'''
    
    def __init__(self):
        ...
    
    def get_load_result(self) -> aspose.pdf.TeXLoadResult:
        '''Gets result for TeX load and compiling - did everything go smoothly or were there any comments/errors.
        
        :returns:'''
        ...

    @property
    def job_name(self) -> str:
        '''Gets/set the name of the job.'''
        ...
    
    @job_name.setter
    def job_name(self, value: str):
        ...
    
    @property
    def input_directory(self) -> aspose.pdf.ITeXInputDirectory:
        '''Gets/sets TeX input directory.'''
        ...
    
    @input_directory.setter
    def input_directory(self, value: aspose.pdf.ITeXInputDirectory):
        ...
    
    @property
    def output_directory(self) -> aspose.pdf.ITeXOutputDirectory:
        '''Gets/sets TeX output directory.'''
        ...
    
    @output_directory.setter
    def output_directory(self, value: aspose.pdf.ITeXOutputDirectory):
        ...
    
    
    @property
    def required_input_directory(self) -> aspose.pdf.ITeXInputDirectory:
        '''Gets/sets TeX requires input directory. Required input is the files that are somehow included into the main .tex file,
           e.g., packages for which there's no built-in support..'''
        ...
    
    @required_input_directory.setter
    def required_input_directory(self, value: aspose.pdf.ITeXInputDirectory):
        ...

    @property
    def repeat(self) -> bool:
        '''Gets/sets the flag indicating whether it is necessary to run the TeX job twice in case,
        for example, there are references in input TeX file(s). In general, this behavior is useful when
        the engine collects some data along the typesetting process and stores it in an auxilliary file,
        all at the first run. And at the second run, the engine somehow uses that data.'''
        ...
    
    @repeat.setter
    def repeat(self, value: bool):
        ...
    
    @property
    def subset_fonts(self) -> bool:
        '''Gets/sets the flag indicating whether to subset fonts in output file or not.'''
        ...
    
    @subset_fonts.setter
    def subset_fonts(self, value: bool):
        ...
    
    @property
    def show_terminal_output(self) -> bool:
        '''Gets/sets the flag indicating whether to show terminal output on the console.'''
        ...
    
    @show_terminal_output.setter
    def show_terminal_output(self, value: bool):
        ...
    
    @property
    def date_time(self) -> datetime.datetime:
        '''Gets/sets a certain value for date/time primitives like year, month, day and time.'''
        ...
    
    @date_time.setter
    def date_time(self, value: datetime.datetime):
        ...
    
    @property
    def no_ligatures(self) -> bool:
        '''Gets/sets a flag that cancels ligatures in all fonts.'''
        ...
    
    @no_ligatures.setter
    def no_ligatures(self, value: bool):
        ...
    
    @property
    def rasterize_formulas(self) -> bool:
        '''Gets/sets a flag that allows to rasterize math formulas.'''
        ...
    
    @rasterize_formulas.setter
    def rasterize_formulas(self, value: bool):
        ...
    
    ...

class TeXMemoryOutputDirectory:
    '''Implements fetching an output stream from memory. You can use it, for example,
    when you don't want the accompanying output (like a log file) to be written to
    disk but you'd like to read it afterwards from memory.'''
    
    def __init__(self):
        ...
    
    ...

class TeXSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to TeX format'''
    
    def __init__(self):
        ...
    
    def add_font_encs(self, font_encs: list[str]) -> None:
        '''Adds a font ancoding to the font encoding list
        
        :param font_encs: The font encs.'''
        ...
    
    def clear_font_encs(self) -> None:
        '''Clears the font encoding list'''
        ...
    
    @property
    def out_directory_path(self) -> str:
        '''Output directory path for help files.'''
        ...
    
    @out_directory_path.setter
    def out_directory_path(self, value: str):
        ...
    
    @property
    def pages_count(self) -> int:
        '''Returns the number of pages after conversion.'''
        ...
    
    ...

class TextStamp(aspose.pdf.Stamp):
    '''Reresents textual stamp.'''
    
    @overload
    def __init__(self, value: str):
        '''Initializes a new instance of the :class:`TextStamp` class.
        
        :param value: Stamp value.'''
        ...
    
    @overload
    def __init__(self, value: str, text_state: aspose.pdf.text.TextState):
        '''Initializes a new instance of the :class:`TextStamp` class.
        
        :param value: Stamp value.
        :param text_state: Stamp text state.'''
        ...
    
    @overload
    def __init__(self, formatted_text: aspose.pdf.facades.FormattedText):
        '''Initializes a new instance of the :class:`TextStamp` class with formattedText object
        
        :param formatted_text: FormattedText object which contains text of the stamp.'''
        ...
    
    def put(self, page: aspose.pdf.Page) -> None:
        '''Adds textual stamp on the page.
        
        :param page: Page for stamping.'''
        ...
    
    @property
    def width(self) -> float:
        '''Desired width of the stamp on the page.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def height(self) -> float:
        '''Desired height of the stamp on the page.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def draw(self) -> bool:
        '''This property determines how stamp is drawn on page. If Draw = true stamp is drawn as graphic operators and if draw = false then stamp is drawn as text.'''
        ...
    
    @draw.setter
    def draw(self, value: bool):
        ...
    
    @property
    def treat_y_indent_as_base_line(self) -> bool:
        '''Defines coordinate origin for placing text.
        If TreatYIndentAsBaseLine = true (default when Draw = true) YIndent value will be treated as text base line.
        If TreatYIndentAsBaseLine = false (default when Draw = false) YIndent value will be treated as bottom (descent line) of text.'''
        ...
    
    @treat_y_indent_as_base_line.setter
    def treat_y_indent_as_base_line(self, value: bool):
        ...
    
    @property
    def word_wrap(self) -> bool:
        '''Defines word wrap. If this property set to true and Width value specified, text will be broken in the several lines to fit into specified width. Default value: false.'''
        ...
    
    @word_wrap.setter
    def word_wrap(self, value: bool):
        ...

    @property
    def word_wrap_mode(self) -> None:
        '''Gets or sets the word wrap mode for text rendering.'''
        ...
    
    @word_wrap_mode.setter
    def word_wrap_mode(self, value: None):
        ...

    @property
    def justify(self) -> bool:
        '''Defines text justification. If this property is set to true, both left and right edges of the text are aligned. Default value: false.'''
        ...
    
    @justify.setter
    def justify(self, value: bool):
        ...
    
    @property
    def scale(self) -> bool:
        '''Defines scaling of the text. If this property is set to true and Width value specified, text will be scaled in order to fit to specified width.'''
        ...
    
    @scale.setter
    def scale(self, value: bool):
        ...
    
    @property
    def value(self) -> str:
        '''Gets or sets string value which is used as stamp on the page.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    @property
    def text_state(self) -> aspose.pdf.text.TextState:
        '''Gets text properties of the stamp. See :attr:`TextStamp.text_state` for details.'''
        ...
    
    @property
    def text_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Alignment of the text inside the stamp.'''
        ...
    
    @text_alignment.setter
    def text_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def replacement_font(self) -> aspose.pdf.text.Font:
        '''Gets or sets font used for replacing if user font does not contain required character.'''
        ...
    
    @replacement_font.setter
    def replacement_font(self, value: aspose.pdf.text.Font):
        ...
    
    @property
    def no_character_behavior(self) -> None:
        '''Gets or sets mode that defines behavior in case fonts don't contain requested characters.'''
        ...
    
    @no_character_behavior.setter
    def no_character_behavior(self, value: None):
        ...

    @property
    def max_row_width(self) -> float:
        '''Max row height for WordWrap option.'''
        ...
    
    @max_row_width.setter
    def max_row_width(self, value: float):
        ...

    class NoCharacterAction:
         '''Action to perform if font does not contain required character.'''

         THROW_EXCEPTION: NoCharacterAction
         USE_STANDARD_FONT: NoCharacterAction
         REPLACE_ANYWAY: NoCharacterAction
         USE_CUSTOM_REPLACEMENT_FONT: NoCharacterAction
    ...

class TimestampSettings:
    '''Represents the ocsp settings using during signing process.'''
    
    def __init__(self, server_url: str, basic_auth_credentials: str, digest_hash_algorithm: aspose.pdf.DigestHashAlgorithm):
        '''Initializes a new instance of the :class:`TimestampSettings` class.
        
        :param server_url: The timestamp server url.
        :param basic_auth_credentials: The basic authentication credentials, username and password are combined into a string "username:password".
        :param digest_hash_algorithm: The hash algorithm name, if it is omitted then sha1 is used.'''
        ...
    
    @property
    def server_url(self) -> str:
        '''Gets/sets the timestamp server url.'''
        ...
    
    @server_url.setter
    def server_url(self, value: str):
        ...
    
    @property
    def basic_auth_credentials(self) -> str:
        '''Gets/sets the basic authentication credentials, Username and password are combined into a string "username:password".'''
        ...
    
    @basic_auth_credentials.setter
    def basic_auth_credentials(self, value: str):
        ...
    
    @property
    def digest_hash_algorithm(self) -> aspose.pdf.DigestHashAlgorithm:
        '''Gets/sets the digest algorithm for internal hash functions.'''
        ...
    
    @digest_hash_algorithm.setter
    def digest_hash_algorithm(self, value: aspose.pdf.DigestHashAlgorithm):
        ...
    
    ...

class TocInfo:
    '''Represents table of contents info.'''
    
    def __init__(self):
        '''Initializes a new instance of the :class:`TocInfo` class.'''
        ...
    
    @property
    def column_info(self) -> aspose.pdf.ColumnInfo:
        '''Gets or sets column info.'''
        ...
    
    @column_info.setter
    def column_info(self, value: aspose.pdf.ColumnInfo):
        ...
    
    @property
    def format_array(self) -> list[aspose.pdf.LevelFormat]:
        '''Gets or sets format array for table of contents.'''
        ...
    
    @format_array.setter
    def format_array(self, value: list[aspose.pdf.LevelFormat]):
        ...
    
    @property
    def format_array_length(self) -> int:
        '''Gets or sets format array length'''
        ...
    
    @format_array_length.setter
    def format_array_length(self, value: int):
        ...
    
    @property
    def title(self) -> aspose.pdf.text.TextFragment:
        '''Gets or sets table of contents title.'''
        ...
    
    @title.setter
    def title(self, value: aspose.pdf.text.TextFragment):
        ...
    
    @property
    def is_count_toc_pages(self) -> bool:
        '''Gets or sets is count or passed toc pages.'''
        ...
    
    @is_count_toc_pages.setter
    def is_count_toc_pages(self, value: bool):
        ...
    
    @property
    def page_numbers_prefix(self) -> str:
        '''Gets or sets is prefix before page number.'''
        ...
    
    @page_numbers_prefix.setter
    def page_numbers_prefix(self, value: str):
        ...
    
    @property
    def is_show_page_numbers(self) -> bool:
        '''Gets or sets is show page numbers at Toc.'''
        ...
    
    @is_show_page_numbers.setter
    def is_show_page_numbers(self, value: bool):
        ...
    
    @property
    def line_dash(self) -> aspose.pdf.text.TabLeaderType:
        '''Gets or sets TOC line dash.'''
        ...
    
    @line_dash.setter
    def line_dash(self, value: aspose.pdf.text.TabLeaderType):
        ...
    
    @property
    def copy_to_outlines(self) -> bool:
        '''Gets or sets is TOC copied to outlines.'''
        ...
    
    @copy_to_outlines.setter
    def copy_to_outlines(self, value: bool):
        ...
    
    ...

class TxtLoadOptions(aspose.pdf.LoadOptions):
    '''Load options for TXT to PDF conversion.'''
    
    def __init__(self):
        ...
    
    ...

class UnifiedSaveOptions(aspose.pdf.SaveOptions):
    '''This class represents saving options for saving that
    uses unified conversion way (with unified internal document model)'''
    
    def __init__(self):
        ...
    
    @property
    def extract_ocr_sublayer_only(self) -> bool:
        '''This atrribute turned on functionality for extracting image or text
        for PDF documents with OCR sublayer.'''
        ...
    
    @extract_ocr_sublayer_only.setter
    def extract_ocr_sublayer_only(self, value: bool):
        ...
    
    @property
    def try_merge_adjacent_same_background_images(self) -> bool:
        '''Sometimes PDFs contain background images (of pages or table cells)
        constructed from several same tiling background images put one near other.
        In such case renderers of target formats (f.e MsWord for DOCS format) sometimes generates
        visible boundaries beetween parts of background images,
        cause their techniques of image edge smoothing (anti-aliasing) is different from Acrobat Reader.
        If it looks like exported document contains such visible boundaries between
        parts of same background images, please try use this setting to get rid
        of that unwanted effect.
        ATTENTION! This optimization of quality usually essentially slows down conversion,
        so, please, use this option only when it's really necessary.'''
        ...
    
    @try_merge_adjacent_same_background_images.setter
    def try_merge_adjacent_same_background_images(self, value: bool):
        ...

    @property
    def is_multi_threading(self) -> bool:
        '''Process pages in few threads.'''
        ...
    
    @is_multi_threading.setter
    def is_multi_threading(self, value: bool):
        ...
    

    class ProgressEventHandlerInfo:
          '''This class represents information about conversion progress that can be used in external applicatuion to show conversion progress to end user'''
    
          @property
          def event_type(self) -> aspose.pdf.ProgressEventType:
              '''Type of progress event that occured'''
              ...

          @property
          def value(self) -> int:
              '''current value of progress value'''
              ...

          @property
          def max_value(self) -> int:
              '''maximum possible value of progress value'''
              ...
    ...

class UnsupportedFontTypeException(RuntimeError):
    '''The exception that is thrown when a font type is not supported.'''
    
    def __init__(self, message: str):
        '''Initializes a new instance of the :class:`UnsupportedFontTypeException` class.
        
        :param message: The message.'''
        ...
    
    ...

class WarningInfo:
    '''Immutable object for encapsulating warning information.'''
    
    def __init__(self, type: aspose.pdf.WarningType, message: str):
        '''Constructs instance for gathering information.
        
        :param type: the warning type to set
        :param message: the warning message to set'''
        ...
    
    @property
    def warning_message(self) -> str:
        '''Returns string representation of warning message.
        
        :returns: the warning message'''
        ...
    
    @property
    def warning_type_property(self) -> aspose.pdf.WarningType:
        '''Returns warning type.
        
        :returns: the warning type'''
        ...
    
    ...

class Watermark:
    '''Represents a watermark of the page.'''
    
    @overload
    def __init__(self, image: aspose.pydrawing.Image, rect: aspose.pdf.Rectangle):
        '''Initializes a watermark object with an image and it's position on a page.
        
        :param image: Image of the watermark.
        :param rect: Position of the watermark on the page.'''
        ...
    
    @overload
    def __init__(self, image: aspose.pydrawing.Image):
        '''Initializes a watermark object with an image.
        
        :param image: Image of the watermark.'''
        ...
    
    @property
    def image(self) -> aspose.pydrawing.Image:
        '''Gets an image of the watermark.'''
        ...
    
    @property
    def position(self) -> aspose.pdf.Rectangle:
        '''Gets a position of the watermark's image on a page.'''
        ...
    
    @property
    def available(self) -> bool:
        '''Gets a flag the watermark is present.'''
        ...
    
    ...

class WatermarkArtifact(aspose.pdf.Artifact):
    '''Class describes watermark artifact. This may be used to'''
    
    def __init__(self):
        '''Creates instance of Watermark artifact.'''
        ...
    
    ...

class WebHyperlink(aspose.pdf.Hyperlink):
    '''Represents web hyperlink object.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`WebHyperlink` class.'''
        ...
    
    @overload
    def __init__(self, url: str):
        '''Initializes a new instance of the :class:`WebHyperlink` class.
        
        :param url: Web url for hyperlink.'''
        ...
    
    @property
    def url(self) -> str:
        '''Gets or sets the web url.'''
        ...
    
    @url.setter
    def url(self, value: str):
        ...
    
    ...

class XForm:
    '''Class represent XForm'''
    
    @overload
    def get_resources(self, allow_create: bool) -> aspose.pdf.Resources:
        '''Returns resources of Form X-Object
        
        :param allow_create: If For does not have resources and allowCreate is true, Resources will be automatically created for the form.
        :returns: Resources.'''
        ...
    
    @overload
    def get_resources(self) -> aspose.pdf.Resources:
        '''Returns resources of Form X-Object. If For does not have resources and allowCreate is true, Resources will be automatically created for the form.
        
        :returns: Resources object'''
        ...
    
    @staticmethod
    def create_new_form(self, source: aspose.pdf.Page, document: aspose.pdf.Document) -> aspose.pdf.XForm:
        '''Creates XForm which duplicates contents of the page.
        
        :param source: Source page
        :param document: Document where new XForm will be added.
        :returns: Newly created XForm.'''
        ...
    
    def free_memory(self) -> None:
        '''Clears cached data'''
        ...
    
    @property
    def b_box(self) -> aspose.pdf.Rectangle:
        '''Gets or sets form bounding box.'''
        ...
    
    @b_box.setter
    def b_box(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets form name. Form name is name which used to reference form in XObejct ductionary in page resources.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def it(self) -> str:
        '''Gets form IT. Form IT is a name describing the intent of the XObject.'''
        ...
    
    @property
    def subtype(self) -> str:
        '''Gets form Subtype.'''
        ...

    @property
    def contents(self) -> aspose.pdf.OperatorCollection:
        '''Gets operators of the form.'''
        ...
    
    @property
    def opi(self) -> aspose.pdf.Opi:
        '''Gets The Open Prepress Interface (OPI).'''
        ...
    
    @property
    def matrix(self) -> aspose.pdf.Matrix:
        '''Gets or sets matrix of the form.'''
        ...
    
    @matrix.setter
    def matrix(self, value: aspose.pdf.Matrix):
        ...
    
    @property
    def resources(self) -> aspose.pdf.Resources:
        '''Gets Form XObject resources.'''
        ...
    
    @property
    def rectangle(self) -> aspose.pdf.Rectangle:
        '''Gets or sets rectangel of the form.'''
        ...
    
    ...

class XFormCollection:
    '''Class represents collection of XFormCollection.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.XForm:
        '''Returns XForm by index.
        
        :param index: Index of XFormCollection. XForms numbering is started from 1
        :returns: Retreived XForm'''
        ...
    
    @overload
    def delete(self, index: int) -> None:
        '''Delete XForm from collectin
        
        :param index: Index of XForm which must be deleted'''
        ...
    
    @overload
    def delete(self) -> None:
        '''Deletes all XForms from collection.'''
        ...
    
    @overload
    def delete(self, name: str) -> None:
        '''Deletes XForm from collection by form name.
        
        :param name: Name of XForm to be deleted.'''
        ...
    
    def get_form_name(self, form: aspose.pdf.XForm) -> str:
        '''Returns name of the form in this form collection.
        
        :param form: Form which name is searched.
        :returns: Form name in the collection; Null if form is not contained in the collection.'''
        ...

    def free_memory(self) -> None:
        '''Clears cached data, frees memory etc.'''
        ...

    @property
    def is_synchronized(self) -> bool:
        '''Returns true if object is synchronized.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Synchronization object.'''
        ...
    
    ...

class XImage:
    '''Class representing image X-Object.'''
    
    @overload
    def save(self, stream: Any) -> None:
        '''Saves image data into stream as JPEG image.
        
        :param stream: Stream where image data will be saved.'''
        ...
    
    @overload
    def save(self, stream: Any, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        '''Saves image into stream with requested format.
        
        :param stream: Stream where image will be saved
        :param format: Format which will be used for image enconding. System.Drawing.Imaging.ImageFormat'''
        ...
    
    @overload
    def save(self, stream: Any, resolution: int) -> None:
        '''Saves image data into stream as JPEG image with specified resolution.
        
        :param stream: Stream where image data will be saved.
        :param resolution: Image resolution'''
        ...
    
    @overload
    def save(self, stream: Any, format: aspose.pydrawing.Imaging.ImageFormat, resolution: int) -> None:
        '''Saves image into stream with requested format with specified resolution.
        
        :param stream: Stream where image will be saved
        :param format: Format which will be used for image enconding. System.Drawing.Imaging.ImageFormat
        :param resolution: Image resolution'''
        ...
    
    def rename(self, name: str) -> None:
        '''Renames image and replaces all references to the image with the new name
        
        :param name: New image name.'''
        ...
    
    def add_stencil_mask(self, mask_stream: Any) -> None:
        '''Adds a stencil mask to the XImage.
        
        :param mask_stream: Stencil mask bitmap stream.'''
        ...
 
    def get_color_type(self) -> aspose.pdf.ColorType:
        '''Returns color type of image.
        
        :returns: The color type value.'''
        ...
    
    @staticmethod
    def detect_color_type(self, bmp: aspose.pydrawing.Bitmap) -> aspose.pdf.ColorType:
        ''':param bmp: Image.
        :returns: Color type.'''
        ...
    
    def is_the_same_object(self, image: aspose.pdf.XImage) -> bool:
        '''Returns true if both images references to the same object.
        
        :param image: Image to be compared with "this" image.
        :returns: Boolean value which is true if images references to the same object.'''
        ...
    
    def get_name_in_collection(self) -> str:
        '''Returns name of the image in ints collection.
        
        :returns: Image key (name).'''
        ...
    
    def to_stream(self) -> Any:
        '''Returns the original image stream.
        
        :returns: The original image stream.'''
        ...
    
    @property
    def contains_transparency(self) -> bool:
        '''If the image contains transparancy than return true; otherwise, false.'''
        ...
    
    @property
    def grayscaled(self) -> aspose.pydrawing.Image:
        '''Gets grayscaled version of image.'''
        ...
    
    @property
    def filter_type(self) -> aspose.pdf.ImageFilterType:
        '''Gets image filter type.'''
        ...
    
    @property
    def width(self) -> int:
        '''Gets width of the image.'''
        ...
    
    @property
    def height(self) -> int:
        '''Gets height of the image.'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets image name. Please note that if you change name of the image which has references in page contents, document may became incorrect. Please use XImage.Rename method in this case.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
   
    @property
    def image_mask(self) -> bool:
        '''Gets a flag indicating whether the image shall be treated as an image mask (see 8.9.6, "Masked Images").
        If this flag is true, the value of BitsPerComponent shall be 1 and Mask and ColorSpace shall not be specified; unmasked areas shall bepainted using the current nonstroking colour. Default value: false.'''
        ...
 
    @property
    def metadata(self) -> aspose.pdf.Metadata:
        '''Metadata of the image.'''
        ...
    
    ...

class XImageCollection:
    '''Class representing XImage collection.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.XImage:
        '''Gets image from collection by its index.
        
        :param index: Image index
        :returns: Retrieved image.'''
        ...
    
    @overload
    def add(self, image: aspose.pdf.XImage) -> str:
        '''Adds new image to Image list. This method adds image as reference to the same PdfObject (which allows to decrease file size)
        
        :param image: XImage to be added.
        :returns: Name of the added image.'''
        ...
    
    @overload
    def add(self, image: Any) -> str:
        '''Adds entity to the end of the collection, so entity can be accessed by the last index.
        
        :param image: Stream containing image data (in JPEG format).
        :returns: Name of the added image.'''
        ...
    
    @overload
    def add(self, image: Any, filter_type: aspose.pdf.ImageFilterType) -> str:
        '''Adds entity to the end of the collection, so entity can be accessed by the last index.
        
        :param image: Stream containing image data.
        :param filter_type: The image filter type.
        :returns: Name of the added image.'''
        ...
    
    @overload
    def add(self, image: Any, quality: int) -> None:
        '''Adds entity to the end of the collection, so entity can be accessed by the last index.
        
        :param image: Stream containing image data (in JPEG format).
        :param quality: JPEG quality.'''
        ...
    
    @overload
    def delete(self, index: int) -> None:
        '''Removes index from collection by index.
        
        :param index: Image index.'''
        ...
    
    @overload
    def delete(self, index: int, action: aspose.pdf.ImageDeleteAction) -> None:
        '''Removes image from collection by index performing action specified by action parameter.
        
        :param index: Index of the image to be removed.
        :param action: Action perfromed after image deleting.'''
        ...
    
    @overload
    def delete(self, name: str) -> None:
        '''Removes item from collection by name.
        
        :param name: Name of image which must to be deleted.'''
        ...
    
    @overload
    def delete(self, name: str, action: aspose.pdf.ImageDeleteAction) -> None:
        '''Removes item from collection by name.
        
        :param name: Name of image which must to be deleted.
        :param action: Action to be performed with image object.'''
        ...
    
    @overload
    def delete(self) -> None:
        '''Deletes images from collection.'''
        ...
    
    @overload
    def replace(self, index: int, stream: Any) -> None:
        '''Replace image in collection with another image.
        
        :param index: Index of collection item which will be replaced.
        :param stream: Stream containing image data (in JPEG format).'''
        ...
    
    @overload
    def replace(self, index: int, stream: Any, quality: int, is_black_and_white: bool) -> None:
        '''Replace image in collection with another image.
        
        :param index: Index of collection item which will be replaced.
        :param stream: Stream containing image data (in JPEG format).
        :param quality: Quality of JPEG compression, in percent (valid vaues are 0..100).
        :param is_black_and_white: If true, image is compressed with CCITT compression method which provides better compression for black nad white image. May be used only for black and white images.'''
        ...
    
    @overload
    def replace(self, index: int, stream: Any, quality: int) -> None:
        '''Replace image in collection with another image.
        
        :param index: Index of collection item which will be replaced.
        :param stream: Stream containing image data (in JPEG format).
        :param quality: JPEG quality.'''
        ...
    
    def get_image_name(self, image: aspose.pdf.XImage) -> str:
        '''Returns name in images list which is key of the given image.
        
        :param image: Image to search.
        :returns: Name (key) of the found image; null if images was not found.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Returns true if object is synchronized.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Returns synchronization object.'''
        ...
    
    @property
    def names(self) -> list[str]:
        '''Gets array of image names.'''
        ...
    
    ...

class XmlLoadOptions(aspose.pdf.LoadOptions):
    '''Represents options for loading/importing XML file into pdf document.'''
    
    @overload
    def __init__(self):
        '''Creates :class:`XmlLoadOptions` object without xsl data.'''
        ...
    
    @overload
    def __init__(self, xsl_file: str):
        '''Creates :class:`XmlLoadOptions` object with xsl data.
        
        :param xsl_file: Xsl file to convert xml document into pdf document.'''
        ...
    
    @overload
    def __init__(self, xsl_stream: Any):
        '''Creates :class:`XmlLoadOptions` object with xsl data.
        
        :param xsl_stream: Xsl stream to convert xml document into pdf document.'''
        ...
    
    @property
    def xsl_stream(self) -> Any:
        '''Gets xsl data for converting xml into pdf document.'''
        ...
    
    ...

class XmlSaveOptions(aspose.pdf.SaveOptions):
    '''Save options for export to Xml format'''
    
    def __init__(self):
        ...
    
    ...

class XmpField:
    '''Represents XMP field.'''
    
    def to_structure(self) -> list[aspose.pdf.XmpField]:
        '''Gets value as a structure.
        
        :returns: The tructure.'''
        ...
    
    def to_array(self) -> list[aspose.pdf.XmpValue]:
        '''Gets value as an array.
        
        :returns: The array.'''
        ...
    
    empty: aspose.pdf.XmpField
    
    lang: aspose.pdf.XmpField
    
    @property
    def prefix(self) -> str:
        '''Gets the prefix.'''
        ...
    
    @prefix.setter
    def prefix(self, value: str):
        ...
    
    @property
    def namespace_uri(self) -> str:
        '''Gets the namespace URI.'''
        ...
    
    @namespace_uri.setter
    def namespace_uri(self, value: str):
        ...
    
    @property
    def local_name(self) -> str:
        '''Gets or sets the name of the local.'''
        ...
    
    @local_name.setter
    def local_name(self, value: str):
        ...
    
    @property
    def name(self) -> str:
        '''Gets the name.'''
        ...
    
    @property
    def value(self) -> aspose.pdf.XmpValue:
        '''Gets the value.'''
        ...
    
    @property
    def field_type(self) -> aspose.pdf.XmpFieldType:
        '''Gets the type of the field.'''
        ...
    
    @property
    def is_empty(self) -> bool:
        '''Gets a value indicating whether this instance is empty.'''
        ...
    
    ...

class XmpPdfAExtensionField(aspose.pdf.XmpPdfAExtensionObject):
    '''This schema describes a field in a structured type. It is very similar to the PDF/A Property Value Type
    schema, but defines a field in a structure instead of a property.
    Schema namespace URI: http://www.aiim.org/pdfa/ns/field#
    Required schema namespace prefix: pdfaField.'''
    
    def __init__(self, name: str, value: str, value_type: str, description: str):
        '''Initializes object.
        
        :param name: The field name.
        :param value: The field value.
        :param value_type: The field value type.
        :param description: The field description.'''
        ...
    
    @property
    def name(self) -> str:
        '''Field name. Field names must be valid XML element names.'''
        ...
    
    @property
    def value_type(self) -> str:
        '''Field value type, drawn from XMP Specification 2004, or an embedded PDF/A value type extension
        schema. Predefined XMP type names or names of custom types.'''
        ...
    
    ...

class XmpPdfAExtensionObject:
    '''Represents the base class for field, property, value type instances.'''
    
    @property
    def description(self) -> str:
        '''Gets the description.'''
        ...
    
    @property
    def value(self) -> str:
        '''Gets or sets the value.'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    ...

class XmpPdfAExtensionProperty(aspose.pdf.XmpPdfAExtensionField):
    '''Describes a single property. Schema namespace URI: http://www.aiim.org/pdfa/ns/property#
    Required schema namespace prefix: pdfaProperty'''
    
    def __init__(self, name: str, value: str, value_type: str, category: aspose.pdf.XmpPdfAExtensionCategoryType, description: str):
        '''Initializes new object.
        
        :param name: The property name.
        :param value: The property value.
        :param value_type: The property value type.
        :param category: The property category.
        :param description: The property description.'''
        ...
    
    @property
    def category(self) -> aspose.pdf.XmpPdfAExtensionCategoryType:
        '''Gets the property category.'''
        ...
    
    ...

class XmpPdfAExtensionSchema:
    '''Describes the XMP extension schema which is provided by PDF/A-1.'''
    
    def __init__(self, description: aspose.pdf.XmpPdfAExtensionSchemaDescription):
        '''Initializes new object.
        
        :param description: The schema description.'''
        ...
    
    def add(self, obj: aspose.pdf.XmpPdfAExtensionObject) -> None:
        '''Adds new object into schema.
        
        :param obj: The new object.'''
        ...
    
    def contains(self, obj: aspose.pdf.XmpPdfAExtensionObject) -> bool:
        '''Determines whether obj exists in schema.
        
        :param obj: The obj to find.
        :returns: True - object exists in schema; otherwise, false.'''
        ...
    
    def remove(self, obj: aspose.pdf.XmpPdfAExtensionObject) -> None:
        '''Removes the object from schema.
        
        :param obj: The object to remove.'''
        ...
    
    def get_property(self, name: str) -> aspose.pdf.XmpPdfAExtensionProperty:
        '''Returns PDF/A property by its name.
        
        :param name: Property name.
        :returns: The property.'''
        ...
    
    @property
    def description(self) -> aspose.pdf.XmpPdfAExtensionSchemaDescription:
        '''Gets the schema description.'''
        ...
    
    @property
    def objects(self) -> None:
        '''Gets the list of objects (properties, value types).'''
        ...
    
    DEFAULT_EXTENSION_NAMESPACE_PREFIX: str
    
    DEFAULT_EXTENSION_NAMESPACE_URI: str
    
    DEFAULT_SCHEMA_NAMESPACE_PREFIX: str
    
    DEFAULT_SCHEMA_NAMESPACE_URI: str
    
    DEFAULT_PROPERTY_NAMESPACE_PREFIX: str
    
    DEFAULT_PROPERTY_NAMESPACE_URI: str
    
    DEFAULT_VALUE_TYPE_NAMESPACE_PREFIX: str
    
    DEFAULT_VALUE_NAMESPACE_URI: str
    
    DEFAULT_FIELD_NAMESPACE_PREFIX: str
    
    DEFAULT_FIELD_NAMESPACE_URI: str
    
    RDF_PREFIX: str
    
    RDF_NAMESPACE_URI: str
    
    ...

class XmpPdfAExtensionSchemaDescription:
    '''Represents the description of XMP extension schema which is provided by PDF/A-1.'''
    
    def __init__(self, prefix: str, namespace_uri: str, description: str):
        '''Initializes new object.
        
        :param prefix: The prefix.
        :param namespace_uri: The namespace URI.
        :param description: The optional desciption.'''
        ...
    
    @property
    def prefix(self) -> str:
        '''Gets the prefix.'''
        ...
    
    @property
    def namespace_uri(self) -> str:
        '''Gets the namespace URI.'''
        ...
    
    @property
    def description(self) -> str:
        '''Gets the optional description.'''
        ...
    
    ...

class XmpPdfAExtensionValueType(aspose.pdf.XmpPdfAExtensionObject):
    '''The PDF/A ValueType schema is required for all property value types which are not defined in the XMP 2004 specification, i.e. for value types outside of the following list:
    - Array types (these are container types which may contain one or more fields): Alt, Bag, Seq
    - Basic value types: Boolean, (open and closed) Choice, Date, Dimensions, Integer, Lang Alt, Locale, MIMEType, ProperName, Real, Text, Thumbnail, URI, URL, XPath
    - Media Management value types: AgentName, RenditionClass, ResourceEvent, ResourceRef, Version
    - Basic Job/Workflow value type: Job
    - EXIF schema value types: Flash, CFAPattern, DeviceSettings, GPSCoordinate, OECF/SFR, Rational
    Schema namespace URI: http://www.aiim.org/pdfa/ns/type#
    Required schema namespace prefix: pdfaType'''
    
    def __init__(self, type: str, namespace_uri: str, prefix: str, description: str):
        '''Initializes new object.
        
        :param type: The value type.
        :param namespace_uri: The namespace URI.
        :param prefix: The prefix.
        :param description: The description.'''
        ...
    
    def add(self, field: aspose.pdf.XmpPdfAExtensionField) -> None:
        '''Add new field.
        
        :param field: The field to add.'''
        ...
    
    def add_range(self, fields: list[aspose.pdf.XmpPdfAExtensionField]) -> None:
        '''Adds the range of fields.
        
        :param fields: The fields to add.'''
        ...
    
    def remove(self, field: aspose.pdf.XmpPdfAExtensionField) -> None:
        '''Removes the field from the list of fields.
        
        :param field: The field to remove.'''
        ...
    
    def clear(self) -> None:
        '''Clears all fields.'''
        ...
    
    @property
    def type(self) -> str:
        '''Gets the value type.'''
        ...
    
    @property
    def namespace_uri(self) -> str:
        '''Gets the namespace URI.'''
        ...
    
    @property
    def prefix(self) -> str:
        '''Gets the prefix.'''
        ...
    
    @property
    def fields(self) -> list[aspose.pdf.XmpPdfAExtensionField]:
        '''Gets the list of fields.'''
        ...
    
    ...

class XmpValue:
    '''Represents XMP value'''
    
    @overload
    def __init__(self, value: str):
        '''Constructor for string value.
        
        :param value: String value.'''
        ...
    
    @overload
    def __init__(self, value: int):
        '''Consructor for integer value.
        
        :param value: Integer value.'''
        ...
    
    @overload
    def __init__(self, value: float):
        '''Constructor for floating point Value.
        
        :param value: Double value.'''
        ...
    
    @overload
    def __init__(self, value: datetime.datetime):
        '''Constructor for date time value.
        
        :param value: Date time value.'''
        ...
    
    @overload
    def __init__(self, array: list[aspose.pdf.XmpValue]):
        '''Constructor for array value.
        
        :param array: Array value.'''
        ...
    
    def to_string_value(self) -> str:
        '''Converts to string.
        
        :returns: String value.'''
        ...
    
    def to_integer(self) -> int:
        '''Converts to integer.
        
        :returns: Integer value.'''
        ...
    
    def to_double(self) -> float:
        '''Converts to double.
        
        :returns: Double value.'''
        ...
    
    def to_date_time(self) -> datetime.datetime:
        '''Converts to date time.
        
        :returns: DateTime value.'''
        ...
    
    def to_array(self) -> list[aspose.pdf.XmpValue]:
        '''Returns array.
        
        :returns: Array value'''
        ...
    
    def to_structure(self) -> list[aspose.pdf.XmpField]:
        '''Returns XMP value as structure (set of fields).
        
        :returns: Structure value.'''
        ...
    
    def to_field(self) -> aspose.pdf.XmpField:
        '''Returns XMP value as XMP field.
        
        :returns: Field value.'''
        ...
    
    @property
    def is_string(self) -> bool:
        '''Returns true if value is string.'''
        ...
    
    @property
    def is_integer(self) -> bool:
        '''Returns true if value is integer.'''
        ...
    
    @property
    def is_double(self) -> bool:
        '''Returns true if value is floating point value.'''
        ...
    
    @property
    def is_date_time(self) -> bool:
        '''Returns true if value is DateTime.'''
        ...
    
    @property
    def is_field(self) -> bool:
        '''Returns true if XmpValue is field.'''
        ...
    
    @property
    def is_named_value(self) -> bool:
        '''Returns true if XmpValue is named value.'''
        ...
    
    @property
    def is_raw(self) -> bool:
        '''Value is unsupported/unknown and raw XML code is provided.
        
        :returns: True if value returned as raw data.'''
        ...
    
    @property
    def is_named_values(self) -> bool:
        '''Returns true is XmpValue represents named values.'''
        ...
    
    @property
    def is_structure(self) -> bool:
        '''Returns true is XmpValue represents structure.'''
        ...
    
    @property
    def is_array(self) -> bool:
        '''Returns true is XmpValue is array.'''
        ...
    
    ...

class XpsLoadOptions(aspose.pdf.LoadOptions):
    '''Represents options for loading/importing xps file into pdf document.'''
    
    def __init__(self):
        ...
    
    @property
    def batch_size(self) -> int:
        '''Defines batch size if batched conversion is applicable
        to source and destination formats pair.'''
        ...
    
    @batch_size.setter
    def batch_size(self, value: int):
        ...
    
    ...

class XpsSaveOptions(aspose.pdf.UnifiedSaveOptions):
    '''Save options for export to Xps format'''
    
    def __init__(self):
        ...
    
    @property
    def save_transparent_texts(self) -> bool:
        '''Indicates whether to preserve transparent (OCR'ed) text.'''
        ...
    
    @save_transparent_texts.setter
    def save_transparent_texts(self, value: bool):
        ...
    
    @property
    def batch_size(self) -> int:
        '''Defines batch size if batched conversion is applicable
        to source and destination formats pair.'''
        ...
    
    @batch_size.setter
    def batch_size(self, value: int):
        ...
    
    @property
    def use_new_imaging_engine(self) -> bool:
        '''Gets or sets UseNewImagingEngine option.'''
        ...
    
    @use_new_imaging_engine.setter
    def use_new_imaging_engine(self, value: bool):
        ...
    
    ...

class XslFoLoadOptions(aspose.pdf.XmlLoadOptions):
    '''Represents options for loading/importing XSL-FO file into pdf document.'''
    
    @overload
    def __init__(self):
        '''Creates :class:`XslFoLoadOptions` object without xsl data.'''
        ...
    
    @overload
    def __init__(self, xsl_file: str):
        '''Creates :class:`XslFoLoadOptions` object with xsl data.
        
        :param xsl_file: Xsl file to convert XSL-FO document into pdf document.'''
        ...
    
    @overload
    def __init__(self, xsl_stream: Any):
        '''Creates :class:`XslFoLoadOptions` object with xsl data.
        
        :param xsl_stream: Xsl stream to convert XSL-FO document into pdf document.'''
        ...
    
    @property
    def base_path(self) -> str:
        '''The base path/url from which are searched relative paths to external resources (if any) referenced in loaded SVG file.'''
        ...
    
    @base_path.setter
    def base_path(self, value: str):
        ...
    
    @property
    def parsing_errors_handling_type(self) -> None:
        '''Source XSLFO document can contain formatting errors. This enum enumerates possible strategies of handking of that errors'''
        ...
    
    @parsing_errors_handling_type.setter
    def parsing_errors_handling_type(self, value: None):
        ...
    
    class ParsingErrorsHandlingTypes:
          '''Source XSLFO document can contain formatting errors. This enum enumerates possible strategies of handling of such formatting errors'''
          
          TRY_IGNORE: ParsingErrorsHandlingTypes
          THROW_EXCEPTION_IMMEDIATELY: ParsingErrorsHandlingTypes
          INVOKE_CUSTOM_HANDLER: ParsingErrorsHandlingTypes

    ...

class AFRelationship:
    '''Enumeration describes associated files relationship.'''
    
    SOURCE: AFRelationship
    DATA: AFRelationship
    ALTERNATIVE: AFRelationship
    SUPPLEMENT: AFRelationship
    UNSPECIFIED: AFRelationship
    ENCRYPTED_PAYLOAD: AFRelationship
    NONE: AFRelationship

class BlendMode:
    '''The blend modes enumeration.'''
    
    NORMAL: BlendMode
    MULTIPLY: BlendMode
    SCREEN: BlendMode
    OVERLAY: BlendMode
    DARKEN: BlendMode
    LIGHTEN: BlendMode
    COLOR_DODGE: BlendMode
    COLOR_BURN: BlendMode
    HARD_LIGHT: BlendMode
    SOFT_LIGHT: BlendMode
    DIFFERENCE: BlendMode
    EXCLUSION: BlendMode
    HUE: BlendMode
    SATURATION: BlendMode
    COLOR: BlendMode
    LUMINOSITY: BlendMode
    COMPATIBLE: BlendMode

class BorderCornerStyle:
    '''Enumerates the border corner styles for border.'''
    
    NONE: BorderCornerStyle
    ROUND: BorderCornerStyle

class BorderSide:
    '''Enumerates the border sides.'''
    
    NONE: BorderSide
    LEFT: BorderSide
    TOP: BorderSide
    RIGHT: BorderSide
    BOTTOM: BorderSide
    ALL: BorderSide
    BOX: BorderSide

class CollectionFieldSubtype:
    '''Represents the subtype parameter of a field in a sceme collection.'''
    
    NONE: CollectionFieldSubtype
    S: CollectionFieldSubtype
    D: CollectionFieldSubtype
    N: CollectionFieldSubtype
    F: CollectionFieldSubtype
    DESC: CollectionFieldSubtype
    MOD_DATE: CollectionFieldSubtype
    CREATION_DATE: CollectionFieldSubtype
    SIZE: CollectionFieldSubtype
    COMPRESSED_SIZE: CollectionFieldSubtype


class ColorSpace:
    '''The color spaces enumeration.'''
    
    DEVICE_RGB: ColorSpace
    DEVICE_CMYK: ColorSpace
    DEVICE_GRAY: ColorSpace

class ColorType:
    '''Specifies color type of elements on page.'''
    
    RGB: ColorType
    GRAYSCALE: ColorType
    BLACK_AND_WHITE: ColorType
    UNDEFINED: ColorType

class ColumnAdjustment:
    '''Enumerates column adjustment types.'''
    
    CUSTOMIZED: ColumnAdjustment
    AUTO_FIT_TO_CONTENT: ColumnAdjustment
    AUTO_FIT_TO_WINDOW: ColumnAdjustment

class ContentDisposition:
    '''MIME protocol Content-Disposition header.'''
    
    INLINE: ContentDisposition
    ATTACHMENT: ContentDisposition

class ConvertErrorAction:
    '''This class represents action for conversion errors.'''
    
    DELETE: ConvertErrorAction
    NONE: ConvertErrorAction

class ConvertSoftMaskAction:
    '''This action represents actions for conversion of images with soft mask.'''
    
    DEFAULT: ConvertSoftMaskAction
    CONVERT_TO_STENCIL_MASK: ConvertSoftMaskAction

class ConvertTransparencyAction:
    '''This class represents action for conversion of transparency.'''
    
    DEFAULT: ConvertTransparencyAction
    MASK: ConvertTransparencyAction

class CryptoAlgorithm:
    '''Represent type of cryptographic algorithm that used in encryption/decryption routines.'''
    
    RC4X40: CryptoAlgorithm
    RC4X128: CryptoAlgorithm
    AE_SX128: CryptoAlgorithm
    AE_SX256: CryptoAlgorithm

class DigestHashAlgorithm:
    '''Represent type of algoritm that maps data to a "hash"'''
    
    SHA1: DigestHashAlgorithm
    SHA256: DigestHashAlgorithm
    SHA512: DigestHashAlgorithm

class Direction:
    '''Text direction.'''
    
    L2R: Direction
    R2L: Direction

class ExtendedBoolean:
    '''Represents boolean type that supports Undefined value.'''
    
    UNDEFINED: ExtendedBoolean
    FALSE: ExtendedBoolean
    TRUE: ExtendedBoolean

class ExtractImageMode:
    '''Defines different modes which can be used while extracting images from documents.'''
    
    DEFINED_IN_RESOURCES: ExtractImageMode
    ACTUALLY_USED: ExtractImageMode

class FieldValueType:
    '''Represents the type of a field value in a schema collection.'''
    
    NONE: FieldValueType
    TEXT: FieldValueType
    NUMBER: FieldValueType
    DATE: FieldValueType

class FileEncoding:
    '''Encoding of the attached file. Possible values: Zip - file is compressed with ZIP, None - file is non compressed.'''
    
    NONE: FileEncoding
    ZIP: FileEncoding

class Fixup:
    '''This enum represents an type of Fixup.'''
    
    CONVERT_ALL_PAGES_INTO_CMYK_IMAGES_AND_PRESERVE_TEXT_INFORMATION: Fixup
    CONVERT_FONTS_TO_OUTLINES: Fixup
    DERIVE_PAGE_GEOMETRY_BOXES_FROM_CROP_MARKS: Fixup
    EMBED_MISSING_FONTS: Fixup
    ROTATE_PAGES_TO_LANDSCAPE: Fixup
    ROTATE_PAGES_TO_PORTRAIT: Fixup

class FontSubsetStrategy:
    '''enumerates strategies for font subsetting'''
    
    SUBSET_EMBEDDED_FONTS_ONLY: FontSubsetStrategy
    SUBSET_ALL_FONTS: FontSubsetStrategy

class HorizontalAlignment:
    '''Describes horizontal alignment.'''
    
    NONE: HorizontalAlignment
    LEFT: HorizontalAlignment
    CENTER: HorizontalAlignment
    RIGHT: HorizontalAlignment
    JUSTIFY: HorizontalAlignment
    FULL_JUSTIFY: HorizontalAlignment

class HtmlDocumentType:
    '''Represents enumeration of the Html document types.'''
    
    XHTML: HtmlDocumentType
    HTML5: HtmlDocumentType

class HtmlMediaType:
    '''Specifies possible media types used during rendering.'''
    
    PRINT: HtmlMediaType
    SCREEN: HtmlMediaType

class HtmlPageLayoutOption:
    '''Specifies flags that together other options determine sizes and layouts of pages.'''
    
    NONE: HtmlPageLayoutOption
    FIT_TO_WIDEST_CONTENT_WIDTH: HtmlPageLayoutOption
    SCALE_TO_PAGE_WIDTH: HtmlPageLayoutOption

class ImageDeleteAction:
    '''Action which performed with image object when image is removed from collection. If image object is removed'''
    
    KEEP_CONTENTS: ImageDeleteAction
    NONE: ImageDeleteAction
    FORCE_DELETE: ImageDeleteAction
    CHECK: ImageDeleteAction

class ImageFileType:
    '''Enumerates the image file types.'''
    
    UNKNOWN: ImageFileType
    SVG: ImageFileType
    DICOM: ImageFileType
    BASE64: ImageFileType

class ImageFilterType:
    '''Enumeration representing image filter type.'''
    
    JPEG2000: ImageFilterType
    JPEG: ImageFilterType
    FLATE: ImageFilterType
    CCITT_FAX: ImageFilterType

class ImportFormat:
    '''Specifies import format.'''
    
    CGM: ImportFormat

class LoadFormat:
    '''Specifies load format.'''
    
    CGM: LoadFormat
    HTML: LoadFormat
    EPUB: LoadFormat
    XML: LoadFormat
    XSLFO: LoadFormat
    PCL: LoadFormat
    XPS: LoadFormat
    TEX: LoadFormat
    SVG: LoadFormat
    MHT: LoadFormat
    PS: LoadFormat
    MD: LoadFormat
    TXT: LoadFormat
    APS: LoadFormat
    PDFXML: LoadFormat
    OFD: LoadFormat
    DJVU: LoadFormat
    CDR: LoadFormat

class NumberingStyle:
    '''Enumeration of supported page numbering style for PageLabel class.'''
    
    NUMERALS_ARABIC: NumberingStyle
    NUMERALS_ROMAN_UPPERCASE: NumberingStyle
    NUMERALS_ROMAN_LOWERCASE: NumberingStyle
    LETTERS_UPPERCASE: NumberingStyle
    LETTERS_LOWERCASE: NumberingStyle
    NONE: NumberingStyle

class PageCoordinateType:
    '''Describes page coordinate type.'''
    
    MEDIA_BOX: PageCoordinateType
    CROP_BOX: PageCoordinateType

class PageLayout:
    '''Descibes page layout.'''
    
    SINGLE_PAGE: PageLayout
    ONE_COLUMN: PageLayout
    TWO_COLUMN_LEFT: PageLayout
    TWO_COLUMN_RIGHT: PageLayout
    TWO_PAGE_LEFT: PageLayout
    TWO_PAGE_RIGHT: PageLayout
    DEFAULT: PageLayout

class PageMode:
    '''Class descibes used components of the document page.'''
    
    USE_NONE: PageMode
    USE_OUTLINES: PageMode
    USE_THUMBS: PageMode
    FULL_SCREEN: PageMode
    USE_OC: PageMode
    USE_ATTACHMENTS: PageMode

class PasswordType:
    '''This enum represents  known password types used for password protected pdf documents.'''
    
    NONE: PasswordType
    USER: PasswordType
    OWNER: PasswordType
    INACCESSIBLE: PasswordType

class PdfFormat:
    '''This class represents an pdf format.'''
    
    PDF_A_1A: PdfFormat
    PDF_A_1B: PdfFormat
    PDF_A_2A: PdfFormat
    PDF_A_3A: PdfFormat
    PDF_A_2B: PdfFormat
    PDF_A_2U: PdfFormat
    PDF_A_3B: PdfFormat
    PDF_A_3U: PdfFormat
    V_1_0: PdfFormat
    V_1_1: PdfFormat
    V_1_2: PdfFormat
    V_1_3: PdfFormat
    V_1_4: PdfFormat
    V_1_5: PdfFormat
    V_1_6: PdfFormat
    V_1_7: PdfFormat
    V_2_0: PdfFormat
    PDF_UA_1: PdfFormat
    PDF_X_1A_2001: PdfFormat
    PDF_X_1A: PdfFormat
    PDF_X_3: PdfFormat
    ZUG_FE_RD: PdfFormat

class Permissions:
    '''This enum represents user's permissions for a pdf.'''
    
    PRINT_DOCUMENT: Permissions
    MODIFY_CONTENT: Permissions
    EXTRACT_CONTENT: Permissions
    MODIFY_TEXT_ANNOTATIONS: Permissions
    FILL_FORM: Permissions
    EXTRACT_CONTENT_WITH_DISABILITIES: Permissions
    ASSEMBLE_DOCUMENT: Permissions
    PRINTING_QUALITY: Permissions

class PrintDuplex:
    '''The paper handling option to use when printing the file from the print dialog..'''
    
    SIMPLEX: PrintDuplex
    DUPLEX_FLIP_SHORT_EDGE: PrintDuplex
    DUPLEX_FLIP_LONG_EDGE: PrintDuplex

class PrintScaling:
    '''The page scaling option that shall be selected when a print dialog is displayed for this document.'''
    
    APP_DEFAULT: PrintScaling
    NONE: PrintScaling

class ProgressEventType:
    '''This enum describes possible progress event types
    that can occure during conversion'''
    
    TOTAL_PROGRESS: ProgressEventType
    SOURCE_PAGE_ANALYSED: ProgressEventType
    RESULT_PAGE_CREATED: ProgressEventType
    RESULT_PAGE_SAVED: ProgressEventType

class ReturnAction:
    '''Enum represented a program workflow action in case of invoking the
    :meth:`IWarningCallback.warning` method.'''
    
    CONTINUE: ReturnAction
    ABORT: ReturnAction

class Rotation:
    '''Enumeration of possible rotation values.'''
    
    NONE: Rotation
    ON90: Rotation
    ON180: Rotation
    ON270: Rotation
    ON360: Rotation

class SaveFormat:
    '''Specifies format'''
    
    PDF: SaveFormat
    NONE: SaveFormat
    DOC: SaveFormat
    XPS: SaveFormat
    HTML: SaveFormat
    XML: SaveFormat
    TE_X: SaveFormat
    DOC_X: SaveFormat
    SVG: SaveFormat
    MOBI_XML: SaveFormat
    EXCEL: SaveFormat
    EPUB: SaveFormat
    PPTX: SaveFormat
    APS: SaveFormat
    PDF_XML: SaveFormat
    PS: SaveFormat
    EPS: SaveFormat
    MARKDOWN: SaveFormat

class TabOrder:
    '''Tab order on the page'''
    
    NONE: TabOrder
    ROW: TabOrder
    COLUMN: TabOrder
    DEFAULT: TabOrder
    MANUAL: TabOrder

class TableBroken:
    '''Enumerates the table broken.'''
    
    NONE: TableBroken
    VERTICAL: TableBroken
    VERTICAL_IN_SAME_PAGE: TableBroken
    IS_IN_NEXT_PAGE: TableBroken

class TeXLoadResult:
    '''Results for TeX load and compiling.'''
    
    NOT_EXECUTED: TeXLoadResult
    SPOTLESS: TeXLoadResult
    WARNING_ISSUED: TeXLoadResult
    ERROR_MESSAGE_ISSUED: TeXLoadResult
    FATAL_ERROR_STOP: TeXLoadResult
    INVALID_RESULT: TeXLoadResult

class VerticalAlignment:
    '''Enumeration of possible vertical alignment values.'''
    
    NONE: VerticalAlignment
    TOP: VerticalAlignment
    CENTER: VerticalAlignment
    BOTTOM: VerticalAlignment

class WarningType:
    '''Enum represented warning type.'''
    
    SOURCE_FILE_CORRUPTION: WarningType
    DATA_LOSS: WarningType
    MAJOR_FORMATTING_LOSS: WarningType
    MINOR_FORMATTING_LOSS: WarningType
    COMPATIBILITY_ISSUE: WarningType
    INVALID_INPUT_STREAM_TYPE: WarningType
    UNEXPECTED_CONTENT: WarningType

class XfaTag:
    '''The xfa stream tag'''
    
    TEMPLATE: XfaTag
    DATASETS: XfaTag
    CONFIG: XfaTag
    LOCALSET: XfaTag
    FORM: XfaTag

class XmpFieldType:
    '''This enum represents types of a XMP field.'''
    
    STRUCT: XmpFieldType
    ARRAY: XmpFieldType
    PROPERTY: XmpFieldType
    PACKET: XmpFieldType
    UNKNOWN: XmpFieldType

class XmpPdfAExtensionCategoryType:
    '''Property category: internal or external.'''
    
    INTERNAL: XmpPdfAExtensionCategoryType
    EXTERNAL: XmpPdfAExtensionCategoryType

