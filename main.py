epsilon = 0.25
h = 0.001

def f1(y1, y2, y3, D):
    return y1 - 2 * y2 ** 2 - D * y2 + y3

def f2(y1, y2, D):
    return D * y1 + 2 * y1 * y2 + y2

def f3(y1, y3, M):
    return -2 * y3 * (y1 + M)

def k11(f, x, y, z, D):
    return f(x, y, z, D)

def k21(f,  x,  y,  z,  k, D):
    return f(x + h / 2, y + h * k / 2, z + k * h / 2, D)

def k31(f, x, y, z, k, D):
    return f(x + h / 2, y + k * h / 2, z + k * h / 2, D)

def k41(f, x, y, z, k, D):
    return f(x + h, y + h * k, z + h * k, D)

def k12(f, x, y, D):
    return f(x, y, D)

def k22(f, x, y, k, D):
    return f(x + h / 2, y + k * h / 2, D)

def k32(f, x, y, k, D):
    return f(x + h / 2, y + k * h / 2, D)

def k42(f, x, y, k, D):
    return f(x + h, y + h * k, D)

def k13(f, x, y, M):
    return f(x, y, M)

def k23(f, x, y, k, M):
    return f(x + h / 2, y + k * h / 2, M)

def k33(f, x, y, k, M):
    return f(x + h / 2, y + k * h / 2, M)

def k43(f, x, y, k, M):
    return f(x + h, y + h * k, M)

def NextValue(y,  y_list):
    return y + h * (y_list[0] + 2 * y_list[1] + 2 * y_list[2] + y_list[3]) / 6

if __name__ == '__main__':

    print('Hello! Please, enter D equal 0 or 2:')
    D = int(input())
    if D == 0:
        print('Please, enter list of M values, where 1/2 < M < 14:')
        M = float(input())
    elif D == 2:
        print('Please, enter list of M values, where 1/2 < M <= 3, 3 < M <= 8.5, 8.5 < M <= 14:')
        M = float(input())
    else:
        print('Bad D value!')

    y_1 = - M + epsilon
    y_2 = D * M / (1 - 2 * M) + epsilon
    y_3 = (D * D * M + 4 * M ** 3 - 4 * M ** 2 + M) / (2 * M - 1) ** 2 + epsilon
    t = 0
    t_list = [t]
    y_1_list = [y_1]
    y_2_list = [y_2]
    y_3_list = [y_3]
    while t <= 11:
        k1 = k11(f1, y_1, y_2, y_3, D)
        k2 = k21(f1, y_1, y_2, y_3, k1, D)
        k3 = k31(f1, y_1, y_2, y_3, k2, D)
        k4 = k41(f1, y_1, y_2, y_3, k3, D)

        y_1_k_list = [k1, k2, k3, k4]

        k1 = k12(f2, y_1, y_2, D)
        k2 = k22(f2, y_1, y_2, k1, D)
        k3 = k32(f2, y_1, y_2, k2, D)
        k4 = k42(f2, y_1, y_2, k3, D)

        y_2_k_list = [k1, k2, k3, k4]

        k1 = k13(f3, y_1, y_3, M)
        k2 = k23(f3, y_1, y_3, k1, M)
        k3 = k33(f3, y_1, y_3, k2, M)
        k4 = k43(f3, y_1, y_3, k3, M)

        y_3_k_list = [k1, k2, k3, k4]

        y_1 = NextValue(y_1, y_1_k_list)
        y_2 = NextValue(y_2, y_2_k_list)
        y_3 = NextValue(y_3, y_3_k_list)

        t_list.append(t)
        y_1_list.append(y_1)
        y_2_list.append(y_2)
        y_3_list.append(y_3)

        t += h

    import matplotlib as mpl
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    #print(len(t_list), len(y_1_list))
    fig1 = plt.figure()
    plt.plot(t_list, y_1_list)
    fig2 = plt.figure()
    plt.plot(t_list, y_2_list)
    fig3 = plt.figure()
    plt.plot(t_list, y_3_list)
    '''
    fig2 = plt.figure()
    plt.plot(y_2_list, y_1_list)
    plt.plot(y_3_list, y_1_list)
    plt.plot(y_3_list, y_2_list)
    fig3 = plt.figure()
    ax = fig3.gca(projection='3d')
    ax.plot(y_1_list, y_2_list, y_3_list, label='chto eto')
    ax.legend()
    '''
    plt.show()
