from audioop import cross
import pyttsx3 

def situation(det):
	situate = []
	# 交差点
	if ('crosswalk' in det):
		situate.append('交差点が近いです')
		# crosswalkの始まり
		cross_start = 1 - det['crosswalk'][0][1] - det['crosswalk'][0][3] / 2
		print(cross_start)
		if (cross_start < 0.5):
			situate.append('交差点です')
			
			if(not any (['red light' in det, 'green light' in det, 'p_red light' in det, 'p_green light' in det])):
				situate.append('信号がありません。')
			elif ('p_red light' in det or 'red light' in det):
				situate.append('信号赤')
			elif ('p_green light' in det or 'green light' in det):
				situate.append('信号緑')
			
			if (cross_start > 0.7 ):
				situate.append('横断歩道です')
				if (det['crosswalk'][0][0] < 0.4):
					situate.append('右に寄ってます')
				if (det['crosswalk'][0][0] > 0.6):
					situate.append('左に寄ってます')
					# crosswalkの終わり
					cross_end = det['crosswalk'][0][1] - det['crosswalk'][0][3] / 2
				if (cross_end > 0.7):
					situate.append('もう少しで渡り終えます')

	# 歩道
	if ('sidewalk'in det and 'roadway'in det):
		# 左側通行
		if (det['sidewalk'][0][0] < det['roadway'][0][0]):
			if (det['sidewalk'][0][0] <= 0.25):
				situate.append('車道に近いです左に寄って')
		# 右側通行
		elif (det['sidewalk'][0][0] > det['roadway'][0][0]):
			if (det['sidewalk'][0][0] >= 0.75):
				situate.append('車道に近いです右に寄って')

		#普通の曲がり角	 corner_start < 0.5だと、隣にある道路が常に条件を満たしてしまう
		if (det['roadway'][0][2] > 0.8):
			situate.append('曲がり角が近いです')
			# 目の前のroadwayの始まり
			corner_start = 1 - det['roadway'][0][1] - det['roadway'][0][3] / 2
			if (corner_start < 0.5):
				situate.append('曲がり角です')
				# 目の前のroadwayの終わり
				corner_end = det['roadway'][0][1] - det['roadway'][0][3] / 2
				if(corner_end > 0.7):
					situate.append('もう少しで渡り終えます')

	if (len(situate) != 0):
		if(speech(situate) == 0):
			return


def speech(situate):
	s = pyttsx3.init()
	rate = s.getProperty('rate')
	s.setProperty('rate',300)

	# for word in situate:
	# 	s.say(word)  
	# 	s.runAndWait()

	s.say(situate[-1])  
	s.runAndWait()

	return 0


if __name__ == '__main__':
    situation()
