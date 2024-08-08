#!/usr/bin/node

const axios = require('axios');

const filmNum = process.argv[2];
const filmURL = `https://swapi-api.alx-tools.com/api/films/${filmNum}/`;

async function fetchCharacters() {
  try {
    const response = await axios.get(filmURL);
    const filmData = response.data;

    const characterURLs = filmData.characters;

    for (const url of characterURLs) {
      const charResponse = await axios.get(url);
      const characterData = charResponse.data;
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

fetchCharacters();
