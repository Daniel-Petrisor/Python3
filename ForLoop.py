'''
========== FOR LOOP ===========
IN PYTHON UN ITERABILE È UN OGGETTO IN GRADO DI RESTITUIRE VALORI UNO ALLA VOLTA
'''

# RANGE
# ==========================
for i in range(5):
    print(i)

''' Output:
0
1
2
3
4
'''

# RANGE and CONTINUE
# ==========================
for i in range(5):
    if i == 3:
        continue
    print(i)

''' Output:
0
1
2
4
'''

# RANGE and BREAK
# ==========================
for i in range(5):
    if i == 3:
        break
    print(i)

''' Output:
0
1
2
'''

# RANGE - BREAK and ELSE
# ==========================
for i in range(1, 8):
    print(i)
    if i % 7 == 0:
        print("multiplo di 7 trovato")
        break
else:
    print("nessun multiplo di 7 nell'intervallo")

''' Output:
1
2
3
4
nessun multiplo di 7 nell'intervallo
'''

# RANGE - TRY and CONTINUE
# ==========================
for i in range(5):
    print('-' * 20)
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print("diviso per 0")
        continue
    finally:
        print("esegui sempre")
    print(i)

''' Output:
-------------------- 
esegui sempre        
0
-------------------- 
esegui sempre        
1
--------------------
esegui sempre
2
--------------------
diviso per 0
esegui sempre
--------------------
esegui sempre
4
'''



# LIST
# ==========================
for i in [1, 2, 3, 4]:
    print(i)

''' Output:
0
1
2
3
4
'''

# TUPLA
# ==========================
for i in ('a', 'b', 'c', 4):
    print(i)

''' Output:
a
b
c
4
'''

# LIST contain TUPLA
# ==========================
for i in [(1, 2), (3, 4), (5, 6)]:
    print(i)

''' Output:
(1, 2)
(3, 4)
(5, 6)
'''

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

''' Output:
1 2
3 4
5 6
'''

# STRING
# ==========================
for i in 'hello':
    print(i)

''' Output:
h
e
l
l
o
'''


# STRING
# ==========================
s = 'hello'
for i in s:
    print(i)

''' Output:
h
e
l
l
o
'''

# STRING and INDEX
# ==========================
s = 'hello'
idx = 0
for c in s:
    print(idx, c)
    idx += 1

''' Output:
0 h
1 e
2 l
3 l
4 o
'''

# STRING and INDEX
# Metodo migliore
# ==========================
s = 'hello'
for i in range(len(s)):
    print(i, s[i])

''' Output:
0 h
1 e
2 l
3 l
4 o
'''

# STRING and INDEX
# ==========================
s = 'hello'
for i, c in enumerate(s):
    print(i, c)

''' Output:
0 h
1 e
2 l
3 l
4 o
'''