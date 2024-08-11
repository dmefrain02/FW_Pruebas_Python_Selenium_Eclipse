import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class ActionCollection:
    '''Collection of actions'''
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.PdfAction:
        '''Gets action by its index.
        
        :param index: Index of action.
        :returns: Retreived action.'''
        ...
    
    @overload
    def delete(self, index: int) -> None:
        '''Removes action from collection by index.
        
        :param index: Index of action to remove.'''
        ...
    
    @overload
    def delete(self) -> None:
        '''Delete all actions.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Returns true if object is synchronized.'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets synchronization object.'''
        ...
    
    ...

class Annotation(aspose.pdf.BaseParagraph):
    '''Class representing annotation object.'''
    
    def get_rectangle(self, consider_rotation: bool) -> aspose.pdf.Rectangle:
        '''Returns rectangle of annotation taking into consideration page rotation.
        
        :param consider_rotation: If true, page rotation is takein into consideration.
        :returns: True - if rectangle found; otherwise, false.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor for annotation processing.
        
        :param visitor: AnnotationSelector object.'''
        ...
    
    def flatten(self) -> None:
        '''Places annotation contents directly on the page,
        annotation object will be removed.'''
        ...
    
    def change_after_resize(self, transform: aspose.pdf.Matrix) -> None:
        '''Update parameters and appearance, according to the matrix transform.
        
        :param transform: Matrix that use for transformation (resize).'''
        ...
    
    @property
    def horizontal_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets or sets text alignment for annotation.'''
        ...
    
    @horizontal_alignment.setter
    def horizontal_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    update_appearance_on_convert: bool
    
    use_font_subset: bool
    
    @property
    def flags(self) -> aspose.pdf.annotations.AnnotationFlags:
        '''Flags of the annotation.'''
        ...
    
    @flags.setter
    def flags(self, value: aspose.pdf.annotations.AnnotationFlags):
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets width of the annotation.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def actions(self) -> aspose.pdf.annotations.PdfActionCollection:
        '''Gets list of annotatation actions.'''
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets height of the annotation.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def rect(self) -> aspose.pdf.Rectangle:
        '''Gets or sets annotation rectangle.'''
        ...
    
    @rect.setter
    def rect(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def contents(self) -> str:
        '''Gets or sets annotation text.'''
        ...
    
    @contents.setter
    def contents(self, value: str):
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets annotation name on the page.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def modified(self) -> datetime.datetime:
        '''Gets or sets date and time when annotation was recently modified.'''
        ...
    
    @modified.setter
    def modified(self, value: datetime.datetime):
        ...
    
    @property
    def color(self) -> aspose.pdf.Color:
        '''Gets or sets annotation color.'''
        ...
    
    @color.setter
    def color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def border(self) -> aspose.pdf.annotations.Border:
        '''Gets or sets annotation border characteristics. :attr:`Annotation.border`'''
        ...
    
    @border.setter
    def border(self, value: aspose.pdf.annotations.Border):
        ...
    
    @property
    def active_state(self) -> str:
        '''Gets or sets current annotation appearance state.'''
        ...
    
    @active_state.setter
    def active_state(self, value: str):
        ...
    
    @property
    def characteristics(self) -> aspose.pdf.annotations.Characteristics:
        '''Gets annotation characteristics.'''
        ...
    
    @property
    def states(self) -> aspose.pdf.annotations.AppearanceDictionary:
        '''Gets appearance dictionary of annotation.'''
        ...
    
    @property
    def alignment(self) -> aspose.pdf.annotations.TextAlignment:
        '''Annotation alignment. This property is obsolete. Use HorizontalAligment instead.'''
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.pdf.annotations.TextAlignment):
        ...
    
    @property
    def text_horizontal_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets or sets text alignment for annotation.'''
        ...
    
    @text_horizontal_alignment.setter
    def text_horizontal_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def full_name(self) -> str:
        '''Gets full qualified name of the annotation.
        
        :returns:'''
        ...
    
    @property
    def appearance(self) -> aspose.pdf.annotations.AppearanceDictionary:
        '''Gets appearance dictionary of the annotation.'''
        ...
    
    @property
    def page_index(self) -> int:
        '''Gets index of page which contains annotation.'''
        ...
    
    ...

class AnnotationActionCollection(aspose.pdf.BaseActionCollection):
    '''Represents the collection of annotation actions.'''
    
    @property
    def on_enter(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the cursor enters the annotation�s active area.'''
        ...
    
    @on_enter.setter
    def on_enter(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_exit(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the cursor exits the annotation�s active area.'''
        ...
    
    @on_exit.setter
    def on_exit(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_press_mouse_btn(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the mouse button is pressed inside the annotation�s active area.'''
        ...
    
    @on_press_mouse_btn.setter
    def on_press_mouse_btn(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_release_mouse_btn(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the mouse button is released inside the annotation�s active area.'''
        ...
    
    @on_release_mouse_btn.setter
    def on_release_mouse_btn(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_receive_focus(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the annotation receives the input focus.'''
        ...
    
    @on_receive_focus.setter
    def on_receive_focus(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_open_page(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the page containing the annotation is opened.'''
        ...
    
    @on_open_page.setter
    def on_open_page(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_close_page(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the page containing the annotation is closed.'''
        ...
    
    @on_close_page.setter
    def on_close_page(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_show_page(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the page containing the annotation becomes visible in the viewer application�s user interface.'''
        ...
    
    @on_show_page.setter
    def on_show_page(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_hide_page(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the page containing the annotation is no longer visible in the viewer application�s user interface.'''
        ...
    
    @on_hide_page.setter
    def on_hide_page(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_lost_focus(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the annotation loses the input focus.'''
        ...
    
    @on_lost_focus.setter
    def on_lost_focus(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_modify_character(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when user modifies character of the field.'''
        ...
    
    @on_modify_character.setter
    def on_modify_character(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_validate(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when user changes contents of the field.'''
        ...
    
    @on_validate.setter
    def on_validate(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_format(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed to format field value.'''
        ...
    
    @on_format.setter
    def on_format(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def on_calculate(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to calculate field value.'''
        ...
    
    @on_calculate.setter
    def on_calculate(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    ...

class AnnotationCollection:
    '''Class representing annotation collection.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.Annotation:
        '''The index of the element to get.
        
        :param index: The index value started from one.
        :returns: Annotation object'''
        ...
    
    @overload
    def delete(self, index: int) -> None:
        '''Deletes annotation from the collection by index.
        
        :param index: Index of annotation which shall be deleted.'''
        ...
    
    @overload
    def delete(self) -> None:
        '''Deletes all annotations from the collection.'''
        ...
    
    @overload
    def delete(self, annotation: aspose.pdf.annotations.Annotation) -> None:
        '''Deletes specified annotation from the collection.
        
        :param annotation: Annotation which shall be deleted.'''
        ...
    
    def add(self, annotation: aspose.pdf.annotations.Annotation, consider_rotation: bool) -> None:
        '''Adds annotation to the collection. If page is rotated then annotation rectangle will be recalculated accordingly.
        
        :param annotation: Annotation which shall be added.
        :param consider_rotation: If true and if page is rotated then annotation position will be recaculated accroding to page rotation.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor to process annotation.
        
        :param visitor: Annotation selector object.'''
        ...
    
    def find_by_name(self, name: str) -> aspose.pdf.annotations.Annotation:
        '''Returns annotation by its name.
        
        :param name: Name of the annotation
        :returns: Annotation object if found; otherwise, null.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Gets a value indicating whether access to the Aspose.Pdf.Annotations.AnnotationCollection is synchronized (thread safe).'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets an object that can be used to synchronize access to Aspose.Pdf.Annotations.AnnotationCollection.'''
        ...
    
    ...

class AnnotationSelector:
    '''This class is used for selecting annotations using Visitor template idea.'''
    
    @overload
    def __init__(self):
        '''Initializes new instance of the AnnotationSelector class.'''
        ...
    
    @overload
    def __init__(self, annotation: aspose.pdf.annotations.Annotation):
        '''Initializes new :class:`AnnotationSelector` object.
        
        :param annotation: Annotation to be selected.
                           This object only describes some characteristics we want found annotations to have, e.g. the type of annotation.'''
        ...
    
    @overload
    def visit(self, link: aspose.pdf.annotations.LinkAnnotation) -> None:
        '''Select link annotation if AnnotationSelector was initialized with LinkAnnotation object.
        
        :param link: LinkAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, attachment: aspose.pdf.annotations.FileAttachmentAnnotation) -> None:
        '''Select attachment annotation if AnnotationSelector was initialized with FileAttachmentAnnotation object.
        
        :param attachment: FileAttachmentAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, text: aspose.pdf.annotations.TextAnnotation) -> None:
        '''Select text annotation if AnnotationSelector was initialized with TextAnnotation object.
        
        :param text: TextAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, redact: aspose.pdf.annotations.RedactionAnnotation) -> None:
        '''Select redact annotation if AnnotationSelector was initialized with RedactAnnotation object.
        
        :param redact: RedactAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, freetext: aspose.pdf.annotations.FreeTextAnnotation) -> None:
        '''Select freetext annotation if AnnotationSelector was initialized with FreeTextAnnotation object.
        
        :param freetext: FreeTextAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, highlight: aspose.pdf.annotations.HighlightAnnotation) -> None:
        '''Select attachment annotation if AnnotationSelector was initialized with FreeTextAnnotation object.
        
        :param highlight: HighlightAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, underline: aspose.pdf.annotations.UnderlineAnnotation) -> None:
        '''Select underline annotation if AnnotationSelector was initialized with UnderlineAnnotation object.
        
        :param underline: UnderlineAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, strike_out: aspose.pdf.annotations.StrikeOutAnnotation) -> None:
        '''Select strikeOut annotation if AnnotationSelector was initialized with StrikeOutAnnotation object.
        
        :param strike_out: StrikeOutAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, squiggly: aspose.pdf.annotations.SquigglyAnnotation) -> None:
        '''Select squiggly annotation if AnnotationSelector was initialized with SquigglyAnnotation object.
        
        :param squiggly: SquigglyAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, popup: aspose.pdf.annotations.PopupAnnotation) -> None:
        '''Select popup annotation if AnnotationSelector was initialized with PopupAnnotation object.
        
        :param popup: PopupAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, line: aspose.pdf.annotations.LineAnnotation) -> None:
        '''Select line annotation if AnnotationSelector was initialized with LineAnnotation object.
        
        :param line: LineAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, circle: aspose.pdf.annotations.CircleAnnotation) -> None:
        '''Select circle annotation if AnnotationSelector was initialized with CircleAnnotation object.
        
        :param circle: CircleAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, square: aspose.pdf.annotations.SquareAnnotation) -> None:
        '''Select square annotation if AnnotationSelector was initialized with SquareAnnotation object.
        
        :param square: SquareAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, ink: aspose.pdf.annotations.InkAnnotation) -> None:
        '''Select ink annotation if AnnotationSelector was initialized with InkAnnotation object.
        
        :param ink: InkAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, polyline: aspose.pdf.annotations.PolylineAnnotation) -> None:
        '''Select polyline annotation if AnnotationSelector was initialized with PolylineAnnotation object.
        
        :param polyline: PolylineAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, polygon: aspose.pdf.annotations.PolygonAnnotation) -> None:
        '''Select polygon annotation if AnnotationSelector was initialized with PolygonAnnotation object.
        
        :param polygon: PolygonAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, caret: aspose.pdf.annotations.CaretAnnotation) -> None:
        '''Select caret annotation if AnnotationSelector was initialized with CaretAnnotation object.
        
        :param caret: CaretAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, stamp: aspose.pdf.annotations.StampAnnotation) -> None:
        '''Select stamp annotation if AnnotationSelector was initialized with StampAnnotation object.
        
        :param stamp: StampAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, widget: aspose.pdf.annotations.WidgetAnnotation) -> None:
        '''Select widget annotation if AnnotationSelector was initialized with WidgetAnnotation object.
        
        :param widget: WidgetAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, watermark: aspose.pdf.annotations.WatermarkAnnotation) -> None:
        '''Select watermark annotation if AnnotationSelector was initialized with WatermarkAnnotation object.
        
        :param watermark: WatermarkAnnotation for selecting.'''
        ...
    
    @overload
    def visit(self, movie: aspose.pdf.annotations.MovieAnnotation) -> None:
        '''Select movie annotation if AnnotationSelector was initialized with MovieAnnotation object.
        
        :param movie: MovieAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, rich_media: aspose.pdf.annotations.RichMediaAnnotation) -> None:
        '''Select movie annotation if AnnotationSelector was initialized with RichMedia annotation object.
        
        :param rich_media: RichMedia annotation.'''
        ...
    
    @overload
    def visit(self, screen: aspose.pdf.annotations.ScreenAnnotation) -> None:
        '''Select screen annotation if AnnotationSelector was initialized with ScreenAnnotation object.
        
        :param screen: ScreenAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, pdf_3d: aspose.pdf.annotations.PDF3DAnnotation) -> None:
        '''Select PDF3D annotation if AnnotationSelector was initialized with PDF3DAnnotation object.
        
        :param pdf_3d: PDF3DAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, color_bar: aspose.pdf.annotations.ColorBarAnnotation) -> None:
        '''Select ColorBar annotation if AnnotationSelector was initialized with ColorBar object.
        
        :param color_bar: PDF3DAnnotation object for selecting.'''
        ...
    
    @overload
    def visit(self, trim_mark: aspose.pdf.annotations.TrimMarkAnnotation) -> None:
        '''Selects the  if the:class:`AnnotationSelector` was initialized with a :class:`TrimMarkAnnotation` object.
        
        :param trim_mark: The :class:`TrimMarkAnnotation` object for selection.'''
        ...
    
    @overload
    def visit(self, bleed_mark: aspose.pdf.annotations.BleedMarkAnnotation) -> None:
        '''Selects the  if the:class:`AnnotationSelector` was initialized with a
        :class:`BleedMarkAnnotation` object.
        
        :param bleed_mark: The :class:`BleedMarkAnnotation` object for selection.'''
        ...
    
    @overload
    def visit(self, registration_mark: aspose.pdf.annotations.RegistrationMarkAnnotation) -> None:
        '''Selects the  if the:class:`AnnotationSelector` was initialized with a
        :class:`RegistrationMarkAnnotation` object.
        
        :param registration_mark: The :class:`RegistrationMarkAnnotation` object for selection.'''
        ...
    
    @overload
    def visit(self, page_information: aspose.pdf.annotations.PageInformationAnnotation) -> None:
        '''Selects the  if the:class:`AnnotationSelector` was initialized with a
        :class:`PageInformationAnnotation` object.
        
        :param page_information: The :class:`PageInformationAnnotation` object for selection.'''
        ...

    @property
    def selected(self) -> list[aspose.pdf.annotations.Annotation]:
        '''The list of selected objects.'''
        ...
    
    ...

class AppearanceDictionary:
    '''Annotation appearance dictionary specifying how the annotation shall be presented visually on the page.'''
    
    @overload
    def add(self, key: object, value: object) -> None:
        '''Adds an element with the provided key and value.
        
        :param key: Element key.
        :param value: Element value.'''
        ...
    
    @overload
    def add(self, key: str, value: aspose.pdf.XForm) -> None:
        '''Add X form for specifed key.
        
        :param key: Element key.
        :param value: XForm object value.'''
        ...
    
    def clear(self) -> None:
        '''Removes all elements from the dictionary.'''
        ...
    
    def copy_to(self, array: list[aspose.pdf.XForm], index: int) -> None:
        '''Copies the elements of the dictionary to an Array, starting at a particular Array index.
        
        :param array: Array where items must be copied.
        :param index: Index where items must be copied.'''
        ...
    
    def contains_key(self, key: str) -> bool:
        '''Determines does this dictionary contasins specified key.
        
        :param key: Key to search in the dictionary.
        :returns: true if key is found.'''
        ...
    
    def remove(self, key: str) -> bool:
        '''Removes key from the dictionary.
        
        :param key: Key to be removed from the dictionary.
        :returns: true if key was successfully removed.'''
        ...
    
    def try_get_value(self, key: str, value: aspose.pdf.XForm) -> bool:
        '''Tries to find key in the dictionary and retreives value if found.
        
        :param key: Key to search in the dictionary.
        :param value: Retreived value.
        :returns: true if key was found.'''
        ...
    
    @property
    def is_read_only(self) -> bool:
        '''Gets a value indicating whether dictionary is read-only.'''
        ...
    
    @property
    def is_fixed_size(self) -> bool:
        '''Gets a value indicating whether dictionary has a fixed size.'''
        ...
    
    @property
    def keys(self) -> None:
        '''Gets keys of the dictionary. If appearance dictionary has subditionaries, then :attr:`AppearanceDictionary.keys` contains (N|R|D).state values,
        where N - normal appearance, R - rollover appearance, D - down appearance and state - the name of the state
        (e.g. On, Off for checkboxes).'''
        ...
    
    @property
    def values(self) -> None:
        '''Gets the list of the dictionary values.
        Result collection contains the list of XForm objects.'''
        ...
    
    @property
    def is_synchronized(self) -> bool:
        '''Gets a value indicating whether access to the dictionary is synchronized (thread safe).'''
        ...
    
    @property
    def sync_root(self) -> object:
        '''Gets an object that can be used to synchronize access to the dictionary.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of elements contained in the dictionary.'''
        ...
    
    ...

class BleedMarkAnnotation(aspose.pdf.annotations.CornerPrinterMarkAnnotation):
    '''Represents a Bleed Mark annotation.
    
    Bleed marks are placed at the corners of a printed page to indicate where the page is to be trimmed and how far it is allowed to deviate
    from the trim marks.'''
    
    def __init__(self, page: aspose.pdf.Page, position: aspose.pdf.annotations.PrinterMarkCornerPosition):
        '''Initializes a new instance of the :class:`BleedMarkAnnotation` class.
        
        :param page: The page where the annotation will be added.
        :param position: The position of the bleed mark on the page.
        
        This constructor creates a BleedMarkAnnotation and adds it to the specified page at the specified position.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor for annotation processing.
        
        :param visitor: AnnotationSelector object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class Border:
    '''Class representing characteristics of annotation border.'''
    
    def __init__(self, parent: aspose.pdf.annotations.Annotation):
        '''Constructor for border object.
        
        :param parent: Parent annotation.'''
        ...
    
    @property
    def h_corner_radius(self) -> float:
        '''Gets or sets horizontal corner radius.'''
        ...
    
    @h_corner_radius.setter
    def h_corner_radius(self, value: float):
        ...
    
    @property
    def v_corner_radius(self) -> float:
        '''Gets or sets vertical corner radius.'''
        ...
    
    @v_corner_radius.setter
    def v_corner_radius(self, value: float):
        ...
    
    @property
    def width(self) -> int:
        '''Gets or sets border width.'''
        ...
    
    @width.setter
    def width(self, value: int):
        ...
    
    @property
    def effect_intensity(self) -> int:
        '''Gets or sets effect intencity. Valid range of value is [0..2].'''
        ...
    
    @effect_intensity.setter
    def effect_intensity(self, value: int):
        ...
    
    @property
    def style(self) -> aspose.pdf.annotations.BorderStyle:
        '''Gets or sets border style. :class:`BorderStyle`'''
        ...
    
    @style.setter
    def style(self, value: aspose.pdf.annotations.BorderStyle):
        ...
    
    @property
    def effect(self) -> aspose.pdf.annotations.BorderEffect:
        '''Gets or sets border effect. :class:`BorderEffect`'''
        ...
    
    @effect.setter
    def effect(self, value: aspose.pdf.annotations.BorderEffect):
        ...
    
    @property
    def dash(self) -> aspose.pdf.annotations.Dash:
        '''Gets or sets dash pattern.'''
        ...
    
    @dash.setter
    def dash(self, value: aspose.pdf.annotations.Dash):
        ...
    
    ...

class CaretAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Class representing Caret annotation.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Constructor for usign in Generator.
        
        :param document: Document where annotation will be created.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Caret annotation on the specified page.
        
        :param page: Document's page where annotation should be created.
        :param rect: Required rectangle that sets annotation's border.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def frame(self) -> aspose.pdf.Rectangle:
        '''Gets or sets caret rectangle.'''
        ...
    
    @frame.setter
    def frame(self, value: aspose.pdf.Rectangle):
        ...
    
    @property
    def symbol(self) -> aspose.pdf.annotations.CaretSymbol:
        '''Gets or sets symbol associated with caret. :class:`CaretSymbol`'''
        ...
    
    @symbol.setter
    def symbol(self, value: aspose.pdf.annotations.CaretSymbol):
        ...
    
    ...

class Characteristics:
    '''Represents annotation characteristics'''
    
    @property
    def background(self) -> aspose.pydrawing.Color:
        '''Gets or sets color of the background'''
        ...
    
    @background.setter
    def background(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def border(self) -> aspose.pydrawing.Color:
        '''Gets or sets color of the border.'''
        ...
    
    @border.setter
    def border(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def rotate(self) -> aspose.pdf.Rotation:
        '''Gets or sets rotation of the annotation.'''
        ...
    
    @rotate.setter
    def rotate(self, value: aspose.pdf.Rotation):
        ...
    
    ...

class CircleAnnotation(aspose.pdf.annotations.CommonFigureAnnotation):
    '''Class representing Circle annotation.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Constructor for Circle annotation.
        
        :param document: Document where annotation will be created.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Circle annotation on the specified page.
        
        :param page: Document's page where annotation should be created.
        :param rect: Required rectangle that sets annotation's border.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class ColorBarAnnotation(aspose.pdf.annotations.PrinterMarkAnnotation):
    '''Class representing ColorBarAnnotation annotation.
    Property Color ignored, instead used ColorsOfCMYK color.
    On creation, the ratio of width and height determines the orientation of the annotation - horizontal or vertical.
    Next, it checks that the annotation rectangle is outside the TrimBox, and if not, then it is shifted to the nearest location outside the TrimBox,
    taking into account the orientation of the annotation. It is possible to reduce the width (height) so that the annotation fits outside the TrimBox.
    If there is no space for the layout, the width/height can be set to zero (in this case, the annotation is present on the page, but not displayed).'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, color_of_cmyk: aspose.pdf.annotations.ColorsOfCMYK):
        '''Creates new ColorBar annotation on the specified page.
        
        :param page: Document's page where annotation should be created.
        :param rect: Required rectangle that sets annotation's drawing area.
        :param color_of_cmyk: Color for which annotation drawing.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    def change_after_resize(self, transform: aspose.pdf.Matrix) -> None:
        '''Update parameters and appearance, according to the matrix transform and moving outside of TrimBox if nesseary.
        
        :param transform: Matrix specifying the transformation.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def color_of_cmyk(self) -> aspose.pdf.annotations.ColorsOfCMYK:
        '''Gets or sets color (one of cyan, magenta, yellow, black) for which the annotation is drawing.'''
        ...
    
    @color_of_cmyk.setter
    def color_of_cmyk(self, value: aspose.pdf.annotations.ColorsOfCMYK):
        ...
    
    ...

class CommonFigureAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Abstract class representing common figure annotation.'''
    
    @property
    def interior_color(self) -> aspose.pdf.Color:
        '''Interior color with which to fill the annotation�s rectangle or ellipse.'''
        ...
    
    @interior_color.setter
    def interior_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def frame(self) -> aspose.pdf.Rectangle:
        '''The rectangle describing the numerical differences between two rectangles:
        the Rect entry of the annotation and the actual boundaries of the underlying square or circle.'''
        ...
    
    @frame.setter
    def frame(self, value: aspose.pdf.Rectangle):
        ...
    
    ...

class CornerPrinterMarkAnnotation(aspose.pdf.annotations.PrinterMarkAnnotation):
    '''Represents annotation types that are placed in the corners of the printed page.'''
    
    @property
    def position(self) -> aspose.pdf.annotations.PrinterMarkCornerPosition:
        '''Get or sets the position of the mark on the page.'''
        ...
    
    @position.setter
    def position(self, value: aspose.pdf.annotations.PrinterMarkCornerPosition):
        ...
    
    ...


class CustomExplicitDestination(aspose.pdf.annotations.ExplicitDestination):
    '''Represents custom explicit destination.'''
    
    def to_string(self) -> str:
        '''Converts to page number.
        
        :returns: Page number.'''
        ...
    
    ...

class Dash:
    '''Class representing line dash pattern.'''
    
    def __init__(self, on: int, off: int):
        '''Constructor for Dash.
        
        :param on: Length of the dash.
        :param off: Length of the gap.'''
        ...
    
    @overload
    def __init__(self, pattern: list[int]):
        '''Constructor for Dash. Defines a pattern of dashes and gaps that shall be used in drawing a dashed border.
        
        :param pattern: A dash array (of two values minimum) defining a pattern of dashes and gaps that shall be used in drawing a dashed border.'''
        ...

    @property
    def on(self) -> int:
        '''Gets or sets length of dash.'''
        ...
    
    @on.setter
    def on(self, value: int):
        ...
    
    @property
    def off(self) -> int:
        '''Gets or sets length of gap between dashes.'''
        ...
    
    @off.setter
    def off(self, value: int):
        ...

    @property
    def pattern(self) -> list[int]:
        '''Gets dash array defining a pattern of dashes and gaps that shall be used in drawing a dashed border.'''
        ...
    
    ...

class DefaultAppearance:
    '''Describes default appearance of field (font, text size and color).'''
    
    @overload
    def __init__(self):
        '''Constructor of DefaultAppearance.'''
        ...
    
    @overload
    def __init__(self, font_name: str, font_size: float, text_color: aspose.pydrawing.Color):
        '''Constructor of DefaultAppearance.
        
        :param font_name: Font name.
        :param font_size: Font size.
        :param text_color: Color of text.'''
        ...
    
    @overload
    def __init__(self, font: aspose.pdf.text.Font, font_size: float, text_color: aspose.pydrawing.Color):
        '''Constructor of Default Appearance. Previously created font may be specified as default font.
        
        :param font: Font which will be used as default.
        :param font_size: Font size.
        :param text_color: Color of text.'''
        ...
    
    @property
    def font_size(self) -> float:
        '''Gets font size in default apperance.'''
        ...
    
    @font_size.setter
    def font_size(self, value: float):
        ...
    
    @property
    def text_color(self) -> aspose.pydrawing.Color:
        '''Gets or sets the color of text in the default appearance.'''
        ...
    
    @text_color.setter
    def text_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def font_name(self) -> str:
        '''Gets font name in the default appearance.'''
        ...
    
    @font_name.setter
    def font_name(self, value: str):
        ...
    
    @property
    def font_resource_name(self) -> str:
        '''Gets font name in the default appearance.'''
        ...
    
    @font_resource_name.setter
    def font_resource_name(self, value: str):
        ...
    
    @property
    def font(self) -> aspose.pdf.text.Font:
        '''Gets font specified as default for text.'''
        ...
    
    @property
    def text(self) -> str:
        '''Gets the list of pdf operators which represent appearence.'''
        ...
    
    ...

class DocumentActionCollection:
    '''Class describes actions performed on some actions with document'''
    
    def __init__(self, document: aspose.pdf.Document):
        '''Constructor for DocumentActionCollection. Constructs DocumentActionCollection objects from Pdf.Kit.Engine Document object.
        
        :param document: Document for which action colleciton is created.'''
        ...
    
    @property
    def before_saving(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets action performed before document saving.'''
        ...
    
    @before_saving.setter
    def before_saving(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def before_closing(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets action that will be performed before documetn closing.'''
        ...
    
    @before_closing.setter
    def before_closing(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def after_saving(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets action that will be performed after document saving.'''
        ...
    
    @after_saving.setter
    def after_saving(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def before_printing(self) -> aspose.pdf.annotations.PdfAction:
        '''Action that will be performed before document printing.'''
        ...
    
    @before_printing.setter
    def before_printing(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def after_printing(self) -> aspose.pdf.annotations.PdfAction:
        '''Action that will be performed after document printing.'''
        ...
    
    @after_printing.setter
    def after_printing(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    ...

class ExplicitDestination:
    '''Represents the base class for explicit destinations in PDF document.'''
    
    @overload
    @staticmethod
    def create_destination(self, page: aspose.pdf.Page, type: aspose.pdf.annotations.ExplicitDestinationType, values: list[float]) -> aspose.pdf.annotations.ExplicitDestination:
        '''Creates instances of ExplicitDestination descendant classes.
        
        :param page: The object of destination page.
        :param type: The type of explicit destination.
        :param values: Array of double values.
        :returns: The explicit destination object.'''
        ...
    
    @overload
    @staticmethod
    def create_destination(self, doc: aspose.pdf.Document, page_number: int, type: aspose.pdf.annotations.ExplicitDestinationType, values: list[float]) -> aspose.pdf.annotations.ExplicitDestination:
        '''Creates instances of ExplicitDestination descendant classes.
        
        :param doc: Document where destination will be created.
        :param page_number: Number of the page.
        :param type: Destionatyion type.
        :param values: Array of destination specific values.
        :returns: The explicit destination object.'''
        ...
    
    @overload
    @staticmethod
    def create_destination(self, page_number: int, type: aspose.pdf.annotations.ExplicitDestinationType, values: list[float]) -> aspose.pdf.annotations.ExplicitDestination:
        '''Creates instances of ExplicitDestination descendant classes.
        
        :param page_number: The destination page number.
        :param type: The type of explicit destination.
        :param values: Array of double values.
        :returns: The explicit destination object.'''
        ...
    
    def to_string(self) -> str:
        '''Returns string representation of ExplicitDestination object.
        
        :returns: String representation.'''
        ...
    
    @property
    def page(self) -> aspose.pdf.Page:
        '''Gets the destination page object'''
        ...
    
    @property
    def page_number(self) -> int:
        '''Gets the destination page number'''
        ...
    
    ...

class FdfReader:
    '''Class which performes reading of FDF format.'''
    
    @staticmethod
    def read_annotations(self, stream: Any, document: aspose.pdf.Document) -> None:
        '''Import annotations from FDF file and put them into document.
        
        :param stream: Source stream containing FDF file.
        :param document: Document where annotations will be added.'''
        ...
    
    ...

class FileAttachmentAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Class describes file attachment annotation.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, file_spec: aspose.pdf.FileSpecification):
        '''Creates new FileAttachment annotation on the specified page.
        
        :param page: Document's page where annotation should be created.
        :param rect: Required rectangle that sets annotation's border.
        :param file_spec: Describes the file that shoud be bound with the annotation.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def opacity(self) -> float:
        '''Gets or sets icon's opacity from 0 to 1: 0 - completely transparant, 1 - completely opaque.'''
        ...
    
    @opacity.setter
    def opacity(self, value: float):
        ...
    
    @property
    def file(self) -> aspose.pdf.FileSpecification:
        '''The specification of the file associated with this annotation.'''
        ...
    
    @file.setter
    def file(self, value: aspose.pdf.FileSpecification):
        ...
    
    @property
    def icon(self) -> aspose.pdf.annotations.FileIcon:
        '''Gets or sets icon that shall be used in displaying annotation.'''
        ...
    
    @icon.setter
    def icon(self, value: aspose.pdf.annotations.FileIcon):
        ...
    
    ...

class FitBExplicitDestination(aspose.pdf.annotations.ExplicitDestination):
    '''Represents explicit destination that displays the page with its contents magnified just enough to fit its bounding box entirely within the window both horizontally and vertically. If the required horizontal and vertical magnification factors are different, use the smaller of the two, centering the bounding box within the window in the other dimension.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page):
        '''Creates local explicit destination.
        
        :param page: The destination page object.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, page_number: int):
        '''Creates remote explicit destination.
        
        :param document: The parent document that contains this object.
        :param page_number: The destination page number of remote document.'''
        ...
    
    @overload
    def __init__(self, page_number: int):
        '''Creates remote explicit destination.
        
        :param page_number: The destination page number of remote document.'''
        ...
    
    def to_string(self) -> str:
        '''Converts the object state into string value. Example: "1 FitB".
        
        :returns: String value representing object state.'''
        ...
    
    ...

class FitBHExplicitDestination(aspose.pdf.annotations.ExplicitDestination):
    '''Represents explicit destination that displays the page with the vertical coordinate top positioned at the top edge of the window and the contents of the page magnified just enough to fit the entire width of its bounding box within the window. A null value for top specifies that the current value of that parameter is to be retained unchanged.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, top: float):
        '''Creates local explicit destination.
        
        :param page: The destination page object.
        :param top: The vertical coordinate top positioned at the top edge of the window.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, page_number: int, top: float):
        '''Creates remote explicit destination.
        
        :param document: The parent document that contains this object.
        :param page_number: The destination page number of remote document.
        :param top: The vertical coordinate top positioned at the top edge of the window.'''
        ...
    
    @overload
    def __init__(self, page_number: int, top: float):
        '''Creates remote explicit destination.
        
        :param page_number: The destination page number of remote document.
        :param top: The vertical coordinate top positioned at the top edge of the window.'''
        ...
    
    def to_string(self) -> str:
        '''Converts the object state into string value. Example: "1 FitBH 100".
        
        :returns: String value representing object state.'''
        ...
    
    @property
    def top(self) -> float:
        '''Gets the vertical coordinate top positioned at the top edge of the window.'''
        ...
    
    ...

class FitBVExplicitDestination(aspose.pdf.annotations.ExplicitDestination):
    '''Represents explicit destination that displays the page with the horizontal coordinate left positioned at the left edge of the window and the contents of the page magnified just enough to fit the entire height of its bounding box within the window. A null value for left specifies that the current value of that parameter is to be retained unchanged.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, left: float):
        '''Creates local explicit destination.
        
        :param page: The destination page object.
        :param left: The horizontal coordinate left positioned at the left edge of the window.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, page_number: int, left: float):
        '''Creates remote explicit destination.
        
        :param document: The parent document that contains this object.
        :param page_number: The destination page number of remote document.
        :param left: The horizontal coordinate left positioned at the left edge of the window.'''
        ...
    
    @overload
    def __init__(self, page_number: int, left: float):
        '''Creates remote explicit destination.
        
        :param page_number: The destination page number of remote document.
        :param left: The horizontal coordinate left positioned at the left edge of the window.'''
        ...
    
    def to_string(self) -> str:
        '''Converts the object state into string value. Example: "1 FitBV 100".
        
        :returns: String value representing object state.'''
        ...
    
    @property
    def left(self) -> float:
        '''Gets the horizontal coordinate left positioned at the left edge of the window.'''
        ...
    
    ...

class FitExplicitDestination(aspose.pdf.annotations.ExplicitDestination):
    '''Represents explicit destination that displays the page with its contents magnified just enough to fit the entire page within the window both horizontally and vertically. If the required horizontal and vertical magnification factors are different, use the smaller of the two, centering the page within the window in the other dimension.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page):
        '''Creates local explicit destination.
        
        :param page: The destination page object.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, page_number: int):
        '''Creates remote explicit destination.
        
        :param document: The Aspose.Pdf.Document object.
        :param page_number: The destination page number.'''
        ...
    
    @overload
    def __init__(self, page_number: int):
        '''Creates remote explicit destination.
        
        :param page_number: The destination page number of remote document.'''
        ...
    
    def to_string(self) -> str:
        '''Converts the object state into string value. Example: "1 Fit".
        
        :returns: String value representing object state.'''
        ...
    
    ...

class FitHExplicitDestination(aspose.pdf.annotations.ExplicitDestination):
    '''Represents explicit destination that displays the page with the vertical coordinate top positioned at the top edge of the window and the contents of the page magnified just enough to fit the entire width of the page within the window. A null value for top specifies that the current value of that parameter is to be retained unchanged.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, top: float):
        '''Creates local explicit destination.
        
        :param page: The destination page object.
        :param top: The vertical coordinate top positioned at the top edge of the window.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, page_number: int, top: float):
        '''Creates remote explicit destination.
        
        :param document: The parent document that contains this object.
        :param page_number: The destination page number of remote document.
        :param top: The vertical coordinate top positioned at the top edge of the window.'''
        ...
    
    @overload
    def __init__(self, page_number: int, top: float):
        '''Creates remote explicit destination.
        
        :param page_number: The destination page number of remote document.
        :param top: The vertical coordinate top positioned at the top edge of the window.'''
        ...
    
    def to_string(self) -> str:
        '''Converts the object state into string value. Example: "1 FitH 100".
        
        :returns: String value representing object state.'''
        ...
    
    @property
    def top(self) -> float:
        '''Gets the vertical coordinate top positioned at the top edge of the window.'''
        ...
    
    ...

class FitRExplicitDestination(aspose.pdf.annotations.ExplicitDestination):
    '''Represents explicit destination that displays the page with its contents magnified just enough to fit the rectangle specified by the coordinates left, bottom, right, and topentirely within the window both horizontally and vertically. If the required horizontal and vertical magnification factors are different, use the smaller of the two, centering the rectangle within the window in the other dimension. A null value for any of the parameters may result in unpredictable behavior.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, left: float, bottom: float, right: float, top: float):
        '''Creates local explicit destination.
        
        :param page: The destination page object.
        :param left: Left horizontal coordinate of visible rectangle.
        :param bottom: Bottom vertical coordinate of visible rectangle.
        :param right: Right horizontal coordinate of visible rectangle.
        :param top: Top vertical coordinate of visible rectangle.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, page_number: int, left: float, bottom: float, right: float, top: float):
        '''Creates remote explicit destination.
        
        :param document: The parent document that contains this object.
        :param page_number: The destination page number of remote document.
        :param left: Left horizontal coordinate of visible rectangle.
        :param bottom: Bottom vertical coordinate of visible rectangle.
        :param right: Right horizontal coordinate of visible rectangle.
        :param top: Top vertical coordinate of visible rectangle.'''
        ...
    
    @overload
    def __init__(self, page_number: int, left: float, bottom: float, right: float, top: float):
        '''Creates remote explicit destination.
        
        :param page_number: The destination page number of remote document.
        :param left: Left horizontal coordinate of visible rectangle.
        :param bottom: Bottom vertical coordinate of visible rectangle.
        :param right: Right horizontal coordinate of visible rectangle.
        :param top: Top vertical coordinate of visible rectangle.'''
        ...
    
    def to_string(self) -> str:
        '''Converts the object state into string value. Example: "1 FitR 100 200 300 400".
        
        :returns: String value representing object state.'''
        ...
    
    @property
    def left(self) -> float:
        '''Gets left horizontal coordinate of visible rectangle.'''
        ...
    
    @property
    def bottom(self) -> float:
        '''Gets bottom vertical coordinate of visible rectangle.'''
        ...
    
    @property
    def right(self) -> float:
        '''Gets right horizontal coordinate of visible rectangle.'''
        ...
    
    @property
    def top(self) -> float:
        '''Gets top vertical coordinate of visible rectangle.'''
        ...
    
    ...

class FitVExplicitDestination(aspose.pdf.annotations.ExplicitDestination):
    '''Represents explicit destination that displays the page with the horizontal coordinate left positioned at the left edge of the window and the contents of the page magnified just enough to fit the entire height of the page within the window. A null value for left specifies that the current value of that parameter is to be retained unchanged.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, left: float):
        '''Creates local explicit destination.
        
        :param page: The destination page object.
        :param left: The horizontal coordinate left positioned at the left edge of the window.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, page_number: int, left: float):
        '''Creates remote explicit destination.
        
        :param document: The parent document that contains this object.
        :param page_number: The destination page number of remote document.
        :param left: The horizontal coordinate left positioned at the left edge of the window.'''
        ...
    
    @overload
    def __init__(self, page_number: int, left: float):
        '''Creates remote explicit destination.
        
        :param page_number: The destination page number of remote document.
        :param left: The horizontal coordinate left positioned at the left edge of the window.'''
        ...
    
    def to_string(self) -> str:
        '''Converts the object state into string value. Example: "1 FitV 100".
        
        :returns: String value representing object state.'''
        ...
    
    @property
    def left(self) -> float:
        '''Gets the horizontal coordinate left positioned at the left edge of the window.'''
        ...
    
    ...

class FixedPrint:
    '''Represent Fixed print data of Watermark Annotation.'''
    
    @property
    def matrix(self) -> aspose.pdf.Matrix:
        '''Gets or sets matrix value.'''
        ...
    
    @matrix.setter
    def matrix(self, value: aspose.pdf.Matrix):
        ...
    
    @property
    def horizontal_translation(self) -> float:
        '''Gets or sets horizontal translation.'''
        ...
    
    @horizontal_translation.setter
    def horizontal_translation(self, value: float):
        ...
    
    @property
    def vertical_translation(self) -> float:
        '''Gets or sets vertical translation.'''
        ...
    
    @vertical_translation.setter
    def vertical_translation(self, value: float):
        ...
    
    ...

class FreeTextAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Represents a free text annotation that displays text directly on the page. Unlike an ordinary text annotation, a free text annotation has no open or closed state; instead of being displayed in a pop-up window, the text is always visible.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document, appearance: aspose.pdf.annotations.DefaultAppearance):
        '''Constructor to use with Generator.
        
        :param document: Document where annotation will be created.
        :param appearance: Default Appearance'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, appearance: aspose.pdf.annotations.DefaultAppearance):
        '''Creates new FreeText annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param appearance: The default appearance to be used in formatting the text.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def starting_style(self) -> aspose.pdf.annotations.LineEnding:
        '''Gets or sets line ending style for line ending point.
        OThis property is obsolete, please use EndingStyle.'''
        ...
    
    @starting_style.setter
    def starting_style(self, value: aspose.pdf.annotations.LineEnding):
        ...
    
    @property
    def ending_style(self) -> aspose.pdf.annotations.LineEnding:
        '''Gets or sets line ending style for line ending point.'''
        ...
    
    @ending_style.setter
    def ending_style(self, value: aspose.pdf.annotations.LineEnding):
        ...
    
    @property
    def justification(self) -> aspose.pdf.annotations.Justification:
        '''Gets or set a code specifying the form of quadding (justification) to be used in displaying the annotation�s text.'''
        ...
    
    @justification.setter
    def justification(self, value: aspose.pdf.annotations.Justification):
        ...
    
    @property
    def default_appearance(self) -> str:
        '''Gets or sets the default appearance string to be used in formatting the text.'''
        ...
    
    @default_appearance.setter
    def default_appearance(self, value: str):
        ...
    
    @property
    def default_appearance_object(self) -> aspose.pdf.annotations.DefaultAppearance:
        '''Object which represents default appearance of FreeText annotation.'''
        ...
    
    @property
    def intent(self) -> aspose.pdf.annotations.FreeTextIntent:
        '''Gets or sets the intent of the free text annotation.'''
        ...
    
    @intent.setter
    def intent(self, value: aspose.pdf.annotations.FreeTextIntent):
        ...
    
    @property
    def default_style(self) -> str:
        '''Gets or sets a default style string.'''
        ...
    
    @default_style.setter
    def default_style(self, value: str):
        ...
    
    @property
    def text_style(self) -> aspose.pdf.annotations.TextStyle:
        '''Gets or sets style of the text in appearance. when text style is changed, text appearance is updated.'''
        ...
    
    @text_style.setter
    def text_style(self, value: aspose.pdf.annotations.TextStyle):
        ...
    
    @property
    def rotate(self) -> aspose.pdf.Rotation:
        '''Angle of annotation rotation.'''
        ...
    
    @rotate.setter
    def rotate(self, value: aspose.pdf.Rotation):
        ...
    
    @property
    def callout(self) -> list[aspose.pdf.Point]:
        '''Array of point specifying callout line.'''
        ...
    
    @callout.setter
    def callout(self, value: list[aspose.pdf.Point]):
        ...
    
    @property
    def text_rectangle(self) -> aspose.pdf.Rectangle:
        '''Rectangle describing the numerical differences between two rectangles: the Rect entry of the annotation
        and a rectangle contained within that rectangle. The inner rectangle is where the annotation�s text should be displayed.'''
        ...
    
    @text_rectangle.setter
    def text_rectangle(self, value: aspose.pdf.Rectangle):
        ...
    
    ...

class GoToAction(aspose.pdf.annotations.PdfAction):
    '''Represents a go-to action that changes the view to a specified destination (page, location, and magnification factor).'''
    
    @overload
    def __init__(self, page: int):
        '''Constructor for GoToAction class.
        
        :param page: The destination page number to jump to.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page):
        '''Constructor for GoToAction class.
        
        :param page: Aspose.Pdf.Page destination object to jump to.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, type: aspose.pdf.annotations.ExplicitDestinationType, values: list[float]):
        '''Constructor for GoToAction class.
        
        :param page: Destination page.
        :param type: Destination type.
        :param values: Action parameters.'''
        ...
    
    @overload
    def __init__(self, destination: aspose.pdf.annotations.ExplicitDestination):
        '''Constructor.
        
        :param destination: Explicit destination.'''
        ...
    
    @overload
    def __init__(self):
        '''Constructor.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, name: str):
        '''Action which linked with Named Destination.
        
        :param doc: Document where action will be created.
        :param name: Name of the destination.'''
        ...
    
    @property
    def destination(self) -> aspose.pdf.annotations.IAppointment:
        '''Gets or sets the destination to jump to.'''
        ...
    
    @destination.setter
    def destination(self, value: aspose.pdf.annotations.IAppointment):
        ...
    
    ...

class GoToRemoteAction(aspose.pdf.annotations.GoToAction):
    '''Represents a remote go-to action that is similar to an ordinary go-to action but jumps to a destination in another PDF file instead of the current file.'''
    
    @overload
    def __init__(self, remote_pdf: str, remote_page_number: int):
        '''Initializes GoToRemoteAction object.
        
        :param remote_pdf: Destination PDF document.
        :param remote_page_number: Destination page number.'''
        ...
    
    @overload
    def __init__(self, remote_pdf: str, destination: aspose.pdf.annotations.ExplicitDestination):
        '''Initializes GoToRemoteAction object.
        
        :param remote_pdf: Destination PDF document.
        :param destination: Destination in the  PDF document.'''
        ...
    
    @property
    def destination(self) -> aspose.pdf.annotations.IAppointment:
        '''Gets or sets the destination to jump to.'''
        ...
    
    @destination.setter
    def destination(self, value: aspose.pdf.annotations.IAppointment):
        ...
    
    @property
    def file(self) -> aspose.pdf.FileSpecification:
        '''Gets or sets the specification of the file in which the destination is located.'''
        ...
    
    @file.setter
    def file(self, value: aspose.pdf.FileSpecification):
        ...
    
    @property
    def new_window(self) -> aspose.pdf.ExtendedBoolean:
        '''Gets or sets a flag specifying whether to open the destination document in a new window.'''
        ...
    
    @new_window.setter
    def new_window(self, value: aspose.pdf.ExtendedBoolean):
        ...
    
    ...

class GoToURIAction(aspose.pdf.annotations.PdfAction):
    '''Represents a URI action causes a URI to be resolved.'''
    
    def __init__(self, uri: str):
        '''Constructor.
        
        :param uri: The uniform resource identifier to resolve.'''
        ...
    
    @property
    def uri(self) -> str:
        '''Gets or sets the uniform resource identifier to resolve.'''
        ...
    
    @uri.setter
    def uri(self, value: str):
        ...
    
    ...

class HideAction(aspose.pdf.annotations.PdfAction):
    '''Represents a hide action that hides or shows one or more annotations on the screen by setting or clearing their Hidden flags.'''
    
    @overload
    def __init__(self, annotation: aspose.pdf.annotations.Annotation):
        '''Initializes a new instance of the :class:`HideAction` class for the specified annotation.
        
        :param annotation: An annotation to be hidden.'''
        ...
    
    @overload
    def __init__(self, annotation: aspose.pdf.annotations.Annotation, is_hidden: bool):
        '''Initializes a new instance of the :class:`HideAction` class for the specified annotation and invisibility flag.
        
        :param annotation: An annotation to be hidden or shown.
        :param is_hidden: A flag indicating whether to hide the annotation (true) or show it (false).'''
        ...
    
    @overload
    def __init__(self, field_name: str):
        '''Initializes a new instance of the :class:`HideAction` class for the specified field name.
        
        :param field_name: A text string giving the fully qualified field name of an interactive form field.'''
        ...
    
    @overload
    def __init__(self, field_name: str, is_hidden: bool):
        '''Initializes a new instance of the :class:`HideAction` class for the specified field name and invisibility flag.
        
        :param field_name: A text string giving the fully qualified field name of an interactive form field.
        :param is_hidden: A flag indicating whether to hide the field (true) or show it (false).'''
        ...
    
    @overload
    def __init__(self, annotations: list[aspose.pdf.annotations.Annotation]):
        '''Initializes a new instance of the :class:`HideAction` class for the specified annotations.
        
        :param annotations: An array of annotations to be hidden.'''
        ...
    
    @overload
    def __init__(self, annotations: list[aspose.pdf.annotations.Annotation], is_hidden: bool):
        '''Initializes a new instance of the :class:`HideAction` class for the specified annotations and for invisibility flag.
        
        :param annotations: An array of annotations to be hidden or shown.
        :param is_hidden: A flag indicating whether to hide the annotations (true) or show it (false).'''
        ...
    
    @overload
    def __init__(self, names: list[str]):
        '''Initializes a new instance of the :class:`HideAction` class for the specified field names.
        
        :param names: An array of strings giving the fully qualified field names of an interactive form fields.'''
        ...
    
    @overload
    def __init__(self, names: list[str], is_hidden: bool):
        '''Initializes a new instance of the :class:`HideAction` class for the specified field names and for invisibility flag.
        
        :param names: An array of strings giving the fully qualified field names of an interactive form fields.
        :param is_hidden: A flag indicating whether to hide the fields (true) or show it (false).'''
        ...
    
    @property
    def is_hidden(self) -> bool:
        '''Gets or sets status of the annotation(s) to hide/display.'''
        ...
    
    @is_hidden.setter
    def is_hidden(self, value: bool):
        ...
    
    ...

class HighlightAnnotation(aspose.pdf.annotations.TextMarkupAnnotation):
    '''Represents a highlight annotation that highlights a range of text in the document.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Highlight annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class IAnnotationVisitor:
    '''Defines Visitor for visiting different document annotations.'''
    
    @overload
    def visit(self, link: aspose.pdf.annotations.LinkAnnotation) -> None:
        '''Visit/select link annotation.
        
        :param link: LinkAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, attachment: aspose.pdf.annotations.FileAttachmentAnnotation) -> None:
        '''Visit/select attachment annotation.
        
        :param attachment: FileAttachmentAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, text: aspose.pdf.annotations.TextAnnotation) -> None:
        '''Visit/select text annotation.
        
        :param text: TextAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, freetext: aspose.pdf.annotations.FreeTextAnnotation) -> None:
        '''Visit/select freetext annotation.
        
        :param freetext: FreeTextAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, highlight: aspose.pdf.annotations.HighlightAnnotation) -> None:
        '''Visit/select highlight annotation.
        
        :param highlight: HighlightAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, underline: aspose.pdf.annotations.UnderlineAnnotation) -> None:
        '''Visit/select underline annotation.
        
        :param underline: UnderlineAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, strike_out: aspose.pdf.annotations.StrikeOutAnnotation) -> None:
        '''Visit/select strikeOut annotation.
        
        :param strike_out: StrikeOutAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, squiggly: aspose.pdf.annotations.SquigglyAnnotation) -> None:
        '''Visit/select squiggly annotation.
        
        :param squiggly: SquigglyAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, popup: aspose.pdf.annotations.PopupAnnotation) -> None:
        '''Visit/select popup annotation.
        
        :param popup: PopupAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, line: aspose.pdf.annotations.LineAnnotation) -> None:
        '''Visit/select line annotation.
        
        :param line: LineAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, circle: aspose.pdf.annotations.CircleAnnotation) -> None:
        '''Visit/select circle annotation.
        
        :param circle: CircleAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, square: aspose.pdf.annotations.SquareAnnotation) -> None:
        '''Visit/select square annotation.
        
        :param square: SquareAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, ink: aspose.pdf.annotations.InkAnnotation) -> None:
        '''Visit/select ink annotation.
        
        :param ink: InkAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, polyline: aspose.pdf.annotations.PolylineAnnotation) -> None:
        '''Visit/select polyline annotation.
        
        :param polyline: PolylineAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, polygon: aspose.pdf.annotations.PolygonAnnotation) -> None:
        '''Visit/select polygon annotation.
        
        :param polygon: PolygonAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, caret: aspose.pdf.annotations.CaretAnnotation) -> None:
        '''Visit/select caret annotation.
        
        :param caret: CaretAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, stamp: aspose.pdf.annotations.StampAnnotation) -> None:
        '''Visit/select stamp annotation.
        
        :param stamp: StampAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, widget: aspose.pdf.annotations.WidgetAnnotation) -> None:
        '''Visit/select widget annotation.
        
        :param widget: WidgetAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, movie: aspose.pdf.annotations.MovieAnnotation) -> None:
        '''Visit/select movie annotation.
        
        :param movie: MovieAnnotation object example/template.'''
        ...
    
    @overload
    def visit(self, screen: aspose.pdf.annotations.ScreenAnnotation) -> None:
        '''Visit/select screen annotation.
        
        :param screen: ScreenAnnotation object example/template.'''
        ...

    @overload
    def visit(self, trim_mark: aspose.pdf.annotations.TrimMarkAnnotation) -> None:
        '''Visit/select a trim mark annotation.
        
        :param trim_mark: The :class:`TrimMarkAnnotation` object example/template.'''
        ...
    
    @overload
    def visit(self, bleed_mark: aspose.pdf.annotations.BleedMarkAnnotation) -> None:
        '''Visit/select a bleed mark annotation.
        
        :param bleed_mark: The :class:`BleedMarkAnnotation` object example/template.'''
        ...
    
    @overload
    def visit(self, registration_mark: aspose.pdf.annotations.RegistrationMarkAnnotation) -> None:
        '''Visit/select a registration mark annotation.
        
        :param registration_mark: The :class:`RegistrationMarkAnnotation` object example/template.'''
        ...
    
    @overload
    def visit(self, page_information: aspose.pdf.annotations.PageInformationAnnotation) -> None:
        '''Visit/select a page information annotation.
        
        :param page_information: The :class:`PageInformationAnnotation` object example/template.'''
        ...
    
    ...

class IAppointment:
    '''Represents general interface for actions and destinations.'''
    
    def to_string(self) -> str:
        '''Returns string representation
        
        :returns: String representation.'''
        ...
    
    ...

class ImportDataAction(aspose.pdf.annotations.PdfAction):
    '''Upon invocation of an import-data action, Forms Data Format (FDF) data shall be imported into the document’s interactive form from a specified file.'''
    
    @property
    def data(self) -> aspose.pdf.FileSpecification:
        '''The FDF file from which to import the data.'''
        ...
    
    @data.setter
    def data(self, value: aspose.pdf.FileSpecification):
        ...
    
    ...

class InkAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Represents a freehand "scribble" composed of one or more disjoint paths.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document, ink_list: list[list[aspose.pdf.Point]]):
        '''Constructor for Ink annotation for Generator.
        
        :param document: Document where ink annotation will be created.
        :param ink_list: An array of Point[] arrays, each representing a stroked path.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, ink_list):
        '''Creates new Ink annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param ink_list: An array of Point[] arrays, each representing a stroked path.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, ink_list: list[list[aspose.pdf.Point]]):
        '''Creates new Ink annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param ink_list: An array of Point[] arrays, each representing a stroked path.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    def change_after_resize(self, transform: aspose.pdf.Matrix) -> None:
        '''Updates the points in InkList, according to the matrix transform.
        
        :param transform: Matrix specifying the transformation.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def cap_style(self) -> aspose.pdf.annotations.CapStyle:
        '''Style of ink annotation line endings.'''
        ...
    
    @cap_style.setter
    def cap_style(self, value: aspose.pdf.annotations.CapStyle):
        ...
    
    @property
    def ink_list(self) -> list[list[aspose.pdf.Point]]:
        '''Gets or sets list of gestures that are independent lines which are represented by Point[] arrays.'''
        ...
    
    @ink_list.setter
    def ink_list(self, value: list[list[aspose.pdf.Point]]):
        ...
    
    ...

class JavascriptAction(aspose.pdf.annotations.PdfAction):
    '''Class representing javascript action.'''
    
    def __init__(self, java_script: str):
        '''Constructor.
        
        :param java_script: JavaScript code.'''
        ...
    
    @property
    def script(self) -> str:
        '''Gets or sets javascript code.'''
        ...
    
    @script.setter
    def script(self, value: str):
        ...
    
    ...

class LaunchAction(aspose.pdf.annotations.PdfAction):
    '''Represents a launch action that launches an application or opens or prints a document.'''
    
    @overload
    def __init__(self, file: str):
        '''Creates a launch action.
        
        :param file: The file to be launched.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, file: str):
        '''Creates a launch action.
        
        :param document: Document where action will be created.
        :param file: The file to be launched.'''
        ...
    
    @property
    def file(self) -> str:
        '''Gets or sets the application to be launched or the document to be opened or printed.'''
        ...
    
    @file.setter
    def file(self, value: str):
        ...
    
    @property
    def new_window(self) -> aspose.pdf.ExtendedBoolean:
        '''Gets or sets a flag specifying whether to open the destination document in a new window (affect PDF documents only).'''
        ...
    
    @new_window.setter
    def new_window(self, value: aspose.pdf.ExtendedBoolean):
        ...
    
    ...

class LineAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Class representing line annotation.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document, start: aspose.pdf.Point, end: aspose.pdf.Point):
        '''Constructor for using with Generator.
        
        :param document: Document where annotation will be created.
        :param start: Starting point.
        :param end: Ending point.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, start: aspose.pdf.Point, end: aspose.pdf.Point):
        '''Creates new Line annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param start: A point, specifying the starting coordinate of the line.
        :param end: A point, specifying the ending coordinate of the line.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor to annotation processing.
        
        :param visitor: Visitor object'''
        ...
    
    def change_after_resize(self, transform: aspose.pdf.Matrix) -> None:
        '''Updates the Starting and Ending points, according to the matrix transform.
        
        :param transform: Matrix specifying the transformation.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def starting(self) -> aspose.pdf.Point:
        '''Gets or sets starting point of line.'''
        ...
    
    @starting.setter
    def starting(self, value: aspose.pdf.Point):
        ...
    
    @property
    def starting_style(self) -> aspose.pdf.annotations.LineEnding:
        '''Gets or sets line ending style for line starting point.'''
        ...
    
    @starting_style.setter
    def starting_style(self, value: aspose.pdf.annotations.LineEnding):
        ...
    
    @property
    def ending(self) -> aspose.pdf.Point:
        '''Gets or sets line ending point.'''
        ...
    
    @ending.setter
    def ending(self, value: aspose.pdf.Point):
        ...
    
    @property
    def ending_style(self) -> aspose.pdf.annotations.LineEnding:
        '''Gets or sets ending style for end point of line.'''
        ...
    
    @ending_style.setter
    def ending_style(self, value: aspose.pdf.annotations.LineEnding):
        ...
    
    @property
    def interior_color(self) -> aspose.pdf.Color:
        '''Gets or sets interior color of the annotation.'''
        ...
    
    @interior_color.setter
    def interior_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def leader_line(self) -> float:
        '''Gets or sets leader line length.'''
        ...
    
    @leader_line.setter
    def leader_line(self, value: float):
        ...
    
    @property
    def leader_line_extension(self) -> float:
        '''Gets or sets length of leader line extension.'''
        ...
    
    @leader_line_extension.setter
    def leader_line_extension(self, value: float):
        ...
    
    @property
    def show_caption(self) -> bool:
        '''Gets or sets boolean flag which determinies is contents must be shown as caption.'''
        ...
    
    @show_caption.setter
    def show_caption(self, value: bool):
        ...
    
    @property
    def leader_line_offset(self) -> float:
        '''Gets or sets leader line offset.'''
        ...
    
    @leader_line_offset.setter
    def leader_line_offset(self, value: float):
        ...
    
    @property
    def caption_offset(self) -> aspose.pdf.Point:
        '''Gets or sets caption text offset from its normal position.'''
        ...
    
    @caption_offset.setter
    def caption_offset(self, value: aspose.pdf.Point):
        ...
    
    @property
    def caption_position(self) -> aspose.pdf.annotations.CaptionPosition:
        '''Gets or sets annotation caption position.'''
        ...
    
    @caption_position.setter
    def caption_position(self, value: aspose.pdf.annotations.CaptionPosition):
        ...
    
    @property
    def measure(self) -> aspose.pdf.annotations.Measure:
        '''Measure units specifed for this annotation.'''
        ...
    
    @measure.setter
    def measure(self, value: aspose.pdf.annotations.Measure):
        ...
    
    @property
    def intent(self) -> aspose.pdf.annotations.LineIntent:
        '''Gets or sets the intent of the line annotation.'''
        ...
    
    @intent.setter
    def intent(self, value: aspose.pdf.annotations.LineIntent):
        ...
    
    ...

class LinkAnnotation(aspose.pdf.annotations.Annotation):
    '''Represents either a hypertext link to a destination elsewhere in the document or an action to be performed.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Link annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def action(self) -> aspose.pdf.annotations.PdfAction:
        '''An action to be performed when the link annotation is activated.'''
        ...
    
    @action.setter
    def action(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def destination(self) -> aspose.pdf.annotations.IAppointment:
        '''A destination to be displayed when the annotation is activated.'''
        ...
    
    @destination.setter
    def destination(self, value: aspose.pdf.annotations.IAppointment):
        ...
    
    @property
    def highlighting(self) -> aspose.pdf.annotations.HighlightingMode:
        '''The visual effect to be used when the mouse button is pressed or held down inside its active area.'''
        ...
    
    @highlighting.setter
    def highlighting(self, value: aspose.pdf.annotations.HighlightingMode):
        ...
    
    ...

class MarkupAnnotation(aspose.pdf.annotations.Annotation):
    '''Abstract class representing markup annotation.'''
    
    @overload
    def set_review_state(self, state: aspose.pdf.annotations.AnnotationState, user_name: str) -> None:
        '''Sets the review state for an annotation. Marked and Unmarked states are ignored as they do not belong to the Review StateModel.
        Note, the state stored in other text annotation which has state and statemodel keys.
        
        :param state: Status for assignment.
        :param user_name: The username that appears in the comments header.
                          The name can be the same as the name in the Title of the target annotation or different if the status is set by another user.'''
        ...
    
    @overload
    def set_review_state(self, state: aspose.pdf.annotations.AnnotationState) -> None:
        '''Sets the review state for an annotation. Marked and Unmarked states are ignored as they do not belong to the Review StateModel.
        The state is set by the user who created the target annotation. The value is taken from the Title property of the target annotation.
        Note, the state stored in other text annotation which has state and statemodel keys.
        
        :param state: Status for assignment.'''
        ...
    
    def clear_state(self) -> None:
        '''Clears state and state model for the annotation.
        For example, clears the review status for an annotation.
        Note, the state stored in other text annotation which has state and statemodel keys.'''
        ...
    
    def set_marked_state(self, marked: bool) -> None:
        '''Sets Marked и Unmarked state for the annotation.
        Note, the state stored in other text annotation which has state and statemodel keys.
        
        :param marked: True if sets Marked state, and false if sets Unmarked state.'''
        ...
    
    def get_state(self) -> aspose.pdf.annotations.AnnotationState:
        '''Gets the state of the annotation.
        Note, the state stored in other text annotation which has state and statemodel keys.
        
        :returns: Annotation state.'''
        ...
    
    def get_state_model(self) -> aspose.pdf.annotations.AnnotationStateModel:
        '''Gets the state model of the annotation.
        Note, the state stored in other text annotation which has state and statemodel keys.
        
        :returns: Annotation state model.'''
        ...

    @property
    def title(self) -> str:
        '''Gets or sets a text that shall be displayed in title bar of annotation.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def rich_text(self) -> str:
        '''Gets or sets a rich text string to be displayed in the pop-up window when the annotation is opened.'''
        ...
    
    @rich_text.setter
    def rich_text(self, value: str):
        ...
    
    @property
    def creation_date(self) -> datetime.datetime:
        '''Gets date and time when annotation was created.'''
        ...
    
    @property
    def subject(self) -> str:
        '''Gets text representing desciption of the object.'''
        ...
    
    @subject.setter
    def subject(self, value: str):
        ...
    
    @property
    def popup(self) -> aspose.pdf.annotations.PopupAnnotation:
        '''Pop-up annotation for entering or editing the text associated with this annotation.'''
        ...
    
    @popup.setter
    def popup(self, value: aspose.pdf.annotations.PopupAnnotation):
        ...
    
    @property
    def opacity(self) -> float:
        '''Gets or sets the constant opacity value to be used in painting the annotation.'''
        ...
    
    @opacity.setter
    def opacity(self, value: float):
        ...
    
    @property
    def in_reply_to(self) -> aspose.pdf.annotations.Annotation:
        '''A reference to the annotation that this annotation is "in reply to".
        Both annotations must be on the same page of the document.'''
        ...
    
    @in_reply_to.setter
    def in_reply_to(self, value: aspose.pdf.annotations.Annotation):
        ...
    
    @property
    def reply_type(self) -> aspose.pdf.annotations.ReplyType:
        '''A string specifying the relationship (the "reply type") between this annotation
        and one specified by InReplyTo.'''
        ...
    
    @reply_type.setter
    def reply_type(self, value: aspose.pdf.annotations.ReplyType):
        ...
    
    ...

class Measure:
    '''Class which describes Measure coordinate system.'''
    
    def __init__(self, annotation: aspose.pdf.annotations.Annotation):
        '''Creates Measure object for measure annotations.
        
        :param annotation: Annotation for which measure will be bound.'''
        ...
    
    @property
    def scale_ratio(self) -> str:
        '''A text string expressing the scale ratio of the drawing.'''
        ...
    
    @scale_ratio.setter
    def scale_ratio(self, value: str):
        ...
    
    @property
    def x_format(self) -> None:
        '''A number format array for measurement of change along the xaxis and, if Y is not present, along the y axis as well'''
        ...
    
    @x_format.setter
    def x_format(self, value: None):
        ...
    
    @property
    def y_format(self) -> None:
        '''A number format array for measurement of change along the y axis.'''
        ...
    
    @y_format.setter
    def y_format(self, value: None):
        ...
    
    @property
    def distance_format(self) -> None:
        '''A number format array for measurement of distance in any direction.'''
        ...
    
    @distance_format.setter
    def distance_format(self, value: None):
        ...
    
    @property
    def area_format(self) -> None:
        '''A number format array for measurement of area.'''
        ...
    
    @area_format.setter
    def area_format(self, value: None):
        ...
    
    @property
    def angle_format(self) -> None:
        '''A number format array for measurement of angles.'''
        ...
    
    @angle_format.setter
    def angle_format(self, value: None):
        ...
    
    @property
    def slope_format(self) -> None:
        '''A number format array for measurement of the slope of a line.'''
        ...
    
    @slope_format.setter
    def slope_format(self, value: None):
        ...
    
    @property
    def origin(self) -> aspose.pdf.Point:
        '''Point that shall specify the origin of the measurement coordinate system in default user space coordinates.'''
        ...
    
    @origin.setter
    def origin(self, value: aspose.pdf.Point):
        ...
    
    @property
    def xy_factor(self) -> float:
        '''A factor that shall be used to convert the largest units along the y axis to the largest units along the x axis.'''
        ...
    
    @xy_factor.setter
    def xy_factor(self, value: float):
        ...

    
    class NumberFormat:
          '''Number format for measure.'''

          def __init__(self, measure: aspose.pdf.annotations.Measure):
              '''Constructor for NumberFormat class.
        
              :param measure: Measure object which contains this number format.'''
              
              ...
    
          @property
          def unit_label(self) -> str:
              '''A text string specifying a label for displaying the units.'''
              ...

          @unit_label.setter 
          def unit_label(self, value: str):
              ...

          @property
          def convresion_factor(self) -> double:
              '''The conversion factor used to multiply a value in partial units of the previous number format array element to obtain a value in the units of this number format.'''
              ...

          @convresion_factor.setter 
          def convresion_factor(self, value: double):
              ...

          @property
          def fraction_displayment(self) -> aspose.pdf.annotations.Measure.NumberFormat.FractionStyle:
              '''In what manner fractional values are displayed.'''
              ...

          @fraction_displayment.setter 
          def fraction_displayment(self, value: aspose.pdf.annotations.Measure.NumberFormat.FractionStyle):
              ...

          @property
          def precision(self) -> int:
              '''In what manner fractional values are displayedIf FractionDisplayment is ShowAsDecimal, this value is precision of fractional value; It shall me multiple of 10. Default is 100.'''
              ...

          @precision.setter 
          def precision(self, value: int):
              ...

          
          @property
          def denominator(self) -> int:
              '''If FractionDisplayment is ShowAsFraction, this value is denominator of the fraction. Default value is 16.'''
              ...

          @denominator.setter 
          def denominator(self, value: int):
              ...

          @property
          def force_denominator(self) -> bool:
              '''If FractionDisplayment is ShowAsFraction, this value determines meay or not the fraction be reduced. If value is true fraction may not be reduced.'''
              ...

          @force_denominator.setter 
          def force_denominator(self, value: bool):
              ...

          @property
          def thousands_separator(self) -> str:
              '''Text that shall be used between orders of thousands in display of numerical values. An empty string indicates that no text shall be added. Default is comma.'''
              ...

          @thousands_separator.setter 
          def thousands_separator(self, value: str):
              ...

          @property
          def fraction_separator(self) -> str:
              '''Text that shall be used as the decimal position in displaying numerical values. An empty string indicates that the default shall be used. Default is period character.'''
              ...

          @fraction_separator.setter 
          def fraction_separator(self, value: str):
              ...

          @property
          def before_text(self) -> str:
              '''Text that shall be concatenated to the left of the label.'''
              ...

          @before_text.setter 
          def before_text(self, value: str):
              ...

          @property
          def after_text(self) -> str:
              '''Text that shall be concatenated after the label.'''
              ...

          @after_text.setter 
          def after_text(self, value: str):
              ...

          class FractionStyle:
                '''Value which indicates in which manner fraction values are displayed.'''
             
                SHOW_AS_DECIMAL: FractionStyle
                SHOW_AS_FRACTION: FractionStyle
                ROUND: FractionStyle
                TRUNCATE: FractionStyle
    
    class NumberFormatList:
          '''Represents list of number formats.'''

          def __init__(self, measure: aspose.pdf.annotations.Measure):
              '''Constructor for NumberFormatList class.
        
              :param measure: Parent measure object.'''
              
              ...
    
          def add(self, value: aspose.pdf.annotations.Measure.NumberFormat) -> None:
              '''Adds number format to list.
        
              :param value: Value to be added into list.''' 
              ...

          def insert(self, index: int, value: aspose.pdf.annotations.Measure.NumberFormat) -> None:
              '''Inserts number format into list.
        
              :param index: Index where new element will be added..
              :param value: Value to be inserted.''' 
              ...

          def remove_at(self, index: int) -> None:
              '''Removes number format from list.
        
              :param index: Index of item to be removed.''' 
              ...
   

          @property
          def count(self) -> int:
              '''Count if items in the list.'''
              ...   
    ...

class MediaClip:
    '''Class describes media clip object of rendition.'''
    
    ...

class MediaClipData(aspose.pdf.annotations.MediaClip):
    '''Class describes media clip data.'''
    
    @property
    def data(self) -> aspose.pdf.FileSpecification:
        '''Return file specification which contains actual media data .'''
        ...
    
    ...

class MediaClipSection(aspose.pdf.annotations.MediaClip):
    '''This class descibes Media clip section.'''
    
    ...

class MediaRendition(aspose.pdf.annotations.Rendition):
    '''Class describes media rendition.'''
    
    @property
    def media_clip(self) -> aspose.pdf.annotations.MediaClip:
        '''Gets or sets media clip obkects associated with rendition.'''
        ...
    
    ...

class MovieAnnotation(aspose.pdf.annotations.Annotation):
    '''Represents a movie annotation that contains animated graphics and sound to be presented on the computer screen and through the speakers. When the annotation is activated, the movie is played.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document, movie_file: str):
        '''Constructor for using with Generator.
        
        :param document: Document where movie annotation will be created.
        :param movie_file: Name of movie file.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, movie_file: str):
        '''Creates new Sound annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param movie_file: A movie file to be played when the annotation is activated.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets the title of the movie annotation.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def file(self) -> aspose.pdf.FileSpecification:
        '''Gets or sets a file specification identifying a self-describing movie file.'''
        ...
    
    @file.setter
    def file(self, value: aspose.pdf.FileSpecification):
        ...
    
    @property
    def poster(self) -> bool:
        '''Gets or sets a flag or stream specifying whether and how a poster image representing the movie shall be displayed. If true, the poster image shall be retrieved from the movie file; if it is false, no poster shall be displayed.'''
        ...
    
    @poster.setter
    def poster(self, value: bool):
        ...
    
    @property
    def aspect(self) -> aspose.pdf.Point:
        '''Gets or sets the width and height of the movie�s bounding box, in pixels.'''
        ...
    
    @aspect.setter
    def aspect(self, value: aspose.pdf.Point):
        ...
    
    @property
    def rotate(self) -> int:
        '''Gets or sets the number of degrees by which the movie shall be rotated clockwise relative to the page. The value shall be a multiple of 90.'''
        ...
    
    @rotate.setter
    def rotate(self, value: int):
        ...
    
    ...

class NamedAction(aspose.pdf.annotations.PdfAction):
    '''Represents named actions that PDF viewer applications are expected to support.'''
    
    def __init__(self, action: aspose.pdf.annotations.PredefinedAction):
        '''Constructor for Named Action class.
        
        :param action: Action for which this object is created.'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets or sets the action to be performed.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    ...

class NamedDestination:
    '''Instead of being defined directly with the explicit syntax, a destination may be referred to indirectly by means of a name object or a byte string.'''
    
    def __init__(self, doc: aspose.pdf.Document, name: str):
        '''Create named destination.
        
        :param doc: Document where named destination should be created.
        :param name: Name to which destination refers.'''
        ...
    
    @property
    def name(self) -> str:
        '''Gets the name of named destination.'''
        ...
    
    ...

class PDF3DAnnotation(aspose.pdf.annotations.Annotation):
    '''Class PDF3DAnnotation. This class cannot be inherited.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, pdf_3d_artwork: aspose.pdf.annotations.PDF3DArtwork):
        '''Initializes a new instance of the :class:`PDF3DAnnotation` class.
        
        :param page: The page.
        :param rect: The rectangle.
        :param pdf_3d_artwork: The 3D Artwork.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, pdf_3d_artwork: aspose.pdf.annotations.PDF3DArtwork, activation: aspose.pdf.annotations.PDF3DActivation):
        '''Initializes a new instance of the :class:`PDF3DAnnotation` class.
        
        :param page: The page.
        :param rect: The rectangle.
        :param pdf_3d_artwork: The 3D Artwork.
        :param activation: The activation mode.
        :raises System.Exception: 3D Stream is already added to current 3D Artwork'''
        ...
    
    @overload
    def set_image_preview(self, filename: str) -> None:
        '''Sets the image preview.
        
        :param filename: The image preview filename.'''
        ...
    
    @overload
    def set_image_preview(self, image: Any) -> None:
        '''Sets the image preview.
        
        :param image: The image stream.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor for annotation processing.
        
        :param visitor: AnnotationSelector object.'''
        ...
    
    def set_default_view_index(self, index: int) -> None:
        '''Sets the index of the default view.
        
        :param index: The default view index.'''
        ...
    
    def clear_image_preview(self) -> None:
        '''Clears the image preview.'''
        ...
    
    def get_image_preview(self) -> Any:
        '''Gets the image preview.
        
        :returns: Image preview as stream.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def pdf_3d_artwork(self) -> aspose.pdf.annotations.PDF3DArtwork:
        '''Gets the 3D Artwork.'''
        ...
    
    @property
    def lighting_scheme(self) -> aspose.pdf.annotations.PDF3DLightingScheme:
        '''Gets the lighting scheme.'''
        ...
    
    @property
    def content(self) -> aspose.pdf.annotations.PDF3DContent:
        '''Gets or sets the content.'''
        ...
    
    @content.setter
    def content(self, value: aspose.pdf.annotations.PDF3DContent):
        ...
    
    @property
    def render_mode(self) -> aspose.pdf.annotations.PDF3DRenderMode:
        '''Gets the render mode.'''
        ...
    
    @property
    def view_array(self) -> aspose.pdf.annotations.PDF3DViewArray:
        '''Gets the view array.'''
        ...
    
    ...

class PDF3DArtwork:
    '''Class PDF3DArtwork.'''
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, content: aspose.pdf.annotations.PDF3DContent, lighting_scheme: aspose.pdf.annotations.PDF3DLightingScheme, render_mode: aspose.pdf.annotations.PDF3DRenderMode):
        '''Initializes a new instance of the :class:`PDF3DArtwork` class.
        
        :param doc: The document.
        :param content: The content.
        :param lighting_scheme: The lighting scheme.
        :param render_mode: The render mode.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, content: aspose.pdf.annotations.PDF3DContent):
        '''Initializes a new instance of the :class:`PDF3DArtwork` class.
        
        :param doc: The document.
        :param content: The content.'''
        ...
    
    def get_views_list(self) -> None:
        '''Get the views as list.
        
        :returns: ReadOnlyCollection\<PDF3DView\>.'''
        ...
    
    def get_views_array(self) -> list[aspose.pdf.annotations.PDF3DView]:
        '''Gets the views array.
        
        :returns: Array of views.'''
        ...
    
    @property
    def lighting_scheme(self) -> aspose.pdf.annotations.PDF3DLightingScheme:
        '''Gets or sets the lighting scheme.'''
        ...
    
    @lighting_scheme.setter
    def lighting_scheme(self, value: aspose.pdf.annotations.PDF3DLightingScheme):
        ...
    
    @property
    def render_mode(self) -> aspose.pdf.annotations.PDF3DRenderMode:
        '''Gets or sets the render mode.'''
        ...
    
    @render_mode.setter
    def render_mode(self, value: aspose.pdf.annotations.PDF3DRenderMode):
        ...
    
    @property
    def view_array(self) -> aspose.pdf.annotations.PDF3DViewArray:
        '''Gets the view array.'''
        ...
    
    ...

class PDF3DContent:
    '''Class PDF3DContent.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PDF3DContent` class.'''
        ...
    
    @overload
    def __init__(self, filename: str):
        '''Initializes a new instance of the :class:`PDF3DContent` class.
        
        :param filename: The filename.
        :raises System.ArgumentException: Unknown 3D Artwork type'''
        ...
    
    @overload
    def load_as_prc(self, filename: str) -> None:
        '''Loads 3D content with the specified filename as PRC format.
        
        :param filename: The filename.'''
        ...
    
    @overload
    def load_as_prc(self, stream: Any) -> None:
        '''Loads 3D content from stream as PRC format.
        
        :param stream: The 3D content stream.'''
        ...
    
    @overload
    def load_as_prc(self, stream: bytes) -> None:
        '''Loads 3D content from byte array as PRC format.
        
        :param stream: The stream.'''
        ...
    
    @overload
    def load_as_u3d(self, filename: str) -> None:
        '''Loads 3D content with the specified filename as U3D format.
        
        :param filename: The filename.'''
        ...
    
    @overload
    def load_as_u3d(self, stream: Any) -> None:
        '''Loads 3D content from stream as U3D format.
        
        :param stream: The 3D content stream.'''
        ...
    
    @overload
    def load_as_u3d(self, stream: bytes) -> None:
        '''Loads 3D content from byte array as U3D format.
        
        :param stream: The stream.'''
        ...
    
    def load(self, filename: str) -> None:
        '''Loads 3D content with the specified filename.
        
        :param filename: The filename.
        :raises System.ArgumentException: Unknown 3D content type'''
        ...
    
    def save_to_file(self, filename: str) -> None:
        '''Saves 3D content to file.
        
        :param filename: The file name.
        :raises System.ArgumentException: 3DArtwork content format is PRC or U3D.'''
        ...
    
    def get_as_stream(self) -> Any:
        '''Gets 3D content as stream.
        
        :returns: Stream.'''
        ...
    
    def get_as_byte_array(self) -> bytes:
        '''Gets 3D content as byte array.
        
        :returns: System.Byte[].'''
        ...
    
    @property
    def extension(self) -> str:
        '''Gets the extension .'''
        ...
    
    ...

class PDF3DCrossSection:
    '''Class PDF3DCrossSection.'''
    
    def __init__(self, doc: aspose.pdf.Document):
        '''Initializes a new instance of the :class:`PDF3DCrossSection` class.
        
        :param doc: The document.'''
        ...
    
    @property
    def center(self) -> aspose.pdf.Point3D:
        '''Gets or sets the cross section rotation center.'''
        ...
    
    @center.setter
    def center(self, value: aspose.pdf.Point3D):
        ...
    
    @property
    def cutting_plane_opacity(self) -> float:
        '''Gets or sets the cutting plane opacity.
        
        :raises System.Exception: The number must be in the range [0 , 1]'''
        ...
    
    @cutting_plane_opacity.setter
    def cutting_plane_opacity(self, value: float):
        ...
    
    @property
    def cutting_plane_orientation(self) -> aspose.pdf.annotations.PDF3DCuttingPlaneOrientation:
        '''Gets or sets the cutting plane orientation.
        
        :raises System.Exception: Only one of the values shall be Null'''
        ...
    
    @cutting_plane_orientation.setter
    def cutting_plane_orientation(self, value: aspose.pdf.annotations.PDF3DCuttingPlaneOrientation):
        ...
    
    @property
    def cutting_plane_color(self) -> aspose.pdf.Color:
        '''Gets or sets the color of the cutting plane.'''
        ...
    
    @cutting_plane_color.setter
    def cutting_plane_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def cutting_planes_intersection_color(self) -> aspose.pdf.Color:
        '''Gets or sets the color of the cutting planes intersection.'''
        ...
    
    @cutting_planes_intersection_color.setter
    def cutting_planes_intersection_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def visibility(self) -> bool:
        '''Gets or sets a value indicating visibility of the cutting planes intersection.'''
        ...
    
    @visibility.setter
    def visibility(self, value: bool):
        ...
    
    ...

class PDF3DCrossSectionArray:
    '''Class PDF3DCrossSectionArray.'''
    
    def __init__(self, doc: aspose.pdf.Document):
        '''Initializes a new instance of the :class:`PDF3DCrossSectionArray` class.
        
        :param doc: The document.'''
        ...
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.PDF3DCrossSection:
        '''Gets or sets the :class:`PDF3DCrossSection` at the specified index.
        
        :param index: The index.
        :returns: Cross section.
        
        :raises System.IndexOutOfRangeException: Invalid index: index should be in the range [1..n] where n equals to the cross sections count.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.pdf.annotations.PDF3DCrossSection):
        ...
    
    def add(self, cross_section: aspose.pdf.annotations.PDF3DCrossSection) -> None:
        '''Adds the specified cross section to views array .
        
        :param cross_section: The cross section.'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes cross section from array at specified index.
        
        :param index: The index of removed cross section in array.
        :raises System.IndexOutOfRangeException: Invalid index: index should be in the range [1..n] where n equals to the cross sections count.'''
        ...
    
    def remove_all(self) -> None:
        '''Removes all cross section from array.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the cross section count.'''
        ...
    
    ...

class PDF3DCuttingPlaneOrientation:
    '''Class PDF3DCuttingPlaneOrientation.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PDF3DCuttingPlaneOrientation` class.'''
        ...
    
    @overload
    def __init__(self, angle_x: float, angle_y: float, angle_z: float):
        '''Initializes a new instance of the :class:`PDF3DCuttingPlaneOrientation` class.
        
        :param angle_x: The angle x.
        :param angle_y: The angle y.
        :param angle_z: The angle z.'''
        ...
    
    @property
    def angle_x(self) -> float:
        '''Gets or sets the angle to X axis.'''
        ...
    
    @angle_x.setter
    def angle_x(self, value: float):
        ...
    
    @property
    def angle_y(self) -> float:
        '''Gets or sets the angle to Y axis.'''
        ...
    
    @angle_y.setter
    def angle_y(self, value: float):
        ...
    
    @property
    def angle_z(self) -> float:
        '''Gets or sets the angle to Z axis.'''
        ...
    
    @angle_z.setter
    def angle_z(self, value: float):
        ...
    
    ...

class PDF3DLightingScheme:
    '''Class PDF3DLightingScheme.'''
    
    @overload
    def __init__(self, type: aspose.pdf.annotations.LightingSchemeType):
        '''Initializes a new instance of the :class:`PDF3DLightingScheme` class.
        
        :param type: The lighting scheme type.'''
        ...
    
    @overload
    def __init__(self, type_name: str):
        '''Initializes a new instance of the :class:`PDF3DLightingScheme` class.
        
        :param type_name: Name of the lighting scheme type.
        :raises System.ArgumentException: Unknown lighting scheme type argument'''
        ...
    
    @property
    def type(self) -> aspose.pdf.annotations.LightingSchemeType:
        '''Gets the lighting scheme type.'''
        ...
    
    artwork: aspose.pdf.annotations.PDF3DLightingScheme
    
    none: aspose.pdf.annotations.PDF3DLightingScheme
    
    white: aspose.pdf.annotations.PDF3DLightingScheme
    
    day: aspose.pdf.annotations.PDF3DLightingScheme
    
    night: aspose.pdf.annotations.PDF3DLightingScheme
    
    hard: aspose.pdf.annotations.PDF3DLightingScheme
    
    primary: aspose.pdf.annotations.PDF3DLightingScheme
    
    blue: aspose.pdf.annotations.PDF3DLightingScheme
    
    red: aspose.pdf.annotations.PDF3DLightingScheme
    
    cube: aspose.pdf.annotations.PDF3DLightingScheme
    
    cad: aspose.pdf.annotations.PDF3DLightingScheme
    
    headlamp: aspose.pdf.annotations.PDF3DLightingScheme
    
    ...

class PDF3DRenderMode:
    '''Class PDF3DRenderMode.'''
    
    @overload
    def __init__(self, subtype: aspose.pdf.annotations.RenderModeType):
        '''Initializes a new instance of the :class:`PDF3DRenderMode` class.
        
        :param subtype: The render mode type.'''
        ...
    
    @overload
    def __init__(self, type_name: str):
        '''Initializes a new instance of the :class:`PDF3DRenderMode` class.
        
        :param type_name: Name of the type.
        :raises System.ArgumentException: Unknown a render mode type argument'''
        ...
    
    def get_auxiliary_colour(self) -> aspose.pdf.Color:
        '''Gets the auxiliary colour.
        
        :returns: Color.'''
        ...
    
    def set_auxiliary_colour(self, color: aspose.pdf.Color) -> aspose.pdf.annotations.PDF3DRenderMode:
        '''Sets the auxiliary colour.
        
        :param color: The color.
        :returns: PDF3DRenderMode.'''
        ...
    
    def get_face_color(self) -> object:
        '''Gets the color of the face.
        
        :returns: Object.'''
        ...
    
    def set_face_color(self, color: aspose.pdf.Color) -> aspose.pdf.annotations.PDF3DRenderMode:
        '''Sets the color of the face.
        
        :param color: The color.
        :returns: PDF3DRenderMode.'''
        ...
    
    def get_opacity(self) -> float:
        '''Gets the opacity.
        
        :returns: System.Double.'''
        ...
    
    def set_opacity(self, opacity: float) -> aspose.pdf.annotations.PDF3DRenderMode:
        '''Sets the opacity.
        
        :param opacity: The opacity.
        :returns: PDF3DRenderMode.'''
        ...
    
    def set_crease_value(self, crease_value: float) -> aspose.pdf.annotations.PDF3DRenderMode:
        '''Sets the crease value.
        
        :param crease_value: The crease value.
        :returns: PDF3DRenderMode.'''
        ...
    
    def get_crease_value(self) -> float:
        '''Gets the crease value.
        
        :returns: System.Double.'''
        ...
    
    @property
    def type(self) -> aspose.pdf.annotations.RenderModeType:
        '''Gets the type.'''
        ...
    
    solid: aspose.pdf.annotations.PDF3DRenderMode
    
    solid_wireframe: aspose.pdf.annotations.PDF3DRenderMode
    
    transparent: aspose.pdf.annotations.PDF3DRenderMode
    
    transparent_ware_frame: aspose.pdf.annotations.PDF3DRenderMode
    
    bounding_box: aspose.pdf.annotations.PDF3DRenderMode
    
    transparent_bounding_box: aspose.pdf.annotations.PDF3DRenderMode
    
    transparent_bounding_box_outline: aspose.pdf.annotations.PDF3DRenderMode
    
    wireframe: aspose.pdf.annotations.PDF3DRenderMode
    
    shaded_wireframe: aspose.pdf.annotations.PDF3DRenderMode
    
    vertices: aspose.pdf.annotations.PDF3DRenderMode
    
    shaded_vertices: aspose.pdf.annotations.PDF3DRenderMode
    
    illustration: aspose.pdf.annotations.PDF3DRenderMode
    
    solid_outline: aspose.pdf.annotations.PDF3DRenderMode
    
    shaded_illustration: aspose.pdf.annotations.PDF3DRenderMode
    
    ...

class PDF3DStream:
    '''Class PDF3DStream.'''
    
    def __init__(self, doc: aspose.pdf.Document, pdf_3d_artwork: aspose.pdf.annotations.PDF3DArtwork):
        '''Initializes a new instance of the :class:`PDF3DStream` class.
        
        :param doc: The document.
        :param pdf_3d_artwork: The 3D Artwork.'''
        ...
    
    @property
    def content(self) -> aspose.pdf.annotations.PDF3DContent:
        '''Gets or sets the content.'''
        ...
    
    @content.setter
    def content(self, value: aspose.pdf.annotations.PDF3DContent):
        ...
    
    ...

class PDF3DView:
    '''Class PDF3DView.'''
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, camera_position: aspose.pdf.Matrix3D, camera_orbit: float, view_name: str):
        '''Initializes a new instance of the :class:`PDF3DView` class.
        
        :param doc: The document.
        :param camera_position: The camera position.
        :param camera_orbit: The camera orbit.
        :param view_name: Name of the view.'''
        ...
    
    @overload
    def __init__(self, doc: aspose.pdf.Document, view: aspose.pdf.annotations.PDF3DView, view_name: str):
        '''Initializes a new instance of the :class:`PDF3DView` class.
        
        :param doc: The document.
        :param view: The view.
        :param view_name: Name of the view.'''
        ...
    
    @property
    def lighting_scheme(self) -> aspose.pdf.annotations.PDF3DLightingScheme:
        '''Gets or sets the lighting scheme of view.'''
        ...
    
    @lighting_scheme.setter
    def lighting_scheme(self, value: aspose.pdf.annotations.PDF3DLightingScheme):
        ...
    
    @property
    def render_mode(self) -> aspose.pdf.annotations.PDF3DRenderMode:
        '''Gets or sets the render mode of view.'''
        ...
    
    @render_mode.setter
    def render_mode(self, value: aspose.pdf.annotations.PDF3DRenderMode):
        ...
    
    @property
    def cross_sections_array(self) -> aspose.pdf.annotations.PDF3DCrossSectionArray:
        '''Gets the cross sections array of view.'''
        ...
    
    @property
    def view_name(self) -> str:
        '''Gets or sets the name of the view.'''
        ...
    
    @view_name.setter
    def view_name(self, value: str):
        ...
    
    @property
    def camera_position(self) -> aspose.pdf.Matrix3D:
        '''Gets or sets the camera position of view.'''
        ...
    
    @camera_position.setter
    def camera_position(self, value: aspose.pdf.Matrix3D):
        ...
    
    @property
    def camera_orbit(self) -> float:
        '''Gets or sets the camera orbit of view.'''
        ...
    
    @camera_orbit.setter
    def camera_orbit(self, value: float):
        ...
    
    @property
    def back_ground_color(self) -> aspose.pdf.Color:
        '''Gets or sets the color of the back ground of view.'''
        ...
    
    @back_ground_color.setter
    def back_ground_color(self, value: aspose.pdf.Color):
        ...
    
    ...

class PDF3DViewArray:
    '''Class PDF3DViewArray.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.PDF3DView:
        '''Gets or sets the :class:`PDF3DView` to view array at the specified index.
        
        :param index: The index.
        :returns: PDF3DView.
        
        :raises System.IndexOutOfRangeException: Invalid index: index should be in the range [1..n] where n equals to the views count.'''
        ...
    
    def __setitem__(self, index: int, value: aspose.pdf.annotations.PDF3DView):
        ...
    
    def add(self, view: aspose.pdf.annotations.PDF3DView) -> None:
        '''Adds the specified view.
        
        :param view: The view.
        :raises System.ArgumentException: Only one entry of 3D view is allowed'''
        ...
    
    def remove_at(self, index: int) -> None:
        '''Removes view from views array at specified index.
        
        :param index: The view index.
        :raises System.IndexOutOfRangeException: Invalid index: index should be in the range [1..n] where n equals to the views count.'''
        ...
    
    def remove_all(self) -> None:
        '''Removes all views.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets the views count.'''
        ...
    
    ...

class PageInformationAnnotation(aspose.pdf.annotations.PrinterMarkAnnotation):
    '''Represents a Page Information annotation in a PDF document. This annotation contains the file name,
    page number, and the date and time of the annotation creation.
    
    This class is primarily used to add metadata to a specific page in the PDF document, which can be useful
    for tracking and referencing purposes. For instance, it can be used to mark pages during the printing process
    or to provide additional information about the page when viewing the document.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Initializes a new instance of the :class:`PageInformationAnnotation` class on the given page in the given location.
        
        :param page: The page with which the annotation will be associated.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor for annotation processing.
        
        :param visitor: AnnotationSelector object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...


class PdfAction:
    '''Represents Action in PDF document'''
    
    def get_ecma_script_string(self) -> str:
        '''Gets string for ECMAScript Action.
        
        :returns: Return string for JS entry for ECMAScript Action or null else.'''
        ...

    @property
    def next(self) -> aspose.pdf.annotations.ActionCollection:
        '''Next actions in sequence.'''
        ...
    
    ...

class PdfActionCollection:
    '''Class describes list of actions.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.annotations.PdfAction:
        '''Gets action by its index.
        
        :param index: Action index value.
        :returns: Action index if found; otherwise, throws'''
        ...
    
    def delete(self, index: int) -> None:
        '''Remove action by index.
        
        :param index: Index of action to remove.'''
        ...
    
    def add(self, action: aspose.pdf.annotations.PdfAction) -> None:
        '''Add action to action list.
        
        :param action: Action to be added.'''
        ...
    
    @property
    def count(self) -> int:
        '''Gets count of actions.'''
        ...
    
    ...

class PolyAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Abstract base class for poly- annotations.'''
    
    def change_after_resize(self, transform: aspose.pdf.Matrix) -> None:
        '''Updates the points in Vertices, according to the matrix transform.
        
        :param transform: Matrix specifying the transformation.'''
        ...
    
    @property
    def measure(self) -> aspose.pdf.annotations.Measure:
        '''Measure units specifed for this annotation.'''
        ...
    
    @measure.setter
    def measure(self, value: aspose.pdf.annotations.Measure):
        ...
    
    @property
    def vertices(self) -> list[aspose.pdf.Point]:
        '''Gets or sets an array of points representing the horizontal and vertical coordinates of each vertex.'''
        ...
    
    @vertices.setter
    def vertices(self, value: list[aspose.pdf.Point]):
        ...
    
    @property
    def interior_color(self) -> aspose.pdf.Color:
        '''Gets or sets the interior color with which to fill the annotation�s line endings.'''
        ...
    
    @interior_color.setter
    def interior_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def starting_style(self) -> aspose.pdf.annotations.LineEnding:
        '''Gets or sets the style of first line ending.'''
        ...
    
    @starting_style.setter
    def starting_style(self, value: aspose.pdf.annotations.LineEnding):
        ...
    
    @property
    def ending_style(self) -> aspose.pdf.annotations.LineEnding:
        '''Gets or sets the style of second line ending.'''
        ...
    
    @ending_style.setter
    def ending_style(self, value: aspose.pdf.annotations.LineEnding):
        ...
    
    @property
    def intent(self) -> aspose.pdf.annotations.PolyIntent:
        '''Gets or sets the intent of the polygon or polyline annotation.'''
        ...
    
    @intent.setter
    def intent(self, value: aspose.pdf.annotations.PolyIntent):
        ...
    
    ...

class PolygonAnnotation(aspose.pdf.annotations.PolyAnnotation):
    '''Class representing polygon annotation.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document, vertices: list[aspose.pdf.Point]):
        '''Constructor for using with Generator.
        
        :param document: Document where annotation will be added.
        :param vertices: Array of points.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, vertices: list[aspose.pdf.Point]):
        '''Creates new Polygon annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param vertices: An array of polygon vertices points.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object for annotation processing.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class PolylineAnnotation(aspose.pdf.annotations.PolyAnnotation):
    '''Represents polyline annotation that is similar to polygon, except that the first and last vertex are not implicitly connected.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, vertices: list[aspose.pdf.Point]):
        '''Creates new Polyline annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param vertices: An array of polygon vertices points.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class PopupAnnotation(aspose.pdf.annotations.Annotation):
    '''Represents the pop-up annotation that displays text in a pop-up window for entry and editing.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Constructor. for using in Generator.
        
        :param document: Document where new popup annotation will be created.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Popup annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def open(self) -> bool:
        '''Gets or sets a flag specifying whether the pop-up annotation should initially be displayed open.'''
        ...
    
    @open.setter
    def open(self, value: bool):
        ...
    
    @property
    def parent(self) -> aspose.pdf.annotations.Annotation:
        '''Gets or sets the parent annotation with which this pop-up annotation shall be associated.
        If this entry is present, the parent annotation�s Contents, M, C, and T entries shall override those of the pop-up annotation itself.'''
        ...
    
    @parent.setter
    def parent(self, value: aspose.pdf.annotations.Annotation):
        ...
    
    ...

class PrinterMarkAnnotation(aspose.pdf.annotations.Annotation):
    '''Abstract class representing printer mark annotation.'''
    
    @overload
    @staticmethod
    def add_printer_marks(self, document: aspose.pdf.Document, marks_kind: aspose.pdf.annotations.PrinterMarksKind) -> None:
        '''Adds printer's marks to all pages in the specified document.
        
        :param document: The document to which the printer's marks will be added.
        :param marks_kind: The kind of printer's marks to add.
        :raises System.ArgumentNullException: Thrown when the  is null.
        
        This method adds various types of printer's marks based on the provided :class:`PrinterMarksKind` flags.
        If :attr:`PrinterMarksKind.NONE` is provided, no marks are added.'''
        ...
    
    @overload
    @staticmethod
    def add_printer_marks(self, page: aspose.pdf.Page, marks_kind: aspose.pdf.annotations.PrinterMarksKind) -> None:
        '''Adds printer's marks to the specified page.
        
        :param page: The page to which the printer's marks will be added.
        :param marks_kind: The kind of printer's marks to add.
        :raises System.ArgumentNullException: Thrown when the  is null.
        
        This method adds various types of printer's marks based on the provided :class:`PrinterMarksKind` flags.
        If :attr:`PrinterMarksKind.NONE` is provided, no marks are added.'''
        ...
    
    ...

class PrinterMarksKindExtensions:
    '''Provides extension methods for the :class:`PrinterMarksKind` enumeration.'''
    
    @staticmethod
    def has_flag_fast(self, value: aspose.pdf.annotations.PrinterMarksKind, flag: aspose.pdf.annotations.PrinterMarksKind) -> bool:
        '''Determines whether the current value includes a specified flag.
        
        :param value: The current value of the :class:`PrinterMarksKind` enumeration.
        :param flag: The flag to check.
        :returns: true if the flag is included in the current value; otherwise, false.'''
        ...
    
    ...

class RedactionAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Represents Redact annotation.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Constructor for RedactionAnnotation. For using in Generator.
        
        :param document: Document where new annotation will be created.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Constructor for RedactAnnotation.
        
        :param page: Page where annotation will be placed.
        :param rect: Annotation position on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    def flatten(self) -> None:
        '''Flattens annotation i.e. removes annotation and adds its'''
        ...
    
    def redact(self) -> None:
        '''Flattens annotation and redacts page contents (i.e. removes text and image under redacted annotation)'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def quad_point(self) -> list[aspose.pdf.Point]:
        '''An array of 8xN numbers specifying the coordinates of content region that is intended to be removed.'''
        ...
    
    @quad_point.setter
    def quad_point(self, value: list[aspose.pdf.Point]):
        ...
    
    @property
    def default_appearance(self) -> str:
        '''Gets or sets the default appearance string to be used in formatting the text.'''
        ...
    
    @default_appearance.setter
    def default_appearance(self, value: str):
        ...
    
    @property
    def fill_color(self) -> aspose.pdf.Color:
        '''Gets or sets color to fill annotation.'''
        ...
    
    @fill_color.setter
    def fill_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def border_color(self) -> aspose.pdf.Color:
        '''Gets or sets color of border which is drawn when redaction is not active.'''
        ...
    
    @border_color.setter
    def border_color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def overlay_text(self) -> str:
        '''Gets or sets text to print on redact annotation.'''
        ...
    
    @overlay_text.setter
    def overlay_text(self, value: str):
        ...
    
    @property
    def font_size(self) -> float:
        '''Gets or sets font size for OverlayText.'''
        ...
    
    @font_size.setter
    def font_size(self, value: float):
        ...
    
    @property
    def repeat(self) -> bool:
        '''If true overlay text will be repated on the annotation.'''
        ...
    
    @repeat.setter
    def repeat(self, value: bool):
        ...
    
    @property
    def text_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets or sets. Alignment of Overlay Text.'''
        ...
    
    @text_alignment.setter
    def text_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    ...

class RegistrationMarkAnnotation(aspose.pdf.annotations.PrinterMarkAnnotation):
    '''Represents a Registration Mark annotation.
    
    Registration marks are symbols added to printing plates or screens to ensure proper alignment of colors during the printing process.'''
    
    def __init__(self, page: aspose.pdf.Page, position: aspose.pdf.annotations.PrinterMarkSidePosition):
        '''Initializes a new instance of the :class:`RegistrationMarkAnnotation` class on the given page in the given location.
        
        :param page: The page with which the annotation will be associated.
        :param position: Position of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor for annotation processing.
        
        :param visitor: AnnotationSelector object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def position(self) -> aspose.pdf.annotations.PrinterMarkSidePosition:
        '''Gets or sets the position of the registration mark on a page.'''
        ...
    
    @position.setter
    def position(self, value: aspose.pdf.annotations.PrinterMarkSidePosition):
        ...
    
    ...

class Rendition:
    '''Class which describes rendition object of RendtionAnnotation.'''
    
    @property
    def name(self) -> str:
        '''Text string specifying the name of the rendition for use in a user interface and for name tree lookup by JavaScript actions.'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def rendition_type(self) -> aspose.pdf.annotations.RenditionType:
        '''Gets rendition type.'''
        ...
    
    ...

class RenditionAction(aspose.pdf.annotations.PdfAction):
    '''A rendition action that controls the playing of multimedia content.'''
    
    @property
    def rendition(self) -> aspose.pdf.annotations.Rendition:
        '''Gets or sets rendition associated with the action.'''
        ...
    
    @property
    def rendition_operation(self) -> aspose.pdf.annotations.RenditionOperation:
        '''The operation to perform when the action is triggered.'''
        ...
    
    @rendition_operation.setter
    def rendition_operation(self, value: aspose.pdf.annotations.RenditionOperation):
        ...
    
    @property
    def java_script(self) -> str:
        '''Gets or sets JavaScript code associated with the action.'''
        ...
    
    @java_script.setter
    def java_script(self, value: str):
        ...
    
    ...

class RichMediaAnnotation(aspose.pdf.annotations.Annotation):
    '''Class describes RichMediaAnnotation which allows embed video/audio data into PDF document.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Initializes RichMediaAnnotation.
        
        :param page: Page where object being created.
        :param rect: Rectangle coordinates.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor for this annotation.
        
        :param visitor: Visitor instance.'''
        ...
    
    def add_custom_data(self, name: str, data: Any) -> None:
        '''Add custom named data (for example required for flash script).
        
        :param name: Name of the data.
        :param data: Data.'''
        ...
    
    def set_content(self, file_name: str, audio: Any) -> None:
        '''Set content stream.
        
        :param file_name: Name of the stream.
        :param audio: Data stream.'''
        ...
    
    def set_poster(self, image_stream: Any) -> None:
        '''Set poster of the annotation.
        
        :param image_stream: Stream containing poster image.'''
        ...
    
    def update(self) -> None:
        '''Updates data with specified parameters.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def custom_player(self) -> Any:
        '''Sets or gets custom flash player to play video/audio data.'''
        ...
    
    @custom_player.setter
    def custom_player(self, value: Any):
        ...
    
    @property
    def custom_flash_variables(self) -> str:
        '''Sets or gets flash variables which passed to player.'''
        ...
    
    @custom_flash_variables.setter
    def custom_flash_variables(self, value: str):
        ...
    
    @property
    def content(self) -> Any:
        '''Data of the Rich Media content.'''
        ...
    
    @property
    def type(self) -> None:
        '''Gets or sets type of content. Possible values: Audio, Video.'''
        ...
    
    @type.setter
    def type(self, value: None):
        ...
    
    @property
    def activate_on(self) -> None:
        '''Event which activates application.'''
        ...
    
    @activate_on.setter
    def activate_on(self, value: None):
        ...
    
    ...

class ScreenAnnotation(aspose.pdf.annotations.Annotation):
    '''A screen annotation that specifies a region of a page upon which media clips may be played.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, media_file: str):
        '''Creates new Screen annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param media_file: The path to multimedia file.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def title(self) -> str:
        '''Gets or sets the title of the screen annotation.'''
        ...
    
    @title.setter
    def title(self, value: str):
        ...
    
    @property
    def action(self) -> aspose.pdf.annotations.PdfAction:
        '''Gets or sets an action to be performed when the annotation is activated.'''
        ...
    
    ...

class SelectorRendition(aspose.pdf.annotations.Rendition):
    '''Class describes selector rendition.'''
    
    @property
    def renditions(self) -> list[aspose.pdf.annotations.Rendition]:
        '''Gets array of renditions.'''
        ...
    
    ...

class SoundAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Represents a sound annotation that contains sound recorded from the computer�s microphone or imported from a file.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, sound_file: str):
        '''Creates new Sound annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param sound_file: A sound file defining the sound to be played when the annotation is activated.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle, sound_file: str, sound_sample_data: aspose.pdf.annotations.SoundSampleData):
        '''Creates new Sound annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.
        :param sound_file: A sound file defining the sound to be played when the annotation is activated.
        :param sound_sample_data: A sound sample data contains extra of sound parameters such as sampling rate, bits per sample and so on.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def icon(self) -> aspose.pdf.annotations.SoundIcon:
        '''Gets or sets an icon to be used in displaying the annotation.'''
        ...
    
    @icon.setter
    def icon(self, value: aspose.pdf.annotations.SoundIcon):
        ...
    
    @property
    def sound_data(self) -> aspose.pdf.annotations.SoundData:
        '''Gets a sound object defining the sound to be played when the annotation is activated.'''
        ...
    
    ...

class SoundData:
    '''Represents a sound data defining the sound to be played when the annotation is activated.'''
    
    @property
    def rate(self) -> int:
        '''Gets or sets the sampling rate, in samples per second.'''
        ...
    
    @rate.setter
    def rate(self, value: int):
        ...
    
    @property
    def channels(self) -> int:
        '''Gets or sets the number of sound channels.'''
        ...
    
    @channels.setter
    def channels(self, value: int):
        ...
    
    @property
    def bits(self) -> int:
        '''Gets or sets the number of bits per sample value per channel.'''
        ...
    
    @bits.setter
    def bits(self, value: int):
        ...
    
    @property
    def contents(self) -> Any:
        '''Gets stream of the sound to be played when the annotation is activated.'''
        ...
    
    @property
    def encoding(self) -> aspose.pdf.annotations.SoundEncoding:
        '''Gets or sets the encoding format for the sample data.'''
        ...
    
    @encoding.setter
    def encoding(self, value: aspose.pdf.annotations.SoundEncoding):
        ...
    
    ...

class SoundSampleData:
    '''Represents additional entries specific to a sound object (Section 9.2 PDF1-7)'''
    
    @overload
    def __init__(self, sampling_rate: int):
        '''Initializes new sound sample data.
        
        :param sampling_rate: The sampling rate.'''
        ...
    
    @overload
    def __init__(self, sampling_rate: int, number_of_sound_channels: int):
        '''Initializes new sound sample data.
        
        :param sampling_rate: The sampling rate.
        :param number_of_sound_channels: The number of sound channels.'''
        ...
    
    @overload
    def __init__(self, sampling_rate: int, number_of_sound_channels: int, bits_per_channel: int):
        '''Initializes new sound sample data.
        
        :param sampling_rate: The sampling rate.
        :param number_of_sound_channels: The number of sound channels.
        :param bits_per_channel: The number of bits per sample value per channel.'''
        ...
    
    @overload
    def __init__(self, sampling_rate: int, number_of_sound_channels: int, bits_per_channel: int, sound_sample_data_encoding_format: aspose.pdf.annotations.SoundSampleDataEncodingFormat):
        '''Initializes new sound sample data.
        
        :param sampling_rate: The sampling rate.
        :param number_of_sound_channels: The number of sound channels.
        :param bits_per_channel: The number of bits per sample value per channel.
        :param sound_sample_data_encoding_format: The encoding format for the sample data.'''
        ...
    
    @property
    def sampling_rate(self) -> int:
        '''Gets or sets the sampling rate.'''
        ...
    
    @sampling_rate.setter
    def sampling_rate(self, value: int):
        ...
    
    @property
    def number_of_sound_channels(self) -> int:
        '''Gets or sets the number of sound channels.'''
        ...
    
    @number_of_sound_channels.setter
    def number_of_sound_channels(self, value: int):
        ...
    
    @property
    def bits_per_channel(self) -> int:
        '''Gets or sets the number of bits per sample value per channel.'''
        ...
    
    @bits_per_channel.setter
    def bits_per_channel(self, value: int):
        ...
    
    @property
    def encoding_format(self) -> aspose.pdf.annotations.SoundSampleDataEncodingFormat:
        '''Gets or sets the encoding format.'''
        ...
    
    @encoding_format.setter
    def encoding_format(self, value: aspose.pdf.annotations.SoundSampleDataEncodingFormat):
        ...
    
    DEFAULT_SAMPLING_RATE: int
    
    DEFAULT_OF_SOUND_CHANNELS: int
    
    DEFAULT_OF_BITS_PER_CHANNEL: int
    
    DEFAULT_ENCODING_FORMAT: aspose.pdf.annotations.SoundSampleDataEncodingFormat
    
    ...

class SquareAnnotation(aspose.pdf.annotations.CommonFigureAnnotation):
    '''Class representing square annotation.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Constructor for using with Generator.
        
        :param document: Documennt where annotation will be created.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Square annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor to process annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class SquigglyAnnotation(aspose.pdf.annotations.TextMarkupAnnotation):
    '''Represents the squiggly annotation that appears as a jagged underline in the text of a document.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Squiggly annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class StampAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Represents rubber stamp annotation.
    This type of annotation displays text or graphics intended to look as if they were stamped on the page with a rubber stamp.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Constructor
        
        :param document: Document where annotation will be created.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Stamp annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Acepts :class:`AnnotationSelector` visitor when browsing annotation collection.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def icon(self) -> aspose.pdf.annotations.StampIcon:
        '''Gets or sets icon for rubber stamp.'''
        ...
    
    @icon.setter
    def icon(self, value: aspose.pdf.annotations.StampIcon):
        ...
    
    @property
    def image(self) -> Any:
        '''Gets or sets image of the annotation.'''
        ...
    
    @image.setter
    def image(self, value: Any):
        ...
    
    ...

class StrikeOutAnnotation(aspose.pdf.annotations.TextMarkupAnnotation):
    '''Represents a strikeout annotation that appears as a strikeout in the text of the document.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new StrikeOut annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class SubmitFormAction(aspose.pdf.annotations.PdfAction):
    '''Class which describes submit-form action.'''
    
    def __init__(self):
        '''Initializes SubmitFormAction object.'''
        ...
    
    @property
    def flags(self) -> int:
        '''Gets or sets flagas of submit action'''
        ...
    
    @flags.setter
    def flags(self, value: int):
        ...
    
    @property
    def url(self) -> aspose.pdf.FileSpecification:
        '''Destination URL.'''
        ...
    
    @url.setter
    def url(self, value: aspose.pdf.FileSpecification):
        ...
    
    EXCLUDE: int
    
    INCLUDE_NO_VALUE_FIELDS: int
    
    EXPORT_FORMAT: int
    
    GET_METHOD: int
    
    SUBMIT_COORDINATES: int
    
    XFDF: int
    
    INCLUDE_APPEND_SAVES: int
    
    INCLUDE_ANNOTATIONS: int
    
    SUBMIT_PDF: int
    
    CANONICAL_FORMAT: int
    
    EXCL_NON_USER_ANNOTS: int
    
    EXCL_F_KEY: int
    
    EMBED_FORM: int
    
    ...

class TextAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Represents a text annotation that is a �sticky note� attached to a point in the PDF document.'''
    
    @overload
    def __init__(self, document: aspose.pdf.Document):
        '''Constructor for annotation when used in Generator.
        
        :param document: Document where text annotation will be created.'''
        ...
    
    @overload
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Text annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    def change_after_resize(self, transform: aspose.pdf.Matrix) -> None:
        '''Overrides the definition in the base class with an empty body.
        
        :param transform: Matrix specifying the transformation.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def open(self) -> bool:
        '''Gets or sets a flag specifying whether the annotation should initially be displayed open.'''
        ...
    
    @open.setter
    def open(self, value: bool):
        ...
    
    @property
    def icon(self) -> aspose.pdf.annotations.TextIcon:
        '''Gets or sets an icon to be used in displaying the annotation.'''
        ...
    
    @icon.setter
    def icon(self, value: aspose.pdf.annotations.TextIcon):
        ...
    
    @property
    def state(self) -> aspose.pdf.annotations.AnnotationState:
        '''Gets or sets the state to which the original annotation should be set.'''
        ...
    
    @state.setter
    def state(self, value: aspose.pdf.annotations.AnnotationState):
        ...
    
    ...

class TextMarkupAnnotation(aspose.pdf.annotations.MarkupAnnotation):
    '''Abstract base class for text markup annotations.'''
    
    def change_after_resize(self, transform: aspose.pdf.Matrix) -> None:
        '''Updates the QuadPoints, according to the matrix transform.
        
        :param transform: Matrix that use for transformation (resize).'''
        ...
    
    def get_marked_text(self) -> str:
        '''Gets text under markup annotation as string.
        
        :returns: String containing text that is under markup annotation.'''
        ...
    
    def get_marked_text_fragments(self) -> aspose.pdf.text.TextFragmentCollection:
        '''Gets text under markup annotation as :class:`aspose.pdf.text.TextFragmentCollection`.
        
        :returns: :class:`aspose.pdf.text.TextFragmentCollection` containing :class:`aspose.pdf.text.TextFragment` s that is under markup annotation.'''
        ...
    
    @property
    def quad_points(self) -> list[aspose.pdf.Point]:
        '''Gets or sets an array of points specifying the coordinates of n quadrilaterals. Each quadrilateral encompasses a word or group of contiguous words in the text underlying the annotation.'''
        ...
    
    @quad_points.setter
    def quad_points(self, value: list[aspose.pdf.Point]):
        ...
    
    ...

class TextStyle:
    '''Class represents style of text in annotation'''
    
    @property
    def font_name(self) -> str:
        '''Name of the font.'''
        ...
    
    @font_name.setter
    def font_name(self, value: str):
        ...
    
    @property
    def font_size(self) -> float:
        '''Fonst size.'''
        ...
    
    @font_size.setter
    def font_size(self, value: float):
        ...
    
    @property
    def alignment(self) -> aspose.pdf.annotations.TextAlignment:
        '''Gets or sets horizontal alignment of the text.'''
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.pdf.annotations.TextAlignment):
        ...
    
    @property
    def horizontal_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Text alignment. Valid values are: Left, Center, Rigth.'''
        ...
    
    @horizontal_alignment.setter
    def horizontal_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        '''Color of the text.'''
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    ...

class TrimMarkAnnotation(aspose.pdf.annotations.CornerPrinterMarkAnnotation):
    '''Represents a Trim Mark annotation.
    
    Trim marks are placed at the corners of a printed page to indicate where the page is to be trimmed.'''
    
    def __init__(self, page: aspose.pdf.Page, position: aspose.pdf.annotations.PrinterMarkCornerPosition):
        '''Initializes a new instance of the :class:`TrimMarkAnnotation` class.
        
        :param page: The page where the annotation will be added.
        :param position: The position of the trim mark on the page.
        
        This constructor creates a TrimMarkAnnotation and adds it to the specified page at the specified position.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor for annotation processing.
        
        :param visitor: AnnotationSelector object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class UnderlineAnnotation(aspose.pdf.annotations.TextMarkupAnnotation):
    '''Represents an underline annotation that appears as an underline in the text of the document.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Creates new Underline annotation on the specified page.
        
        :param page: The document's page where annotation should be created.
        :param rect: The annotation rectangle, defining the location of the annotation on the page.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor object to process the annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    ...

class WatermarkAnnotation(aspose.pdf.annotations.Annotation):
    '''Class describes Watermark annotation object.'''
    
    def __init__(self, page: aspose.pdf.Page, rect: aspose.pdf.Rectangle):
        '''Constructor for Watermark annotation class.
        
        :param page: Page where annotation should be placed.
        :param rect: Position of the annotation.'''
        ...
    
    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Apply visitor for annotation.
        
        :param visitor: Visitor object.'''
        ...
    
    def change_after_resize(self, transform: aspose.pdf.Matrix) -> None:
        '''Overrides the definition in the base class with an empty body.
        
        :param transform: Matrix specifying the transformation.'''
        ...
    
    def set_text(self, text: aspose.pdf.facades.FormattedText) -> None:
        '''Set text of the annotation.
        
        :param text: Text value.'''
        ...
    
    def set_text_and_state(self, text: list[str], text_state: aspose.pdf.text.TextState) -> None:
        '''Set text of the annotation.
        
        :param text: Text value.
        :param text_state: Text state.'''
        ...
    
    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets annotation type.'''
        ...
    
    @property
    def fixed_print(self) -> aspose.pdf.annotations.FixedPrint:
        '''Fuxed print object of Watermark annotation.'''
        ...
    
    @property
    def opacity(self) -> float:
        '''Gets or sets opacity of the annotation.'''
        ...
    
    @opacity.setter
    def opacity(self, value: float):
        ...
    
    ...

class WidgetAnnotation(aspose.pdf.annotations.Annotation):
    '''Class representing widget annotation.'''
    
    def __init__(self, doc: aspose.pdf.Document):
        '''Create annotation (used for Generator)
        
        :param doc: Document where annotation will be created.'''
        ...
    
    @overload
    def export_to_json(self, stream: Any, options: aspose.pdf.engine.io.convertstrategies.converthelpers.ExportFieldsToJsonOptions) -> Iterable[aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult]:
        '''Exports the specified PDF form field to JSON format and writes the result to the provided stream.
        
        :param stream: The stream to write the JSON output to.
        :param options: Optional settings for exporting the form field to JSON.
        :returns: A collection of :class:`aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult` indicating the result of the export operation for the specified form field and its child elements, if present.'''
        ...
    
    @overload
    def export_to_json(self, file_name: str, options: aspose.pdf.engine.io.convertstrategies.converthelpers.ExportFieldsToJsonOptions) -> Iterable[aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult]:
        '''Exports the specified PDF form field to JSON format and writes the result to the specified file.
        
        :param file_name: The name of the file to write the JSON output to.
        :param options: Optional settings for exporting the form field to JSON.
        :returns: A collection of :class:`aspose.pdf.engine.io.convertstrategies.converthelpers.FieldSerializationResult` indicating the result of the export operation for the specified form field and its child elements, if present.'''
        ...

    def accept(self, visitor: aspose.pdf.annotations.AnnotationSelector) -> None:
        '''Accepts visitor.
        
        :param visitor: Visitor to be accepted.'''
        ...
    
    def get_checked_state_name(self) -> str:
        '''Returns name of "checked" state according to existing state names.
        
        :returns: The name of the "checked" state for this annotation.'''
        ...

    @property
    def annotation_type(self) -> aspose.pdf.annotations.AnnotationType:
        '''Gets type of annotation.'''
        ...
    
    @property
    def actions(self) -> aspose.pdf.annotations.AnnotationActionCollection:
        '''Gets the annotation actions.'''
        ...
    
    @property
    def on_activated(self) -> aspose.pdf.annotations.PdfAction:
        '''An action which shall be performed when the annotation is activated.'''
        ...
    
    @on_activated.setter
    def on_activated(self, value: aspose.pdf.annotations.PdfAction):
        ...
    
    @property
    def highlighting(self) -> aspose.pdf.annotations.HighlightingMode:
        '''Annotation highlighting mode.'''
        ...
    
    @highlighting.setter
    def highlighting(self, value: aspose.pdf.annotations.HighlightingMode):
        ...
    
    @property
    def parent(self) -> aspose.pdf.forms.Field:
        '''Gets annotation parent.'''
        ...
    
    @property
    def default_appearance(self) -> aspose.pdf.annotations.DefaultAppearance:
        '''Gets or sets default appearance of the field.'''
        ...
    
    @default_appearance.setter
    def default_appearance(self, value: aspose.pdf.annotations.DefaultAppearance):
        ...
    
    @property
    def read_only(self) -> bool:
        '''Gets or sets read only status of the field.'''
        ...
    
    @read_only.setter
    def read_only(self, value: bool):
        ...
    
    @property
    def required(self) -> bool:
        '''Gets or sets required status of the field.'''
        ...
    
    @required.setter
    def required(self, value: bool):
        ...
    
    @property
    def exportable(self) -> bool:
        '''Gets or sets exportable flag of the field.'''
        ...
    
    @exportable.setter
    def exportable(self, value: bool):
        ...
    
    ...

class XYZExplicitDestination(aspose.pdf.annotations.ExplicitDestination):
    '''Represents explicit destination that displays the page with the coordinates (left, top) positioned at the upper-left corner of the window and the contents of the page magnified by the factor zoom. A null value for any of the parameters left, top, or zoom specifies that the current value of that parameter is to be retained unchanged. A zoom value of 0 has the same meaning as a null value.'''
    
    @overload
    def __init__(self, page: aspose.pdf.Page, left: float, top: float, zoom: float):
        '''Creates local explicit destination.
        
        :param page: The destination page object.
        :param left: Left horizontal coordinate of the upper-left corner of the window.
        :param top: Top vertical coordinate of the upper-left corner of the window.
        :param zoom: Zoom factor.'''
        ...
    
    @overload
    def __init__(self, document: aspose.pdf.Document, page_number: int, left: float, top: float, zoom: float):
        '''Creates remote explicit destination.
        
        :param document: The parent document that contains this object.
        :param page_number: The destination page number of remote document.
        :param left: Left horizontal coordinate of the upper-left corner of the window.
        :param top: Top vertical coordinate of the upper-left corner of the window.
        :param zoom: Zoom factor.'''
        ...
    
    @overload
    def __init__(self, page_number: int, left: float, top: float, zoom: float):
        '''Creates remote explicit destination.
        
        :param page_number: The destination page number of remote document.
        :param left: Left horizontal coordinate of the upper-left corner of the window.
        :param top: Top vertical coordinate of the upper-left corner of the window.
        :param zoom: Zoom factor.'''
        ...
    
    @overload
    @staticmethod
    def create_destination(self, page: aspose.pdf.Page, left: float, top: float, zoom: float, consider_rotation: bool) -> aspose.pdf.annotations.XYZExplicitDestination:
        '''Create destintion to specified location of the page considering page rotation if required.
        
        :param page: Destination page.
        :param left: Left position on the page.
        :param top: Top position on the page.
        :param zoom: Zoom factor (0 for default).
        :param consider_rotation: If true position will be recalculated according to page rotation.
        :returns: Destination object.'''
        ...
    
    @overload
    @staticmethod
    def create_destination_to_upper_left_corner(self, page: aspose.pdf.Page, zoom: float) -> aspose.pdf.annotations.XYZExplicitDestination:
        '''Create destionation to upper left corner of the specifed page.
        
        :param page: Destination page.
        :param zoom: Zoom factor.
        :returns: Destination object.'''
        ...
    
    @overload
    @staticmethod
    def create_destination_to_upper_left_corner(self, page: aspose.pdf.Page) -> aspose.pdf.annotations.XYZExplicitDestination:
        '''Create destination to specified page.
        
        :param page: Destination page.
        :returns: Destination object.'''
        ...
    
    def to_string(self) -> str:
        '''Converts the object state into string value. Example: "1 XYZ 100 200 3".
        
        :returns: String value representing object state.'''
        ...
    
    @property
    def left(self) -> float:
        '''Gets left horizontal coordinate of the upper-left corner of the window.'''
        ...
    
    @property
    def top(self) -> float:
        '''Gets top vertical coordinate of the upper-left corner of the window.'''
        ...
    
    @property
    def zoom(self) -> float:
        '''Gets zoom factor.'''
        ...
    
    ...

class XfdfReader:
    '''Class which peroformes reading of XFDF format.'''
    
    def __init__(self):
        ...
    
    @staticmethod
    def read_annotations(self, stream: Any, document: aspose.pdf.Document) -> None:
        '''Import annotations from XFDF file and put them into document.
        
        :param stream: Source stream containing XFDF file.
        :param document: Document where annotations will be added.'''
        ...
    
    @staticmethod
    def read_fields(self, stream: Any, document: aspose.pdf.Document) -> None:
        '''Import field values from XFDF file.
        
        :param stream: Stream containing XFDF data.
        :param document: Document where fields data will be imported.'''
        ...
    
    ...

class AnnotationFlags:
    '''A set of flags specifying various characteristics of the annotation.'''
    
    DEFAULT: AnnotationFlags
    INVISIBLE: AnnotationFlags
    HIDDEN: AnnotationFlags
    PRINT: AnnotationFlags
    NO_ZOOM: AnnotationFlags
    NO_ROTATE: AnnotationFlags
    NO_VIEW: AnnotationFlags
    READ_ONLY: AnnotationFlags
    LOCKED: AnnotationFlags
    TOGGLE_NO_VIEW: AnnotationFlags
    LOCKED_CONTENTS: AnnotationFlags

class AnnotationState:
    '''The enumeration of states to which the original annotation can be set.'''
    
    UNDEFINED: AnnotationState
    MARKED: AnnotationState
    UNMARKED: AnnotationState
    ACCEPTED: AnnotationState
    REJECTED: AnnotationState
    CANCELLED: AnnotationState
    COMPLETED: AnnotationState
    NONE: AnnotationState

class AnnotationStateModel:
    '''The state model corresponding to state of annotation.'''
    
    UNDEFINED: AnnotationStateModel
    MARKED: AnnotationStateModel
    REVIEW: AnnotationStateModel

class AnnotationType:
    '''Enumeration of annotation types.'''
    
    TEXT: AnnotationType
    CIRCLE: AnnotationType
    POLYGON: AnnotationType
    POLY_LINE: AnnotationType
    LINE: AnnotationType
    SQUARE: AnnotationType
    FREE_TEXT: AnnotationType
    HIGHLIGHT: AnnotationType
    UNDERLINE: AnnotationType
    SQUIGGLY: AnnotationType
    STRIKE_OUT: AnnotationType
    CARET: AnnotationType
    INK: AnnotationType
    LINK: AnnotationType
    POPUP: AnnotationType
    FILE_ATTACHMENT: AnnotationType
    SOUND: AnnotationType
    MOVIE: AnnotationType
    SCREEN: AnnotationType
    WIDGET: AnnotationType
    WATERMARK: AnnotationType
    TRAP_NET: AnnotationType
    PRINTER_MARK: AnnotationType
    REDACTION: AnnotationType
    STAMP: AnnotationType
    RICH_MEDIA: AnnotationType
    UNKNOWN: AnnotationType
    PDF3D: AnnotationType
    COLOR_BAR: AnnotationType
    TRIM_MARK: AnnotationType
    BLEED_MARK: AnnotationType
    REGISTRATION_MARK: AnnotationType
    PAGE_INFORMATION: AnnotationType

class BorderEffect:
    '''Describes effect which should be applied to the border of the annotations.'''
    
    NONE: BorderEffect
    CLOUDY: BorderEffect

class BorderStyle:
    '''Describes style of the annotation border.'''
    
    SOLID: BorderStyle
    DASHED: BorderStyle
    BEVELED: BorderStyle
    INSET: BorderStyle
    UNDERLINE: BorderStyle

class CapStyle:
    '''Style of line ending of Ink annotation line.'''
    
    RECTANGULAR: CapStyle
    ROUNDED: CapStyle

class CaptionPosition:
    '''Enumeration of the annotation�s caption positioning.'''
    
    INLINE: CaptionPosition
    TOP: CaptionPosition

class CaretSymbol:
    '''A symbol to be associated with the caret.'''
    
    NONE: CaretSymbol
    PARAGRAPH: CaretSymbol

class ColorsOfCMYK:
    '''Colors included in the CMYK color model.'''
    
    CYAN: ColorsOfCMYK
    MAGENTA: ColorsOfCMYK
    YELLOW: ColorsOfCMYK
    BLACK: ColorsOfCMYK

class ExplicitDestinationType:
    '''Enumerates the types of explicit destinations.'''
    
    XYZ: ExplicitDestinationType
    FIT: ExplicitDestinationType
    FIT_H: ExplicitDestinationType
    FIT_V: ExplicitDestinationType
    FIT_R: ExplicitDestinationType
    FIT_B: ExplicitDestinationType
    FIT_BH: ExplicitDestinationType
    FIT_BV: ExplicitDestinationType

class FileIcon:
    '''An icon to be used in displaying the annotation.'''
    
    PUSH_PIN: FileIcon
    GRAPH: FileIcon
    PAPERCLIP: FileIcon
    TAG: FileIcon

class FreeTextIntent:
    '''Enumerates the intents of the free text annotation.'''
    
    UNDEFINED: FreeTextIntent
    FREE_TEXT_CALLOUT: FreeTextIntent
    FREE_TEXT_TYPE_WRITER: FreeTextIntent

class HighlightingMode:
    '''Enumerates the annotation�s highlighting mode, the visual effect to be used when the mouse button is pressed or held down inside its active area.'''
    
    NONE: HighlightingMode
    INVERT: HighlightingMode
    OUTLINE: HighlightingMode
    PUSH: HighlightingMode
    TOGGLE: HighlightingMode

class Justification:
    '''Enumerates the forms of quadding (justification) to be used in displaying the annotation�s text.'''
    
    LEFT: Justification
    CENTER: Justification
    RIGHT: Justification

class LaunchActionOperation:
    '''Enumerates the operations to perform with document during launch action executing.'''
    
    UNDEFINED: LaunchActionOperation
    OPEN: LaunchActionOperation
    PRINT: LaunchActionOperation

class LightingSchemeType:
    '''Enum LightingSchemeType: set of lighting scheme types.'''
    
    ARTWORK: LightingSchemeType
    NONE: LightingSchemeType
    WHITE: LightingSchemeType
    DAY: LightingSchemeType
    NIGHT: LightingSchemeType
    HARD: LightingSchemeType
    PRIMARY: LightingSchemeType
    BLUE: LightingSchemeType
    RED: LightingSchemeType
    CUBE: LightingSchemeType
    CAD: LightingSchemeType
    HEADLAMP: LightingSchemeType

class LineEnding:
    '''Enumerates the line ending styles to be used in drawing the line.'''
    
    NONE: LineEnding
    SQUARE: LineEnding
    CIRCLE: LineEnding
    DIAMOND: LineEnding
    OPEN_ARROW: LineEnding
    CLOSED_ARROW: LineEnding
    BUTT: LineEnding
    R_OPEN_ARROW: LineEnding
    R_CLOSED_ARROW: LineEnding
    SLASH: LineEnding

class LineIntent:
    '''Enumerates the intents of the line annotation.'''
    
    UNDEFINED: LineIntent
    LINE_ARROW: LineIntent
    LINE_DIMENSION: LineIntent

class PDF3DActivation:
    '''Enum PDF3DActivation: set of 3D annotation activation mode.'''
    
    ACTIVE_WHEN_OPEN: PDF3DActivation
    ACTIVE_WHEN_VISIBLE: PDF3DActivation
    ACTIVATED_USER_OR_SCRIPT_ACTION: PDF3DActivation

class PolyIntent:
    '''Enumerates the intents of the polygon or polyline annotation.'''
    
    UNDEFINED: PolyIntent
    POLYGON_CLOUD: PolyIntent
    POLY_LINE_DIMENSION: PolyIntent
    POLYGON_DIMENSION: PolyIntent

class PredefinedAction:
    '''Defines different actions which can be triggered from a PDF file.'''
    
    FIRST_PAGE: PredefinedAction
    LAST_PAGE: PredefinedAction
    NEXT_PAGE: PredefinedAction
    PREV_PAGE: PredefinedAction
    PRINT_DIALOG: PredefinedAction
    PRINT: PredefinedAction
    BOOKMARKS_EXPAN_CURRENT_BOOKMARK: PredefinedAction
    BOOKMARKS_HIGHTLIGHT_CURRENT_BOOKMARK: PredefinedAction
    DOCUMENT_ATTACH_FILE: PredefinedAction
    DOCUMENT_CROP_PAGES: PredefinedAction
    DOCUMENT_DELETE_PAGES: PredefinedAction
    DOCUMENT_EXTRACT_PAGES: PredefinedAction
    DOCUMENT_INSERT_PAGES: PredefinedAction
    DOCUMENT_REPLACE_PAGES: PredefinedAction
    DOCUMENT_ROTATE_PAGES: PredefinedAction
    EDIT_CHECK_SPELLING_IN_COM_FIELD_EDIT: PredefinedAction
    EDIT_FIND: PredefinedAction
    EDIT_PREFERENCES: PredefinedAction
    EDIT_SEARCH: PredefinedAction
    FILE_ATTACH_TO_EMAIL: PredefinedAction
    FILE_CLOSE: PredefinedAction
    FILE_CREATE_PDF_FROM_SCANNER: PredefinedAction
    FILE_CREATE_PDF_FROM_WEB_PAGE: PredefinedAction
    FILE_EXIT: PredefinedAction
    FILE_ORGANIZER_OPEN_ORGANIZER: PredefinedAction
    FILE_PRINT: PredefinedAction
    FILE_PROPERTIES: PredefinedAction
    FILE_SAVE_AS: PredefinedAction
    MISCELLANEOUS_ZOOM_IN: PredefinedAction
    MISCELLANEOUS_ZOOM_OUT: PredefinedAction
    PAGE_IMAGES_PRINT_PAGES: PredefinedAction
    VIEW_GO_TO_NEXT_VIEW: PredefinedAction
    VIEW_GO_TO_PAGE: PredefinedAction
    VIEW_GO_TO_PRE_DOCUMENT: PredefinedAction
    VIEW_GO_TO_PRE_VIEW: PredefinedAction
    VIEW_NAVIGATION_PANELS_ARTICLES: PredefinedAction
    VIEW_NAVIGATION_PANELS_ATTACHMENTS: PredefinedAction
    VIEW_NAVIGATION_PANELS_BOOMARKS: PredefinedAction
    VIEW_NAVIGATION_PANELS_COMMENTS: PredefinedAction
    VIEW_NAVIGATION_PANELS_FIELDS: PredefinedAction
    VIEW_NAVIGATION_PANELS_LAYERS: PredefinedAction
    VIEW_NAVIGATION_PANELS_MODEL_TREE: PredefinedAction
    VIEW_NAVIGATION_PANELS_PAGES: PredefinedAction
    VIEW_NAVIGATION_PANELS_SIGNATURES: PredefinedAction
    VIEW_PAGE_DISPLAY_SINGLE_PAGE: PredefinedAction
    VIEW_PAGE_DISPLAY_SINGLE_PAGE_CONTINUOUS: PredefinedAction
    VIEW_PAGE_DISPLAY_TWO_UP: PredefinedAction
    VIEW_PAGE_DISPLAY_TWO_UP_CONTINUOUS: PredefinedAction
    VIEW_TOOLBARS_ADVANCE_EDITING: PredefinedAction
    VIEW_TOOLBARS_COMMENT_MARKUP: PredefinedAction
    VIEW_TOOLBARS_EDIT: PredefinedAction
    VIEW_TOOLBARS_FILE: PredefinedAction
    VIEW_TOOLBARS_FIND: PredefinedAction
    VIEW_TOOLBARS_FORMS: PredefinedAction
    VIEW_TOOLBARS_MEASURING: PredefinedAction
    VIEW_TOOLBARS_OBJECT_DATA: PredefinedAction
    VIEW_TOOLBARS_PAGE_DISPLAY: PredefinedAction
    VIEW_TOOLBARS_PAGE_NAVIGATION: PredefinedAction
    VIEW_TOOLBARS_PRINT_PRODUCTION: PredefinedAction
    VIEW_TOOLBARS_PROPERTIES_BAR: PredefinedAction
    VIEW_TOOLBARS_REDACTION: PredefinedAction
    VIEW_TOOLBARS_SELECT_ZOOM: PredefinedAction
    VIEW_TOOLBARS_TASKS: PredefinedAction
    VIEW_TOOLBARS_TYPEWRITER: PredefinedAction
    VIEW_ZOOM_ACTUAL_SIZE: PredefinedAction
    VIEW_ZOOM_FIT_HEIGHT: PredefinedAction
    VIEW_ZOOM_FIT_PAGE: PredefinedAction
    VIEW_ZOOM_FIT_VISIBLE: PredefinedAction
    VIEW_ZOOM_FIT_WIDTH: PredefinedAction
    VIEW_ZOOM_ZOOM_TO: PredefinedAction
    WINDOW_FULL_SCREEN_MODE: PredefinedAction

class PrinterMarkCornerPosition:
    '''Represents a position of a mark in a corner of a page.'''
    
    TOP_LEFT: PrinterMarkCornerPosition
    TOP_RIGHT: PrinterMarkCornerPosition
    BOTTOM_LEFT: PrinterMarkCornerPosition
    BOTTOM_RIGHT: PrinterMarkCornerPosition

class PrinterMarkSidePosition:
    '''Represents a position of a registration mark on a page.'''
    
    TOP: PrinterMarkSidePosition
    BOTTOM: PrinterMarkSidePosition
    LEFT: PrinterMarkSidePosition
    RIGHT: PrinterMarkSidePosition

class PrinterMarksKind:
    '''Specifies the types of printer's marks to be added to a document.
    
    This enumeration has a System.FlagsAttribute attribute that allows a bitwise combination of its member values.'''
    
    NONE: PrinterMarksKind
    TRIM_MARKS: PrinterMarksKind
    BLEED_MARKS: PrinterMarksKind
    REGISTRATION_MARKS: PrinterMarksKind
    COLOR_BARS: PrinterMarksKind
    PAGE_INFORMATION: PrinterMarksKind
    ALL: PrinterMarksKind

class RenderModeType:
    '''Enum RenderModeType: set of render mode types'''
    
    SOLID: RenderModeType
    SOLID_WIREFRAME: RenderModeType
    TRANSPARENT: RenderModeType
    TRANSPARENT_WARE_FRAME: RenderModeType
    BOUNDING_BOX: RenderModeType
    TRANSPARENT_BOUNDING_BOX: RenderModeType
    TRANSPARENT_BOUNDING_BOX_OUTLINE: RenderModeType
    WIREFRAME: RenderModeType
    SHADED_WIREFRAME: RenderModeType
    VERTICES: RenderModeType
    SHADED_VERTICES: RenderModeType
    ILLUSTRATION: RenderModeType
    SOLID_OUTLINE: RenderModeType
    SHADED_ILLUSTRATION: RenderModeType

class RenditionOperation:
    '''The operation to perform when the action is triggered.'''
    
    PLAY_STOP: RenditionOperation
    STOP: RenditionOperation
    PAUSE: RenditionOperation
    RESUME: RenditionOperation
    PLAY_RESUME: RenditionOperation
    UNDEFINED: RenditionOperation

class RenditionType:
    '''Enumeration describes possible types of Rendition.'''
    
    MEDIA: RenditionType
    SELECTOR: RenditionType
    UNDEFINED: RenditionType

class ReplyType:
    '''Enumerates the kinds of the relationships (the “reply type”) between the annotation and one specified by InReplyTo.'''
    
    UNDEFINED: ReplyType
    REPLY: ReplyType
    GROUP: ReplyType

class SoundEncoding:
    '''The encoding format for the sample data.'''
    
    RAW: SoundEncoding
    SIGNED: SoundEncoding
    MU_LAW: SoundEncoding
    A_LAW: SoundEncoding

class SoundIcon:
    '''Enumerates the icons to be used in displaying the annotation.'''
    
    SPEAKER: SoundIcon
    MIC: SoundIcon

class SoundSampleDataEncodingFormat:
    '''The encoding format for the sound sample data.'''
    
    RAW: SoundSampleDataEncodingFormat
    SIGNED: SoundSampleDataEncodingFormat
    MU_LAW: SoundSampleDataEncodingFormat
    A_LAW: SoundSampleDataEncodingFormat

class StampIcon:
    '''Enumerates the icons to be used in displaying the annotation.'''
    
    DRAFT: StampIcon
    APPROVED: StampIcon
    EXPERIMENTAL: StampIcon
    NOT_APPROVED: StampIcon
    AS_IS: StampIcon
    EXPIRED: StampIcon
    NOT_FOR_PUBLIC_RELEASE: StampIcon
    CONFIDENTIAL: StampIcon
    FINAL: StampIcon
    SOLD: StampIcon
    DEPARTMENTAL: StampIcon
    FOR_COMMENT: StampIcon
    FOR_PUBLIC_RELEASE: StampIcon
    TOP_SECRET: StampIcon

class TextAlignment:
    '''Alignment of text in annotation.'''
    
    LEFT: TextAlignment
    CENTER: TextAlignment
    RIGHT: TextAlignment

class TextIcon:
    '''Enumerates the icons to be used in displaying the annotation.'''
    
    NOTE: TextIcon
    COMMENT: TextIcon
    KEY: TextIcon
    HELP: TextIcon
    NEW_PARAGRAPH: TextIcon
    PARAGRAPH: TextIcon
    INSERT: TextIcon
    CHECK: TextIcon
    CROSS: TextIcon
    CIRCLE: TextIcon
    STAR: TextIcon

