"""
Скрипт, определяющий по последовательности, что произойдет с оценкой под видео,
если последовательно будут произведены действия like или dislike.

Примеры:

>>> like_dislike(['like', 'like'])
'nothing'

>>> like_dislike(['dislike', 'like'])
'like'


"""


from typing import Sequence


def like_dislike(sequence :Sequence) -> str:
    if any([0 if part in ['like', 'dislike', 'nothing'] else 1 for part in sequence]):
        return 'invalid sequence'
    result = 'nothing'
    count = 0
    for seq in sequence:
        if result == seq and not count%2:
            result = 'nothing'
            count += 1
        else:
            result = seq
            count += 1
    return result


if __name__ == "__main__":
    data = [
        ['like', 'dislike'],
        ['nothing', 'like', 'like'],
        ['like', 'like', 'like'],
        ['like', 'like', 'like', 'like'],
        ['like', 'dislike', 'like']]
    results = ['dislike', 'nothing', 'nothing', 'like']
    for dt, rs in zip(data, results):
        assert like_dislike(dt) == rs
