from enum import Enum


class Operations(Enum):
    SUM = "+"
    CONCATENATION = "."
    KLEENE_STAR = "*"


class RegularExpressionHandling:
    def __init__(self, regular_expression: str, mod: int, remainder: int, alphabet: set, operations: set):
        self._regular_expression: str = regular_expression
        self._mod: int = mod
        self._remainder: int = remainder
        self._alphabet: set = alphabet
        self._operations: set = operations

        for i in self._regular_expression:
            if i not in (self._alphabet | self._operations):
                raise AttributeError("Unacceptable symbols")

    def are_exist_necessary_words(self) -> bool:
        stack: list = []
        
        for i in self._regular_expression:
            if i in self._alphabet:
                letter_expr = [False] * self._mod
                if i == '1':
                    letter_expr[0] = True
                else:
                    letter_expr[1] = True

                stack.append(letter_expr)
                
            elif i in self._operations:
                if i == Operations.CONCATENATION.value:
                    lhs = stack.pop()
                    rhs = stack.pop()
                    expr_concatenation = self.__concatenation(lhs, rhs)
                    stack.append(expr_concatenation)
                    
                elif i == Operations.SUM.value:
                    lhs = stack.pop()
                    rhs = stack.pop()
                    expr_sum = self.__sum(lhs, rhs)
                    stack.append(expr_sum)
                    
                elif i == Operations.KLEENE_STAR.value:
                    expr = stack.pop()
                    expr_kleene_star = self.__kleene_star(expr)
                    stack.append(expr_kleene_star)
        answer_storage = stack.pop()

        if stack:
            raise AttributeError("Incorrect expression")
        
        if answer_storage[self._remainder]:
            return True

        return False

    @staticmethod
    def __sum(lhs, rhs) -> list:
        length = len(lhs)
        res = [True] * length
        for i in range(length):
            if lhs[i] | rhs[i]:
                res[i] = True
            else:
                res[i] = False
        return res

    @staticmethod
    def __concatenation(lhs, rhs) -> list:
        length = len(lhs)
        res = [False] * length
        for i in range(length):
            for j in range(length):
                if lhs[i] and rhs[j]:
                    res[(i + j) % length] = True
        return res

    @staticmethod
    def __kleene_star(expr) -> list:
        expr[0] = True
        res = expr.copy()
        length = len(expr)
        for i in range(length - 1):
            tmp = RegularExpressionHandling.__concatenation(res, expr)
            if tmp == res:
                break
            for j in range(length):
                if not tmp[j]:
                    tmp[j] = res[j]
            res = tmp
        return res
