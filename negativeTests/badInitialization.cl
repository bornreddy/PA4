class Main inherits IO {
   main() : Object {
   out_string("marisa")
};
};


class Cons {

      xcdr : Object;
      xcar : Int <- xcdr;
      isNil() : Bool { false };

      init(hd : Int, tl : Object) : Cons {
        {
	    xcar <- hd;
	        xcdr <- tl;
		    self;
		      }
		      };
};

