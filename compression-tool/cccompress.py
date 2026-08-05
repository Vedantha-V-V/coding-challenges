from collections import Counter
import sys
import ast
import math
import argparse
from tree import Tree,Heap

parser = argparse.ArgumentParser(
    prog='main',
    description='Accept files for encoding/decoding',
    epilog='file'
)

parser.add_argument('--encode')
parser.add_argument('--decode')

args = parser.parse_args()

def build_tree(heap):
    tmp1 = None
    tmp2 = None
    while(heap.heap_size()>1):
        tmp1 = heap.remove_min()
        tmp2 = heap.remove_min()
        tmp3 = Tree(tmp1.node_weight()+tmp2.node_weight(),None,tmp1.root_node(),tmp2.root_node())
        heap.insert(tmp3)
    return tmp3

def main():
    if(not args.encode and not args.decode):
        print("File not defined")
        exit(1)

    if(args.encode):
        path = args.encode
        try:
            with open(path,'r',encoding='utf-8-sig') as file:
                data = file.read()
        except:
            data = ""
            print("Error in file handling.")

        data = data.strip()
        vocab = dict(Counter(data))
        # vocab = {'C':32,'D':42,'E':120,'K':7,'L':42,'M':24,'U':37,'Z':2}
    else:
        path = args.decode
        try:
            with open(path,'r',encoding='utf-8-sig') as file:
                data = file.read()
        except:
            data = ""
            print("Error in file handling.")

        sections = data.split("\n")
        try:
            vocab = ast.literal_eval(sections[0])
            encoding = sections[1]
        except:
            print("Encoded file not found...")
            exit(1)

    heap_list = []
    for i in vocab.items():
        tree = Tree(i[1],i[0])
        heap_list.append(tree)

    heap = Heap(heap_list,len(heap_list),1000)
    heap.heapify()
    huffman_tree = build_tree(heap)

    if(args.encode):
        codes = huffman_tree.encode()
        for code in codes.items():
            print(f" Character: {code[0]} | Cipher: {code[1]}")
        print("Compression in progress...")
        encoded_text = ""
        for char in data:
            encoded_text += codes[char]

        with open('encoded.txt','w',encoding='utf-8-sig') as file:
            data = f"{vocab}\n"+ encoded_text
            file.write(data)
        print("Compression complete...")
    else:
        print("Decompression in progress...")
        decoded_text = huffman_tree.decode(encoding)
        with open('decoded.txt','w',encoding='utf-8-sig') as file:
            file.write(decoded_text)
        print("Decompression complete...")

if __name__ == "__main__":
    main()