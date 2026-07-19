
from passlib.context import CryptContext

passcon = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    @staticmethod
    def bcrypt(password):
        return passcon.hash(password)


    @staticmethod
    def verify(hashed_password, plain_password):
        return passcon.verify(plain_password, hashed_password)
    

