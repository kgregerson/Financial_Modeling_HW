{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter Rf rate:1.0\n",
      "Please enter Beta:2\n",
      "Please enter Expected Market Return:5.0\n",
      "('your Expected Return on Asset is:', 9.0)\n"
     ]
    }
   ],
   "source": [
    "riskFree = float(input(\"Please enter Rf rate:\"))\n",
    "Beta = float(input(\"Please enter Beta:\"))\n",
    "expectedMarket = float(input(\"Please enter Expected Market Return:\"))\n",
    "assetReturn = riskFree + Beta*(expectedMarket - riskFree)\n",
    "print((\"your Expected Return on Asset is:\", assetReturn))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
