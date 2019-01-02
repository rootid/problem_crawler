.PHONY:	clean

run:
	python bin/ltcode.py

clean:
	@echo "Cleaning pyc files"
	find . -name "*.pyc" | xargs rm -rf

# vim: noexpandtab
