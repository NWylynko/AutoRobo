def arrayOf16ToMatrix4by4(array):
  # function that converts array that have size of 16 to matrix that shape of 4x4
    mat = []
    for i in range(4):
        raw = []
        for j in range(4):
            k = i * 4 + j
            elm = array[k]
            raw.append(elm)
        mat.append(raw)
    return mat

def logToFile(data):
    f = open("data/" + str(time.time()) + ".json", "a")
    f.write(data)
    f.close()