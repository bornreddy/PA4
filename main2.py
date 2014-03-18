import sys, os

lines = []
file_name = sys.argv[1]
new_file = open((os.path.splitext(file_name)[0] + ".cl-mytype"), "w")
try:
 lines = [line.strip() for line in open(sys.argv[1])]
except:
 print "improper file entry"

def list_to_string(list):
  list_string = ""
  for n in list:
    list_string = list_string + str(n)
  return list_string

class program_object:
  def __init__(self):
    self.class_list = []
  def addClass(self, class_object): 
  	self.class_list.append(class_object)
  def __str__(self):
    return str(len(self.class_list)) + list_to_string(self.class_list)

class no_inherits:
  def __init__(self, name):
    self.name = name
    self.feature_list = []
  def addFeature(self, feature):
    self.feature_list.append(feature)
  def __str__(self):
    return str(self.name) + "\nno_inherits\n" + str(len(self.feature_list)) + list_to_string(self.feature_list) 

class inherits:
  def __init__(self, name, superclass):
  	self.name = name
  	self.superclass = superclass
  	self.feature_list = []
  def addFeature(self, feature):
  	self.feature_list.append(feature)
  def __str__(self):
    return str(self.name) + "\ninherits\n" + str(self.superclass) + "\n" + str(len(self.feature_list)) + list_to_string(self.feature_list)

class identifier:
  def __init__(self, lineno, string):
  	self.lineno = lineno
  	self.string = string
  def __str__(self):
    return self.lineno + "\n" + self.string

class attribute_no_init:
  def __init__(self, name, attr_type):
  	self.name = name
  	self.attr_type = attr_type 
  def __str__(self):
    return "\nattribute_no_init\n" + str(self.name) + "\n" + str(self.attr_type) 

class attribute_init:
  def __init__(self, name, attr_type, init):
  	self.name = name
  	self.attr_type = attr_type
  	self.init = init
  def __str__(self):
    return "\nattribute_init\n" + str(self.name) + "\n" + str(self.attr_type) + "\n" + str(self.init)

class method:
  def __init__(self, name, formal_list, return_type, body):
    self.name = name
    self.formal_list = formal_list
    self.return_type = return_type
    self.body = body
  def addFormal(self, formal):
  	self.formal_list.append(formal)
  def __str__(self):
    formal_list_string = ""
    for n in self.formal_list:
      formal_list_string = formal_list_string + str(n)
    return "\nmethod\n" + str(self.name) + formal_list_string + "\n" + str(self.return_type) + "\n" + str(self.body)

class formal: #composed of two identifiers. one for the name, one for the type
  def __init__(self, name, formal_type):
    self.name = name
    self.formal_type = formal_type
  def __str__(self):
    return str(self.name) + str(self.formal_type)

class assign:
  def __init__(self, lineno, var, rhs):
    self.lineno = lineno
    self.var = var
    self.rhs = rhs
  def __str__(self):
    return self.lineno + "\nassign\n" + str(self.var) + "\n" + str(self.rhs)

class dynamic_dispatch:
  def __init__(self, lineno, expr, method_name, arg_list):
  	self.lineno = lineno
  	self.expr = expr
  	self.method_name = method_name
  	self.arg_list = arg_list
  # def __str__(self):
  #   arg_list_string = ""
  #   return self.lineno + "\ndynamic_dispatch\n" + str(self.expr) + "\n" + str(self.method_name) + "\n" + arg_list
class static_dispatch:
  def __init__(self, lineno, expr, dispatch_type, method_name, arg_list):
  	self.lineno = lineno
  	self.expr = expr
  	self.dispatch_type = dispatch_type
  	self.method_name = method_name
  	self.arg_list = arg_list
class self_dispatch:
  def __init__(self, lineno, method_name, arg_list):
    self.lineno = lineno
    self.method_name = method_name
    self.arg_list = arg_list
class if_object:
  def __init__(self, lineno, predicate, then, else_statment):
    self.lineno = lineno
    self.predicate = predicate
    self.then = then
    self.else_statment = else_statment
class while_object:
  def __init__(self, lineno, predicate, body):
    self.lineno = lineno
    self.predicate = predicate
    self.body = body
class block_object:
  def __init__(self, lineno, expression_list):
    self.lineno = lineno
    self.expression_list = expression_list
class new_object:
  def __init__(self, lineno, class_name):
  	self.lineno = lineno
  	self.class_name = class_name
class isvoid_object:
  def __init__(self, lineno, e):
    self.lineno = lineno
    self.e = e
class plus_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
class minus_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
class times_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
class divide_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y  
class lt_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
class le_object:
  def __init__(self, lineno, x, y):
    self.lineno = lineno
    self.x = x
    self.y = y
class eq_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
class not_object:
  def __init__(self, lineno, x):
  	self.lineno = lineno
  	self.x = x
class negate_object:
  def __init__(self, lineno, x):
  	self.lineno = lineno
  	self.x = x
class integer_object:
  def __init__(self, lineno, value):
    self.lineno = lineno
    self.value = value
  def __str__(self):
    return self.lineno + "\ninteger\n" + self.value
class string:
  def __init__(self, lineno, constant):
    self.lineno = lineno
    self.constant = constant
class expr_identifier_object:
  def __init__(self, lineno, var):
    self.lineno = lineno
    self.var = var
class true_object:
  def __init__(self, lineno):
    self.lineno = lineno
class false_object:
  def __init__(self, lineno):
    self.lineno = lineno
class let_binding_no_init_object:
  def __init__(self, lineno, variable, expr_type):
    self.lineno = lineno
    self.variable = variable
    self.expr_type = expr_type
class let_binding_init_object:
  def __init__(self, lineno, variable, expr_type, value):
    self.lineno = lineno
    self.variable = variable
    self.expr_type = expr_type
    self.value = value
class case_object:
  def __init__(self, lineno, case_expression, branch_list):
    self.case_expression = case_expression
    self.branch_list = branch_list
class branch_object:
  def __init__(self, variable, branch_type, expression):
    self.variable = variable
    self.branch_type = branch_type
    self.expression = expression

p = program_object()

def eat():
  global lines
  tmp = lines[0]
  lines = lines[1:]
  return tmp

def parse_program():
  global p
  global lines
  num_classes = int(eat())
  for n in range(0,num_classes):
    p.addClass(parse_class())

def parse_class():
  global lines
  global p
  name = parse_identifier() 
  determines_inherit = eat()
  if determines_inherit == "no_inherits":
    c = no_inherits(name)
    num_features = int(eat())
    for n in range(0,num_features):
      c.addFeature(parse_feature())
  else:
    superclass = parse_identifier()
    c = inherits(name, superclass)
    num_features = int(eat())
    for n in range(0,num_features):
      c.addFeature(parse_feature())
  return c

def parse_identifier():
  global lines
  lineno = eat()
  string = eat()
  i = identifier(lineno, string)
  return i

def parse_feature():
  global lines
  feature_type = eat()
  if feature_type == "attribute_no_init":
    name = parse_identifier()
    attr_type = parse_identifier()
    f = attribute_no_init(name, attr_type)
  elif feature_type == "attribute_init":
    name = parse_identifier()
    attr_type = parse_identifier()
    init = parse_expression()
    f = attribute_init(name, attr_type, init)
  else:
    name = parse_identifier()   
    num_formals = int(eat())
    formal_list = []
    for n in range(0,num_formals):
      formal_list.append(parse_formal())
    return_type = parse_identifier()
    body = parse_expression()
    f = method(name, formal_list, return_type, body)
  return f

def parse_formal():
  global lines
  name = parse_identifier()
  formal_type = parse_identifier()
  f = formal(name, formal_type)
  return f

def get_list_of_expressions():
  global lines
  expression_list = []
  num_args = int(eat())
  for n in range(0, num_args):
    arg_list.append(parse_expression())
  return expression_list 

def parse_branch(): 
  global lines
  variable = parse_identifier()
  branch_type = parse_identifier()
  expr = parse_expression()
  branch = branch_object(variable, branch_type, expr)
  return branch

def parse_expression():
  global lines
  lineno = eat()
  expression_kind = eat()
  if expression_kind == "assign":
    var = parse_identifier()
    rhs = parse_expression()
    expression = assign(lineno, var, rhs)  
  if expression_kind == "dynamic_dispatch":
    e = parse_expression()
    method = parse_identifier()
    arg_list = get_list_of_expressions()
    expression = dynamic_dispatch(lineno, e, method, arg_list)
  if expression_kind == "static_dispatch":
    e = parse_expression()
    dispatch_type = parse_identifier()
    method_name = parse_identifier()
    arg_list = get_list_of_expressions()
    expression = static_dispatch(lineno, e, dispatch_type, method_name, arg_list)
  if expression_kind == "self_dispatch":
    method_name = parse_identifier()
    arg_list = get_list_of_expressions()
    expression = self_dispatch(lineno, method_name, arg_list)
  if expression_kind == "if":
    predicate = parse_expression()
    then = parse_expression()
    else_statement = parse_expression()
    expression = if_object(lineno, predicate, then, else_statement)
  if expression_kind == "while":
    predicate = parse_expression()
    body = parse_expression()
    expression = while_object(lineno, predicate, body)
  if expression_kind == "block":
    expression_list = get_list_of_expressions()
    expression = block_object(lineno, expression_list)
  if expression_kind == "new":
    class_name = parse_identifier()
    expression = new_object(lineno, class_name)
  if expression_kind == "isvoid":
    e = parse_expression()
    expression = isvoid_object(lineno, e)
  if expression_kind == "plus":
    x = parse_expression()
    y = parse_expression()
    expression = plus_object(lineno, x, y)
  if expression_kind == "minus":
    x = parse_expression()
    y = parse_expression()
    expression = minus_object(lineno, x, y)
  if expression_kind == "times":
    x = parse_expression()
    y = parse_expression()
    expression = times_object(lineno, x, y)
  if expression_kind == "divide":
    x = parse_expression()
    y = parse_expression()
    expression = divide_object(lineno, x, y)
  if expression_kind == "lt":
    x = parse_expression()
    y = parse_expression()
    expression = lt_object(lineno, x, y)
  if expression_kind == "le":
    x = parse_expression()
    y = parse_expression()
    expression = le_object(lineno, x, y)
  if expression_kind == "eq":
    x = parse_expression()
    y = parse_expression()
    expression = eq_object(lineno, x, y)
  if expression_kind == "not":
    x = parse_expression()
    expression = not_object(lineno, x)
  if expression_kind == "negate":
    x = parse_expression()
    expression = negate_object(lineno, x)
  if expression_kind == "integer":
    value = eat()
    expression = integer_object(lineno, value)
  if expression_kind == "string":
    constant = eat()
    expression = string_object(lineno, constant)
  if expression_kind == "identifier":
    variable = parse_identifier()
    expression = expr_identifier_object(lineno, variable)
  if expression_kind == "false":
    expression = false_object(lineno)
  if expression_kind == "true":
    expression = true_object(lineno)
  if expression_kind == "let_binding_no_init":
    variable = parse_identifier()
    expr_type = parse_identifier()
    expression = let_binding_no_init_object(lineno, variable, expr_type)
  if expression_kind == "let_binding_init":
    variable = parse_identifier()
    expr_type = parse_identifier()
    val = parse_expression()
    expression = let_binding_init_object(lineno, variable, expr_type, val)
  if expression_kind == "case":
    case_expression = parse_expression()
    num_branches = int(eat())
    branch_list = []
    for n in range(0, num_branches):
      branch_list.append(parse_branch())
    expression = case_object(lineno, case_expression, branch_list)  
  return expression

parse_program()
print p 


#class map, i'll want to print the classes -- alphabetical, and then print the attributes or the methods

#use isinstance
# if isinstance(p, program_object):
#   print "marisa is so kewl"
# else:
#   print "she's ok" 




 







#errors

#typecheck

#print format 





  









