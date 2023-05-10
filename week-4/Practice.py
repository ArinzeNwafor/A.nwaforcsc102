{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "source": [
    "# Python program to swap two cities\r\n",
    "\r\n",
    "# To take inputs from the user\r\n",
    "city_1 = input('Enter name of City 1: ')\r\n",
    "city_2 = input('Enter name of City 2: ')\r\n",
    "\r\n",
    "# create a temporary variable and swap the cities\r\n",
    "temp = city_1\r\n",
    "city_1 = city_2\r\n",
    "city_2 = temp\r\n",
    "\r\n",
    "print(f\"The name of City 1 after swapping is {city_1}\")\r\n",
    "print(f\"The name of City 2 after swapping is {city_2}\")"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Enter name of City 1: Agungi\n",
      "Enter name of City 2: Mayegun\n",
      "The name of City 1 after swapping is Mayegun\n",
      "The name of City 2 after swapping is Agungi\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "source": [
    " # Program to Check if a Number is Positive, Negative or 0\r\n",
    "\r\n",
    "num = float(input(\"Enter a number: \"))\r\n",
    "if num > 0:\r\n",
    "  print(\"Positive number\")\r\n",
    "elif num == 0:\r\n",
    "  print(\"Zero\")\r\n",
    "else:\r\n",
    "  print(\"Negative number\")"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Enter a number: 5\n",
      "Positive number\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "source": [
    "# COUPE DE ESCRIVA 2023: FOOTBALL PICKS\r\n",
    "\r\n",
    "print(\"Welcome to the COUPE DE ESCRIVA 2023: FOOTBALL PICKS \\n\")\r\n",
    "\r\n",
    "captain = { 'Madiba: ': 'Chubby Obiora-Okafo', 'Blue-Jays: ': 'Christopher Uweh', 'Cirok: ': 'Alexander', 'TSG Walkers: ': 'Ikechukwu'}\r\n",
    "goalkeepers = { 'Madiba: ': 'Chubby Obiora-Okafo','Blue-Jays: ': 'Oladimeji Abaniwondea/Jeffery Awagu', 'Cirok: ': 'Timileyin Pearse/Izuako Jeremy', 'TSG Walkers: ': 'Ayomide Ojituku'}\r\n",
    "\r\n",
    "for pick in captain:\r\n",
    "  print(pick, captain[pick])\r\n",
    "\r\n",
    "print(\"\\n\")\r\n",
    "\r\n",
    "for pick in goalkeepers:\r\n",
    "  print(pick, goalkeepers[pick])"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Welcome to the COUPE DE ESCRIVA 2023: FOOTBALL PICKS \n",
      "\n",
      "Madiba:  Chubby Obiora-Okafo\n",
      "Blue-Jays:  Christopher Uweh\n",
      "Cirok:  Alexander\n",
      "TSG Walkers:  Ikechukwu\n",
      "\n",
      "\n",
      "Madiba:  Chubby Obiora-Okafo\n",
      "Blue-Jays:  Oladimeji Abaniwondea/Jeffery Awagu\n",
      "Cirok:  Timileyin Pearse/Izuako Jeremy\n",
      "TSG Walkers:  Ayomide Ojituku\n"
     ]
    }
   ],
   "metadata": {}
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
 "nbformat_minor": 2
}