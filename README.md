# Technical test for Software Engineer candidates

This is a template repo with a bare-bones starting point. Please feel free to change or ignore.

[Read the book for details of the task][book].

We only accept submissions from people who have been invited. No agencies please.

## Building

```shell script
docker build -t bookcreator-recruitment-censor-test:latest .
```

## Running
```shell script
# Have to pass the files into the container somehow, don't
#    want to have to rebuild every time the inputs change.
docker run 
  --rm \
  --name bookcreator-recruitment-censor-test \
  --mount type=bind,source="$(pwd)"/test,target=/test
  bookcreator-recruitment-censor-test:latest \ 
    --items /test/items.txt \
    --blocklist /test/blocklist.txt
```

[book]: https://read.bookcreator.com/Gr0k3Ie4s3gXU7stHRzFJiILKD83/UEzOFQjyR121W1pKRm47Lg