import os
from bs4 import BeautifulSoup


def get_suspicious_classes(folder_path):
    classes = {}
    dirs = os.listdir(folder_path)
    target_dirs = []
    for d in dirs:
        if d.startswith("ns-"):
            target_dirs.append(d)
    target_dirs.sort()

    for t in target_dirs:
        html_path = folder_path + os.sep + t + os.sep + "index.html"
        file_html = open(html_path, "r")
        html = file_html.read()
        soup = BeautifulSoup(html, 'html.parser')
        print("=============================================")
        print('HTML： {0}'.format(html_path))
        tr = soup.find('body').find_all('tr')
        tr.pop(0)
        td = tr[0].find_all('td')
        class_name = td[0].text
        print('Class: {0}'.format(class_name))
        class_coverage = td[1].find('span').text.replace(' ', '').replace('\n', '')
        if class_coverage != '0%':
            for i in range(2, len(tr) - 1):
                if tr[i].find_all('td')[1].find('span').text.replace(' ', '').replace('\n', '') != '0%':
                    key = '{0}.{1}'.format(class_name, tr[i].find_all('td')[0].text)
                    value = '{0}/{1}'.format(t, tr[i].find_all('td')[0].find('a').get('href'))
                    print(key)
                    print(value)
                    classes[key] = value
                else:
                    continue
        else:
            continue
    return classes


if __name__ == '__main__':
    test_failure_testcase_folder_path = ("/home/zmb/project/Fault_Localization/Benchmark-DS/Zookeeper/Experiment/v1"
                                         "/ZK_1419/htmlReport/1.test.FLEPredicateTest")
    result = get_suspicious_classes(test_failure_testcase_folder_path)
    print('Suspicious Classes: {0}'.format(result))