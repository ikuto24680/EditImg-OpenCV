:INPUT_CHECK
SET INPUTSTR=
SET /P INPUTSTR=

for /l %%P in (1,1,%INPUTSTR%) do (
  echo %%P
  opencv_createsamples.exe -img ./ok/dog/%%P.jpg -num 1000 -vec %%P.vec
)
echo "èIóπ"