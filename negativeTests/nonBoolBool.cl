class Main {
   main() : Object {
     true
   };
};


class Cons inherits Object {
      xcar : Int;
      xcdr : Bool;

      isNil() : Bool { xcdr <- xcar };

      init(hd : Int, tl : Object) : Cons {
        {
            xcar <- hd;
                xcdr <- tl;
                    self;
                      }
                      };
};