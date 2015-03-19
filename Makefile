# Makefile for a PyQGIS plugin

all: compile

dist: package

install: copy2qgis

PY_FILES = HelloServer.py HelloServerDialog.py __init__.py
UI_FILES = Ui_HelloServer.py
                                                                                                                                                                                                                                                                                                                                                                                                               RESOURCE_FILES = resources.py

compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc4 -o $@ $<

%.py : %.ui
	pyuic4 -o $@ $<



clean:
	find ./ -name "*.pyc" -exec rm -rf \{\} \;
	rm -f ../HelloServer.zip
	rm -f Ui_HelloServer.py

package:
	cd .. && find HelloServer/  -print|grep -v Make | grep -v zip | grep -v .git | zip HelloServer.zip -@

localrepo:
	cp ../HelloServer.zip ~/public_html/qgis/HelloServer.zip

copy2qgis: package
	unzip -o ../HelloServer.zip -d ~/.qgis/python/plugins

check test:
	@echo "Sorry: not implemented yet."
