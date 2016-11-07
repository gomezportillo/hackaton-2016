
def reto1(version):
    words = version.split(".")
    for i in range(len(words), 0, -1):
        print(".".join(words[:i]))


reto1(input())
