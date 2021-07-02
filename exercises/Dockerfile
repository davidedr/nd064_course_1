FROM golang:alpine 
LABEL maintainer="d2r"
WORKDIR /go/src/app
ADD go-helloworld/. .
# Solves the "go: go.mod file not found in current directory or any parent directory; see 'go help modules'"
# in docker command: RUN go build  -o helloworld:
# See https://knowledge.udacity.com/questions/596278
ENV GO111MODULE off
RUN go build -o helloworld
EXPOSE 6111:6111
CMD ["./helloworld"]