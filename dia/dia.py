import warnings
import cPickle as pickle

class Sheet :
	'''returned by dia.register_export() but not used otherwise yet.'''
	def __init__(self) :
		self.description = None # 
		self.filename = None # 
		self.name = None # 
		self.objects = None # 
		self.user = None # 

class Matrix :
	'''Dia's matrix to do affine transformation'''
	def __init__(self) :
		self.x0 = None # 
		self.xx = None # 
		self.xy = None # 
		self.y0 = None # 
		self.yx = None # 
		self.yy = None # 

class Paperinfo :
	'''dia.Paperinfo is part of dia.DiagramData describing the paper'''
	def __init__(self) :
		self.height = None # 
		self.is_portrait = None # 
		self.name = None # 
		self.scaling = None # 
		self.width = None # 

class Rectangle :
	'''The dia.Rectangle does not only provide access trough it's members but also via a sequence interface.'''
	def __init__(self) :
		self.bottom = None # 
		self.left = None # 
		self.right = None # 
		self.top = None # 

class Handle :
	'''A handle is used to connect objects or for object resizing.'''
	def __init__(self, obj) :
		self.connect_type = None # 
		self.connected_to = None # 
		self.obj = obj
		self.id = None # 
		self.pos = None # 
		self.type = None # 

	def connect (self, cp) :
		""" connect(ConnectionPoint: cp) -> None.  Connect object A's handle with object B's connection point. To disconnect a handle pass in None. """
		self.connected_to = cp
		cp.connected.append(self.obj)

class Object :
	'''The main building block of diagrams.'''
	def __init__(self, type, *args) :
		self.bounding_box = None # 
		self.connections = [ConnectionPoint(self) for _ in range(8)]
		self.handles = [Handle(self) for _ in range(8)] 
		self.parent = None # 
		self.properties = Properties(self)
		self.properties["elem_width"] = 20
		self.properties["elem_height"] = 20
		self.type = type
	
	def add_property(self, key, value) :
		if key in ('attributes','operations') :
			end = self.connections.pop()
			for _ in range(len(value.value)*2) :
				self.connections.append(ConnectionPoint(self))
			self.connections.append(end)

	def __getitem__(self, key) :
		pass

	def copy (self) :
		""" copy() -> Object.  Create a new object copy. """
		# returns 
		pass
	def destroy (self) :
		""" destroy() -> None.  Release the object. Must not be called when already added to a group or layer. """
		# returns 
		pass
	def distance_from (self) :
		""" distance_from(real: x, real: y) -> real.  Calculate the object's distance from the given point. """
		# returns 
		pass
	def draw (self, renderer) :
		""" draw(dia.Renderer: r) -> None.  Draw the object with the given renderer """
		pass
	def get_object_menu (self) :
		""" get_object_menu() -> Tuple.  Returns a named list of Menuitem(s). """
		# returns 
		pass
	def move (self, x, y) :
		""" move(real: x, real: y) -> None.  Move the entire object. The given point is the new object.obj_pos. """
		# returns 
		pass
	def move_handle (self) :
		""" move_handle(Handle: h, (real: x, real: y)[int: reason, int: modifiers]) -> None.  Move the given handle of the object to the given position """
		# returns 
		pass
		
class Diagram :
	'''Subclass of dia.DiagramData (at least in the C implementation) adding interfacing the GUI elements.'''
	def __init__(self, filename) :
		self.data = DiagramData() # 
		self.displays = [] # 
		self.filename = filename 
		self.modified = None # 
		self.selected = None
		#self._signals = {}

	def add_update (self, top, left, bottom, right) :
		""" add_update(real: top, real: left, real: bottom, real: right) -> None.  Add the given rectangle to the update queue. """
		# returns 
		pass

	def add_update_all (self) :
		""" add_update_all() -> None.  Add the diagram visible area to the update queue. """
		# returns 
		pass

	def connect_after (self, signal_name, callback) :
		""" connect_after(string: signal_name, Callback: func) -> None.  Listen to diagram events in ['removed', 'selection_changed']. """
		#self._signals[signal_name] = callback
		pass
		
	def display (self) :
		""" display() -> Display.  Create a new display of the diagram. """
		new_display = Display(self)
		self.displays.append(new_display)
		return new_display
		
	def find_clicked_object (self) :
		""" find_clicked_object(real[2]: point, real: distance) -> Object.  Find an object in the given distance of the given point. """
		# returns 
		pass
		
	def find_closest_connectionpoint (self, x, y, obj = None) :
		""" find_closest_connectionpoint(real: x, real: y[, Object: o]) -> (real: dist, ConnectionPoint: cp).  Given a point and an optional object to exclude, return the distance and closest connection point or None. """
		# returns 
		pass

	def find_closest_handle (self, point) :
		""" find_closest_handle(real[2]: point) -> (real: distance, Handle: h, Object: o).  Find the closest handle from point and return a tuple of the search results.  Handle and Object might be None. """
		# returns 
		pass

	def flush (self) :
		""" flush() -> None.  If no display update is queued, queue update. """
		pass

	def get_sorted_selected (self) :
		""" get_sorted_selected() -> list.  Return the current selection sorted by Z-Order. """
		# returns 
		pass

	def get_sorted_selected_remove (self) :
		""" get_sorted_selected_remove() -> list.  Return sorted selection and remove it from the diagram. """
		# returns 
		pass
		
	def group_selected (self) :
		""" group_selected() -> None.  Turn the current selection into a group object. """
		pass

	def is_selected (self, obj) :
		""" is_selected(Object: o) -> bool.  True if the given object is already selected. """
		# returns 
		pass

	def remove_all_selected (self) :
		""" remove_all_selected() -> None.  Delete all selected objects. """
		pass
		
	def save (self, filename) :
		""" save(string: filename) -> None.  Save the diagram under the given filename. """
		pickle.dump(self, open(filename, "wb"))

	def select (self, obj) :
		""" select(Object: o) -> None.  Add the given object to the selection. """
		pass

	def ungroup_selected (self) :
		""" ungroup_selected() -> None.  Split all groups in the current selection into single objects. """
		pass

	def unselect (self, obj) :
		""" unselect(Object: o) -> None.  Remove the given object from the selection) """
		pass

	def update_connections (self, obj) :
		""" update_connections(Object: o) -> None.  Update all connections of the given object. Might move connected objects. """
		pass

	def update_extents (self) :
		""" update_extents() -> None.  Force recaculation of the diagram extents. """
		pass

class Properties (dict) :
	'''
	A dictionary interface to dia.Object's standard properties.
	Many propertiescan be get and set through this. If there is a specific method
	to change anobjects property like o.move() or o.move_handle() use that instead.
	'''
	def __init__(self, obj, *args):
		self.obj = obj
		dict.__init__(self, args)

	def get (self, key) :
		val = dict.__getitem__(self, key)
		return val

	def has_key (self) :
		""" (NULL) """
		pass
	def keys (self) :
		""" (NULL) """
		pass
		
	def __getitem__(self, key):
		val = dict.__getitem__(self, key)
		return val
		
	def __setitem__(self, key, val):
		prop = Property(key, val)
		dict.__setitem__(self, key, prop)
		self.obj.add_property(key, prop)

		
class ObjectType :
	'''The dia.Object factory. Allows to create objects of the specific type. Use: factory = get_object_type(<type name>) to get a grip on it.'''
	def __init__(self, type) :
		self.name = type # 
		self.version = None # 
		pass
	#@staticmethod
	def create (self, x=0,y=0) :
		""" create(real: x, real: y) -> (Object: o, Handle: h1, Handle: h2)  Create a new object of this type. Returns a tuple containing the new object and up to two handles. """
		obj = Object(self)
		return (obj,Handle(obj),Handle(obj))
		
class ExportFilter :
	'''returned by dia.register_export() but not used otherwise yet.'''
	def __init__(self) :
		self.name = None # 
		self.unique_name = None # 

class BezPoint :
	'''A dia.Point, a bezier type and two control points (dia.Point) make a bezier point.'''
	def __init__(self) :
		self.p1 = None # 
		self.p2 = None # 
		self.p3 = None # 
		self.type = None # 

class ConnectionPoint :
	'''One of the major features of Dia are connectable objects. They work by this type accesible through dia.Object.connections[].'''
	def __init__(self, obj) :
		self.connected = [] # 
		self.directions = None # 
		self.flags = None # 
		self.object = obj 
		self.pos = None # 


class Arrow :
	'''Dia's line objects usually ends with an dia.Arrow'''
	def __init__(self) :
		self.length = None # 
		self.type = None # 
		self.width = None # 

class Error :
	'''The error object is just a helper to redirect errors to messages'''
	def __init__(self) :
		pass
	def write (self) :
		""" (NULL) """
		pass

class Menuitem :
	'''dia.Menuitem is holding menu functions for dia.Object'''
	def __init__(self) :
		self.active = None # 
		self.text = None # 
		pass
	def call (self) :
		""" call() -> None.  Invoke the menuitem callback on object. """
		pass

class Property :
	'''Interface to so called StdProps, the mechanism to control most of Dia's canvas objects properties. '''
	def __init__(self, name, value) :
		self.name = name # 
		self.type = None # 
		self.value = value # 
		self.visible = None # 
		pass

class Display :
	'''A Diagram can have multiple displays but every Display has just one Diagram.'''
	def __init__(self, diagram) :
		self.diagram = diagram 
		self.origin = None # 
		self.visible = None # 
		self.zoom_factor = None # 

	def add_update_all (self) :
		""" add_update_all() -> None.  Add the diagram visible area to the update queue. """
		pass

	def close (self) :
		""" close() -> None.  Close the display possibly asking to save. """
		pass

	def flush (self) :
		""" flush() -> None.  If no display update is queued, queue update. """
		pass

	def resize_canvas (self, width, height) :
		""" resize_canvas(int: width, int: height) -> None.  BEWARE: Changing the drawing area but not the window size. """
		pass
		
	def scroll (self, dx, dy) :
		""" scroll(real: dx, real: dy) -> None.  Scroll the visible area by the given delta. """
		pass

	def scroll_down (self) :
		""" scroll_down() -> None. Scroll downwards by a fixed amount. """
		pass

	def scroll_left (self) :
		""" scroll_left() -> None. Scroll to the left by a fixed amount. """
		pass

	def scroll_right (self) :
		""" scroll_right() -> None. Scroll to the right by a fixed amount. """
		pass

	def scroll_up (self) :
		""" scroll_up() -> None. Scroll upwards by a fixed amount. """
		pass

	def set_origion (self, x, y) :
		""" set_origion(real: x, real, y) -> None.  Move the given diagram point to the top-left corner of the visible area. """
		# returns 
		pass
		
	def set_title (self, title) :
		""" set_title(string: title) -> None.  Temporary change of the diagram title. """
		pass

	def zoom (self, point, factor) :
		""" zoom(real[2]: point, real: factor) -> None.  Zoom around the given point. """
		# returns 
		pass

class Layer :
	'''A Layer is part of a Diagram and can contain objects.'''
	def __init__(self, name) :
		self.extents = None # 
		self.name = name
		self.objects = [] # 
		self.visible = 1 # 

	def add_object (self, object) :
		self.objects.append(object)
		""" add_object(Object: o[, int: position]) -> None.  Add the object to the layer at the top or the given position counting from bottom. """

	def destroy (self) :
		""" Release the layer. Must not be called when already added to a diagram. """
		pass

	def find_closest_connection_point (self, x, y, obj = None) :
		""" find_closest_connectionpoint(real: x, real: y[, Object: o]) -> (real: dist, ConnectionPoint: cp).  Given a point and an optional object to exclude return the distance and the closest connection point or None. """
		#(real: dist, ConnectionPoint: cp)
		pass

	def find_closest_object (self, x, y, maxdist) :
		""" find_closest_object(real: x, real: y, real: maxdist) -> Object.  Find an object in the given maximum distance of the given point. """
		pass

	def find_objects_in_rectangle (self, top, left, bottom, right) :
		""" find_objects_in_rectangle(real: top, real left, real: bottom, real: right) -> Objects  Returns a list of objects found in the given rectangle. """
		pass

	def object_get_index (self, obj) :
		""" object_get_index(Object: o) -> int.  Returns the index of the object in the layers list of objects. """
		return self.objects.index(obj)

	def remove_object (self, obj) :
		""" remove_object(Object: o) -> None  Remove the object from the layer and delete it. """
		self.objects.remove(obj)
		del obj

	def render (self, r) :
		""" render(dia.Renderer: r) -> None.  Render the layer with the given renderer """
		pass

	def update_extents (self) :
		""" update_extents() -> None.  Force recaculation of the layer extents. """
		pass
		
class Point :
	'''The dia.Point does not only provide access trough it's members but also via a sequence interface.'''
	def __init__(self) :
		self.x = None # 
		self.y = None # 
		pass

class Color :
	'''A color either defined by a color string or by a tuple with three elements (r, g, b) with type float 0.0 ... 1.0 or range int 0 ... 65535'''
	def __init__(self) :
		self.alpha = None # 
		self.blue = None # 
		self.green = None # 
		self.red = None # 
		pass
		
class Text :
	'''Many objects (dia.Object) having text to display provide this property.'''
	def __init__(self) :
		self.color = None # 
		self.font = None # 
		self.height = None # 
		self.position = None # 
		self.text = None # 
		pass
		
class Image :
	'''dia.Image gets passed into DiaRenderer.draw_image'''
	def __init__(self) :
		self.filename = None # 
		self.height = None # 
		self.mask_data = None # 
		self.rgb_data = None # 
		self.uri = None # 
		self.width = None # 
		pass
		
class dia :
	'''The dia module allows to write Python plug-ins for Dia [http://live.gnome.org/Dia/Python]

This modules is designed to run Python scripts embedded in Dia. To make your script accessible
to Dia you have to put it into $HOME/.dia/python and let it call one of the register_*() functions.
It is possible to write import filters [register_import()] and export filters [register_export()], as well as scripts to manipulate existing diagrams or create new ones [register_action()].

For stand-alone Python bindings to Dia see http://mail.gnome.org/archives/dia-list/2007-March/msg00092.html'''
	def __init__(self) :
		self._active_display = None
		self._diagrams = []
		self._actions = {}
		self._callbacks = {}
		self._import = {}
		self._export = {}
		self._plugins = []
		self._sheets = []
		self._registered_types = {}
	
	def active_display (self) :
		""" active_display() -> Display.  Delivers the currently active display 'dia.Display' or None """
		if not self._active_display :
			if self._diagrams[0] : self._active_display = self._diagrams[0]
		return self._active_display
		
	def diagrams (self) :
		""" diagrams() -> List of Diagram.  Returns the list of currently open diagrams """
		return self._diagrams
		
	@staticmethod
	def get_object_type (type) :
		""" get_object_type(string: type) -> ObjectType.  From a type name like "Standard - Line" return the factory to create objects of that type, see: DiaObjectType """
		return ObjectType(type)

	def group_create (self, objs) :
		""" group_create(List of Object: objs) -> Object.  Create a group containing the given list of dia.Object(s) """
		return Object("Group", objs)

	def load (self, filename) :
		""" load(string: name) -> Diagram.  Loads a diagram from the given filename """
		diagram = pickle.load(open(filename, "rb"))
		self._diagrams.append(diagram)
		return self._diagrams[len(self._diagrams)-1]
		
	def message (self, type, msg) :
		""" message(int: type, string: msg) -> None.  Popup a dialog with given message """
		warnings.warn(msg)
		
	def new (self, name) :
		""" new(string: name) -> Diagram.  Create an empty diagram """
		diagram = Diagram(name)
		self._diagrams.append(diagram)
		return diagram
		
	def register_action (self, action, description, menupath, func) :
		""" register_action(string: action, string: description, string: menupath, Callback: func) -> None.  Register a callback function which appears in the menu. Depending on the menu path used during registrationthe callback gets called with the current DiaDiagramData object """
		self._actions[action] = [(description, menupath, func)]
		
	def register_callback (self, description, menupath, func) :
		""" register_callback(string: description, string: menupath, Callback: func) -> None.  Register a callback function which appears in the menu. Depending on the menu path used during registrationthe callback gets called with the current DiaDiagramData object """
		self._callbacks[description] = [(menupath, func)]

	def register_export (self, name, extension, r) :
		""" register_export(string: name, string: extension, Renderer: r) -> None.  Allows to register an export filter written in Python. It needs to conform to the DiaRenderer interface. """
		self._export[name] = [(extension, r)]

	def register_import (self, name, extension, func) :
		""" register_import(string: name, string: extension, Callback: func) -> None.  Allows to register an import filter written in Python, that is mainly a callback function which fills thegiven DiaDiagramData from the given filename """
		self._import[name] = [(extension, func)]

	def register_plugin (self, filename) :
		""" register_plugin(string: filename) -> None.  Registers a single plug-in given its filename, that is load a dynamic module. """
		self._plugins.append(filename)

	def registered_sheets (self) :
		""" registered_sheets() -> List of registered sheets.  A list of all registered sheets. """
		return self._sheets
		
	def registered_types (self) :
		""" registered_types() -> Dict of ObjectType indexed by their name.  A dictionary of all registered object factories, aka. DiaObjectType """
		return self._registered_types
		
	def update_all (self) :
		""" update_all() -> None.  Force an asynchronous update of all existing diagram displays """
		for diagram in self._diagrams :
			diagram.flush()

class Font :
	'''Provides access to some objects font property.'''
	def __init__(self) :
		self.family = None # 
		self.name = None # 
		self.style = None # 
		pass

class DiagramData :
	'''
	The 'low level' diagram object. It contains everything to manipulate diagrams
	from im- and export filters as well as from the UI. It does not provide any access
	to GUI elements related to the diagram.Use the subclass dia.Diagram object for such matters.
	'''
	def __init__(self) :
		self.active_layer = None # 
		self.bg_color = None # 
		self.extents = None # 
		self.grid_visible = None # 
		self.grid_width = None # 
		self.hguides = None # 
		self.layers = [] # 
		self.paper = None # 
		self.selected = None # 
		self.vguides = None # 
		#self._signals = {}

	def add_layer (self, layer, position = 0) :
		""" add_layer(Layer: layer[, int: position]) -> Layer.  Add a layer to the diagram at the top or the given position counting from bottom. """
		self.layers.insert(position, Layer(layer))
		return self.layers[position]

	def connect_after (self, signal_name, callback) :
		""" connect_after(string: signal_name, Callback: func) -> None.  Listen to diagram events in ['object_add', 'object_remove']. """
		#self._signals[signal_name] = callback
		pass
		
	def delete_layer (self, layer) :
		""" delete_layer(Layer: layer) -> None.  Remove the given layer from the diagram. """
		self.layers.remove(layer)
		
	def get_sorted_selected (self) :
		""" get_sorted_selected() -> list.  Return the current selection sorted by Z-Order. """
		# returns 
		pass

	def lower_layer (self) :
		""" lower_layer() -> None.  Move the layer towards the bottom. """
		# returns 
		pass

	def raise_layer (self) :
		""" raise_layer() -> None.  Move the layer towards the top. """
		# returns 
		pass
		
	def set_active_layer (self, layer) :
		""" set_active_layer(Layer: layer) -> None.  Make the given layer the active one. """
		self.active_layer = layer

	def update_extents (self) :
		""" update_extents() -> None.  Recalculation of the diagram extents. """
		pass

