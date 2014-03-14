class Cons {
      xcar : Int;
      xcdr : Object;
      xcar : Object;
      isNil() : Bool { false };

      init(hd : Int, tl : Object) : Cons {
        {
	    xcar <- hd;
	        xcdr <- tl;
		    self;
		      }
		      };
};

