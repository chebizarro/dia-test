from dia import *

_dia = dia()

def active_display() :
	global _dia
	return _dia.active_display()
	
def diagrams() :
	global _dia
	return _dia.diagrams()
	
def get_object_type(type) :
	global _dia
	return _dia.get_object_type(type)

def group_create(objs) :
	global _dia
	return _dia.group_create("Group", objs)

def load(filename) :
	global _dia
	return _dia.load(filename)
	
def message(type, msg) :
	global _dia
	_dia.message(type, msg)
	
def new(name) :
	global _dia
	return _dia.new(name)
		
def register_action(action, description, menupath, func) :
	global _dia
	_dia.register_action(action, description, menupath, func)
	
def register_callback(description, menupath, func) :
	global _dia
	_dia.register_callback(description, menupath, func)
	
def register_export(name, extension, r) :
	global _dia
	_dia.register_export(name, extension, r)

def register_import(name, extension, func) :
	global _dia
	_dia.register_import(name, extension, func)

def register_plugin(filename) :
	global _dia
	_dia.register_plugin(filename)

def registered_sheets() :
	global _dia
	return _dia.registered_sheets()
	
def registered_types() :
	global _dia
	return _dia.registered_types()
	
def update_all() :
	global _dia
	_dia.update_all()
