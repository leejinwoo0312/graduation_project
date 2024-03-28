from py3dbp import Packer, Bin, Item, Painter
packer_box1 = Packer()
packer_box2 = Packer()

box1 = Bin('Bin-1',(5,3,5),100,0,0)
box2 = Bin('Bin-2',(5,3,5),100,0,0)

packer_box1.addBin(box1)
packer_box2.addBin(box2)

item1 = Item('1','item1','cube',(1,1,1),1,1,100,True,'blue')
item2 = Item('2','item2','cube',(3,3,3),1,1,100,True,'blue')
item3 = Item('3','item3','cube',(2,2,2),1,1,100,True,'blue')
item4 = Item('4','item4','cube',(2,2,2),1,1,100,True,'blue')
item5 = Item('5','item5','cube',(2,2,1),1,1,100,True,'blue')
item6 = Item('6','item6','cube',(1,3,2),1,1,100,True,'blue')
item7 = Item('7','item7','cube',(1,2,2),1,1,100,True,'blue')
item8 = Item('8','item8','cube',(2,2,1),1,1,100,True,'blue')
item9 = Item('9','item9','cube',(2,2,1),1,1,100,True,'blue')
item10 = Item('10','item10','cube',(2,2,2),1,1,100,True,'blue')

packer_box1.addItem(item1)
packer_box1.addItem(item2)
packer_box1.addItem(item3)
packer_box1.addItem(item4)
packer_box1.addItem(item5)
packer_box1.addItem(item6)
packer_box1.addItem(item7)
packer_box1.addItem(item8)
packer_box1.addItem(item9)
packer_box1.addItem(item10)

packer_box1.pack(
    bigger_first=True,
    distribute_items=True,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.8,
    number_of_decimals=0
)

container1 = packer_box1.bins[0]
painter1 = Painter(container1)
fig1 = painter1.plotBoxAndItems(
    title='container 1',
    alpha=0.8,
    write_num=False,
    fontsize=10
)

fig1.show()

item11 = Item('11','item1','cube',(1,1,1),1,1,100,True,'green')
item12 = Item('12','item2','cube',(3,3,3),1,1,100,True,'green')
item13 = Item('13','item3','cube',(2,2,2),1,1,100,True,'green')
item14 = Item('14','item4','cube',(2,2,2),1,1,100,True,'green')
item15 = Item('15','item5','cube',(2,2,1),1,1,100,True,'green')
item16 = Item('16','item6','cube',(1,3,2),1,1,100,True,'green')
item17 = Item('17','item7','cube',(1,2,2),1,1,100,True,'green')
item18 = Item('18','item8','cube',(2,2,1),1,1,100,True,'green')
item19 = Item('19','item9','cube',(2,2,1),1,1,100,True,'green')
item20 = Item('20','item10','cube',(2,2,2),1,1,100,True,'green')

packer_box2.addItem(item11)
packer_box2.addItem(item12)
packer_box2.addItem(item13)
packer_box2.addItem(item14)
packer_box2.addItem(item15)
packer_box2.addItem(item16)
packer_box2.addItem(item17)
packer_box2.addItem(item18)
packer_box2.addItem(item19)
packer_box2.addItem(item20)

packer_box2.pack(
    bigger_first=True,
    distribute_items=True,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.8,
    number_of_decimals=0
)

container2 = packer_box2.bins[0]
painter2 = Painter(container2)
fig2 = painter2.plotBoxAndItems(
    title='container 2',
    alpha=0.8,
    write_num=False,
    fontsize=10
)

fig2.show()
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 시각화 함수 정의
def plot_container(ax, container, offset_x=0, container_title="Container", item_color='blue'):
    ax.set_title(container_title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 컨테이너 내의 항목들을 플로팅
    for item in container.items:
        # 항목의 크기와 위치를 가져옵니다
        width, depth, height = item.getDimension()
        x, y, z = item.position
        x += offset_x  # X축으로의 이동 적용
        
        # 항목을 3D 상자로 플로팅
        ax.bar3d(x, y, z, width, depth, height, color=item_color, alpha=0.8,)

# 새로운 그림 생성
fig = plt.figure(figsize=(14, 7))

# 컨테이너 1에 대한 서브플롯
ax1 = fig.add_subplot(121, projection='3d')
plot_container(ax1, packer_box1.bins[0], 0, "Container 1", 'blue')

# 컨테이너 2에 대한 서브플롯, X축으로 5단위만큼 이동
ax2 = fig.add_subplot(122, projection='3d', sharey=ax1, sharez=ax1)
plot_container(ax2, packer_box2.bins[0], 5, "Container 2", 'green')

plt.tight_layout()
plt.show()


'''


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def plot_container_combined(ax, container1, container2, offset_x=5, container1_title="Container 1", container2_title="Container 2", container1_color='blue', container2_color='green'):
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    for item in container1.items:
        width, depth, height = item.getDimension()
        x, y, z = item.position
        ax.bar3d(x, y, z, width, depth, height, color=container1_color, alpha=0.5,edgecolor='k')

    for item in container2.items:
        width, depth, height = item.getDimension()
        x, y, z = item.position
        ax.bar3d(x + offset_x, y, z, width, depth, height, color=container2_color, alpha=0.5,edgecolor='k')

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')

plot_container_combined(ax, packer_box1.bins[0], packer_box2.bins[0], 5, 'Container 1', 'Container 2', 'blue', 'green')

plt.show()


