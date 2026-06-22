PYTHON ?= python3
PROFILE_JSON ?= ask_long.json
VENV_DIR ?= .venv
VENV_PYTHON := $(VENV_DIR)/bin/python
POETRY := $(VENV_DIR)/bin/poetry
PROJECT_DIR := src
SCRIPT := src/generate_profile.py
OUTPUT_NAME := Saravanakumar_Arunachalam_Resume

.PHONY: help build clean pdf long ask short poorni setup bootstrap

help:
	@echo "Targets:"
	@echo "  make build         Generate the resume using PROFILE_JSON=$(PROFILE_JSON)"
	@echo "  make setup         Create .venv, install Poetry, and install dependencies"
	@echo "  make bootstrap     Setup the environment and build the resume"
	@echo "  make long          Generate using ask_long.json"
	@echo "  make ask           Generate using ask.json"
	@echo "  make short         Generate using ask_short.json"
	@echo "  make poorni        Generate using poorni.json"
	@echo "  make pdf           Alias for build"
	@echo "  make clean         Remove generated resume files"
	@echo "  make help          Show this help"
	@echo ""
	@echo "Variables:"
	@echo "  PROFILE_JSON=ask_long.json|ask.json|ask_short.json|poorni.json"
	@echo "  VENV_DIR=.venv"
	@echo "  PYTHON=python3"

build:
	cd $(PROJECT_DIR) && ../$(POETRY) run python generate_profile.py $(PROFILE_JSON)

pdf: bootstrap

setup:
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_PYTHON) -m pip install --upgrade pip poetry
	cd $(PROJECT_DIR) && ../$(POETRY) env use ../$(VENV_PYTHON)
	cd $(PROJECT_DIR) && ../$(POETRY) lock
	cd $(PROJECT_DIR) && ../$(POETRY) install

bootstrap: setup build

long:
	$(MAKE) bootstrap PROFILE_JSON=ask_long.json

ask:
	$(MAKE) bootstrap PROFILE_JSON=ask.json

short:
	$(MAKE) bootstrap PROFILE_JSON=ask_short.json

poorni:
	$(MAKE) bootstrap PROFILE_JSON=poorni.json

clean:
	rm -f "$(OUTPUT_NAME).docx" "$(OUTPUT_NAME).pdf" "src/$(OUTPUT_NAME).docx" "src/$(OUTPUT_NAME).pdf" "Saravanakumar_Resume.docx" "Saravanakumar_Resume.pdf"
