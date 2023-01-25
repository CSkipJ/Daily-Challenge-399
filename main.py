class Valdic_Holder:
  """A fancy way to hold a list of valdics. Why am 
  i making this more complicated."""

  def __init__(self):
    self.valdic_lst = []

  def is_valdic(self, points):
    """Returns true if valdic exists in the list. Returns false is it doesn't."""
    if self.valdic_lst:
      for valdic in self.valdic_lst:
        if valdic.get_points() == points:
          return True
      return False
    else:
      return False

  def get_valdic(self, points):
    for valdic in self.valdic_lst:
      if valdic.get_points() == points:
        return valdic

  def add_valdic(self, valdic):
    self.valdic_lst.append(valdic)

  def get_largest(self):
    largest = Valdic(0)
    for valdic in self.valdic_lst:
      if valdic.len() > largest.len():
        largest = valdic
    return largest

#END Class valdic_holder

class Valdic:
  """Holds a dictionary with a collection of words whose values are all equal to points"""

  def __init__(self, points):
    self.points = points
    self.word_list = []

  def add_word(self, word):
    self.word_list.append(word)

  def get_points(self):
    return self.points

  def report(self):
    print(f"Valdic {self.points} has {len(self.word_list)} words.")
    
  def len(self):
    return len(self.word_list)

  def __str__(self):
    retval = ''
    for word in self.word_list:
      retval += word #+ '\n'
    return retval

# END valdic Class
  
def word_points(word):
  tot = 0
  for letter in word:
    for key, val in alpha.items():
      if letter == key:
        tot += alpha[key]
  return tot

#END word_points()
  
alpha = {'a':1,  'b':2,  'c':3,  'd':4,  'e':5,
         'f':6,  'g':7,  'h':8,  'i':9,  'j':10,
         'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
         'p':16, 'q':17, 'r':18, 's':19, 't':20,
         'u':21, 'v':22, 'w':23, 'x':24, 'y':25,
         'z':26}

valdic_holder = Valdic_Holder()

with open('word_list.txt') as file_obj:
  for word in file_obj:
    points = word_points(word)
    if valdic_holder.is_valdic(points):
      valdic = valdic_holder.get_valdic(points)
      valdic.add_word(word)
    else:
      valdic = Valdic(points)
      valdic_holder.add_valdic(valdic)

largest = valdic_holder.get_largest()
largest.report()

with open('word_output.txt', 'w') as file_obj:
  file_obj.writelines(largest.__str__())


#Challenge

#Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of lowercase letters, find the sum of the values of the letters in the string.

# lettersum("") => 0
# lettersum("a") => 1
# lettersum("z") => 26
# lettersum("cab") => 6
# lettersum("excellent") => 100
# lettersum("microspectrophotometries") => 317

# Optional bonus challenges

# Use the enable1 word list for the optional bonus challenges.

#     microspectrophotometries is the only word with a letter sum of 317. Find the only word with a letter sum of 319.

#     How many words have an odd letter sum?

#     There are 1921 words with a letter sum of 100, making it the second most common letter sum. What letter sum is most common, and how many words have it?

#     zyzzyva and biodegradabilities have the same letter sum as each other (151), and their lengths differ by 11 letters. Find the other pair of words with the same letter sum whose lengths differ by 11 letters.

#     cytotoxicity and unreservedness have the same letter sum as each other (188), and they have no letters in common. Find a pair of words that have no letters in common, and that have the same letter sum, which is larger than 188. (There are two such pairs, and one word appears in both pairs.)

#     The list of word { geographically, eavesdropper, woodworker, oxymorons } contains 4 words. Each word in the list has both a different number of letters, and a different letter sum. The list is sorted both in descending order of word length, and ascending order of letter sum. What's the longest such list you can find?