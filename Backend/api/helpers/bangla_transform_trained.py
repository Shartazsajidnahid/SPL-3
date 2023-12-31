from bntransformer import BanglaQA
from pathlib import Path

# Get the current file's path
current_file_path = Path(__file__)

# Get the parent directory of the current file
parent_directory = current_file_path.parent
folder_name = "test-nahid-trained"
folder_path = parent_directory / folder_name

bnqa2 = BanglaQA(folder_path)
bnqa = BanglaQA()


location = "কোথায় দুর্ঘটনা ঘটেছে?"
time = "কখন দুর্ঘটনা ঘটেছিলো?"
vehicle = "কোন যানবাহন দুর্ঘটনায় জড়িত ছিল?"
dead2 = "কে মারা গেছে?"
dead = "কতজন নিহত অথবা মারা গিয়েছে অথবা মৃত?"
injured = "কতজন আহত?"

# question = "কোথায় দুর্ঘটনা ঘটেছে?          "
# context = "বরগুনার বামনা উপজেলায় ট্রাক ও মোটরসাইকেলের মুখোমুখি সংঘর্ষে জয় দে নামের জাতীয় নিরাপত্তা গোয়েন্দা (এনএসআই) সংস্থার এক কর্মকর্তা নিহত হয়েছেন। আজ শনিবার দুপুর সোয়া ১২টার দিকে উপজেলা সদরের ফায়ার সার্ভিসের কার্যালয়-সংলগ্ন সোনাখালী এলাকায় পাথরঘাটা-বামনা সড়কে এ দুর্ঘটনা ঘটে। সূত্র জানায়, নিহত জয় দে চট্টগ্রামের পটিয়া উপজেলার বাসিন্দা। তিনি এনএসআইয়ের মাঠ কর্মকর্তা হিসেবে কর্মরত ছিলেন। দুর্ঘটনায় মেহেদী হাসান নামের আরেক মাঠ কর্মকর্তা গুরুতর আহত হয়েছেন। তাঁকে বরিশালের শের-ই-বাংলা মেডিকেল কলেজ হাসপাতালে ভর্তি করা হয়েছে। মেহেদী হাসানের বাড়ি পিরোজপুরের ভান্ডারিয়া উপজেলায়। প্রত্যক্ষদর্শী ও স্থানীয় লোকজনের সঙ্গে কথা বলে জানা গেছে, আজ দুপুরে বরগুনা থেকে মোটরসাইকেলে বামনায় যাচ্ছিলেন এনএসআইয়ের দুই কর্মকর্তা। দুপুর সোয়া ১২টার দিকে পাথরঘাটা-বামনা সড়কের বামনা ফায়ার সার্ভিস কার্যালয়-সংলগ্ন সোনাখালী এলাকায় তাঁদের বহনকারী মোটরসাইকেলের সঙ্গে একটি ট্রাকের মুখোমুখি সংঘর্ষ হয়। এতে ঘটনাস্থলেই এনএসআই কর্মকর্তা জয় দে নিহত হন। গুরুতর আহত হন আরেক কর্মকর্তা মেহেদী হাসান। আশঙ্কাজনক অবস্থায় তাঁকে উদ্ধার করে বামনা উপজেলা স্বাস্থ্য কমপ্লেক্সে নিয়ে প্রাথমিক চিকিৎসা দেওয়া হয়। পরে তাঁকে বরিশালের শের-ই-বাংলা মেডিকেল কলেজ হাসপাতালে পাঠানো হয়। দুর্ঘটনায় মোটরসাইকেলটি দুমড়েমুচড়ে যায়। বামনা উপজেলা স্বাস্থ্য ও পরিবার পরিকল্পনা কর্মকর্তা মনিরুজ্জামান প্রথম আলোকে বলেন, জয় দে ঘটনাস্থলেই নিহত হন। মেহেদী হাসান বুকে আঘাত পেয়েছেন। হাসপাতালে নিয়ে আসার পর তাঁর কান দিয়ে রক্ত পড়ছিল। প্রাথমিক চিকিৎসা দিয়ে আশঙ্কাজনক অবস্থায় দ্রুত তাঁকে বরিশালের শের-ই-বাংলা মেডিকেল কলেজ হাসপাতালে পাঠানো হয়েছে। বামনা থানার ভারপ্রাপ্ত কর্মকর্তা মাইনুল ইসলাম প্রথম আলোকে বলেন, ট্রাকটিকে জব্দ করা হয়েছে। তবে ট্রাকের চালক ও তাঁর সহকারী পালিয়ে গেছেন। পুলিশ ট্রাকচালক ও মালিকের পরিচয় শনাক্তের চেষ্টা চালাচ্ছে।"
# answers = bnqa.find_answer(context, question)
# print(answers["answer"])

async def find_parameters(news):
	result = {
		'location': find_location(news)['answer'],
		'time': find_time(news)['answer'],
		'dead': find_dead(news)['answer'],
		'injured': find_injured(news)['answer']
	}
	return result


def find_location(news):
	return bnqa.find_answer(news, location)

def find_time(news):
	return bnqa.find_answer(news, time)

def find_vehicle(news):
	return bnqa.find_answer(news, vehicle)

def find_dead(news):
	return bnqa.find_answer(news, dead)

def find_injured(news):
	return bnqa.find_answer(news, injured)
