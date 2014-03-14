import sys, os

class_list = []
class_names = []

def addClass(class_list,c):
  if c.identifier not in class_names:
    class_list.append(c)
    class_names.append(c.identifier)
  else:
    print "ERROR: " + c.line_no + ": Type-Check: redefined Class"
    os.remove(class_file)
    sys.exit()

def isingle(item):
	yield item

class program_object:
  def __init__(self, num_classes):
    self.num_classes = num_classes
  def __str__(self):
    return self.num_classes  + "\n"

class class_object:
  def __init__(self, line_no, identifier, inherits):
    self.line_no = line_no
    self.identifier = identifier
    self.inherits = inherits 
    self.inherit_line = -1
    self.numFeatures = 0
    self.attribute_list = []
    self.method_list = []
  def setInheritLine(self,inherit_line):
  	self.inherit_line = inherit_line
  def setNumFeatures(self, numFeatures):
  	self.numFeatures = numFeatures
  def addAttribute(self, attribute):
  	self.attribute_list.append(attribute)
  def addMethod(self, method):
  	self.method_list.append(method)
  def __str__(self):
    if (self.inherit_line == -1):
      return str(self.line_no) + "\n" + self.identifier + "\nno_inherits\n" + str(self.numFeatures) + "\n"
    else:
      return str(self.line_no) + "\n" + self.identifier + "\ninherits\n" + str(self.inherit_line) + "\n" + self.inherits + "\n" + str(self.numFeatures) + "\n"
   
class attribute_object:
  def __init__(self, kind, line_no_identifier, identifier, line_no_return_type, return_type):   
  	self.kind = kind
  	self.line_no_identifier = line_no_identifier
  	self.identifier = identifier
  	self.line_no_return_type = line_no_return_type
  	self.return_type = return_type
  def addExpression(self,expression):
  	self.expression = expression
  def __str__(self):
  	if self.kind == "attribute_no_init":
  	  return self.kind + "\n" + self.line_no_identifier + "\n" + self.identifier + "\n" + self.line_no_return_type + "\n" + self.return_type + "\n"
  	elif self.kind == "attribute_init":
  	  return self.kind + "\n" + self.line_no_identifier + "\n" + self.identifier + "\n" + self.line_no_return_type + "\n" + self.return_type + "\n"
  	else:
  	  "something went wrong - assignment_object entered for wrong type of node"

class method_object:
  def __init__(self, kind, line_no_identifier, identifier, numFormals):
    self.kind = kind
    self.line_no_identifier = line_no_identifier
    self.identifier = identifier
    self.numFormals = numFormals
  def update(self, line_no_return_type, return_type):
  	self.line_no_return_type = line_no_return_type
  	self.return_type = return_type 
  def __str__(self):
  	return (self.kind + "\n" + self.line_no_identifier + "\n" + self.identifier + "\n" + self.numFormals
  		+ "\n" + self.line_no_return_type + "\n" + self.return_type  + "\n")

class formal_object:
  def __init__(self, line_no_identifier, identifier, line_no_type, formal_type):
    self.line_no_identifier = line_no_identifier
    self.identifier = identifier
    self.line_no_type = line_no_type
    self.formal_type = formal_type
  def __str__(self):
  	return self.line_no_identifier + "\n" + self.identifier + "\n" + self.line_no_type + "\n" + self.formal_type  + "\n"

class false_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  def __str__(self):
  	return self.line_no + "\nfalse\n"

class true_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  def __str__(self):
  	return self.line_no + "\ntrue\n"

class string_object:
  def __init__(self,line_no, string_value):
  	self.line_no = line_no
  	self.string_value = string_value
  def __str__(self):
  	return self.line_no + "\nstring\n" + self.string_value + "\n"

class integer_object:
  def __init__(self,line_no, integer_value):
  	self.line_no = line_no
  	self.integer_value = integer_value
  def __str__(self):
  	return self.line_no + "\ninteger\n" + self.integer_value  + "\n"

class identifier_object:
  def __init__(self, line_no, line_no_name, name):
  	self.line_no = line_no
  	self.line_no_name = line_no_name
  	self.name = name
  def __str__(self):
    return self.line_no + "\nidentifier\n" + self.line_no_name + "\n" + self.name  + "\n"

class not_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\nnot\n" + out_string

class eq_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\neq\n" + out_string

class le_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\nle\n" + out_string


class lt_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\nlt\n" + out_string

class negate_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\nnegate\n" + out_string

class divide_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\divide\n" + out_string

class times_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\ntimes\n" + out_string

class minus_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\nminus\n" + out_string

class plus_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\nplus\n" + out_string

class isvoid_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	out_string = ""
  	for e in self.expression_list:
  	  out_string = out_string + str(e)
  	# if out_string != "":
  	#   out_string  = out_string + "\n"
  	return self.line_no + "\nisvoid\n" + out_string 

class new_object:
  def __init__(self, line_no, line_no_type, new_type):
  	self.line_no = line_no
  	self.line_no_type = line_no_type
  	self.new_type = new_type
  def __str__(self):
  	return self.line_no + "\nnew\n" + self.line_no_type + "\n" + self.new_type  + "\n"

class case_object:
  def __init__(self, line_no, case_expression, numCases):
  	self.line_no = line_no
  	self.case_expression = case_expression
  	self.numCases = numCases
  	self.incase_list = []
  def addCase(self, formal, expression):
    c = incase_object(formal,expression)
    self.incase_list.append(c)
  def __str__(self):
  	caseString = ""
  	for c in self.incase_list:
  	  caseString = caseString + str(c)
  	return self.line_no + "\ncase\n" +  str(self.case_expression) + self.numCases  + "\n" + caseString #the line number was printed out ahead of time, the number of cases and the line are sept printings

class incase_object:
  def __init__(self,formal,expression):
  	self.formal = formal
  	self.expression = expression
  def __str__(self):
  	return str(self.formal) + str(self.expression)

##come back to let so we can do multiple bindings
class let_object:
  def __init__(self, line_no, numBindings):
    self.line_no = line_no
    self.numBindings = numBindings
    self.binding_list = []
    self.expression_list = []
  def addBindingObject(self, bindingObject):
    self.binding_list.append(bindingObject)
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	bindingString = ""
  	expressionString = ""
  	for b in self.binding_list:
  	  bindingString = bindingString + str(b)
  	for e in self.expression_list:
  	  expressionString = expressionString + str(e)
  	return self.line_no + "\nlet\n" + self.numBindings + "\n" + bindingString + expressionString

class binding_init_object:
  def __init__(self):
  	self.expression_list = []
  	self.formal_list = []
  def addFormal(self, formal):
  	self.formal_list.append(formal)
  def addExpression(self,expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	formalString = ""
  	for n in self.formal_list:
  	  formalString = formalString + str(n)
  	formalString = formalString
  	expressionString = ""
  	for e in self.expression_list:
  	  expressionString = expressionString + str(e)
  	return "let_binding_init\n" + formalString + expressionString

class binding_no_init_object:
  def __init__(self):
  	self.expression_list = []
  	self.formal_list = []
  def addFormal(self, formal):
  	self.formal_list.append(formal)
  def __str__(self):
  	formalString = ""
  	for n in self.formal_list:
  	  formalString = formalString + str(n)
  	formalString = formalString
  	expressionString = ""
  	for e in self.expression_list:
  	  expressionString = expressionString + str(e)
  	return "let_binding_no_init\n" + formalString + expressionString

class block_object:
  def __init__(self, line_no, numExpressions):
  	self.line_no = line_no
  	self.numExpressions = numExpressions
  	self.expression_list = []
  def addExpression(self, expression):
    self.expression_list.append(expression)
  def __str__(self):
  	expressionString = ""
  	for e in self.expression_list:
  	  expressionString = expressionString + str(e)
  	return self.line_no + "\nblock\n" + self.numExpressions + "\n" + expressionString

class while_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	expressionString = ""
  	for e in self.expression_list:
  	  expressionString = expressionString + str(e)
  	return self.line_no + "\nwhile\n" + expressionString

class if_object:
  def __init__(self, line_no):
  	self.line_no = line_no
  	self.expression_list = []
  def addExpression(self, expression):
  	self.expression_list.append(expression)
  def __str__(self):
  	expressionString = ""
  	for e in self.expression_list:
  	  expressionString = expressionString + str(e)
  	return self.line_no + "\nif\n" + expressionString

class self_dispatch_object:
  def __init__(self, expression_line_no, expression_value, line_no_dispatch, dispatch_identifier, numExpressions):
    self.expression_line_no = expression_line_no
    self.expression_value = expression_value
    self.line_no_dispatch = line_no_dispatch
    self.dispatch_identifier = dispatch_identifier
    self.numExpressions = numExpressions
    self.expression_list = []
  def addExpression(self,expression):
    self.expression_list.append(expression)
  def __str__(self):
    expressionString = ""
    for e in self.expression_list:
      expressionString = expressionString + str(e)
    return self.expression_line_no + "\n" + self.expression_value + "\n" + self.line_no_dispatch + "\n" + self.dispatch_identifier + "\n" + self.numExpressions + "\n" + expressionString

class dynamic_dispatch_object:
  def __init__(self, expression_line_no, expression_value, line_no_identifier, identifier, numArgs):
    self.expression_line_no = expression_line_no
    self.expression_value = expression_value
    self.dispatch_expression = None
    self.line_no_identifier = line_no_identifier
    self.identifier = identifier
    self.numArgs = numArgs
    self.expression_list = []
  def addDispatchExpression(self,dispatch_expression):
    self.dispatch_expression = dispatch_expression
  def addExpression(self,expression):
    self.expression_list.append(expression)
  def __str__(self):
    dispatch_expressionString = ""
    if self.dispatch_expression != None:
      dispatch_expressionString = str(self.dispatch_expression)
    expressionString = ""
    for e in self.expression_list:
      expressionString = expressionString + str(e)
    return self.expression_line_no + "\n" + self.expression_value + "\n" + dispatch_expressionString + self.line_no_identifier + "\n" + self.identifier + "\n" + self.numArgs  + "\n" + expressionString

class static_dispatch_object:
  def __init__(self, expression_line_no, expression_value, line_no_parent_type, parent_type, line_no_identifier, identifier, numArgs):
    self.expression_line_no = expression_line_no
    self.expression_value = expression_value
    self.dispatch_expression = None
    self.line_no_parent_type = line_no_parent_type
    self.parent_type = parent_type
    self.line_no_identifier = line_no_identifier
    self.identifier = identifier
    self.numArgs = numArgs
    self.expression_list = []
  def addDispatchExpression(self,dispatch_expression):
    self.dispatch_expression = dispatch_expression
  def addExpression(self,expression):
    self.expression_list.append(expression)
  def __str__(self):
    dispatch_expressionString = ""
    if self.dispatch_expression != None:
      dispatch_expressionString = str(self.dispatch_expression)
    expressionString = ""
    for e in self.expression_list:
      expressionString = expressionString + str(e)
    return self.expression_line_no + "\n" + self.expression_value + "\n" + dispatch_expressionString + self.line_no_parent_type + "\n" + self.parent_type + "\n" + self.line_no_identifier + "\n" + self.identifier + "\n" + self.numArgs  + "\n" + expressionString

class assign_object:
  def __init__(self, expression_line_no, expression_value, line_no_identifier, identifier):
    self.expression_line_no = expression_line_no
    self.expression_value = expression_value
    self.line_no_identifier = line_no_identifier
    self.identifier = identifier
    self.expression_list = []
  def addExpression(self,expression):
    self.expression_list.append(expression)
  def __str__(self):
    expressionString = ""
    for e in self.expression_list:
      expressionString = expressionString + str(e)
    return self.expression_line_no + "\n" + self.expression_value + "\n" + self.line_no_identifier + "\n" + self.identifier  + "\n" + expressionString

# lines = [line.strip() for line in open(sys.argv[1])]
file_name = sys.argv[1]
new_file = os.path.splitext(file_name)[0]
class_file = new_file + ".cl-type"
type_file = open(class_file, "w")
descent_file = new_file + ".cl-descent"
ast_file = open(descent_file,"w")

try:
 lines = [line.strip() for line in open(sys.argv[1])]
except:
 print "improper file entry"


 #open up my file


def eat():
  global lines
  tmp = lines[0]
  lines = lines[1:]
  return tmp

def parse_program():
  global lines
  p = program_object(lines[0])
  num_classes = eat()
  type_num = int(num_classes) + 5
  type_file.write("class_map\n")
  type_file.write(str(type_num) + "\n")
  ast_file.write(str(p))
  for n in range(0,int(num_classes)):
    parse_class()

def parse_class():
  global lines
  global p
  line_no = eat()
  identifier = eat()
  if lines[0] == "no_inherits":
  	inherits = None 
  	lines = lines[1:]
  else:
  	inherit_line = lines[1]
  	inherits = lines[2]
  	lines = lines[3:]
  c = class_object(line_no, identifier, inherits)
  if inherits != None:
  	c.setInheritLine(inherit_line) 
  num_features = eat()
  c.setNumFeatures(num_features)
  ast_file.write(str(c))
  for n in range(0,int(num_features)):
  	feature_index = n
  	c = parse_feature(c)
  addClass(class_list,c)

def parse_feature(cc):
  global lines
  kind = eat()
  line_no_identifier = eat()
  identifier = eat()
  current_attributes = []
  current_methods = []
  for m in cc.method_list:
      current_methods.append(m.identifier)
  for m in cc.attribute_list:
      current_attributes.append(m.identifier)
  if kind == "attribute_no_init":
    line_no_return_type = eat()
    return_type = eat()
    f = attribute_object(kind, line_no_identifier, identifier, line_no_return_type, return_type)
    if f.identifier in current_attributes:
      print "ERROR: " + f.line_no_identifier + ": Type-Check: redefined attribute name"
      os.remove(class_file)
      sys.exit()
    cc.addAttribute(f)
    ast_file.write(str(f)) 
  elif kind == "attribute_init":
    line_no_return_type = eat()
    return_type = eat()
    f = attribute_object(kind, line_no_identifier, identifier, line_no_return_type, return_type)
    ast_file.write(str(f))
    expression = parse_expression()
    f.addExpression(expression)
    if f.identifier in current_attributes:
      print "ERROR: " + f.line_no_identifier + ": Type-Check: redefined attribute name"
      os.remove(class_file)
      sys.exit()
    cc.addAttribute(f)
  else:
    numFormals = eat() 
    m = method_object(kind, line_no_identifier, identifier, numFormals)
    if m.identifier in current_methods:
      print "ERROR: " + m.line_no_identifier + ": Type-Check: redefined method name"
      os.remove(class_file)
      sys.exit()
    line_no_return_type = eat()
    return_type = eat()
    m.update(line_no_return_type, return_type)
    cc.addMethod(m)
    ast_file.write(str(m))
    if (numFormals != "0"):
  	  for n in range(0, int(numFormals)):
  	    parse_formal()
    parse_expression()
  return cc
  	
  	
def parse_formal():
  line_no_identifier = eat()
  identifier = eat()
  line_no_type = eat()
  formal_type = eat()
  f = formal_object(line_no_identifier, identifier, line_no_type, formal_type)  
  ast_file.write(str(f))
  return f 	

def parse_binding():
  binding_type = eat()
  if binding_type == "let_binding_init":
  	f = binding_init_object()
  	ast_file.write("let_binding_init\n")
  	fr= parse_formal()
  	f.addFormal(fr)
  	ex = parse_expression()
  	f.addExpression(ex)
  	return f  
  elif binding_type == "let_binding_no_init\n":
  	f = binding_no_init_object()
  	ast_file.write(str(f))
  	fr = parse_formal()
  	f.addFormal(fr)
  	return f 
  else:
  	print "something went very wrong"

def parse_expression():
  f = 0
  expression_line_no = eat()
  expression_value = eat()
  if expression_value == "false":
    f = false_object(expression_line_no)
    ast_file.write(str(f))
  if expression_value == "true":
   f = true_object(expression_line_no)
   ast_file.write(str(f))
   # return f
  if expression_value == "string":
  	string_value = eat()
  	f = string_object(expression_line_no, string_value)
  	ast_file.write(str(f))
  	# return f
  if expression_value == "integer":
  	integer_value = eat()
  	f = integer_object(expression_line_no, integer_value)
  	ast_file.write(str(f))
  	# return f
  if expression_value == "identifier":
  	line_no_name = eat()
  	name = eat()
  	f = identifier_object(expression_line_no, line_no_name, name)
  	ast_file.write(str(f))
  	# return f
  if expression_value == "not":
  	f = not_object(expression_line_no)
  	ast_file.write(str(f))
  	f.addExpression(parse_expression()) 
  	# return f
  if expression_value == "eq":
  	f = eq_object(expression_line_no)
  	ast_file.write(str(f))
  	for n in range(0,2):
  	  f.addExpression(parse_expression())
  	# return f
  if expression_value == "le":	 									
  	f = le_object(expression_line_no)
  	ast_file.write(str(f))
  	for n in range(0,2):
  	  f.addExpression(parse_expression())
  	# return f
  if expression_value == "lt":	 									
  	f = lt_object(expression_line_no)
  	ast_file.write(str(f))
  	for n in range(0,2):
  	  f.addExpression(parse_expression())
  	# return f
  if expression_value == "negate":	 									
  	f = negate_object(expression_line_no)
  	ast_file.write(str(f))
  	f.addExpression(parse_expression())
  	# return f
  if expression_value == "divide":	 									
  	f = divide_object(expression_line_no)
  	ast_file.write(str(f))
  	for n in range(0,2):
  	  f.addExpression(parse_expression())
  	# return f
  if expression_value == "times":	 									
  	f = times_object(expression_line_no)
  	ast_file.write(str(f)) 
  	for n in range(0,2):
  	  f.addExpression(parse_expression())
  	# return f
  if expression_value == "minus":	 									
  	f = minus_object(expression_line_no)
  	ast_file.write(str(f))
  	for n in range(0,2):
  	  f.addExpression(parse_expression())
  	# return f
  if expression_value == "plus":	 									
  	f = plus_object(expression_line_no)
  	ast_file.write(str(f))
  	for n in range(0,2):
  	  f.addExpression(parse_expression())
  if expression_value == "isvoid":	 									
  	f = isvoid_object(expression_line_no)
  	ast_file.write(str(f))
  	f.addExpression(parse_expression())
  	# return f
  if expression_value == "new":
  	line_no_type = eat()
  	new_type = eat()
  	f = new_object(expression_line_no, line_no_type, new_type)
  	ast_file.write(str(f))
  	# return f
  if expression_value == "case":
    case_expression = parse_expression()
    numCases = eat()
    
    f = case_object(expression_line_no, case_expression, numCases)
    ast_file.write(str(f)) #######################messing up the write up in the ast. fix this later on.
    for n in range(0,int(numCases)):
      fr = parse_formal()
      ex = parse_expression()
      f.addCase(fr,ex)
  if expression_value == "let":
  	numBindings = eat()
  	f = let_object(expression_line_no, numBindings)
  	ast_file.write(str(f))
  	for n in range(0,int(numBindings)):
  	  f.addBindingObject(parse_binding())
  	f.addExpression(parse_expression())
  	# return f
  	# return f
  if expression_value == "block":
  	numExpressions = eat()
  	f = block_object(expression_line_no, numExpressions)
  	ast_file.write(str(f))
  	for n in range(0,int(numExpressions)):
  	  f.addExpression(parse_expression())
  	# return f
  if expression_value == "while":	 									
  	f = while_object(expression_line_no)
  	ast_file.write(str(f))
  	for n in range(0,2):
  	  f.addExpression(parse_expression())
  	# return f
  if expression_value == "if":
    f = if_object(expression_line_no)
    ast_file.write(str(f))
    for n in range(0,3):
      f.addExpression(parse_expression())
    # return f
  if expression_value == "self_dispatch":
    line_no_dispatch = eat()
    dispatch_identifier = eat()
    numExpressions = eat()
    f = self_dispatch_object(expression_line_no, expression_value, line_no_dispatch, dispatch_identifier, numExpressions)
    ast_file.write(str(f))
    for n in range(0, int(numExpressions)):
  	  f.addExpression(parse_expression())
  if expression_value == "dynamic_dispatch":

    ########## this prints out at a bad place -- fix printing entirely later on 
    dispatch_expression = parse_expression()
    line_no_identifier = eat()
    identifier = eat()
    numArgs = eat()
    f = dynamic_dispatch_object(expression_line_no, expression_value, line_no_identifier, identifier, numArgs)
    ast_file.write(str(f))
    f.addDispatchExpression(dispatch_expression)
    
    for n in range(0, int(numArgs)):
      f.addExpression(parse_expression())
    # return f
  if expression_value == "static_dispatch":
    dispatch_expression = parse_expression()
    line_no_parent_type = eat()
    parent_type = eat()
    line_no_identifier = eat()
    identifier = eat()
    numArgs = eat()
    f = static_dispatch_object(expression_line_no, expression_value, line_no_parent_type, parent_type, line_no_identifier, identifier, numArgs)
    ast_file.write(str(f))
    f.addDispatchExpression(dispatch_expression)
    for n in range(0,int(numArgs)):
  	  f.addExpression(parse_expression())
  	# return f
  if expression_value == "assign":
  	line_no_identifier = eat()
  	identifier = eat()
  	f = assign_object(expression_line_no, expression_value, line_no_identifier, identifier)
  	ast_file.write(str(f))
  	f.addExpression(parse_expression())
  	# return f
  return f 

#add bool, int, string, io, and object into classMap
c = class_object(0,"Object",None)
addClass(class_list,c)
c = class_object(0,"Int","Object")
addClass(class_list,c)
c = class_object(0,"String","Object")
addClass(class_list,c)
c = class_object(0,"IO","Object")
addClass(class_list,c)
c = class_object(0,"Bool","Object")
addClass(class_list,c)

# class check here - topological sort a graph---store what the class node and what it inherits. then update the attributes
# of the class node based on the toposort
	# parent map here --just for kicks, print it out 

parse_program()

# PYTHON: topological sort of a list of tasks
# read in standard input to "class_lines" list



  
# if len(class_names)!=len(set(class_names)):
#   print "ERROR: " + c.line_no + ": Type-Check: inherits from Int"
#   os.remove(class_file)
#   sys.exit()

class_lines = []

class_names.append(None)

for c in class_list:
  if c.identifier != "Object":
    class_lines.append(c.identifier)
    if c.inherits == None:
      class_lines.append("Object")
    if c.inherits == "Int":
      print "ERROR: " + c.line_no + ": Type-Check: inherits from Int"
      os.remove(class_file)
      sys.exit() 
    if c.inherits == "String":
      print "ERROR: " + c.line_no + ": Type-Check: inherits from String"
      os.remove(class_file)
      sys.exit() 
    if c.inherits == "Bool":
      print "ERROR: " + c.line_no + ": Type-Check: inherits from Bool"
      os.remove(class_file)
      sys.exit() 
    if c.inherits == "SELF_TYPE":
      print "ERROR: " + c.line_no + ": Type-Check: inherits from SELF_TYPE"
      os.remove(class_file)
      sys.exit() 
    if c.inherits not in class_names:
      print "ERROR: " + c.line_no + ": Type-Check: inherits from unknown"
      os.remove(class_file)
      sys.exit()
    else:
      class_lines.append(c.inherits)

if "Main" not in class_names:
  print "ERROR: 0: Type-Check: no Main"
  os.remove(class_file)
  sys.exit()

# print class_lines

task_dict = dict()
degree_dict = dict()
i = 0
while i < len(class_lines) - 1 : 
    #put class_lines into dictionary with task and indegree
    #if the parent(i+1) has not been encountered before, then add it's child (i) to its adjacency list
    if not class_lines[i+1] in task_dict: 
        task_dict[ class_lines[i+1] ] = []
        task_dict[ class_lines[i+1] ].append(class_lines[i]) 
        #update the indegree of the parent to one more
        degree_dict.setdefault(class_lines[i],0)
        degree_dict[class_lines[i]] = degree_dict[class_lines[i]] + 1
   #if the task has been encountered before, check to make sure the child is not a repeat
    else:
        if task_dict[ class_lines[i+1] ].count(class_lines[i]) == 0: 
            task_dict[ class_lines[i+1] ].append(class_lines[i])
            #update indegree of parent
            degree_dict.setdefault(class_lines[i],0)
            degree_dict[class_lines[i]] = degree_dict[class_lines[i]] + 1
    #if necessary, add the child to the degree_dict with a degree of one, otherwise it is already there
    degree_dict.setdefault(class_lines[i+1],0)
    #skip to the next pair
    i = i + 2

def print_task_dict(dictionary):
    for target in dictionary.keys():
        print target ,
        print ":"
        for task in dictionary[target]:
            print task ,
        print "----"

final = []
candidates = []
next = ""
cycle_found = False
while len(degree_dict) != 0:
    for x in degree_dict.keys():
        if degree_dict[x] == 0:
            candidates.append(x)
    if len(candidates) == 0:
        print "ERROR: 0: Type-Check: inheritance cycle"
        os.remove(class_file)
        sys.exit() 
        cycle_found = True
    next = sorted(candidates)[0]
    final.append(next)
    #update indegrees for the removed node
    if task_dict.keys().count(next):
        for task in task_dict[next]:
            degree_dict[task] = degree_dict[task] - 1
    candidates = []
#    print final
    del degree_dict[next]    
if cycle_found == False:
    parent_attributes = []
    parent_methods = []
    for x in final:
      for m in class_list:
        if x == m.identifier:
          child = m
          if child.inherits != None:
            parent = child.inherits
            for c in class_list:
              if parent == c.identifier:
                parent_attributes = c.attribute_list
                parent_methods = c.method_list
          for f in parent_attributes:
            for m in child.attribute_list:
              if f.identifier == m.identifier:
                print "ERROR: " + m.line_no_identifier + ": Type-Check: redefines inherited attribute"
                # os.remove(class_file) ---------- what does this indicate about the tests I'm missing????????
                sys.exit()
          child.attribute_list = parent_attributes + child.attribute_list

         
          # for m in child.method_list:
          #   print m.identifier

has_main = False
for c in class_list:
  if c.identifier == "Main":
    for m in c.method_list:
      if m.identifier == "main":
        has_main = True
        break
if has_main == False:
  print "ERROR: 0: Type-Check: no main method"
  os.remove(class_file)
  sys.exit()


class_list.sort(key=lambda x: x.identifier, reverse=False)
for c in class_list:
  type_file.write(c.identifier + "\n" + str(len(c.attribute_list)) + "\n")
  for attr in c.attribute_list:
    if (attr.kind == "attribute_no_init"):
      type_file.write("no_initializer\n" + attr.identifier + "\n" + attr.return_type + "\n")
    else:
      type_file.write("initializer\n" + attr.identifier + "\n" + attr.return_type + "\n" + str(attr.expression)) 



	
	# common checks here
	# implementation map here 
