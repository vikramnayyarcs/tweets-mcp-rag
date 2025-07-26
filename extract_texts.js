const fs = require('fs');

const data = JSON.parse(fs.readFileSync('tweets.json', 'utf-8'));

const texts = (data.data || [])
  .filter(tweet => tweet && tweet.text)
  .map(tweet => tweet.text);

// Print each tweet clearly, separated by a line
texts.forEach((text, i) => {
  console.log(`--- Tweet #${i + 1} ---\n${text}\n`);
});