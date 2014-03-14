class Main inherits IO {
   main(): Object {
         out_string("marisa")
   };
};

class Cons inherits Object {
      xcar : Int;
      xcdr : Object;
      
      xcar() : Bool { false };

      init(hd : Int, tl : Object) : Cons {
        {
	    xcar <- hd;
	        xcdr <- tl;
		    self;
		      }
 };
};

