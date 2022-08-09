import imageio
import cv2
import pytesseract
import csv
import re, sys

def img_preprocess(img_dir):
	in_img = cv2.imread(img_dir)
	gray_img = cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)
	img = cv2.medianBlur(gray_img, 5)

	return img 

def img2str(img):
	custom_config = r'--oem 3 --psm 6'
	oct_str = pytesseract.image_to_string(img, config=custom_config)
	return oct_str

# inpt a receipt image, no further request
def auto_catch(img):
	# img = img_preprocess("./IMG_20220805_021514.jpg")			# rotation?
	# print(set(img.flatten()))
	_str = img2str(img)
	print(_str)

	_list = _str.split('\n')
	start = 0
	end = -1
	item_list = []
	for i, val in enumerate(_list):
		if(val.find("Member") != -1):
			start = i
			break
	# for i in range(start):
	# 	_ = _list.pop(i)

	for i, val in enumerate(_list):
		p = re.compile(r'S.+')
		if(p.match(val) and re.compile(r'T.+').match(_list[i+1])):
			end = i
			break
		# if(val.find("SUBTOTAL") != -1):
		# 	end = i
		# 	break
	print(start, end)
	# print(end, len(_list))
	# for i in range(end, len(_list)):	
	# 	print(_list[i])
	# 	_ = _list.pop(i)

	for i in range(start+1, end):
		item_list.append(_list[i])
	# for val in _list:
	# 	# print(val.find("Member"))
	# 	if(val.find("Member") == -1):
	# 		_list.pop(0)			# Why operating element of a list in for loop will lead error result?
	# 		print("Not Finding:", val)
	# 	else:
	# 		print("Finding:", val)
	# 		break


	price_list = []
	name_list = []

	for i, val in enumerate(item_list):
		s = -1
		val_list = val.split(' ')
		p = re.compile(r'[0-9]{3,12}')
		for j in range(len(val_list)):
			# print(val_list[j])
			if(p.match(val_list[j])):
				# print("Get, ", val_list[j])
				num = val_list[j]
				s = j+1
				break
		if (s == -1):
			print(val)
			print("Error in num!")
		# q = re.compile(r'.')
		# print(re.findall(".",val_list[-1]))
		if(len(re.findall(".",val_list[-1])) == 1):
			# print(val_list[-1])
			# This one is item you buy
			try:
				price_list.append(float(val_list[-2]))
			except:
				price_list.append(val_list[-2])
			tmp_list = val_list[s: -2]
			name_list.append(' '.join(tmp_list))
		elif(val_list[-1][-2] == '-'):
			# print(val_list)
			# This is a discount val
			price_list[-1] -= float(val_list[-1].split('-')[0])
		else:
			print("Error in price!")
			
	print("price_list:", price_list)
	print("name_list: ", name_list)
	print("###########################")
	print(item_list)

# Request the user to manually crop the receipt only contains From Member to Total.
def manual_catch(img):
	_str = img2str(img)
	print(_str)

	_list = _str.split('\n')
	start = 1
	end = -4
	item_list = []

	for i, val in enumerate(_list):
		if(val.find("Member") != -1):
			start = i
			break
	# for i in range(start):
	# 	_ = _list.pop(i)

	for i, val in enumerate(_list):
		if(val.find("SUBTOTAL") != -1):
			end = i
			break
		elif(re.compile(r'S.+').match(val) and re.compile(r'T.+').match(_list[i+1])):
			end = i
			break

	# print(end, len(_list))
	# for i in range(end, len(_list)):	
	# 	print(_list[i])
	# 	_ = _list.pop(i)

	for i in range(start, end):
		item_list.append(_list[i])
	# for val in _list:
	# 	# print(val.find("Member"))
	# 	if(val.find("Member") == -1):
	# 		_list.pop(0)			# Why operating element of a list in for loop will lead error result?
	# 		print("Not Finding:", val)
	# 	else:
	# 		print("Finding:", val)
	# 		break


	price_list = []
	name_list = []

	for i, val in enumerate(item_list):
		s = -1
		val_list = val.split(' ')
		print(val)
		p = re.compile(r'[0-9]{3,12}')
		for j in range(len(val_list)):
			# print(val_list[j])
			if(p.match(val_list[j])):
				# print("Get, ", val_list[j])
				num = val_list[j]
				s = j+1
				break
		if (s == -1):
			print(val)
			print("Error in num!")
		# q = re.compile(r'.')
		# print(re.findall(".",val_list[-1]))
		if(len(re.findall(".",val_list[-1])) == 1):
			# print(val_list[-1])
			# This one is item you buy
			try:
				price_list.append(float(val_list[-2]))
			except:
				price_list.append(val_list[-2])
			tmp_list = val_list[s: -2]
			name_list.append(' '.join(tmp_list))
		elif(val_list[-1][-2] == '-'):
			# print(val_list)
			# This is a discount val
			price_list[-1] -= float(val_list[-1].split('-')[0])
		else:
			print("Error in price!")
			
	print("price_list:", price_list)
	print("name_list: ", name_list)
	print("###########################")
	print(item_list)


if __name__ == '__main__':
	if(len(sys.argv) == 2):
		img = img_preprocess(sys.argv[1])
	else:
		print("Request IMAGE pass!")
	# auto_catch(img)
	manual_catch(img)

# input item number
# check 12 bit num incase "Member fails"

# print(_str.split('\n'))
# mn. Salt Lake City II #113

#     1818 South 300 West

#            | Salt Lake City, UT 84115

#  70 Member 111933959583

#  F 1215971 HIPPEAS CHED 7.99 E

#  EF 0000282280 /1215971 2.50-E

#  1121474 3M SPONGEX21 13.99 A

#  0000282175 /1121474 3.80-A

#  E 846156 NV OAT HONEY 14.45 E

#  E 0000282333 / 846156 4.40-E.

#  E 1154542 PUDDING B6CT 7.99 E-

#  1119590 8PC MIXING 17.99 A-

#  0000282074 /1119590 5.00-A

#  1493488 KS BABY WIPE 20.99 A

#  0000282577 /149348 4.50-A

#  1604562 BATH TOWELS 10.99 A

#  E 146853 LAUGHING COW 9.49 E

#  F 0000282415 / 14685 3.50-E

#   E 637598 KS CAGE FREE 4.99 E

# E 905061 KS BACO 15.49 E-

#  1649376 CREST 3 sie

#  0000282093 /164937 .00-

#  E 9619 ORG BANANAS 1.89 E

#  9907391 CLEAN36Q 2PK 99.99 A

#  0000282090 /290739 30.00-A

#  1276702 KSFILTE 10PK 19.99 A

#  E 1090675 ORG CHE RIES 10.79 E

# SUBTOTAL 215.31

# TAX 2-1 |
#       xxx TOTAL ee



# , 'SUBTOTAL 215.31', 
# 'TAX 2-1 |',
#  'xxx TOTAL ee', 
#  'XXXXXXXXXXXX3219 CHIP Read', '| aD: 0000000031010 —', 'a= Seat 10380 Appt: 057588 | a', 'Visa Resp: APPROVED eRe', 'Tran ID#: 221500010380.... series.', '\x0c']             