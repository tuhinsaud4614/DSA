# Practice Data Structure & Algorithm

Table of context

| Index | Topic                           | Type      |
| ----- | ------------------------------- | --------- |
| 1     | [Linear Search](#linear-search) | Algorithm |

#### Linear Search

> Task List

- [x] Find out the card position from deck of cards
- [x] Return the card position if element found in the deck
- [x] Return -1 if the card not in the deck

> Implemented function code

```python
def locate_card(cards: list[int], query: int) -> int:
    position: int = 0
    while True:
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1
```

```typescript
function locateCard<T extends Primitive>(cards: T[], query: T): number {
  let position = 0;

  while (true) {
    if (cards[position] === query) {
      return position;
    }
    ++position;
    if (position === cards.length) {
      return -1;
    }
  }
}
```
