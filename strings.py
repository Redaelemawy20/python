name = 'welcome'
# len
print(len(name))

print(name[len(name)-1])

print(name[0:])
print(name[:3])
print(name[3:])
print(name[:])


name = 'oneOne'
# make it -> oneone
print(name)
name = name[:3] + 'o' + name[4:]
print(name)

# qoutes
q = "hello 'ahmed' how are you and your mother?"
print(q)


# escaping
q = "hello ahmed how are you \"and\" your mother?"
print(q)

# multi line strings
ss = """ehwlkwk' kkwkkwkw "kdjwo   kwlheowooww  lll
dkwlwkoeiwo khhoweiowoi fuckhewioslslw"""
print(ss)
print(ss[-1])