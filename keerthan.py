{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1cb8d64a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: 6\n",
      "number is Even\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "if (num % 2) == 0:\n",
    "   print(\"number is Even\")\n",
    "else:\n",
    "   print(\"number is Odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fc3ba8ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number: -1\n",
      "Negative number\n"
     ]
    }
   ],
   "source": [
    "num = float(input(\"Enter a number: \"))\n",
    "if num > 0:\n",
    "   print(\"Positive number\")\n",
    "elif num == 0:\n",
    "   print(\"Zero\")\n",
    "else:\n",
    "   print(\"Negative number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1b7544ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first number: 3\n",
      "Enter second number: 9\n",
      "Enter third number: 2\n",
      "The largest number is 9.0\n"
     ]
    }
   ],
   "source": [
    "\n",
    "num1 = float(input(\"Enter first number: \"))\n",
    "num2 = float(input(\"Enter second number: \"))\n",
    "num3 = float(input(\"Enter third number: \"))\n",
    "\n",
    "if (num1 >= num2) and (num1 >= num3):\n",
    "   largest = num1\n",
    "elif (num2 >= num1) and (num2 >= num3):\n",
    "   largest = num2\n",
    "else:\n",
    "   largest = num3\n",
    "\n",
    "print(\"The largest number is\", largest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "26ffbff1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "6\n",
      "9\n",
      "10\n",
      "11\n",
      "13\n",
      "15\n",
      "17\n",
      "18\n",
      "19\n",
      "22\n",
      "23\n",
      "25\n",
      "26\n",
      "27\n",
      "29\n",
      "30\n",
      "31\n",
      "33\n",
      "34\n",
      "37\n",
      "38\n",
      "39\n",
      "41\n",
      "43\n",
      "45\n",
      "46\n",
      "47\n",
      "50\n",
      "51\n",
      "53\n",
      "54\n",
      "55\n",
      "57\n",
      "58\n",
      "59\n",
      "61\n",
      "62\n",
      "65\n",
      "66\n",
      "67\n",
      "69\n",
      "71\n",
      "73\n",
      "74\n",
      "75\n",
      "78\n",
      "79\n",
      "81\n",
      "82\n",
      "83\n",
      "85\n",
      "86\n",
      "87\n",
      "89\n",
      "90\n",
      "93\n",
      "94\n",
      "95\n",
      "97\n",
      "99\n"
     ]
    }
   ],
   "source": [
    "i = 1\n",
    "while i <= 100:\n",
    "    if(i % 4 != 0) and (i % 7 != 0):\n",
    "        print(i)\n",
    "    i = i + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f24a72fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n",
      "40\n",
      "42\n",
      "44\n",
      "46\n",
      "48\n",
      "50\n",
      "52\n",
      "54\n",
      "56\n",
      "58\n",
      "60\n",
      "62\n",
      "64\n",
      "66\n",
      "68\n",
      "70\n",
      "72\n",
      "74\n",
      "76\n",
      "78\n",
      "80\n",
      "82\n",
      "84\n",
      "86\n",
      "88\n",
      "90\n",
      "92\n",
      "94\n",
      "96\n",
      "98\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "i = 2\n",
    "while i <= 100:\n",
    "    print(i)\n",
    "    i = i + 2\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7be32604",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number:6\n",
      "The sum is 21\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter the number:\"))\n",
    "\n",
    "if num < 0:\n",
    "   print(\"Enter a positive number\")\n",
    "else:\n",
    "   sum = 0\n",
    "   while(num > 0):\n",
    "       sum += num\n",
    "       num -= 1\n",
    "   print(\"The sum is\", sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "37b637b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of rows: 4\n",
      "* \n",
      "\n",
      "* * \n",
      "\n",
      "* * * \n",
      "\n",
      "* * * * \n",
      "\n"
     ]
    }
   ],
   "source": [
    "rows = int(input(\"Enter number of rows: \"))\n",
    "\n",
    "for i in range(rows):\n",
    "    for j in range(i+1):\n",
    "        print(\"* \", end=\"\")\n",
    "    print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fc234ab3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of rows: 3\n",
      "*  *  *  \n",
      "\n",
      "*  *  \n",
      "\n",
      "*  \n",
      "\n"
     ]
    }
   ],
   "source": [
    "rows = int(input(\"Enter number of rows: \"))\n",
    "\n",
    "for i in range(rows, 0, -1):\n",
    "    for j in range(0, i):\n",
    "        print(\"* \", end=\" \")\n",
    "    \n",
    "    print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e33f1392",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of rows: 3\n",
      "1 \n",
      "\n",
      "1 2 \n",
      "\n",
      "1 2 3 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "rows = int(input(\"Enter number of rows: \"))\n",
    "\n",
    "for i in range(rows):\n",
    "    for j in range(i+1):\n",
    "        print(j+1, end=\" \")\n",
    "    print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "60dbbaad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of rows: 4\n",
      "1 2 3 4 \n",
      "\n",
      "1 2 3 \n",
      "\n",
      "1 2 \n",
      "\n",
      "1 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "rows = int(input(\"Enter number of rows: \"))\n",
    "\n",
    "for i in range(rows, 0, -1):\n",
    "    for j in range(1, i+1):\n",
    "        print(j, end=\" \")\n",
    "    \n",
    "    print(\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf7771b8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
