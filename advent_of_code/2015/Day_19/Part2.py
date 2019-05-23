total = 0


def compute(molecule: str, translations: list, total: int) -> int:
    while molecule != 'e':
        for lhs, rhs in translations:
            if lhs in molecule:
                molecule = molecule.replace(lhs, rhs, 1)
                total += 1
                break
    return total


with open("input19_3.txt") as file:
    lines = file.readlines()

medicine = lines[-1].strip()
pairs = [(line.split()[-1], line.split()[0]) for line in lines if "=>" in line]
groups = sorted(pairs, key=lambda x: len(x[0]), reverse=True)

total = compute(medicine, groups, total)

print(total)
