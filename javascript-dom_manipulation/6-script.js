window.onload = async function() {
  const data = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json').then(
    (response) => response.json()
  )
  const character = document.querySelector('#character');
  character.innerText = data.name;
}

