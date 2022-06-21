class AllBrGen():
    def __init__(self, label) -> None:
        self.name = label
    
    def __str__(self) -> str:
        return f'bridge class label: {self.name}'
    
    def generate_tcl(self, filepath, filepath2, raw, phrase, phrase2):
        with open(filepath) as file_object:
            data = file_object.readlines()
            _data = data[raw].replace(phrase, phrase2, 1)
            new_data = data[:raw] + [_data] + data[raw+1:]
        with open(filepath2, "w") as file_object:
            file_object.writelines(new_data)

def main():
    model_group1 = AllBrGen('double_gird_pt_bridges')
    gen_tcl = model_group1.generate_tcl('dd.tcl', 
                                        'eee.tcl', 
                                        763, 
                                        'ZROTATE   20', 
                                        'ZROTATE   30')

if __name__ == '__main__':
    main()