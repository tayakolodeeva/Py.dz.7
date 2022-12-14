from computation import Calc_block as c_calc
from logger import result_logger as write_log
import dataTransformation as d_t
import user as c_ui


def button_click():
    j = d_t.data_formatting(c_ui.input_data())
    calc_result = c_calc(j)
    c_ui.view_data(calc_result, 'Результат операции равен:')
    write_log(j, calc_result)

button_click()