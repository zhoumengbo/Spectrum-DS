import matplotlib
from matplotlib import pyplot as plt
from Utils.getMatrixFromHTML import get_matrix
import similarityCoefficient
matplotlib.use('TkAgg')


def Coefficient(failure_testcase_folder, html_folder):
    result_dic = similarity_measure(failure_testcase_folder, html_folder)
    for k, v in result_dic.items():
        sus = similarityCoefficient.Tarantula(v[0], v[1], v[2], v[3])
        result_dic[k] = sus
    sort_list = sorted(result_dic.items(), key=lambda x: x[1], reverse=True)
    print(sort_list)

    all_value = {}
    for v in result_dic.values():
        if v in all_value:
            all_value[v] = all_value.get(v) + 1
        else:
            all_value[v] = 1
    print('Suspiciousness: {0}'.format(sorted(all_value.items(), key=lambda x: x[0], reverse=True)))

    sort_dic = {k: v for k, v in sort_list[:30]}
    fig, ax = plt.subplots()
    ax.bar(sort_dic.keys(), sort_dic.values())
    plt.xlabel('Statement')
    plt.ylabel('Suspiciousness')
    plt.show()


def similarity_measure(failure_testcase_folder, html_folder):
    class_statement_vector, coverage_matrix, result_vector = get_matrix(failure_testcase_folder, html_folder)
    print('coverage_matrix.shape: {0}, coverage_matrix: {1}'.format(coverage_matrix.shape, coverage_matrix))
    print('result_vector.shape: {0}, result_vector: {1}'.format(result_vector.shape, result_vector))

    result_dic = {}
    index = 0
    num_rows = len(coverage_matrix)
    num_cols = len(coverage_matrix[0])
    for col in range(num_cols):
        N_vector = [0, 0, 0, 0]  # [N_cf, N_uf, N_cs, N_us]
        for row in range(num_rows):
            if coverage_matrix[row][col] == result_vector[row] == 1:
                N_vector[0] += 1
            elif coverage_matrix[row][col] == 0 and result_vector[row] == 1:
                N_vector[1] += 1
            elif coverage_matrix[row][col] == 1 and result_vector[row] == 0:
                N_vector[2] += 1
            else:
                N_vector[3] += 1
        result_dic[class_statement_vector[index]] = N_vector
        index += 1
    return result_dic


if __name__ == '__main__':
    failure_testcase_folder_path = ("/home/zmb/project/Fault_Localization/Benchmark-DS/Zookeeper/Experiment/v1"
                                    "/ZK_1419/htmlReport/1.test.FLEPredicateTest")
    html_folder_path = "/home/zmb/project/Fault_Localization/Benchmark-DS/Zookeeper/Experiment/v1/ZK_1419/htmlReport"
    Coefficient(failure_testcase_folder_path, html_folder_path)
