import numpy as np

one_d=np.array([1,2,3])
two_d=np.array([[1,2,3],[4,5,6],[7,8,9]])
three_d=np.array(
    [
    [[1,2],[3,4],[5,6]],
    [[1,2],[3,4],[5,6]],
    [[1,2],[3,4],[5,6]]
    ]
)
changed=one_d.reshape(3,1)
shape=np.flip(changed)
add=changed*shape
back_to_one= add.flatten().max()
# print(back_to_one)
# print(three_d.size)
print(two_d.shape)