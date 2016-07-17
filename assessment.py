"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   --> The first advantage is abstraction, which allows you to hide the details of
       what's going on under the hood in your code. A well-desiged, object-oriented
       program doesn't force users to worry about how the code works to know how to
       use it.

   --> The second advantage is encapsulation. This just means putting everything specific
       to a class all in one place. A class that subclasses another class shouldn't share
       behaviors or traits with other classes with the same parent, unless all subclasses
       inherit those behaviors or traits.

   --> The third advantage is polymorphism, which is important because it allows classes
       that descend from a common ancestor to be interchangeable in specific, predictable
       ways. If you create an Animal class that has a speak() method, users should be
       able to assume that all classes descended from Animal can also speak.


2. What is a class?

    A class is just a category used to describe a group of things with particular
    characteristics. Python has a File class, for example. All things that are Files
    can read themselves, write to themselves, and so on.

3. What is an instance attribute?

    An instance attribute is a trait whose value is specific to a particular object.
    For example, if you create a Dog class, you might add "name" as an instance
    attribute because each dog has its own name.

4. What is a method?

    A method is simply a function defined on an object. To call an object's method,
    you have to use dot notation, as in frisket.speak().

5. What is an instance in object orientation?

    An instance is an object. When you "instantiate" an object, you're creating an
    instance of a particular class. For example, jiji = Cat() would make jiji
    an instance of the Cat class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is a trait that all instances of the class should share. An instance
   attribute is a trait that may change based on the instance of the class.

   For example, if you had a Mammal class, it might have a class attribute called order
   that equals "vertebrates" because all mammals are vertebrates. Instance attributes
   for mammals might include fur_length, greeting_sound, and has_claws, because these
   qualities will vary among mammals.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """A class to store student information, including first/last name and address.

    Instantiating this class requires three parameters:

    first_name: a string representing the student's first name
    last_name: a string representing the student's last name
    address: a string representing the student's address

    >>> mary = Student("mary","middle","123 456th St")
    >>> mary.first_name
    'mary'
    >>> mary.last_name
    'middle'
    >>> mary.address
    '123 456th St'
    """

    # Contsructor method
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A class to store questions and their correct answers.

    Instantiating this class takes two parameters:
    question: A string containing the question's full text.
    correct_answer: The response you expect a student to give to the question. If
                    a number is given, it will be converted into a string.

    >>> question1 = Question("Who gave the Gettysburg Address?", "Abraham Lincoln")
    >>> question1.question
    'Who gave the Gettysburg Address?'
    >>> question1.correct_answer
    'Abraham Lincoln'

    >>> question2 = Question("What is the meaning of life?",42)
    >>> question2.question
    'What is the meaning of life?'
    >>> question2.correct_answer
    '42'

    """

    # Constructor method
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = str(correct_answer)


class Exam(object):
    """A class that creates an exam.

    Takes one parameter:

    name: a string representing the name of the exam

    Exam also has a class attribute called questions, which you can use to store
    a list of questions you want to ask your students.

    >>> question1 = Question("Who gave the Gettysburg Address?", "Abraham Lincoln")
    >>> question2 = Question("What is the meaning of life?",42)

    >>> hard_quiz = Exam("Hardest Quiz Ever")
    >>> hard_quiz.questions = [question1, question2]

    >>> for question in hard_quiz.questions:
    ...     print question.question
    ...     print question.correct_answer
    ...
    ...
    Who gave the Gettysburg Address?
    Abraham Lincoln
    What is the meaning of life?
    42
    """

    # Constructor method.
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Given a question and its answer, adds the question to the current exam.

        Takes the following parameters:

        question: a string of text
        correct_answer: the answer to the given question; if given as a number, this
                        will be converted to a string.
        """

        # Creates a new instance of the Question class
        new_question = Question(question, correct_answer)

        # Appends that Question to self.questions
        self.questions.append(new_question)



######################################################################
if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
