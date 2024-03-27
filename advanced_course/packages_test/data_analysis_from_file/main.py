from core import file_to_data_dict as ftd, data_formatting, subs_meas_avg as sma
from core import consumption_by_jar_meas as cmj, real_and_bonus_consumption_per_subs as rb
from core import data_dict_to_file_report as fr

report_dict = {}
working_dir = input("Please, insert your working dir path:")
file = input("Please, insert your *.csv data file name:",)
file_path = f"{working_dir}{chr(92)}{file}"
data = ftd(file_path)
formatted_data = data_formatting(data)
report_dict["Operator"] = formatted_data["Operator"]
subs_meas_avg = sma(formatted_data)
report_dict["Subs meas avg"] = subs_meas_avg
jar_consumption = cmj(formatted_data)
report_dict["Consumption by jar"] = jar_consumption
real_bonus_consumption = rb(jar_consumption, formatted_data["PrintSubstrates"], formatted_data["Rework"],
                            formatted_data["SetUp"])
report_dict.update(real_bonus_consumption)
data_length = len(jar_consumption)
fr(report_dict, data_length, working_dir)
