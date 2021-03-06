
# "t>df>h>f>af" 正序 gamma = 1
positive_phase_sequence = [
    "t>df",
    "df>h",
    "h>f",
    "h>af",
    "f>af",
    "f>t",
    "af>t"
]

# "t>af>f>h>df" 逆序 gamma = -1
negative_phase_sequence = [
    "t>af",
    "t>f",
    "af>f",
    "af>h",
    "f>h",
    "h>df",
    "df>t"
]

# 部件符號對照表
symbol_table = {
    'analfin': 'af',
    'dorsalfin': 'df',
    'fin': 'f',
    'eye': 'h',
    'mouth': 'h',
    'head': 'h',
    'tail': 't',
}

# 狀態對照表 向量對照正異常姿態
state_table = {
    '[0.0, 1.0, 1]': 'abnormal',
    '[0.0, 1.0, -1]': 'abnormal',
    '[0.707, 0.707, 1]': 'normal',
    '[-0.707, 0.707, -1]': 'normal',
    '[1.0, 0.0, 1]': 'normal',
    '[-1.0, 0.0, -1]': 'normal',
    '[0.707, -0.707, 1]': 'normal',
    '[-0.707, -0.707, -1]': 'normal',
    '[0.0, -1.0, 1]': 'abnormal',
    '[0.0, -1.0, -1]': 'abnormal',
    '[-0.707, -0.707, 1]': 'abnormal',
    '[0.707, -0.707, -1]': 'abnormal',
    '[-1.0, 0.0, 1]': 'abnormal',
    '[1.0, 0.0, -1]': 'abnormal',
    '[-0.707, 0.707, 1]': 'abnormal',
    '[0.707, 0.707, -1]': 'abnormal',
}

# 向量與2 digit對照表
digital_table = {
    '[0.0, 1.0, 1.0]': 11,
    '[0.0, 1.0, -1.0]': 10,
    '[0.707, 0.707, 1.0]': 21,
    '[-0.707, 0.707, -1.0]': 20,
    '[1.0, 0.0, 1.0]': 31,
    '[-1.0, 0.0, -1.0]': 30,
    '[0.707, -0.707, 1.0]': 41,
    '[-0.707, -0.707, -1.0]': 40,
    '[0.0, -1.0, 1.0]': 51,
    '[0.0, -1.0, -1.0]': 50,
    '[-0.707, -0.707, 1.0]': 61,
    '[0.707, -0.707, -1.0]': 60,
    '[-1.0, 0.0, 1.0]': 71,
    '[1.0, 0.0, -1.0]': 70,
    '[-0.707, 0.707, 1.0]': 81,
    '[0.707, 0.707, -1.0]': 80,
    '[0, 0, 0]': 00,
    '[0.0, 0.0, 0.0]': 00
}

# 2 digit與向量對照表
vector_table = {
    '11': [0.0, 1.0, 1],
    '10': [0.0, 1.0, -1],
    '21': [0.707, 0.707, 1],
    '20': [-0.707, 0.707, -1],
    '31': [1.0, 0.0, 1],
    '30': [-1.0, 0.0, -1],
    '41': [0.707, -0.707, 1],
    '40': [-0.707, -0.707, -1],
    '51': [0.0, -1.0, 1],
    '50': [0.0, -1.0, -1],
    '61': [-0.707, -0.707, 1],
    '60': [0.707, -0.707, -1],
    '71': [-1.0, 0.0, 1],
    '70': [1.0, 0.0, -1],
    '81': [-0.707, 0.707, 1],
    '80': [0.707, 0.707, -1]
}

# 2 digit與向量對照表01 多了0
vector_table01 = {
    '11': [0.0, 1.0, 1],
    '10': [0.0, 1.0, -1],
    '21': [0.707, 0.707, 1],
    '20': [-0.707, 0.707, -1],
    '31': [1.0, 0.0, 1],
    '30': [-1.0, 0.0, -1],
    '41': [0.707, -0.707, 1],
    '40': [-0.707, -0.707, -1],
    '51': [0.0, -1.0, 1],
    '50': [0.0, -1.0, -1],
    '61': [-0.707, -0.707, 1],
    '60': [0.707, -0.707, -1],
    '71': [-1.0, 0.0, 1],
    '70': [1.0, 0.0, -1],
    '81': [-0.707, 0.707, 1],
    '80': [0.707, 0.707, -1],
    '0': [0, 0, 0]
}

# 異常模板
abnormal_template = [
    [31, 41, 60, 70, 80, 21],
    [41, 60, 70, 80, 41],
    [30, 40, 61, 71, 81, 20, 30],
    [40, 61, 71, 81, 40],
    [70, 31, 70],
    [71, 30, 71],
    [51, 61, 71, 30],
    [50, 60, 70, 31],
    [31, 41, 60, 41],
    [30, 40, 61, 40],
    [41, 51, 41, 31],
    [40, 50, 40, 30],
    [41, 51, 10, 20, 30],
    [40, 50, 11, 21, 31],
    [31, 41, 51, 41, 31],
    [30, 40, 50, 40, 30],
    [31, 41, 51, 31, 41, 40, 30],
    [30, 40, 50, 30, 40, 41, 31],
    [51, 41, 31],
    [50, 40, 30],
    [11],
    [10],
    [51],
    [50],
    [61],
    [60],
    [71],
    [70],
    [81],
    [80],
    [31, 41, 51, 10, 20, 30]
]

# 異常模板代表意義
abnormal_meaning = {
    "[31, 41, 60, 70, 80, 21]": "weird swimming",
    "[41, 60, 70, 80, 41]": "dying",
    "[30, 40, 61, 71, 81, 20, 30]": "weird swimming",
    "[40, 61, 71, 81, 40]": "dying",
    "[70, 31, 70]": "exhausted",
    "[71, 30, 71]": "exhausted",
    "[51, 61, 71, 30]": "weird swimming",
    "[50, 60, 70, 31]": "weird swimming",
    "[31, 41, 60, 41]": "weird swimming",
    "[30, 40, 61, 40]": "weird swimming",
    "[41, 51, 41, 31]": "weird swimming",
    "[40, 50, 40, 30]": "weird swimming",
    "[41, 51, 10, 20, 30]": "weird swimming",
    "[40, 50, 11, 21, 31]": "weird swimming",
    "[31, 41, 51, 41, 31]": "weird swimming",
    "[30, 40, 50, 40, 30]": "weird swimming",
    "[31, 41, 51, 31, 41, 40, 30]": "weird swimming",
    "[30, 40, 50, 30, 40, 41, 31]": "weird swimming",
    "[51, 41, 31]": "weird swimming",
    "[50, 40, 30]": "weird swimming"
}

# 異常模板代表意義01
abnormal_meaning01 = {
    "0": "weird swimming",
    "1": "dying",
    "2": "weird swimming",
    "3": "dying",
    "4": "exhausted",
    "5": "exhausted",
    "6": "weird swimming",
    "7": "weird swimming",
    "8": "weird swimming",
    "9": "weird swimming",
    "10": "weird swimming",
    "11": "weird swimming",
    "12": "weird swimming",
    "13": "weird swimming",
    "14": "weird swimming",
    "15": "weird swimming",
    "16": "weird swimming",
    "17": "weird swimming",
    "18": "weird swimming",
    "19": "weird swimming"
}

# 正常模板
normal_template = [
    [30, 40, 30, 20],
    [31, 41, 31, 21],
    [30, 20, 30],
    [31, 21, 31],
    [30, 40, 30],
    [31, 41, 31],
    [40, 30, 20, 30],
    [41, 31, 21, 31],
    [20, 30, 40, 30],
    [21, 31, 41, 31],
    [21],
    [20],
    [31],
    [30],
    [41],
    [40]
]

# 正常模板01 多0
normal_template01 = [
    [30, 40, 30, 20],
    [31, 41, 31, 21],
    [30, 20, 30],
    [31, 21, 31],
    [30, 40, 30],
    [31, 41, 31],
    [40, 30, 20, 30],
    [41, 31, 21, 31],
    [20, 30, 40, 30],
    [21, 31, 41, 31],
    [21],
    [20],
    [31],
    [30],
    [41],
    [40],
    [0]
]
