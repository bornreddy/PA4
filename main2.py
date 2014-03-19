import sys, os

lines = []
file_name = sys.argv[1]
new_file = open((os.path.splitext(file_name)[0] + ".cl-mytype"), "w")
try:
 lines = [line.strip() for line in open(sys.argv[1])]
except:
 print "improper file entry"


M = {("Object","abort"):[("Class","Object")], 
    ("Object","type_name"):[("Class","String")],
    ("Object","copy"):[("SELF_TYPE","C")],
    ("IO","out_string"):[("Class","String"),("SELF_TYPE","C")],
    ("IO","out_int"):[("Class","Int"),("SELF_TYPE","C")],
    ("IO","in_string"):[("Class","String")],
    ("IO","in_int"):[("Class","Int")],
    ("String","length"):[("Class","Int")],
    ("String","concat"):[("Class","String"),("Class","String")],
    ("String","substr"):[("Class","Int"),("Class","Int"),("Class","String")]
    }

class inheritance_node:
  def __init__(self, class_name):
    self.class_name = class_name
    self.child_list = []

  def __str__(self):
    child_string = ""
    for c in self.child_list:
      child_string = child_string + "\n" + str(c) 
    return self.class_name + child_string

  def insert(self, inherits_from, class_name):
    if class_name == "Object":
      return True;
    if self.class_name == inherits_from:
      found = False
      for c in self.child_list:
        if c.class_name == class_name:
          found = True
      if not found:
        n = inheritance_node(class_name)
        self.child_list.append(n)
    else:
      for c in self.child_list:
        c.insert(inherits_from,class_name)

  def find(self, class_name):
    if self.class_name == class_name:
      return True
    else:
      found = False
      for c in self.child_list:
        if c.find(class_name):
          found = True
          break
      return found

  def propogate_features(self):
    self.propogate_features_helper([])

  def get_class(self, class_name):
    for c in p.class_list:
      if c.name.string == class_name:
        return c

  def propogate_features_helper(self, ancestor_features):
    self.get_class(self.class_name).all_features.extend(ancestor_features)
    for c in self.child_list:
      c.propogate_features_helper(self.get_class(self.class_name).all_features)
  

Object_tree = inheritance_node("Object")
Object_tree.insert("Object","String")
Object_tree.insert("Object","Int")
Object_tree.insert("Object","Bool")
Object_tree.insert("Object","IO")

def list_to_string(list):
  if len(list) == 0:
    return ""
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
    class_list_string = ""
    for c in self.class_list:
     if (c.name.string != "Object") and (c.name.string != "String") and \
      (c.name.string != "IO") and (c.name.string != "Bool") and (c.name.string != "Int"):
      class_list_string = class_list_string + "\n" + str(c)
    return str(len(self.class_list)) + class_list_string

class no_inherits:
  def __init__(self, name):
    self.name = name
    self.feature_list = []
    self.all_features = []
  def addFeature(self, feature):
    self.feature_list.append(feature)
    self.all_features.append(feature)
  def __str__(self):
    return str(self.name) + "\nno_inherits\n" + str(len(self.feature_list)) \
     + list_to_string(self.feature_list) 

class inherits:
  def __init__(self, name, superclass):
    self.name = name
    self.superclass = superclass
    self.feature_list = []
    self.all_features = []
  def addFeature(self, feature):
    self.feature_list.append(feature)
    self.all_features.append(feature)
  def __str__(self):
    return str(self.name) + "\ninherits\n" + str(self.superclass) + "\n" \
    + str(len(self.feature_list)) + list_to_string(self.feature_list)

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
    return "\nattribute_no_init\n" + str(self.name) + "\n" + \
    str(self.attr_type) 

class attribute_init:
  def __init__(self, name, attr_type, init):
  	self.name = name
  	self.attr_type = attr_type
  	self.init = init
  def __str__(self):
    return "\nattribute_init\n" + str(self.name) + "\n" + str(self.attr_type) \
    + "\n" + str(self.init)

class method:
  def __init__(self, name, formal_list, return_type, body):
    self.name = name
    self.formal_list = formal_list
    self.return_type = return_type
    self.body = body
  def addFormal(self, formal):
  	self.formal_list.append(formal) #########fix in morning, but if formal list isn't 
    #empty this doens't work - i think this can be detected and handled in the list to string method
  def __str__(self):
    return "\nmethod\n" + str(self.name) + "\n" + str(len(self.formal_list)) \
    + list_to_string(self.formal_list) + "\n" + str(self.return_type) + "\n" \
    + str(self.body)

class formal: 
  def __init__(self, name, formal_type):
    self.name = name
    self.formal_type = formal_type
  def __str__(self):
    return str(self.name) + "\n" + str(self.formal_type)

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
  def __str__(self):
    return self.lineno + "\ndynamic_dispatch\n" + \
    str(self.expr) + "\n" + str(self.method_name) + "\n" + \
    str(len(self.arg_list)) + list_to_string(self.arg_list)
  
class static_dispatch:
  def __init__(self, lineno, expr, dispatch_type, method_name, arg_list):
  	self.lineno = lineno
  	self.expr = expr
  	self.dispatch_type = dispatch_type
  	self.method_name = method_name
  	self.arg_list = arg_list
  def __str__(self):
    return self.lineno + "\nstatic_dispatch\n" + str(self.expr) + "\n" + \
    str(self.dispatch_type) + "\n" + str(self.method_name) + "\n" + \
    str(len(self.arg_list)) + list_to_string(self.arg_list)

class self_dispatch:
  def __init__(self, lineno, method_name, arg_list):
    self.lineno = lineno
    self.method_name = method_name
    self.arg_list = arg_list
  def __str__(self):
    return self.lineno + "\nself_dispatch\n" + str(self.method_name) + "\n" + \
    str(len(self.arg_list)) +  list_to_string(self.arg_list)

class if_object:
  def __init__(self, lineno, predicate, then, else_statement):
    self.lineno = lineno
    self.predicate = predicate
    self.then = then
    self.else_statement = else_statement
  def __str__(self):
    return self.lineno + "\nif\n" + str(self.predicate) + "\n" + str(self.then) \
    + "\n" + str(self.else_statement)

class while_object:
  def __init__(self, lineno, predicate, body):
    self.lineno = lineno
    self.predicate = predicate
    self.body = body
  def __str__(self):
    return self.lineno + "\nwhile\n" + str(self.predicate) + "\n" + str(self.body)

class block_object:
  def __init__(self, lineno, expression_list):
    self.lineno = lineno
    self.expression_list = expression_list
  def __str__(self):
    return self.lineno + "\nblock\n" + str(len(self.expression_list)) + "\n" + \
    list_to_string(self.expression_list)

class new_object:
  def __init__(self, lineno, class_name):
  	self.lineno = lineno
  	self.class_name = class_name
  def __str__(self):
    return self.lineno + "\nnew\n" + str(self.class_name)

class isvoid_object:
  def __init__(self, lineno, e):
    self.lineno = lineno
    self.e = e
  def __str__(self):
    return self.lineno + "\nisvoid\n" + str(self.e)

class plus_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
  def __str__(self):
    return self.lineno + "\nplus\n" + str(self.x) + "\n" + str(self.y)

class minus_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
  def __str__(self):
    return self.lineno + "\nminus\n" + str(self.x) + "\n" + str(self.y)

class times_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
  def __str__(self):
    return self.lineno + "\ntimes\n" + str(self.x) + "\n" + str(self.y)

class divide_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
  def __str__(self):
    return self.lineno + "\ndivide\n" + str(self.x) + "\n" + str(self.y)

class lt_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
  def __str__(self):
    return self.lineno + "\nlt\n" + str(self.x) + "\n" + str(self.y)

class le_object:
  def __init__(self, lineno, x, y):
    self.lineno = lineno
    self.x = x
    self.y = y
  def __str__(self):
    return self.lineno + "\nle\n" + str(self.x) + "\n" + str(self.y)

class eq_object:
  def __init__(self, lineno, x, y):
  	self.lineno = lineno
  	self.x = x
  	self.y = y
  def __str__(self):
    return self.lineno + "\neq\n" + str(self.x) + "\n" + str(self.y)

class not_object:
  def __init__(self, lineno, x):
  	self.lineno = lineno
  	self.x = x
  def __str__(self):
    return self.lineno + "\nnot\n" + str(self.x)

class negate_object:
  def __init__(self, lineno, x):
  	self.lineno = lineno
  	self.x = x
  def __str__(self):
    return self.lineno + "\nnegate\n" + str(self.x)

class integer_object:
  def __init__(self, lineno, value):
    self.lineno = lineno
    self.value = value
  def __str__(self):
    return self.lineno + "\ninteger\n" + self.value

class string_object:
  def __init__(self, lineno, constant):
    self.lineno = lineno
    self.constant = constant
  def __str__(self):
    return self.lineno + "\nstring\n" + self.constant

class expr_identifier_object:
  def __init__(self, lineno, var):
    self.lineno = lineno
    self.var = var
  def __str__(self):
    return self.lineno + "\nidentifier\n" + str(self.var)

class true_object:
  def __init__(self, lineno):
    self.lineno = lineno
  def __str__(self):
    return self.lineno + "\ntrue\n" ###################fix printing issues ---
    # extra spaces when these are in blocks 

class false_object:
  def __init__(self, lineno):
    self.lineno = lineno
  def __str__(self):
    return self.lineno + "\nfalse\n"

class let_binding_no_init_object:
  def __init__(self, lineno, variable, expr_type):
    self.lineno = lineno
    self.variable = variable
    self.expr_type = expr_type
  def __str__(self):
    return self.lineno + "\nlet_binding_no_init\n" + str(self.variable) \
    + "\n" + str(self.expr_type)

class let_binding_init_object:
  def __init__(self, lineno, variable, expr_type, value):
    self.lineno = lineno
    self.variable = variable
    self.expr_type = expr_type
    self.value = value
  def __str__(self):
    return self.lineno + "\nlet_binding_init\n" + str(self.variable) + "\n" + \
    str(self.expr_type) + "\n" + str(self.value)


class case_object:
  def __init__(self, lineno, case_expression, branch_list):
    self.lineno = self.lineno
    self.case_expression = case_expression
    self.branch_list = branch_list
  def __str__(self):
    return self.lineno + "\ncase\n" + str(self.case_expression) + "\n" + str(len(self.branch_list)) \
    + list_to_string(self.branch_list)

class branch_object:
  def __init__(self, variable, branch_type, expression):
    self.variable = variable
    self.branch_type = branch_type
    self.expression = expression
  def __str__(self):
    return str(self.variable) + "\n" + str(self.branch_type) + "\n" + str(self.expression)

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
      f = parse_feature()
      c.addFeature(f)
      if isinstance(f,method):
        tup = (c.name.string,f.name.string)
        type_list = []
        for form in f.formal_list:
          if f.formal_type.string == "SELF_TYPE":
            type_list.append(("SELF_TYPE","C"))
          else:
           type_list.append("Class",f.formal_type.string)
        if f.return_type.string == "SELF_TYPE":
          type_list.append(("SELF_TYPE","C"))
        else:
          type_list.append(("Class",f.return_type.string))
        M[tup] = type_list
        #add this method to M
  else:
    superclass = parse_identifier()
    c = inherits(name, superclass)
    num_features = int(eat())
    for n in range(0,num_features):
      f = parse_feature()
      c.addFeature(f)
      if isinstance(f,method):
        tup = (c.name.string,f.name.string)
        type_list = []
        for form in f.formal_list:
          if f.formal_type.string == "SELF_TYPE":
            type_list.append(("SELF_TYPE","C"))
          else:
           type_list.append("Class",f.formal_type.string)
        if f.return_type.string == "SELF_TYPE":
          type_list.append(("SELF_TYPE","C"))
        else:
          type_list.append(("Class",f.return_type.string))
        M[tup] = type_list
        #add this Method to M
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
    expression_list.append(parse_expression())
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

object_identifier = identifier(0,"Object")
object_class = no_inherits(object_identifier)
object_feature_1_identifier = (0,"abort")
object_feature_1_formal_list = []
object_feature_1_return_type = (0,"Object")
object_feature_1_body = ("body")
object_m1 = method(object_feature_1_identifier, object_feature_1_formal_list, 
            object_feature_1_return_type, object_feature_1_body)
object_feature_2_identifier = (0,"type_name")
object_feature_2_formal_list = []
object_feature_2_return_type = (0,"String")
object_feature_2_body = ("body")
object_m2 = method(object_feature_2_identifier, object_feature_2_formal_list, 
            object_feature_2_return_type, object_feature_2_body)
object_feature_3_identifier = (0,"copy")
object_feature_3_formal_list = []
object_feature_3_return_type = (0,"SELF_TYPE")
object_feature_3_body = ("body")
object_m3 = method(object_feature_3_identifier, object_feature_3_formal_list, 
            object_feature_3_return_type, object_feature_3_body)
object_class.addFeature(object_m1)
object_class.addFeature(object_m2)
object_class.addFeature(object_m3)
p.class_list.append(object_class)

IO_identifier = identifier(0,"IO")
IO_class = inherits(IO_identifier, object_identifier)
IO_feature_1_identifier = identifier(0,"out_string")
IO_formal_name_1 = identifier(0,"x")
IO_formal_type_1 = identifier(0,"String")
IO_feature_1_formal = formal(IO_formal_name_1, IO_formal_type_1)
IO_feature_1_formal_list = [IO_feature_1_formal]
IO_feature_1_return_type = identifier(0,"SELF_TYPE")
IO_feature_1_body = ("body")
IO_m1 = method(IO_feature_1_identifier, IO_feature_1_formal_list,
        IO_feature_1_return_type, IO_feature_1_body)
IO_feature_2_identifier = identifier(0,"out_int")
IO_formal_name_2 = identifier(0,"x")
IO_formal_type_2 = identifier(0,"Int")
IO_feature_2_formal = formal(IO_formal_name_2, IO_formal_type_2)
IO_feature_2_formal_list = [IO_feature_2_formal]
IO_feature_2_return_type = identifier(0,"SELF_TYPE")
IO_feature_2_body = ("body")
IO_m2 = method(IO_feature_2_identifier, IO_feature_2_formal_list,
        IO_feature_2_return_type, IO_feature_2_body)
IO_feature_3_identifier = identifier(0,"in_string")
IO_feature_3_formal_list = []
IO_feature_3_return_type = identifier(0,"String")
IO_feature_3_body = ("body")
IO_m3 = method(IO_feature_3_identifier, IO_feature_3_formal_list,
        IO_feature_3_return_type, IO_feature_3_body)
IO_feature_4_identifier = identifier(0,"in_int")
IO_feature_4_formal_list = []
IO_feature_4_return_type = identifier(0,"Int")
IO_feature_4_body = ("body")
IO_m4 = method(IO_feature_4_identifier, IO_feature_4_formal_list,
        IO_feature_4_return_type, IO_feature_4_body)
IO_class.addFeature(IO_m1)
IO_class.addFeature(IO_m2)
IO_class.addFeature(IO_m3)
IO_class.addFeature(IO_m4)
p.class_list.append(IO_class)

Bool_identifier = identifier(0,"Bool")
Bool_class = inherits(Bool_identifier, object_identifier)
p.class_list.append(Bool_class)

Int_identifier = identifier(0,"Int")
Int_class = inherits(Int_identifier, object_identifier)
p.class_list.append(Int_class)

String_identifier = identifier(0,"String")
String_class = inherits(String_identifier, object_identifier)
String_feature_1_identifier = identifier(0,"length")
String_feature_1_formal_list = []
String_feature_1_return_type = identifier(0,"Int")
String_feature_1_body = ("body")
String_m1 = method(String_feature_1_identifier, String_feature_1_formal_list,
            String_feature_1_return_type, String_feature_1_body)
String_feature_2_identifier = identifier(0,"concat")
String_feature_2_formal_name = identifier(0,"s")
String_feature_2_formal_type = identifier(0,"String")
String_feature_2_formal = formal(String_feature_2_formal_name, String_feature_2_formal_type)
String_feature_2_formal_list = [String_feature_2_formal]
String_feature_2_return_type = identifier(0,"String")
String_feature_2_body = ("body")
String_m2 = method(String_feature_2_identifier, String_feature_2_formal_list,
            String_feature_2_return_type, String_feature_2_body)

String_feature_3_identifier = identifier(0,"concat")
String_feature_3_formal_name1 = identifier(0,"i")
String_feature_3_formal_type1 = identifier(0,"Int")
String_feature_3_formal1 = formal(String_feature_3_formal_name1, String_feature_3_formal_type1)
String_feature_3_formal_name2 = identifier(0,"l")
String_feature_3_formal_type2 = identifier(0,"Int")
String_feature_3_formal2 = formal(String_feature_3_formal_name2, String_feature_3_formal_type2)
String_feature_3_formal_list = [String_feature_3_formal1, String_feature_3_formal2]
String_feature_3_return_type = identifier(0,"String")
String_feature_3_body = ("body")
String_m3 = method(String_feature_3_identifier, String_feature_3_formal_list,
            String_feature_3_return_type, String_feature_3_body)


Bool_identifier = identifier(0,"Bool")
Bool_class = inherits(Bool_identifier, object_identifier)



for n in range(0,len(p.class_list)):
  for c in p.class_list:
    if isinstance(c, no_inherits):
      Object_tree.insert("Object",c.name.string)
    else:
      Object_tree.insert(c.superclass.string, c.name.string)

# print Object_tree

for c in p.class_list:
  if not Object_tree.find(c.name.string):
    print "ERROR: "+ c.name.lineno +": Type-Check:bad inheritance"
    sys.exit()


# print p 



# print "class_map"
# for c in p.class_list:
#   print c.
















#errors



#print format 


#class map, i'll want to print the classes -- alphabetical, and then print the attributes or the methods

#use isinstance
# if isinstance(p, program_object):
#   print "marisa is so kewl"
# else:
#   print "she's ok" 






  









