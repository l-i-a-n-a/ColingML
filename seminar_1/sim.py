import numpy as np
import re
from collections import Counter
from scipy.spatial.distance import cosine

def main():
    # 1) Привести строки к нижнему регистру
    sents = [sent.lower() for sent in process_sents]
    # 2) Произведите токенизацию (например, с помощью регулярного выражения re.split('[^a-z]', t))
    sents = [re.split('[^a-z]', sent) for sent in sents]
    # 3) Составьте словарь всех уникальных слов, встречающихся в предложениях: каждому слову должен соответствовать
    #    индекс от нуля до (d - 1), где d - размер словаря.
    words = [word for sent in sents for word in sent if word != ""]
    counter = Counter(words)
    # 4) Создайте пустую матрицу размера n x d, где n — число предложений.
    matrix = np.zeros((len(sents), len(counter)))
    # 5) Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен
    #    количеству вхождений j-го слова в i-е предложение.
    for idx, sent in enumerate(sents):
        sent_words = [word for word in sent if word != ""]
        sent_counter = Counter(sent_words)
        sent_vector = [sent_counter[word] for word in counter]
        matrix[idx] = sent_vector
    # 6) Найдите косинусное расстояние от предложения в самой первой строке до всех остальных с помощью функции scipy.spatial.distance.cosine.
    comparison_with_first = [cosine(matrix[0], sent) for sent in matrix]
    result = {process_sent.strip(): number for process_sent, number in zip(process_sents, comparison_with_first)}

    close_sent = sorted(result, key=result.get)
    for sent in close_sent[1:4]:
        print(f'{sent} --- {result[sent]}')



process_sents  = open('sentences.txt').readlines()
main()
