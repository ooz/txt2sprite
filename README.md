# txt2sprite

Text to 2D image converter

## Syntax

See [example.txt](example.txt).

## Usage

1. Ensure `pipenv` is installed and use it to install dependencies:

```
pipenv install
```

2. Pipe the text file into the program

```
pipenv run python . < example.txt
```

The output is written to `stdin.png`:

![Result](stdin.png)