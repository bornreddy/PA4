class Main inherits IO  {
  main() : Int {
   { true; 5; }
  };
  i : Marisa;
  t : Marisa;
  l : Marisa <- (i <- t);
};

class Marisa {
  i : Int;
};
