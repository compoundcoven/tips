{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['en' 'th' 'ja']\n",
      "正解率： 1.0\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from sklearn.naive_bayes import GaussianNB\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "#Unicodeのコードポイント頻度測定\n",
    "def count_codePoint(str):\n",
    "    #Unicodeのコードポイントをアドレスとする配列を用意\n",
    "    counter = np.zeros(65535)\n",
    "    \n",
    "    for i in range(len(str)):\n",
    "        #各文字をUnicodeのコードポイントに変換\n",
    "        code_point = ord(str[i])\n",
    "        if code_point > 65535:\n",
    "            continue\n",
    "        #対応するアドレスの出現回数をインクリメント\n",
    "        counter[code_point] += 1\n",
    "        \n",
    "    #各要素を文字数で割って正規化\n",
    "    counter = counter / len(str)\n",
    "    return counter\n",
    "\n",
    "#学習用のデータを準備\n",
    "ja_str = 'これは日本語の文章です'\n",
    "en_str = 'This is English Sentences'\n",
    "th_str = 'นี่คือประโยคภาษาไทย'\n",
    "\n",
    "x_train = [count_codePoint(ja_str), count_codePoint(en_str), count_codePoint(th_str)]\n",
    "y_train = ['ja', 'en', 'th']\n",
    "\n",
    "#学習する\n",
    "clf = GaussianNB()\n",
    "clf.fit(x_train, y_train)\n",
    "\n",
    "#評価用データの準備\n",
    "ja_test_str = 'こんにちは'\n",
    "en_test_str = 'Hello'\n",
    "th_test_str = 'สวัสดี'\n",
    "\n",
    "x_test = [count_codePoint(en_test_str), count_codePoint(th_test_str), count_codePoint(ja_test_str)]\n",
    "y_test = ['en', 'th', 'ja']\n",
    "\n",
    "#評価する\n",
    "y_pred = clf.predict(x_test)\n",
    "print(y_pred)\n",
    "print(\"正解率：\", accuracy_score(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
