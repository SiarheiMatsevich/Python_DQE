import random
import string


# Generator
gen_list = []
for liGen in range(random.randint(2, 10)):
    dict_list = {}
    while len(dict_list) < random.randint(2, 10):
        key = random.choice(string.ascii_lowercase)
        value = random.randint(1, 100)
        dict_list[key] = value
    gen_list.append(dict_list)


# unite
out = {}
for i in gen_list:
    i_num = gen_list.index(i) + 1
    for key, value in i.items():
        new = {f"{key}_{i_num}": value}
        out.update(new)


# Duplicate remover. Unique checker
for u_k, u_v in out.copy().items():
    if u_k in out:
        temp_u = out.copy()
        del temp_u[u_k]
        del_count = 0
        for t_k, t_v in temp_u.items():
            if u_k[:1] == t_k[:1]:
                if u_v >= t_v:
                    if t_k in out:
                        del_count += 1
                        del out[t_k]
        if not del_count:
            out.update({u_k[:1]: u_v})
            del out[u_k]

