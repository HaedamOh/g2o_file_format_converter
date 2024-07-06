import pandas as pd

def g2o_to_csv(g2o_file_path, csv_file_path):
    with open(g2o_file_path, 'r') as file:
        lines = file.readlines()
    
    data = []
    for line in lines:
        if line.startswith('VERTEX_SE3:QUAT_TIME'):
            parts = line.split()
            timestamp = float(parts[9]) + float(parts[10]) * 1e-9  # Convert sec and nsec to a single timestamp
            data.append({
                'timestamp': timestamp,
                'x': float(parts[2]),
                'y': float(parts[3]),
                'z': float(parts[4]),
                'qx': float(parts[5]),
                'qy': float(parts[6]),
                'qz': float(parts[7]),
                'qw': float(parts[8])
            })
    
    df = pd.DataFrame(data)
    df.to_csv(csv_file_path, index=False)

# Example usage
g2o_to_csv('/home/haedamoh/vilens_slam_data/2023-10-20-22-50-05/slam_pose_graph.g2o', '/home/haedamoh/vilens_slam_data/2023-10-20-22-50-05/slam_poses_wildplace_format.csv')
