NOTEBOOKS = cp_exploredata.ipynb exploredata.ipynb modeling1.ipynb 

PY_FILES = cp_exploredata.py exploredata.py modeling1.py

# Make .py versions of all notebooks in NOTEBOOKS 
# Then move all corresponding PY_FILES into the py_files directory
convert_notebooks_to_py_files : 
	for i in $(NOTEBOOKS); do jupyter nbconvert --to script $$i; done
	for j in $(PY_FILES); do mv $$j py_notebook_copies; done