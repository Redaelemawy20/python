from pathlib import Path

path = Path("magic.py")

print(path.absolute())
print(path.exists())
print(path.is_dir())
print(path.absolute())
print(path.is_file())
print(path.stem)
print(path.suffix)
print({path.absolute().parts})
print(path.with_suffix('.hamo'))
for p in path.absolute().parts:
    print(p)


hash = {}
for p in Path().iterdir():
    if p.is_file():
        sf = p.suffix or p.name
        hash[sf] = (hash.get(sf, 0) + 1)
        print(p)
        print(len(sf))

for k,v in hash.items():
    print(f'{k} : {v}')


print([p for p in Path().glob('ma*')])