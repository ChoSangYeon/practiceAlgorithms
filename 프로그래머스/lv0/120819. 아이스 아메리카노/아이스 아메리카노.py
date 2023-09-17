def solution(money):
    coffee = money // 5500
    change = money - 5500 * coffee
    return [coffee, change]