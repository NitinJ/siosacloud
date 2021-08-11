runserver:
	python siosacloud/manage.py runserver

generate-licenses-% :
	python siosacloud/manage.py generate-licenses --count $*

