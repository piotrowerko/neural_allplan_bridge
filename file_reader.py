class AllBrGen():
    def __init__(self, label) -> None:
        self.name = label
    
    def __str__(self) -> str:
        return f'bridge class label: {self.name}'
    
    def generate_tcl(self, filepath, filepath2, raw, phrase, phrase2):
        """changes one raw with arbitrary raw and phrase
        and creates new tcl file"""
        with open(filepath) as file_object:
            data = file_object.readlines()
            _data = data[raw].replace(phrase, phrase2, 1)
            new_data = data[:raw] + [_data] + data[raw+1:]
        with open(filepath2, "w") as file_object:
            file_object.writelines(new_data)

    # def generate_tcl__(self, filepath, 
    #                    filepath2, 
    #                    first_raw_no,
    #                    input_string, 
    #                    skew_reach, 
    #                    angle_change):
    #     angle_from_str = float(input_string[10:15])
    #     new_init_angle = angle_from_str - angle_change
    #     old_bottom_angle, old_angle_step = self._angle_step_bottom_angle(angle_from_str, skew_reach)
    #     new_bottom_angle, new_angle_step = self._angle_step_bottom_angle(new_init_angle, skew_reach)
    #     with open(filepath) as file_object:
    #         data = file_object.readlines()
    #         _data = []
    #         new_angle = 0.0
    #         for raw in range(first_raw_no, first_raw_no + skew_reach, 1):
    #             if raw == first_raw_no:
    #                 new_angle = new_init_angle
    #                 old_angle = angle_from_str
    #             else:
    #                 new_angle -= new_angle_step
    #                 old_angle -= old_angle_step
    #             my_new_str = f'{input_string[:10]}{str(new_angle)}'
    #             my_old_str = f'{input_string[:10]}{str(old_angle)}'
    #             _data.append(data[raw].replace(my_old_str, my_new_str, 1))
    #             pp = 1
    #         new_data = data[:first_raw_no] + _data + data[first_raw_no + skew_reach+1:]
    #         kk = 1
    #     with open(filepath2, "w") as file_object2:
    #         file_object2.writelines(new_data)
            
    def generate_tcl__88(self, filepath, 
                       filepath2, 
                       opposite,
                       first_raw_no,
                       input_string, 
                       skew_reach, 
                       angle_change,
                       fan):
        if opposite:
            counter = -1
        else:
            counter = 1
        angle_from_str = float(input_string[10:15])
        new_init_angle = angle_from_str - angle_change
        if fan:
            old_bottom_angle, old_angle_step = self._angle_step_bottom_angle(angle_from_str, skew_reach)
            new_bottom_angle, new_angle_step = self._angle_step_bottom_angle(new_init_angle, skew_reach)
        else:
            old_angle_step = 0
            new_angle_step = 0
        with open(filepath) as file_object:
            data = file_object.readlines()
            _data = []
            new_angle = 0.0
            for raw in range(first_raw_no, first_raw_no + skew_reach, counter):
                if raw == first_raw_no:
                    new_angle = new_init_angle
                    old_angle = angle_from_str
                else:
                    new_angle -= new_angle_step
                    old_angle -= old_angle_step
                my_new_str = f'{input_string[:10]}{str(new_angle)}'
                my_old_str = f'{input_string[:10]}{str(old_angle)}'
                _data.append(data[raw].replace(my_old_str, my_new_str, 1))
            if opposite:
                _data = _data[::-1]
                new_data = data[:(first_raw_no + skew_reach + 1)] + _data + data[first_raw_no + 1:]
            else:
                new_data = data[:first_raw_no] + _data + data[first_raw_no + skew_reach:]
        with open(filepath2, "w") as file_object2:
            file_object2.writelines(new_data)

    def _angle_step_bottom_angle(self, angle, reach):
        """returns bottom angle and angle step"""
        if angle >= 30:
            bottom_angle = 15
        elif 30 > angle >= 20:
            bottom_angle = 5.0
        elif 20 > angle >= 10:
            bottom_angle = 3.0
        else:
            bottom_angle = 1.0
        angle_step = (angle - bottom_angle) / (abs(reach) - 1)
        return bottom_angle, angle_step


def main():
    model_group1 = AllBrGen('double_gird_pt_bridges')
    print(model_group1)
    starting_angle = 30
    step = -1
    
    for i in range(starting_angle-1, -31, step):
        input_string = f'ZROTATE   {str(i+1)}'
        previous_name = f'angle_{i+1}.tcl'
        file_name = f'angle_{i}.tcl'
        gen_tcl = model_group1.generate_tcl__88(previous_name, 
                                                file_name, 
                                                False,
                                                862, 
                                                input_string, 
                                                1,
                                                -step,
                                                False)

        gen_tcl_mid = model_group1.generate_tcl__88(file_name, 
                                                    file_name, 
                                                    False,
                                                    864, 
                                                    input_string, 
                                                    1,
                                                    -step,
                                                    False)

        gen_tcl_back = model_group1.generate_tcl__88(file_name, 
                                                    file_name, 
                                                    True,
                                                    866, 
                                                    input_string, 
                                                    -1,
                                                    -step,
                                                    False)

if __name__ == '__main__':
    main()