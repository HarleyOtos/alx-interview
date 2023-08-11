#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode);
    process.exit(1);
  }

  const characters = body.characters;

  function fetchCharacterName(url) {
    return new Promise((resolve, reject) => {
      request(url, { json: true }, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
          return;
        }

        if (charResponse.statusCode !== 200) {
          reject(new Error(`Status code: ${charResponse.statusCode}`));
          return;
        }

        resolve(charBody.name);
      });
    });
  }

  async function printCharacterNames() {
    for (const characterUrl of characters) {
      try {
        const characterName = await fetchCharacterName(characterUrl);
        console.log(characterName);
      } catch (err) {
        console.error('Error:', err);
      }
    }
  }

  printCharacterNames();
});
