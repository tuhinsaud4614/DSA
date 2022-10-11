from typing import Any, Final, Literal


def locate_card(cards: list[int], query: int) -> int:
    """
    This function with find out card position from the deck of cards

    Return the card position number
    """

    # Initial position is 0
    position: int = 0

    # Set up a loop for repetition
    while True:

        # Check if element at the current position matches the query
        if cards[position] == query:

            # Found the position Return & exit
            return position

        # Increment the position
        position += 1

        # Check if we have reached the end of the array
        if position == len(cards):

            # Number not found return -1
            return -1


CARDS: Final[tuple[Literal[13], Literal[11], Literal[10], Literal[7],
                   Literal[4], Literal[3], Literal[1], Literal[0]]] = (13, 11, 10, 7, 4, 3, 1, 0)

tests: tuple[dict[str, Any], dict[str, Any], dict[str, Any]] = ({
    'input': {
        'cards': CARDS,
        'query': 7
    },
    'output': 3
}, {
    'input': {
        'cards': CARDS,
        'query': 4
    },
    'output': 4
},  {
    'input': {
        'cards': CARDS,
        'query': 40
    },
    'output': -1
})

for index, test in enumerate(tests):
    result = locate_card(**test['input']) == test['output']
    print(f'Case: {index+1} | Result: {result}')
