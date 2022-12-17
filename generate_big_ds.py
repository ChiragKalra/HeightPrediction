all_lines = open('data/height_and_pose.csv', mode='r', encoding='utf_8_sig').readlines()
duplicate_count = 10_000
output_file = open('data/height_and_pose_big.csv', mode='w', encoding='utf_8_sig')
for _ in range(duplicate_count):
	output_file.writelines(all_lines)
