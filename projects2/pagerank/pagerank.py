import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    contTotal = len(corpus)
    if contTotal == 0:
        return dict()
    pr_ini = (1 - damping_factor) / contTotal
    mapa = {pag: pr_ini for pag in corpus}
    pag_link = corpus[page]
    num_links = len(pag_link)
    if (num_links > 0):
        pr_extra = damping_factor / num_links
        for pagina in pag_link:
            mapa[pagina] += pr_extra
    else:
        pr_extra = damping_factor / contTotal
        for pagina in mapa:
            mapa[pagina] += pr_extra
    return mapa


def sample_pagerank(corpus, damping_factor, n):
    mapa = {}
    lista = []
    for item in corpus:
        mapa[item] = 0
        lista.append(item)
    page = random.choice(lista)
    mapa[page] += 1
    for _ in range(n-1):
        prob = transition_model(corpus, page, damping_factor)
        paginas = list(prob.keys())
        pesos = list(prob.values())
        page = random.choices(paginas, pesos, k=1)[0]
        mapa[page] += 1
    res = {}
    for item in mapa:
        res[item] = mapa[item] / n
    return res


def iterate_pagerank(corpus, damping_factor):
    n = len(corpus.keys())
    ranks = {page: 1/n for page in corpus}
    mapa = {page: [] for page in corpus}
    for itemA in corpus:
        if len(corpus[itemA]) > 0:
            for itemB in corpus[itemA]:
                mapa[itemB].append(itemA)
        else:
            for page in corpus:
                mapa[page].append(itemA)
    while True:
        max = -1
        novo = {}
        for page in corpus:
            sec = 0
            for item in mapa[page]:
                num = len(corpus[item])
                if num == 0:
                    num = n
                sec += ranks[item] / num
            novo_rank = (1-damping_factor)/n + damping_factor*sec
            novo[page] = novo_rank
            if abs(novo_rank - ranks[page]) > max:
                max = abs(novo_rank - ranks[page])
        ranks = novo
        if max <= 0.001:
            break
    return ranks


if __name__ == "__main__":
    main()
