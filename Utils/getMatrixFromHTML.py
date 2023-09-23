import os
import numpy as np
from bs4 import BeautifulSoup
from Utils.getSuspiciousClasses import get_suspicious_classes


def get_matrix(html_folder, failure_testcase_num):
    coverage_matrix = np.array([])
    class_statement_vector = []
    input_title = False
    result_vector = np.array([])
    suspicious_classes = get_suspicious_classes(html_folder, failure_testcase_num)
    print('suspicious_classes: {0}'.format(suspicious_classes))
    testcase_dirs = os.listdir(html_folder)
    for t in testcase_dirs:
        value = 0
        for n in range(1, failure_testcase_num + 1):
            if t.startswith('{0}.'.format(n)):
                value = 1
        result_vector = np.append(result_vector, value)

        print(result_vector)
        vector_classes = np.array([])
        for k, v in suspicious_classes.items():
            html_path = html_folder + os.sep + t + os.sep + v
            print("=============================================")
            print('html_path: {0}'.format(html_path))
            vector = get_vector(html_path)
            if not input_title:
                for i in range(1, vector.size + 1):
                    class_statement_vector.append('{0}.{1}'.format(k, i))
                    coverage_matrix = np.append(coverage_matrix, -1)
            vector_classes = np.append(vector_classes, vector)
        input_title = True
        coverage_matrix = np.row_stack((coverage_matrix, vector_classes))
    coverage_matrix = np.delete(coverage_matrix, 0, 0)
    return class_statement_vector, coverage_matrix, result_vector


def get_vector(path):
    file_html = open(path, "r")
    html = file_html.read()
    soup = BeautifulSoup(html, 'html.parser')
    code = soup.find('code')
    b_fc = code.find_all('b', class_='fc')
    b_nc = code.find_all('b', class_='nc')
    b = code.find_all('b')
    vec = np.array([])
    print('Number of statements：{0}， Covered：{1}， Not covered：{2}'.format(len(b), len(b_fc), len(b_nc)))
    for line in b:
        if line.get('class') == ['fc']:
            vec = np.append(vec, 1)
        else:
            vec = np.append(vec, 0)
    return vec


if __name__ == '__main__':
    html_folder_path = "/home/zmb/project/Fault_Localization/Benchmark-DS/Zookeeper/Experiment/v1/ZK_1412/htmlReport"
    failure_testcase_num = 3
    get_matrix(html_folder_path, failure_testcase_num)