import heapq

class HuffNode:
    def __init__(self, symbol=None, count=None):
        self.symbol = symbol
        self.count = count
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.count < other.count

def count_characters(text):
    char_map = {}
    for char in text:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 0
    return char_map
    
def build_tree(characters):
    huff_tree = []
    for char in characters:
        huff_tree.append(HuffNode(char, characters[char]))

    heapq.heapify(huff_tree)
    while len(huff_tree) > 1:
        left_node = heapq.heappop(huff_tree)
        right_node = heapq.heappop(huff_tree)
        merged_node = HuffNode(count=left_node.count + right_node.count)
        merged_node.left = left_node
        merged_node.right = right_node
        heapq.heappush(huff_tree, merged_node)
    
    return huff_tree[0]

def generate_codes(huffNode, code="", huff_codes={}):
    if huffNode:
        if huffNode.symbol:
            huff_codes[huffNode.symbol] = code
        generate_codes(huffNode.left, code + "0", huff_codes)
        generate_codes(huffNode.right, code + "1", huff_codes)
    return huff_codes


text = "This is a series of characters to be encoded via the Huffman compression algorithm"

map = count_characters(text)
huff_tree = build_tree(map)
huff_codes = generate_codes(huff_tree)

print(huff_codes)