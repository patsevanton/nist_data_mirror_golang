bin:
	govendor sync
	go build

test:
	govendor sync
	go test -v

.PHONY: test bin
.DEFAULT_GOAL := bin
