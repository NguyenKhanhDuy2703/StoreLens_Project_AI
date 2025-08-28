import matplotlib.pyplot as plt

def draw_scatter(data):
    for person_id, person_data in data.items():
        positions = person_data['positions']
        x = [pos[0] for pos in positions]
        y = [pos[1] for pos in positions]
        plt.scatter(x, y, label=f'ID {person_id}')
    
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Object Trajectories')
    plt.legend()
    plt.gca().invert_yaxis()  # Đảo ngược trục y để phù hợp với hệ tọa độ hình ảnh
    plt.show()
