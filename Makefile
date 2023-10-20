# "make convert_notebooks_to_py_files" will:
# make a .py copy of every .ipynb for easier change review.
convert_notebooks_to_py_files : 
	for i in $(shell find ./ -name "*.ipynb"); do jupyter nbconvert --to script $$i; done