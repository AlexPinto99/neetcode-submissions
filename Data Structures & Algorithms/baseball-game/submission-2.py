class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        k = 0
        for i in range(len(operations)):
            if ord(operations[i][0])==ord("-") or ord("0")<=ord(operations[i][0])<=ord("9"):
                record.append(int(operations[i]))
                k+=1
            elif ord(operations[i])==ord("+") and k>=2:
                record.append((int(record[k-1]) + int(record[k-2])))
                k+=1
            elif ord(operations[i])==ord("D"):
                record.append(int(record[k-1])*2)
                k +=1
            else:
                record.pop()
                k -= 1

        sum = 0
        for i in range(len(record)):
            sum += record[i]

        return sum