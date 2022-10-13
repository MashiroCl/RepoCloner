# RepoCloner

Fast and light big scale git repositories cloner.

## Introduciton
You can clone large scale GitHub repositores in a short time with only one command with RepoCloner.

## Requirement
python3.6 and later, pygit2

## Build
```
$ git clone https://github.com/MashiroCl/RepoCloner
$ cd RepoCloner
$ pip install -r requirements.txt
```
Fill the `repositores.csv` with repositories information, we show an example in the `repositories.csv`. Be sure the urls are in the same column.


## General Options
- `-i`, `--input`: Csv path which contains git repository urls (default: ./repositories.csv)
- `-c`, `--column`: Column number of urls in the csv (default: 5)
- `-o`, `--output`: Output path for cloned repositories (default: ./)
