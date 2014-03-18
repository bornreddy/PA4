test = test.cl-ast

make:

	./cool --parse $(addsuffix .cl, $(basename $(test)))
	./cool --class-map $(addsuffix .cl, $(basename $(test)))
	python main2.py  $(test)
	diff $(addsuffix .cl-type, $(basename $(test))) $(addsuffix .cl-mytype, $(basename $(test)))
	diff $(addsuffix .cl-ast, $(basename $(test))) $(addsuffix .cl-descent, $(basename $(test)))


out: 
	python main.py $(test)
clean:
	rm *~ *#
zip:
	zip -l mpr2zp.zip main.py