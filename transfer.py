import trimesh
import numpy as np
import os
import glob

# 定义旋转矩阵：绕 X 轴旋转 90 度 (从 Y-up 转到 Z-up)
# 如果结果反了，把 np.pi/2 改成 -np.pi/2
angle = 0.0
rotation_matrix = trimesh.transformations.rotation_matrix(angle, [1, 0, 0])

input_dir = "./fr3_urdfs//"
output_dir = "./fr3_urdfs/"
os.makedirs(output_dir, exist_ok=True)

for dae_file in glob.glob(os.path.join(input_dir, "*.dae")):
    mesh = trimesh.load(dae_file, force='mesh')
    
    # === 关键步骤：应用变换 ===
    mesh.apply_transform(rotation_matrix)
    
    filename = os.path.basename(dae_file).replace('.dae', '.obj')
    mesh.export(os.path.join(output_dir, filename))
    print(f"Fixed and Converted: {filename}")