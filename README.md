[![Scheduled run](https://github.com/gttrcr/eaziu-launch/actions/workflows/scheduled-workflow.yml/badge.svg?branch=main)](https://github.com/gttrcr/eaziu-launch/actions/workflows/scheduled-workflow.yml)

# EaziU Launch 🚀🍝

An automatic script to make everyday meal a surprise via github actions.

## Instructions
1. Fork this repo
2. Change your `config.json`
3. Change github action to execute the script at your will
4. Enjoy your meal

## config.json
```json
{
    "url": "https://info637989.typeform.com/to/m4bUIenk", // do not change this, this is the lunch form link
    "name": "Michele", // name
    "note": "No Grana aggiunto", // note
    "weight": { // weights for each type of lunch (cumulatives, not percentage)
        "primo": 50,
        "poke": 10,
        "rosticceria": 10,
        "secondo": 30
    }
}
```

| Parameter | Description |
|:-:|:-:|
|url| Lunch form link. **Do not change this**|
|name| Text for field `name`|
|note| Text for field `note`|
|weight| Object with weights for random lunch selection. Cumulative, not percentage. (weight 2 is twice as much probable then 1)|

### Lunch rules
| Course | Description |
|:-:|:-:|
| Primo | Grants a main course (usually some pasta or soup) and a side (or dessert) |
| Secondo | Grants a follow course and a side (or dessert) |
| Poke | Grants a Poke only |
| Rosticceria | Grants a fry main course and a side (or dessert) |
