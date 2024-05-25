import pandas as pd
import numpy as np


chat_id = 5105487223 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Расчет среднего значения и стандартного отклонения для каждой выборки
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    std_x = np.std(x, ddof=1)
    std_y = np.std(y, ddof=1)
    
    # Расчет размеров выборок
    n_x = len(x)
    n_y = len(y)
    
    # Расчет t-статистики и степеней свободы по формуле Уэлча
    t_stat = (mean_x - mean_y) / np.sqrt(std_x**2 / n_x + std_y**2 / n_y)
    df = (std_x**2 / n_x + std_y**2 / n_y)**2 / (std_x**4 / (n_x**2 * (n_x - 1)) + std_y**4 / (n_y**2 * (n_y - 1)))
    
    # Расчет p-значения для двустороннего теста
    p_value = 2 * (1 - t.cdf(abs(t_stat), df))
    
    # Проверка статистической значимости на уровне 0.07
    if p_value < 0.07:
        return True  # Отклонить нулевую гипотезу
    else:
        return False  # Не отклонять нулевую гипотезу
