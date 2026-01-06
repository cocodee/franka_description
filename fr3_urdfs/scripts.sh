./scripts/create_urdf.sh --robot-ee franka_hand  --abs-path --host-dir . --no-prefix fr3
for file in *.dae; do assimp export "$file" "${file%.dae}.obj"; done

