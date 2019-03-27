
INTEGER, PLUS,MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS','EOF'
class Token(object):
    def __init__(self, type, value):
       #token sẽ lưu 
        self.type = type
        
        self.value = value

    def __str__(self):
        """cái chính la token sẽ lưu kiểu này .

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # tạm thời là 1 chữ số +1 chữ số "3+5"
        self.text = text
        # vị trí đang đọc của text 
        self.pos = 0
        # 
        self.current_token = None
        self.current_char = self.text[self.pos]
    def advance(self):
        
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]   
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)                 

    def error(self):
    	# thông báo lỗi 
        raise Exception('lỗi nhập ')

    def get_next_token(self):
       
        text = self.text

        # xác định vị trí cuối của mảng
        # trả về EOF
        # sẽ phải lưu trái và pahri
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # giá trị của pos hiện tại   
        current_char = text[self.pos]

        # kiểm tra nó có pahir số ko 
        # tạm thời sẽ sử dụng số nguyên đã
        # 
        # trả về  INTEGER cho token
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token    

        self.error()

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        
        self.current_token = self.get_next_token()

      
        left = self.current_token
        self.eat(INTEGER)


        op = self.current_token
        if op.type == PLUS:
        	self.eat(PLUS)
        else :
        	self.eat(MINUS)	


        right = self.current_token
        self.eat(INTEGER)
        if op.type ==PLUS:
        	result = left.value + right.value
        else :
        	result = left.value -right.value
        		
        return result


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
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