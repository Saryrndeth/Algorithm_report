from anytree import Node, RenderTree


def gen_freq_dict(f) -> dict:
    line = f.readline()
    f.close()
    temp_dict = dict()
    while line:
        temp_dict[line[0]] = line.count(line[0])
        line = line.replace(line[0], '')
    return dict(sorted(temp_dict.items(), key=lambda x: x[1]))


def gen_binary_huffman_tree(freq_dict: dict) -> Node:
    temp_dict = {i: Node(i, freq=freq_dict[i], isfreq=False) for i in freq_dict.keys()}
    print(temp_dict)
    while len(temp_dict) != 1:
        keys = list(temp_dict.keys())
        temp_dict[f"freq {temp_dict[keys[0]].freq + temp_dict[keys[1]].freq}"] = Node(f"freq {temp_dict[keys[0]].freq + temp_dict[keys[1]].freq}", freq=temp_dict[keys[0]].freq + temp_dict[keys[1]].freq)
        keys = list(temp_dict.keys())
        temp_dict[keys[-1]].isfreq = True
        temp_dict[keys[0]].id = 0
        temp_dict[keys[1]].id = 1
        temp_dict[keys[0]].parent = temp_dict[keys[-1]]
        temp_dict[keys[1]].parent = temp_dict[keys[-1]]
        temp_dict.pop(keys[0])
        temp_dict.pop(keys[1])
        temp_dict = (
            dict(sorted(temp_dict.items(), key=lambda x: x[1].freq)))
        print(temp_dict)

    return temp_dict[list(temp_dict.keys())[0]]


def gen_huffman_final_dict(root: Node) -> dict:
    huffman_final_dict = dict()
    for pre, fill, node in RenderTree(root):
        if not node.isfreq:
            string = ""
            for n in node.path:
                if n.id != -1:
                    string += str(n.id)
            huffman_final_dict[node.name] = string
    return huffman_final_dict


freq_dict: dict = gen_freq_dict(open("C:/Users/Saryrn/Documents/Study/Algorithm-test/test.txt"))
print(freq_dict)
root: Node = gen_binary_huffman_tree(freq_dict)
root.id, root.isfreq = -1, -1

for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}: {node.freq}")

print(gen_huffman_final_dict(root))




