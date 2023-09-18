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


def D(N_cf, N_uf, N_cs, N_us):
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
