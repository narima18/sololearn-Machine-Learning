tp, fp, fn, tn = [int(x) for x in input().split()]
total = tp+ fp+ fn+ tn
accuracy = (tp + tn )/(total) 
precision = tp/ (tp+fp)
recall = tp/ (tp+fn)
f1 = round(1/(((1/precision) + (1/recall)) / 2), 4)
print(round(accuracy, 4))
print(round(precision, 4))
print(round(recall, 4))
print(f1)
