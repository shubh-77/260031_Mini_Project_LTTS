import bmr
import bmi


def test_bmr():
    BMR = bmr.calculate_bmr(70.7, 172.2, 21, "M")
    assert BMR == 1758


def test_bmi():
    BMI = bmi.calculate_bmi(70.7, 172.7)
    assert BMI == 23.704715025402944
