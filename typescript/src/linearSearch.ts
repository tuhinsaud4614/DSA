import { Primitive } from "./types";

const CARDS = [13, 11, 10, 7, 4, 3, 1, 0];

/**
 * This function with find out card position from the deck of cards
 * @template T
 * @param {Array.<T>} cards
 * @param {T} query
 * @returns {number} Position of the card
 */
function locateCard<T extends Primitive>(cards: T[], query: T): number {
  //  Initial position is 0
  let position = 0;

  // Set up a loop for repetition
  while (true) {
    // Check if element at the current position matches the query
    if (cards[position] === query) {
      // Found the position Return & exit
      return position;
    }

    // Increment the position
    ++position;

    // Check if we have reached the end of the array
    if (position === cards.length) {
      // Number not found return -1
      return -1;
    }
  }
}

const tests = [
  {
    input: {
      cards: CARDS,
      query: 7,
    },
    output: 3,
  },
  {
    input: {
      cards: CARDS,
      query: 4,
    },
    output: 4,
  },
  {
    input: {
      cards: CARDS,
      query: 40,
    },
    output: -1,
  },
];

tests.forEach((test) => {
  const result = locateCard(test.input.cards, test.input.query) == test.output;
  console.log(result);
});
