import sys, os

file_name = sys.argv[1]
new_file = os.path.splitext(file_name)[0]
class_file = new_file + ".cl-mytype"
type_file = open(class_file, "w")

try:
 lines = [line.strip() for line in open(sys.argv[1])]
except:
 print "improper file entry"

class program:
  def __init__(self):
    class_list = []
  def addClass(self, class_object):
  	class_list.append(class_object)

class no_inherits:
  def __init__(self, name):
  	name = name
  	feature_list = []
  def addFeature(self, feature):
    feature_list.append(feature)

class inherits:
  def __init__(self, name, superclass):
  	name = name
  	superclass = superclass
  	feature_list = []
  def addFeature(self, feature):
  	feature_list.append(feature)

class identifier:
  def __init__(self, string, lineno):
  	lineno = lineno
  	string = string

class attribute_no_init:
  def __init__(self, name, attr_type):
  	name = name
  	attr_type = attr_type 

class attr_init:
  def __init__(self, name, attr_type, body):
  	name = name
  	attr_type = attr_type
  	body = body

class method:
  def __init__(self, name, return_type, body):
    name = name
    return_type = return_type
    body = body
    formal_list = []
  def addFormal(self, formal):
  	formal_list.append(formal)

class formal: #composed of two identifiers. one for the name, one for the type
  def __init__(self, name, formal_type):
    name = name
    formal_type = formal_type

class assign:
  def __init__(self, lineno, var, rhs):
    lineno = lineno
    var = var
    rhs = rhs

class dynamic_dispatch:
  def __init__(self, lineno, expr, method_name, arg_list):
  	lineno = lineno
  	expr = expr
  	method_name = method_name
  	arg_list = []
  def addArg(self, arg):
    arg_list.append(arg)

class static_dispatch:
  def __init__(self, lineno, expr, dispatch_type, method_name, arg_list):
  	lineno = lineno
  	expr = expr
  	dispatch_type = dispatch_type
  	method_name = method_name
  	arg_list = []
  def addArg(self, arg):
  	arg_list.append(arg)

class self_dispatch:
  def __init__(self, lineno, method_name, arg_list):
    lineno = lineno
    method_name = method_name
    arg_list = []
  def addArg(self, arg):
    arg_list.append(arg)

class if_object:
  def __init__(self, lineno, predicate, then, else_statment):
    lineno = lineno
    predicate = predicate
    then = then
    else_statment = else_statment

class while_object:
  def __init__(self, lineno, predicate, body):
    lineno = lineno
    predicate = predicate
    body = body

class block_object:
  def __init__(self, lineno, expression_list):
    lineno = lineno
    expression_list = []
  def addExpression(self, expression):
  	expression_list.append(expression)

class new_object:
  def __init__(self, lineno, class_name):
  	lineno = lineno
  	class_name = class_name

class isvoid_object:
  def __init__(self, lineno, e):
    lineno = lineno
    e = e

class plus_object:
  def __init__(self, lineno, x, y):
  	lineno = lineno
  	x = x
  	y = y

class minus_object:
  def __init__(self, lineno, x, y):
  	lineno = lineno
  	x = x
  	y = y

class times_object:
  def __init__(self, lineno, x, y):
  	lineno = lineno
  	x = x
  	y = y

class divide_object:
  def __init__(self, lineno, x, y):
  	lineno = lineno
  	x = x
  	y = y
  
class lt_object:
  def __init__(self, lineno, x, y):
  	lineno = lineno
  	x = x
  	y = y

class le_object:
  def __init__(self, lineno, x, y):
    lineno = lineno
    x = x
    y = y

class eq_object:
  def __init__(self, lineno, x, y):
  	lineno = lineno
  	x = x
  	y = y

class not_object:
  def __init__(self, lineno, x):
  	lineno = lineno
  	x = x

class negate_object:
  def __init__(self, lineno, x):
  	lineno = lineno
  	x = x








  









