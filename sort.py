with open("sort-from.txt") as f:
    with open("sort-to.txt", "w+") as f2:
        f2.write("\n".join(["- " + i.strip() for i in sorted(f.read().split("\n"))]))
