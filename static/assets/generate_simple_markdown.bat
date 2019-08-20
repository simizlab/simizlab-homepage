@echo off
set BASE_DIR=%~dp0
set RUN_PY=%BASE_DIR%generate_simple_markdown.py

::==================
set OUTPUT_DIR=I:\project\simizlab-homepages\test1\content\topics
set GENERATE_DATE_LIST=2009-01-21 2009-08-04 2009-09 2009-12-10
::==================

python %RUN_PY% -o %OUTPUT_DIR% -g %GENERATE_DATE_LIST%

PAUSE
