# txt2sprite

Text to 2D image converter

## Advantages

* Create images when developing on terminal-only system (e.g. Android Termux)
* Easily swap color palettes
* Pipeline-friendly
* Open for extension: sprite sheets, animation and further meta data

## Syntax

See [example.txt](example.txt).

## Usage

1. Ensure `pipenv` is installed and use it to install dependencies:

```
pipenv install
```

2. Render a text file

```
pipenv run python . < example.txt
```

or

```
pipenv run python . -i example.txt
```

The output is written to `stdin.png` (can be overridden with `-o` parameter):

![Result](stdin.png)