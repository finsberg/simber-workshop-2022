all: lecture

lecture: lecture.md
	marp lecture.md

show-lecture: lecture.html
	open lecture.html

py2notebooks: scripts/*.py
	mkdir -p notebooks; \
	for pyfile in $^ ; do \
		tmp=$${pyfile/scripts/notebooks}; \
		nbfile=$${tmp/.py/.ipynb}; \
		jupytext $$pyfile --to ipynb -o $$nbfile; \
	done

notebooks2py: notebooks/*.ipynb
	mkdir -p scripts; \
	for nbfile in $^ ; do \
		tmp=$${nbfile/notebooks/scripts}; \
		pyfile=$${tmp/.ipynb/.py}; \
		jupytext $$nbfile --to py -o $$pyfile; \
	done
