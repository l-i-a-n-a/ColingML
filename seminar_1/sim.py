import numpy as np

# Задание: Дан набор предложений, каждое из которых содержит слово "lead" в разных значениях.
# Необходимо с помощью косинусной близости найти 3 предложения, которые ближе всего к первому в корпусе и вывести их


def main():

    sents = open('sentences.txt').readlines()
    # 1) Привести строки к нижнему регистру
    # 2) Произведите токенизацию (например, с помощью регулярного выражения re.split('[^a-z]', t))
    # 3) Составьте словарь всех уникальных слов, встречающихся в предложениях: каждому слову должен соответствовать
    #    индекс от нуля до (d - 1), где d - размер словаря.
    # 4) Создайте пустую матрицу размера n x d, где n — число предложений.
    # 5) Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен
    #    количеству вхождений j-го слова в i-е предложение.
    # 6) Найдите косинусное расстояние от предложения в самой первой строке до всех остальных с помощью функции scipy.spatial.distance.cosine.

    print() # <-- здесь необходимо вывести 3 ближайших предложения: каждое на своей строчке


if __name__ == '__main__':
    main()