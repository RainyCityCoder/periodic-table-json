# periodic-table-json

## Description

This repository is designed to host a minimalist JSON file of the elements known to science (as listed on [ptable.com](https://ptable.com/#?lang=en)). Please see the license for details on what is and isn't permissable.

## Tech Stack

A Python script was used to read existing JSON objects from `periodic-table.json`, build new objects based on user input, and append the new objects to the end of the previous list.

`periodic-table.json` contains a list of JSON objects in the format:

```
{
  "Name": "Hydrogen",
  "Atomic Number": 1,
  "Symbol": "H",
  "Atomic Weight": 1.008
}
```

## Forking

Feel free to fork and utilize this code and data.

## Contributing

Pull requests are welcome. For major changes, please open an issue first.
