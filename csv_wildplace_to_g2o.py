import pandas as pd

def csv_to_g2o(csv_file_path, g2o_file_path):
    df = pd.read_csv(csv_file_path)
    
    with open(g2o_file_path, 'w') as file:
        for idx, row in df.iterrows():
            sec, nsec = divmod(row['timestamp'], 1)
            nsec = int(nsec * 1e9)
            file.write(f"VERTEX_SE3:QUAT_TIME {idx} {row['x']} {row['y']} {row['z']} {row['qx']} {row['qy']} {row['qz']} {row['qw']} {int(sec)} {nsec}\n")

# Example usage
csv_to_g2o('/home/haedamoh/logs/Wild-Places/Venman/V-04/poses_aligned_edited_haedam.csv', '/home/haedamoh/logs/Wild-Places/Venman/V-04/slam_pose_graph.g2o')
