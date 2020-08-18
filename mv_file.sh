#
#  /mnt/c/abc/IMG_20200818120000_FrameNum[4]/zoom/*.jpg --> /mnt/c/abc/IMG_20200818120000_FrameNum[4]/*.jpg
#
#  Mingzhen Shao
#  2020/8/18

for d in */ ; do
#	find "$d" -type f -exec mv {} "$d" \;
	find "$d" -type f -exec mv {} "$d" \;
	find . -type d -depth -empty -exec rmdir "{}" \;
done
