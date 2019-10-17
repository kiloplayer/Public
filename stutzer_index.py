import numpy as np
from scipy.optimize import Bounds, minimize


def cal_stutzer_index(return_access):
    return_access = np.array(return_access)
    information_statistic = lambda theta: np.log(np.mean(np.exp(theta[0] * return_access)))
    theta0 = [-1.]
    bounds = Bounds((-np.inf), (0.))
    result = minimize(information_statistic, theta0, method='SLSQP', bounds=bounds, tol=1e-16)
    if result.success:
        information_statistic = -result.fun
        stutzer_index = np.abs(np.mean(return_access)) / np.mean(return_access) * np.sqrt(2 * information_statistic)
        print('成功找到Information Statistic最大值：' + str(round(information_statistic, 10)))
        print('theta取值为' + str(round(result.x[0], 5)))
        print('stutzer index取值为' + str(round(stutzer_index, 5)))
        result = {'information_statistic': information_statistic,
                  'stutzer_index': stutzer_index,
                  'theta': result.x[0]}
    else:
        print('未找到Information Statistic最大值')

    return result


if __name__ == '__main__':
    # 设定随机数起始位置
    np.random.seed(0)

    # 设定随机收益率序列
    print('随机收益序列：')
    return_access = np.random.normal(loc=0., scale=0.05, size=(100,))
    print('随机序列均值为：' + str(round(np.mean(return_access), 5)))
    result = cal_stutzer_index(return_access)

    # 收益全部非负情况下的结果
    print('\n全部收益非负情况下的结果：')
    return_access_positive = return_access.copy()
    return_access_positive[np.where(return_access_positive < 0)] = 0.
    result = cal_stutzer_index(return_access_positive)

    # 仅有一个收益为-0.1情况下的结果
    print('\n仅有一个收益为-0.1情况下的结果：')
    return_access_positive[-1] = -0.1
    result = cal_stutzer_index(return_access_positive)

    # 仅有一个收益为-0.5情况下的结果
    print('\n仅有一个收益为-0.5情况下的结果：')
    return_access_positive[-1] = -0.5
    result = cal_stutzer_index(return_access_positive)

    # 仅有5个收益为负情况下的结果
    print('\n仅有5个收益为负情况下的结果：')
    return_access_positive[-6:-1] = -0.1
    result = cal_stutzer_index(return_access_positive)

    # 收益全部非正情况下的结果
    print('\n全部收益非正情况下的结果：')
    return_access_negative = return_access.copy()
    return_access_negative[np.where(return_access_negative > 0)] = 0.
    result = cal_stutzer_index(return_access_negative)

    # 设定随机数起始位置
    np.random.seed(100)

    # 设定随机收益率序列
    print('\n\n随机收益序列：')
    return_access = np.random.normal(loc=0., scale=0.05, size=(100,))
    print('随机序列均值为：' + str(round(np.mean(return_access), 5)))
    result = cal_stutzer_index(return_access)

    # 收益全部非负情况下的结果
    print('\n全部收益非负情况下的结果：')
    return_access_positive = return_access.copy()
    return_access_positive[np.where(return_access_positive < 0)] = 0.
    result = cal_stutzer_index(return_access_positive)

    # 仅有一个收益为-0.1情况下的结果
    print('\n仅有一个收益为-0.1情况下的结果：')
    return_access_positive[-1] = -0.1
    result = cal_stutzer_index(return_access_positive)

    # 仅有一个收益为-0.5情况下的结果
    print('\n仅有一个收益为-0.5情况下的结果：')
    return_access_positive[-1] = -0.5
    result = cal_stutzer_index(return_access_positive)

    # 仅有5个收益为负情况下的结果
    print('\n仅有5个收益为负情况下的结果：')
    return_access_positive[-6:-1] = -0.1
    result = cal_stutzer_index(return_access_positive)

    # 收益全部非正情况下的结果
    print('\n全部收益非正情况下的结果：')
    return_access_negative = return_access.copy()
    return_access_negative[np.where(return_access_negative > 0)] = 0.
    result = cal_stutzer_index(return_access_negative)
