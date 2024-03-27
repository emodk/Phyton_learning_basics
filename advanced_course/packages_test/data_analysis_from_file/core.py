def file_to_data_dict(file_path):
    data_as_dict = {}
    try:
        with open(file_path) as f:
            first_line_list = f.readline().split(",")
            first_line_list[-1] = first_line_list[-1].rstrip("\n")
            for line in f:
                new_line_data_list = line.split(",")
                new_line_data_list[-1] = new_line_data_list[-1].rstrip("\n")
                for i in range(len(first_line_list)):
                    key = first_line_list[i]
                    value = new_line_data_list[i]
                    if key not in data_as_dict:
                        data_as_dict[key] = [value]
                    else:
                        data_as_dict[key].append(value)
    except FileNotFoundError:
        print("File or target directory is not found.")
    return data_as_dict


def data_formatting(data_dict):
    data_for_int = ['PrintSubstrates', 'SetUp', 'Rework', 'ScreenChange']
    data_for_float = ['StartWeightBr', 'Value1', 'Value2', 'Value3', 'Value4', 'Value5',
                      'EndWeight', 'Value1End', 'Value2End', 'Value3End', 'Value4End', 'Value5End']
    for key in data_dict.keys():
        # data_type = input(f"data type for {key} (1=txt, 2=int or 3=float):",)
        if key in data_for_int:
            for i in range(len(data_dict[key])):
                data_dict[key][i] = int(data_dict[key][i])
        elif key in data_for_float:
            for i in range(len(data_dict[key])):
                data_dict[key][i] = float(data_dict[key][i])
    return data_dict


def subs_meas_avg(formatted_data_dict):
    subs_weight_avg = []
    data_length = len(formatted_data_dict["Value1"])
    for i in range(data_length):
        total_weight = 0
        subs_counter = 0
        for j in range(1, 6):
            start_weight = formatted_data_dict[f"Value{j}"][i]
            end_weight = formatted_data_dict[f"Value{j}End"][i]
            weight = round(end_weight - start_weight, 4)
            subs_counter += 1
            if weight <= 0:
                subs_counter -= 1
            else:
                total_weight += weight
        if subs_counter != 0:
            avg_weight = round(total_weight / subs_counter, 4)
        else:
            avg_weight = 0
        subs_weight_avg.append(avg_weight)
    return subs_weight_avg


def consumption_by_jar_meas(formatted_data_dict):
    data_length = len(formatted_data_dict["StartWeightBr"])
    weight = 0
    jar_weight_consume = []
    for i in range(data_length):
        start_jar_weight = formatted_data_dict["StartWeightBr"][i]
        end_jar_weight = formatted_data_dict["EndWeight"][i]
        if start_jar_weight != 0 and end_jar_weight != 0:
            weight = round(start_jar_weight - end_jar_weight, 4)
        elif start_jar_weight <= 0.01:
            start_jar_weight = formatted_data_dict["StartWeightBr"][i - 1]
            weight = round((start_jar_weight - end_jar_weight) / 2, 4)
        elif end_jar_weight <= 0.01:
            end_jar_weight = formatted_data_dict["EndWeight"][i + 1]
            weight = round((start_jar_weight - end_jar_weight) / 2, 4)
        if weight < 0:
            weight = 0
        jar_weight_consume.append(weight)
    return jar_weight_consume


def data_dict_to_file_report(reported_data_dict, data_length, working_dir):
    file_name = input("Please insert the report file name (w/t extension):",)
    file_line_data = []
    with open(f"{working_dir}{chr(92)}{file_name}.csv", "a") as fr:
        for key in reported_data_dict.keys():
            file_line_data.append(key)
            reported_data_dict[key] = numeric_to_string_conv(reported_data_dict[key])
        file_line = ",".join(file_line_data)
        fr.write(f"{file_line}\n")
        for i in range(data_length):
            file_line_data = []
            for key in reported_data_dict.keys():
                file_line_data.append(reported_data_dict[key][i])
            file_line = ",".join(file_line_data)
            fr.write(f"{file_line}\n")


def real_and_bonus_consumption_per_subs(jar_consume, printed_substrates, reworked_subs, set_up_subs):
    data_length = len(jar_consume)
    real_cons_per_subs = []
    bonus_cons_per_subs = []
    real_bonus_data = {}
    for i in range(data_length):
        subs_weight_real = round(jar_consume[i] / printed_substrates[i], 4)
        subs_weight_bonus = round(jar_consume[i] / (printed_substrates[i] + reworked_subs[i] + set_up_subs[i]), 4)
        real_cons_per_subs.append(subs_weight_real)
        bonus_cons_per_subs.append(subs_weight_bonus)
    real_bonus_data["real_cons_per_subs"] = real_cons_per_subs
    real_bonus_data["bonus_cons_per_subs"] = bonus_cons_per_subs
    return real_bonus_data


def numeric_to_string_conv(data):
    for i in range(len(data)):
        data[i] = str(data[i])
    return data
