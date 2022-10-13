from typing import List
from csv import reader
from multiprocessing import Pool
import os
import argparse
from pygit2 import clone_repository


def extract_url(csv_path: str, url_column_number:int) -> List[str]:
    with open(csv_path) as f:
        r = reader(f)
        return [row[url_column_number] for row in r]


def clone(url: str, path):
    repo_name = url.split('/')[-1]
    print(f"clone {repo_name} starts", flush=True)
    clone_repository(url, os.path.join(path, repo_name))
    print(f"clone {repo_name} finished", flush=True)


def clone_repositories(url_list: List[str], path: str):
    '''
    url_list: repository urls
    path: local path to clone into
    '''
    pool = Pool()
    pool.starmap(clone, [(url, path) for url in url_list])
    pool.close()
    pool.join()


def command_line()->List[str]:
    parser = argparse.ArgumentParser(description="Fast and light big scale git repositories cloner")

    parser.add_argument('-i', '--input', help="csv path which contains git repository urls", default = "./repositories.csv")
    parser.add_argument('-c', '--column', help="column number of urls in the csv", default=0)
    parser.add_argument('-o','--output', help = "output path for cloned repositories", default="./")

    return parser.parse_args()


if __name__ == "__main__":
    args = command_line()
    repos = extract_url(args.input, int(args.column))
    print(repos)
    clone_repositories(repos, args.output)

    print("=========================================Clone Finished==========================================")

