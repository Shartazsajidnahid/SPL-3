from fastapi import FastAPI
from ..models.NewsArticle import NewsArticle

news_articles = [
      NewsArticle(id=1, title="স্পেস স্টেশনে নতুন যাত্রীরা", content="স্পেস স্টেশনে নতুন যাত্রীদের আগমনে সফলতা পেতে পূর্ববর্তী যাত্রীদের অভিজ্ঞানের গতি নিয়ে কাজ হচ্ছে।"),
    NewsArticle(id=2, title="কোভিড-১৯ টিকা বিতরণে কাঠিন্য", content="কোভিড-১৯ টিকা বিতরণে এখন কাঠিন্যের সামনে দাঁড়িয়েছে, মানুষের আগ্রহের উপর নির্ভর করে।"),
    NewsArticle(id=3, title="শিক্ষার জন্য প্রযুক্তির প্রয়োগ", content="শিক্ষার ক্ষেত্রে প্রযুক্তির প্রয়োগ বাড়ছে, অনলাইন শিক্ষা ব্যবহারের প্রযুক্তি এখন অপরিহার্য হয়েছে।"),
    NewsArticle(id=4, title="দেশে পাওয়া হয়েছে নতুন ডাইনোসর", content="দেশে নতুন ডাইনোসরের অববর্ণনা করা হয়েছে, এটি প্রাচীন কালের জীবন্ত কোষগুলির সম্মানিত অংশ।"),
    NewsArticle(id=5, title="বিশ্বকাপে বাংলাদেশের জয়", content="বাংলাদেশ ক্রিকেট দলের উপর বিশ্বকাপে জয়ের প্রত্যাশা বাড়ছে, প্রস্তুতি চলছে উত্সবের জন্য।"),
    NewsArticle(id=6, title="বৃষ্টির সময় সাবান প্রয়োজন", content="বৃষ্টির সময় হাত ধোতে সাবানের প্রয়োজন৷ বিশেষজ্ঞরা জনগণের জন্য সাবান ব্যবহার প্রস্তাবনা দিচ্ছে।"),
    NewsArticle(id=7, title="বাংলাদেশে নতুন প্রধানমন্ত্রী", content="বাংলাদেশে নতুন প্রধানমন্ত্রী নির্বাচিত হয়েছে, দেশের নেতা প্রধানমন্ত্রী হিসেবে প্রশাসন করবেন।"),
    NewsArticle(id=8, title="বাংলাদেশে সামরিক অবস্থা", content="বাংলাদেশে সামরিক অবস্থার স্থিতি বর্ণনা করা হয়েছে, সেনাবাহিনী প্রস্তুতি নেওয়া হয়েছে সীমান্তে।"),
    NewsArticle(id=9, title="পর্বত শৃঙ্গে পাওয়া হয়েছে নতুন জীবন", content="পর্বত শৃঙ্গে নতুন জীবনের সংকেত প্রাপ্ত হয়েছে, এই সংবাদের বিষয়টি নিয়ে বিস্তারিত আলোচনা হচ্ছে।"),
    
]

def dummy_news():
    return news_articles