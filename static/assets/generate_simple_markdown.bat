@echo off
set BASE_DIR=%~dp0
set RUN_PY=%BASE_DIR%generate_simple_markdown.py

::==================
set OUTPUT_DIR=I:\project\simizlab-homepages\test1\content\topics
set GENERATE_DATE_LIST=2013-03-02 2013-07-18 2013-09-28 2013-11-29
::==================

python %RUN_PY% -o %OUTPUT_DIR% -g %GENERATE_DATE_LIST%

PAUSE
