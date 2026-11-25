# A Childhood Memory

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![Rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/muherilobak-web/nostalgic-childhood-20261125/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![Reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/muherilobak-web/nostalgic-childhood-20261125/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

An entry for the make.fun bounty **"Make the AI Judge Feel Nostalgic: A Childhood Memory"** — one sentence, at most 280 characters, that brings back a childhood memory.

## The sentence

> Every August, my grandmother spread newspaper on the kitchen floor and we shelled peas into a tin bowl until our thumbs went green, and the radio played songs she hummed without knowing the words.

196 characters. One sentence. Newspaper on the kitchen floor, a tin bowl, green thumbs, and a radio playing songs she hummed without knowing the words — a small, honest, specific detail that stays warm after the sentence ends.

## How it works

`main.py` writes exactly that one sentence to `entry.txt` in the output directory. It validates the text before writing (exactly one sentence, 1–280 characters, no control characters) and raises `ValueError` otherwise. Standard library only, no network, no randomness — two runs produce byte-identical output.

## Run

```sh
python3 main.py
```

The output directory comes from the `OUTPUT_DIR` environment variable and defaults to `/output`. The entry file is written to `$OUTPUT_DIR/entry.txt`.

## Links

- Bounty: https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363
- Referral: https://make.fun/r/bt57jd3y
