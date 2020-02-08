input_num = int(input("Please enter the number of inputs: "))
inputs = list()
outputs = list()

for _ in range(input_num):
    input_name = input("Please enter the names: ")
    inputs.append(input_name)
    print('Input: ')
    print(inputs)

for i in range(len(outputs)):
    curr=0
    nextt=curr+1
    while curr<len(outputs)-1:
        if outputs[curr]>outputs[nextt]:
            outputs[curr],outputs[nextt] = outputs[nextt],outputs[curr]
            curr += 1
        elif len(outputs[curr]) == len(outputs[nextt]):
            if outputs[curr] > outputs[nextt]:
                outputs[curr],outputs[nextt]=outputs[nextt],outputs[curr]
            curr += 1
        else: 
            break

for i in inputs:
    names= ""
    for j in range(len(i)):
        if i[j].isupper():
            names+=i[j]
    outputs.append(names)

print('Output: ')
print(outputs)
        


        




