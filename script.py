sample_string = "google.com" * 100000
sd_2 = {}

for charactor in sample_string:
    if charactor in sd_2:
        sd_2[charactor] += 1
    else:
        sd_2[charactor] = 1