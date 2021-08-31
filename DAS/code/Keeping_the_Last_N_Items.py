from collections import deque

def search (lines, pattern , history = 5):
    # Using deque(maxlen=N) creates a fixed-sized queue
    # When new items are added and the queue is full, the oldest item is automatically removed
    prvious_lines  = deque(maxlen=history) 
    for line in lines:
        if pattern in line:
            yield line, prvious_lines
        prvious_lines.append(line)

if __name__ == '__main__':
    with open('sample txts/Lorem.txt') as f:
        for line, prev_line in search(f,'dolor',5):
            for pline in prev_line:
                print(pline,end='-')
            print(line)
            print('_'*100)

