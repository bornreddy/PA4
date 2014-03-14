class Cons inherits List {
      xcar : Int;
      xcdr : List;

      isNil() : Bool { false };

      init(hd : Int, tl : List) : Cons {
        {
	    xcar <- hd;
	        xcdr <- tl;
		    self;
		      }
		      };
};

class List inherits Cons {
      xcar : Int;
      xcdr : List;

      isNil() : Bool { false };

      init(hd : Int, tl : List) : Cons {
        {
	    xcar <- hd;
	        xcdr <- tl;
		    self;
		      }
		      };
}; 
