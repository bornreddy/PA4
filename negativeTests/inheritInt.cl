
class Silly inherits Int {
   copy() : SELF_TYPE { self };
   face() : Object { true } ;
};

class Sally inherits Silly { 
   face () : Object { false };
};



class Main inherits IO {

   x : Sally <- (new Sally).copy();
   y : Silly <- (new Silly).copy();
   main() : Object { 
      y@Int.face()
   };

} ;

