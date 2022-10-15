# 1, 3 --> 6
# 3, 3 --> 4
# 2, 3 --> 5
# 3, 5 --> 8

def over_the_road(address, n):

# # sol1
#     return abs(address-(2*n+1))

# # sol2
#     return max((2*n+1)-address, address-(2*n+1))

# # sol3
#     if  (address-(2*n+1))<0:
#         return -((address-(2*n+1)))
#     else:
#         return (address-(2*n+1))

print(over_the_road(1,3))
print(over_the_road(3,3))
print(over_the_road(2,3))
print(over_the_road(3,5))
