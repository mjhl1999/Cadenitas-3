def reversa(cadena):
    s = ""
    for i in reversed(range(len(cadena))):
        o = len(s)
        s += cadena[i]

    return s
