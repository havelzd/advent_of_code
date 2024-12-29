import sys


args = sys.argv

p1 = 0
p2 = 0


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


# secret = 123
# for _ in range(10):
#     secret = prune(mix(secret, (secret * 64)))
#     secret = prune(mix(secret, int(secret / 32)))
#     secret = prune(mix(secret, (secret * 2048)))
#
#     print(secret)

seq_counts = []
with open(sys.argv[1]) as f:
    secrets = [x.strip() for x in f.readlines()]
for secret in secrets:
    s = secret
    price = s[-1]
    price = int(price)
    s = int(secret)
    seq = []
    price_counts = {}
    for i in range(2001):
        s = prune(mix(s, (s * 64)))
        s = prune(mix(s, int(s / 32)))
        s = prune(mix(s, (s * 2048)))
        p1 += s
        curr_price = str(s)[-1]
        curr_price = int(curr_price)
        price_diff = curr_price - price
        seq.append(price_diff)
        seq = seq[-4:]
        if i >= 3:
            key_hash = hash("".join(map(str, seq)))
            if key_hash in price_counts:
                continue
            price_counts[key_hash] = max(
                price_counts.get(key_hash, 0), curr_price)

        price = curr_price
    seq_counts.append(price_counts)

print(p1)

# find key with max sum of values accros seq_counts
max_key = ""
max_sum = 0
result_dict = {}
for dic in seq_counts:
    for key, value in dic.items():
        result_dict[key] = result_dict.get(key, 0) + value
        if result_dict[key] > max_sum:
            max_sum = result_dict[key]
            max_key = key

print(max_key, max_sum)
