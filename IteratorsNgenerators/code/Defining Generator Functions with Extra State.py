from collections import deque

class linehistory:
    def __init__(self, lines, hist_len = 3):
        self.lines = lines
        self.history = deque(maxlen=hist_len)

    def __iter__(self):
        for lineno, line in enumerate(self.lines,1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

if  __name__ == '__main__':
    with open('sample txts/Lorem.txt') as f:
        lines = linehistory(f)
        for line in lines:
            if  'Donec' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno,hline),end= '')
                lines.history = deque(maxlen= 1)