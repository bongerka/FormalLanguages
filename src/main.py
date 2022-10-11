from typing import Tuple, List
from modules.RegularExpressionHandling import RegularExpressionHandling


def main() -> None:
    alphabet: set = {"a", "b", "c", "1"}
    operations: set = {".", '+', '*'}
    regular_expression, mod, remainder = read_input()
    processing = RegularExpressionHandling(regular_expression, mod, remainder, alphabet, operations)
    result: bool = processing.are_exist_necessary_words()

    if result:
        print("YES")
    else:
        print("NO")


def read_input() -> Tuple[str, int, int]:
    inp: List[str] = input().split()
    regular_expr: str = inp[0]
    mod: int = int(inp[1])
    remainder: int = int(inp[2])
    return regular_expr, mod, remainder


if __name__ == '__main__':
    main()
