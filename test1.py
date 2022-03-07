import logging



#NOSET :0
#Debug :  10       These are used to give Detailed information, typically of interest only when diagnosing problems.
#Info :    20     These are used to confirm that things are working as expected
#Warning :  30     These are used an indication that something unexpected happened, or is indicative of some problem in the near future
#Error :    40        This tells that due to a more serious problem, the software has not been able to perform some function
#Critical :  50    This tells serious error,




logging.basicConfig(filename='main.log' ,level=logging.DEBUG,
                    format='%(asctime)s: - > %(levelname)s - > %(message)s')

def add(a, b):
   logging.debug(f'{a} + {b} = {a+b}')
def sub(a, b):
    logging.debug(f'{a} - {b} = {a-b}')
def mult(a, b):
    logging.debug(f'{a} * {b} = {a*b}')
def div(a, b):
    try:
        logging.debug(f'{a} / {b} = {a/b}')
    except:
        print("lo oved kapara")
        logging.critical("divided by zero from the 26 line in the test 1 file")


class User:
    def __init__(self,name):
        self.name=name
        logging.info(f"a new user created the name is : {self.name}")


sub(5,5)
div(5,0)
add(5,5)
mult(5,5)
u1= User('batman')




















# כתבו קוד פייטוני עם מחללקה בשם MOVIE המחלקה מכילה INIT ו TO STING
# בכל פעם שתיצרו מופע מהמחלקה יש להדפיס לתוך לוג שנקרא MOVIELOG את ההודעה מסוג INFO
# ובכל פעם שאתם קוראים לפנוקציה STR יש להדפיס את TOSTRING לתוך הלוג בתור דיבאג

format='%(asctime)s::%(levelname)s:%(message)s'






