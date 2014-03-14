class Main inherits IO {
  main () : Object { 
      let self : SELF_TYPE <- (new A2I).a2i("678987"), 
          b : String <- (new A2I).i2a(8675309) in
      { 
        out_int(a) ;
        out_string(" == ") ;
        out_string(b) ;
        out_string("\n"); 
      } 
  } ;
} ;