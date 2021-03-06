test = test.cl-ast

make:

	./cool --parse $(addsuffix .cl, $(basename $(test)))
	./cool --class-map $(addsuffix .cl, $(basename $(test)))
	python main2.py  $(test)

out: 
	python main.py $(test)
clean:
	rm *~ *#
zip:
	zip -l mpr2zp.zip main.py