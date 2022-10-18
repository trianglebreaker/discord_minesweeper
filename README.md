# discord_minesweeper

Python script to generate a Minesweeper grid to be pasted into Discord chat.

## Why?

I was messing with my friends by making Minesweeper out of Discord spoiler boxes, except instead of the explosions I'd place some silly inside joke emoji. While I was making the puzzle message, I thought to myself "hey, I should automate this".

## Features

- Customizable board dimensions (must be odd)
- Guarantees the center square is blank (and doesn't spoiler it)

## Usage Example

The following will automatically copy a randomly generated 11 by 11 puzzle with 20 mines to the clipboard, representing empty cells with :small_blue_diamond: and mines as :poop:. The message will be formatted according to Discord's Markdown, without spaces in between the cells.

```
$ python3 main.py -d 11 11 -m 20 -be small_blue_diamond -me poop
```

Use `--help` for details on all of the flags.

## Todo

- Find a way to guarantee puzzles won't require any guesses. It shouldn't be very likely either way, but it's probably still possible.
