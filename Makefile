# "make convert_notebooks_to_py_files" will:
# convert all .ipynb files to .py files for easier change review.
convert_notebooks_to_py_files : 
	for i in $(shell find ./ -name "*.ipynb"); do jupyter nbconvert --to script $$i; done