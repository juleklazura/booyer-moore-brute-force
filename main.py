import time
import statistics


def searchbruteforce(txt, pat):
    i = 0
    j = 0
    while i < len(txt) and j < len(pat):
        if txt[i] == pat[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j >= len(pat):
        return i - len(pat)
    else:
        return 0


def badCharHeuristic(string, size):
    badChar = [-1] * 256
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


def search(txt, pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - badChar[ord(txt[s + j])])


def boyer_moore():
    boyertime = list()
    with open("genes.txt", "r") as arquivo:
        txt = arquivo.read()
    txt.replace(" ", "")
    listapat = ["ttcttcc", "tgcttcctc", "agagttta", "tttgatga", "cccaata", "gttaaaca", "ttgtgt", "aggcccca",
                "caaaa",
                "ctggcgat", "gggtc"]
    for i in range(0, len(listapat)):
        start = time.perf_counter()
        search(txt, listapat[i])
        end = time.perf_counter()
        boyertime.append(end - start)
    print('Tempo Médio Gasto :{}'.format(sum(boyertime) / len(listapat)))
    print('Desvio Padrão dos Tempos Gastos:{}\n\n\n'.format(statistics.pstdev(boyertime)))


def bruteforce():
    bruteforcetime = list()
    with open("genes.txt", "r") as arquivo:
        txt = arquivo.read()
    txt.replace(" ", "")
    listapat = ["ttcttcc", "tgcttcctc", "agagttta", "tttgatga", "cccaata", "gttaaaca", "ttgtgt", "aggcccca",
                "caaaa",
                "ctggcgat", "gggtc"]

    for i in range(0, len(listapat)):
        start = time.perf_counter()
        searchbruteforce(listapat[i], txt)
        end = time.perf_counter()
        bruteforcetime.append(end - start)
    print('Tempo Médio Gasto :{}'.format(sum(bruteforcetime) / len(listapat)))
    print('Desvio Padrão dos Tempos Gastos:{}'.format(statistics.pstdev(bruteforcetime)))


def main():
    print('Resultados Boyer-Moore')
    boyer_moore()
    print('Força Bruta')
    bruteforce()


if __name__ == '__main__':
    main()
