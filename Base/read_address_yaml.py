import os

import yaml


class ReadAddressYaml():
    def __init__(self, filename):
        self.filepath = os.getcwd() + os.sep + "Data" + os.sep + filename

    def read_address_yaml02(self):
        with open(self.filepath, "r", encoding="utf-8")as f:
            return yaml.load(f)


    def read_address_yaml(self):
        with open("../Data/address.yaml", "r", encoding="utf-8")as f:
            return yaml.load(f)

if __name__ == '__main__':
    datas = ReadAddressYaml("address.yaml").read_address_yaml()
    print(datas)
    arrs = []
    for data in datas.get("add_address").values():
        arrs.append((data.get("receipt_name"), data.get("add_phone"), data.get("sheng"),data.get("shi"), data.get("qu"), data.get("detail_addr"), data.get("post_code")))
    print(arrs)
