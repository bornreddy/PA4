SRCS=$(wildcard *.cl-ast)
FILES = $(wildcard *.cl3)
make:
	$(foreach src,$(SRCS), ./cool --type $(src);)
unparse:
	$(foreach src,$(SRCS), ./cool --unparse $(src);)

rename:
	$(foreach file, $(FILES), mv $(file) $(addsuffix .cl, $(basename $(file)));)
clean:
	rm *~ *cl-type *cl-ast
zip:
	zip -l mpr2zp *.cl main.py