Class Main inherits IO {
    main() : Object {
     out_string("marisa")
    };
};

class List inherits Object {
      xcar : Int;
      xcdr : List;

      isNil(marisa:Int) : Bool { false };

      init(hd : Int, tl : List) : Cons {
        {
            xcar <- hd;
                xcdr <- tl;
                    self;
                      }
                      };
}; 

class Cons inherits List {

      isNil(marisa:Bool) : Bool { false};

      init(hd : Int, tl : List) : Cons {
        {
	    xcar <- hd;
	        xcdr <- tl;
		    self;
		      }
		      };
};
