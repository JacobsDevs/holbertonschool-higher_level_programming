window.onload = async () => {
  const data = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr').then(
    (response) => response.json()
  );
  const hello = document.querySelector('#hello');
  hello.innerHTML = data.hello
}
