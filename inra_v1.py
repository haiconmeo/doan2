CHUOI,NHAYKEP,EOF ='CHUOI','\"','EOF'

class Token(object):
    def __init__(self, type, value):
        
        self.type = type
        
        self.value = value

    def __str__(self):

        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        
        self.text = text
        
        self.pos = 0
        
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('loi vai loz')

    def advance(self):
        
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  
        else :    
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    def CHUOI(self):
        result =''
        while self.current_char is not None and self.current_char.isalpha():
            result += self.current_char
            self.advance()
        return result 

    

    def get_next_token(self):
        
        while self.current_char is not None:
            text = self.text

        # xác định vị trí cuối của mảng
        # trả về EOF
        # sẽ phải lưu trái và pahri
            if self.pos > len(text) - 1:
                return Token(EOF, None)

        # giá trị của pos hiện tại   
            self.current_char = text[self.pos]
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isalpha():
                
                return Token(CHUOI, self.CHUOI())

            if self.current_char == '\"':
                self.advance()
                return Token(NHAYKEP, '\"')

            

            self.error()

        return Token(EOF, None)

    def eat(self, token_type):
        
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):

        self.current_token = self.get_next_token()

        
        left = self.current_token
        self.eat(CHUOI)

        
        op1 = self.current_token
        
        self.eat(NHAYKEP)
        

        
        right = self.current_token
        self.eat(CHUOI)
        op2 = self.current_token
        
        self.eat(NHAYKEP)


        print (left.value)
        print (op1.value)
        print (right.value)
        print (op2.value)
        


def main():
    while True:
        try:
            
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()