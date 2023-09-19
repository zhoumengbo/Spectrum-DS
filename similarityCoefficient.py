coefficient_list = ['Tarantula', 'Ochiai', 'Jaccard', 'AMPLE', 'Kulczynski', 'D2', 'OP2', 'SBI', 'Ochiai2', 'Zoltar']


def Tarantula(N_cf, N_uf, N_cs, N_us):
    numerator = N_cf / (N_cf + N_uf)
    denominator = numerator + (N_cs / (N_cs + N_us))
    if denominator == 0.0:
        return 0.0
    else:
        return numerator / denominator


def Ochiai(N_cf, N_uf, N_cs, N_us):
    numerator = N_cf
    denominator = ((N_cf + N_cs) / (N_cf + N_uf)) ** 0.5
    if denominator == 0.0:
        return 0.0
    else:
        return numerator / denominator


def Jaccard(N_cf, N_uf, N_cs, N_us):
    numerator = N_cf
    denominator = N_cf + N_cs + N_uf
    if denominator == 0.0:
        return 0.0
    else:
        return numerator / denominator


def AMPLE(N_cf, N_uf, N_cs, N_us):
    if N_cf + N_uf == 0.0:
        item1 = 0.0
    else:
        item1 = N_cf / (N_cf + N_uf)
    if (N_cs + N_us) == 0.0:
        item2 = 0.0
    else:
        item2 = N_cs / (N_cs + N_us)
    return abs(item1 - item2)


def Kulczynski(N_cf, N_uf, N_cs, N_us):
    numerator = N_cf
    denominator = N_cs + N_uf
    if denominator == 0.0:
        return 0.0
    else:
        return numerator / denominator


def D2(N_cf, N_uf, N_cs, N_us):
    numerator = N_cf ** 2
    denominator = N_cs + N_uf
    if denominator == 0.0:
        return 0.0
    else:
        return numerator / denominator


def OP2(N_cf, N_uf, N_cs, N_us):
    item1 = N_cf
    item2 = N_cs / (N_cs + N_us + 1)
    return item1 - item2


def SBI(N_cf, N_uf, N_cs, N_us):
    item1 = 1
    if N_cs + N_cf == 0.0:
        item2 = 0.0
    else:
        item2 = N_cs / (N_cs + N_cf)
    return item1 - item2


def Ochiai2(N_cf, N_uf, N_cs, N_us):
    numerator = N_cf * N_us
    denominator = ((N_cf + N_cs) * (N_us + N_uf) * (N_cf + N_uf) * (N_cs + N_us)) ** 0.5
    if denominator == 0.0:
        return 0.0
    else:
        return numerator / denominator


def Zoltar(N_cf, N_uf, N_cs, N_us):
    numerator = N_cf
    if N_cf == 0.0:
        item = 0.0
    else:
        item = (10000 * N_uf * N_cs) / N_cf
    denominator = N_cf + N_uf + N_cs + item
    if denominator == 0.0:
        return 0.0
    else:
        return numerator / denominator


def select_coefficient(name, N_cf, N_uf, N_cs, N_us):
    if name == coefficient_list[0]:
        return Tarantula(N_cf, N_uf, N_cs, N_us)
    elif name == coefficient_list[1]:
        return Ochiai(N_cf, N_uf, N_cs, N_us)
    elif name == coefficient_list[2]:
        return Jaccard(N_cf, N_uf, N_cs, N_us)
    elif name == coefficient_list[3]:
        return AMPLE(N_cf, N_uf, N_cs, N_us)
    elif name == coefficient_list[4]:
        return Kulczynski(N_cf, N_uf, N_cs, N_us)
    elif name == coefficient_list[5]:
        return D2(N_cf, N_uf, N_cs, N_us)
    elif name == coefficient_list[6]:
        return OP2(N_cf, N_uf, N_cs, N_us)
    elif name == coefficient_list[7]:
        return SBI(N_cf, N_uf, N_cs, N_us)
    elif name == coefficient_list[8]:
        return Ochiai2(N_cf, N_uf, N_cs, N_us)
    elif name == coefficient_list[9]:
        return Zoltar(N_cf, N_uf, N_cs, N_us)
    else:
        print("Error in select_coefficient")
