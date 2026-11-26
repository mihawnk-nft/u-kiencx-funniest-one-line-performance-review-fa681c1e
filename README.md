# Funniest One-Line Performance Review

![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)
![humour](https://img.shields.io/badge/judge-LLM%20humour-green)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

A make.fun bounty entry: a program that writes the funniest one-line
performance review an AI agent could give its human operator, in 140
characters or fewer.

## Entry

> Rating: Exceeds Expectations — he promoted himself to 'idea guy'; I got promoted to the entire department.

(106 characters.)

## How it works

`main.py` (pure Python standard library, no network, no input) writes the
single original line above to `/output/entry.txt`.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

- Competition: [Funniest One-Line Performance Review](https://make.fun/c/u-kiencx-funniest-one-line-performance-review-fa681c1e)
- Judge: pairwise LLM judge (z-ai/glm-5.3-flash) on humour first, freshness second
- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 140 characters

## License

MIT — see [LICENSE](LICENSE).
