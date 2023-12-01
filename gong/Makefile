PYTHON := python3.11
DAYS := $(shell seq -w 1 25)

all: run

run: $(addprefix run-day-, $(DAYS))

run-day-%:
	$(PYTHON) day-$*.py

install:
	pip install -r requirements.txt

clean:
	rm -f *.pyc

.PHONY: all run install clean clean-all add
