sample_string = "google.com" * 1000000
sample_dict = {}

word_count = {letter:sample_string.count(letter) for letter in set(sample_string) }
