def crc(data, poly):
    ones = poly.count('1')
    data = list(data + ('0' * ones))

    for i in range(len(data) - ones):
        if data[i] == '1':
            for j, bit in enumerate(poly):
                data[i+j] = str(int(bit) ^ int(data[i+j]))
    return ''.join(data[-ones:])


if __name__ == '__main__':
    assert crc('11010011101100', '1011') == '100'
