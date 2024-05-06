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
