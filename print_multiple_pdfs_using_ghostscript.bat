echo off
REM Batch file to print multiple PDF files using installed ghostscript

REM           set dfile="small_sample_1.pdf"
REM           set alist=small_sample_1.pdf small_sample_2.pdf
REM C:\Program Files\gs\gs9.53.3\bin>gswin64c.exe -sDEVICE=mswinpr2 -dBATCH -dNOPAUSE -dPDFFitPage -sOutputFile="%printer%Canon MF220 Series V4" test.pdf
SET MY_PATH=C:\Program Files\gs\gs9.53.3\bin
REM "C:\Program Files\gs\gs9.53.3\bin\gswin64c.exe" -sDEVICE=mswinpr2 -dBATCH -dNOPAUSE -dPDFFitPage -dNoCancel -sOutputFile="%printer%Canon MF220 Series V4" small_sample_1.pdf
REM the following line prints without intervention, the -dQUIET argument is absent, meaning it will display in STDOUT the steps and progress of the print job
REM "C:\Program Files\gs\gs9.53.3\bin\gswin64c.exe" -sDEVICE=mswinpr2 -dBATCH -dNOPAUSE -dPDFFitPage -dNoCancel -dQueryUser=3 -sOutputFile="%printer%Canon MF220 Series V4" small_sample_1.pdf
REM             for /r %%i in (small_sample*.pdf) do echo %%i
REM for %%i in (*.pdf) do echo "%%i"
REM the following line works - 2021-02-16
REM for %%i in (*.pdf) do "%MY_PATH%\gswin64c.exe" -sDEVICE=mswinpr2 -dBATCH -dNOPAUSE -dPDFFitPage -dQueryUser=3 -sOutputFile="%printer%Canon MF220 Series V4" "%%i"

SET MY_EXECUTABLE_PATH=C:\Program Files\gs\gs9.53.3\bin
for %%i in (*.pdf) do "%MY_EXECUTABLE_PATH%"\gswin64c.exe -sDEVICE=mswinpr2 -dBATCH -dNOPAUSE -dPDFFitPage -dQueryUser=3 -sOutputFile="%printer%Canon MF220 Series V4" "%%i"
