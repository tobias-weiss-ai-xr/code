# syntax=docker/dockerfile:1

FROM golang:1.24-alpine

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY *.go ./
COPY database ./database
COPY data_generator ./data_generator
COPY performance ./performance
COPY charts ./charts

RUN go build -o /stock-market-retriever

CMD [ "/stock-market-retriever" ]
