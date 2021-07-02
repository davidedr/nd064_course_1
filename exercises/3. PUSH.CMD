@ECHO OFF
CLS

REM Push container to repo
ECHO Tag...
docker tag go-helloworld davidedr/go-helloworld:v1.0.0
ECHO Login...
docker login
ECHO Push...
docker push davidedr/go-helloworld:v1.0.0