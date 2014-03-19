class Main inherits IO  {
  main() : Int {
   { true; 5; }
  };
  i : Marisa;
  t : Marisa;
  l : Marisa <- (i <- t);
};

class Marisa {
  main() : Bool {
   true
  };
  i : Int;
};

class D inherits B {

};

class E inherits B {

};

class B inherits A {

};

class C inherits A {

};


class A {

};