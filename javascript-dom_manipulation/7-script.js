window.onload = async () => {
  const data = await fetch('https://swapi-api.hbtn.io/api/films/?format=json').then(
    (response) => response.json()
  );
  const ul = document.querySelector('ul');
  data.results.forEach(element => {
    const li = document.createElement('li');
    li.innerText = element.title;
    ul.appendChild(li)
  });
};
