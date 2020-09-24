import sys

inp = []
for line in sys.stdin:

    inp += line.split()

out = set()

for i in range(len(inp)):
    for j in range(0, len(inp)):
        if j != i:

            b = inp[i] + inp[j]
            compound = "".join(b)
            if compound not in out:

                out.add(compound)
print('\n'.join(sorted(list(out))))